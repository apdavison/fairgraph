"""
Base functionality
"""

# Copyright 2018-2020 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from collections import defaultdict
from datetime import datetime, date
import warnings
from copy import copy
import logging
from uuid import UUID

from requests.exceptions import HTTPError
try:
    from tabulate import tabulate
    have_tabulate = True
except ImportError:
    have_tabulate = False
from .utility import (compact_uri, expand_uri, as_list)
from .registry import Registry, generate_cache_key, lookup, lookup_by_id, lookup_type, lookup_by_iri


logger = logging.getLogger("fairgraph")


class EmbeddedMetadata(object, metaclass=Registry):

    def __init__(self, **properties):
        for field in self.fields:
            try:
                value = properties[field.name]
            except KeyError:
                if field.required:
                    msg = "Field '{}' is required.".format(field.name)
                    if field.strict_mode:
                        raise ValueError(msg)
                    else:
                        warnings.warn(msg)
                value = None
            if value is None:
                value = field.default
                if callable(value):
                    value = value()
            elif isinstance(value, (list, tuple)) and len(value) == 0:  # empty list
                value = None
            field.check_value(value)
            setattr(self, field.name, value)

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ")"
        return template.format(self=self)

    def to_jsonld(self):
        data = {}
        for field in self.fields:
            value = getattr(self, field.name)
            if value is not None:
                data[field.path] = value

    @classmethod
    def from_jsonld(cls, data, client, resolved=False):
        properties = {}
        for field in cls.fields:
            properties[field.name] = field.deserialize_v3(data, client, resolved=resolved)
        return cls(**properties)

    @classmethod
    def set_strict_mode(cls, value, field_name=None):
        if value not in (True, False):
            raise ValueError("value should be either True or False")
        if field_name:
            for field in cls.fields:
                if field.name == field_name:
                    field.strict_mode = value
                    return
            raise ValueError("No such field: {}".format(field_name))
        else:
            for field in cls.fields:
                field.strict_mode = value


class KGObjectV3(object, metaclass=Registry):
    """Base class for Knowledge Graph objects"""
    object_cache = {}  # for caching based on object ids
    save_cache = defaultdict(dict)  # for caching based on queries
    fields = []
    existence_query_fields = ["name"]
    # Note that this default value of existence_query_fields should in
    # many cases be over-ridden.
    # It assumes that "name" is unique within instances of a given type,
    # which may often not be the case.

    def __init__(self, id=None, data=None, space=None, **properties):
        for field in self.fields:
            try:
                value = properties[field.name]
            except KeyError:
                if field.required:
                    msg = "Field '{}' is required.".format(field.name)
                    if field.strict_mode:
                        raise ValueError(msg)
                    else:
                        warnings.warn(msg)
                value = None
            if value is None:
                value = field.default
                if callable(value):
                    value = value()
            elif isinstance(value, (list, tuple)) and len(value) == 0:  # empty list
                value = None
            field.check_value(value)
            setattr(self, field.name, value)

        self.id = id
        self._space = space
        self.data = data

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ", id={self.id})"
        return template.format(self=self)

    @property
    def space(self):
        if self.data:
            if "https://schema.hbp.eu/myQuery/space" in self.data:
                self._space = self.data["https://schema.hbp.eu/myQuery/space"]
            elif "https://core.kg.ebrains.eu/vocab/meta/space" in self.data:
                self._space = self.data["https://core.kg.ebrains.eu/vocab/meta/space"]
        return self._space

    @classmethod
    def from_kg_instance(cls, data, client, resolved=False):
        # normalize data by compacting keys
        D = {
            compact_uri(key, cls.context): value
            for key, value in data.items() if key[0] != "@"
        }
        D["@id"] =  data["@id"]
        D["@type"] = compact_uri(data["@type"], cls.context)
        D["@context"] = data.get("@context", cls.context)
        for otype in compact_uri(as_list(cls.type), cls.context):  # todo: update class generation to ensure classes are already compacted
            if otype not in D["@type"]:
                print("Warning: type mismatch {} - {}".format(otype, D["@type"]))
        args = {}
        for field in cls.fields:
            if field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize_v3(data_item, client, resolved=resolved)
        return cls(id=D["@id"], data=D, **args)

    @classmethod
    def _fix_keys(cls, data):
        """
        The KG Query API does not allow the same field name to be used twice in a document.
        This is a problem when resolving linked nodes which use the same field names
        as the 'parent'. As a workaround, we prefix the field names in the linked node
        with the class name.
        This method removes this prefix.
        This feels like a kludge, and I'd be happy to find a better solution.
        """
        prefix = cls.__name__ + "__"
        for key in list(data):
            # need to use list() in previous line to avoid
            # "dictionary keys changed during iteration" error in Python 3.8+
            if key.startswith(prefix):
                fixed_key = key.replace(prefix, "")
                data[fixed_key] = data.pop(key)
        return data

    @classmethod
    def from_uri(cls, uri, client, use_cache=True, scope="released", resolved=False):
        data = client.instance_from_full_uri(uri, use_cache=use_cache,
                                             scope=scope, resolved=resolved)
        if data is None:
            return None
        else:
            #try:
            return cls.from_kg_instance(data, client, resolved=resolved)
            #except ValueError as err:
            #    return None

    @classmethod
    def from_uuid(cls, uuid, client, use_cache=True, scope="released", resolved=False):
        logger.info("Attempting to retrieve {} with uuid {}".format(cls.__name__, uuid))
        if len(uuid) == 0:
            raise ValueError("Empty UUID")
        try:
            val = UUID(uuid, version=4)  # check validity of uuid
        except ValueError as err:
            raise ValueError("{} - {}".format(err, uuid))
        uri = cls.uri_from_uuid(uuid, client)
        return cls.from_uri(uri, client, use_cache=use_cache, scope=scope, resolved=resolved)

    @classmethod
    def from_id(cls, id, client, use_cache=True, scope="released", resolved=False):
        if id.startswith("http"):
            return cls.from_uri(id, client, use_cache=use_cache, scope=scope, resolved=resolved)
        else:
            return cls.from_uuid(id, client, use_cache=use_cache, scope=scope, resolved=resolved)

    @property
    def uuid(self):
        # todo: consider using client._kg_client.uuid_from_absolute_id
        if self.id is not None:
            return self.id.split("/")[-1]
        else:
            return None

    @classmethod
    def uri_from_uuid(cls, uuid, client):
        return client.uri_from_uuid(uuid)

    @classmethod
    def list(cls, client, size=100, from_index=0, api="query",
             scope="released", resolved=False, space=None, **filters):
        """List all objects of this type in the Knowledge Graph"""

        def get_filter_value(filters, field):
            value = filters[field.name]
            if not isinstance(value, field.types):
            #     if isinstance(value, str) and issubclass(field.types[0], OntologyTerm):
            #         value = field.types[0](value)
            #     else:
                raise TypeError("{} must be of type {}".format(field.name, field.types))
            if hasattr(value, "iri"):
                filter_value = value.iri
            elif hasattr(value, "id"):
                filter_value = value.id
            else:
                filter_value = value
            return filter_value

        if api == "query":
            filter_queries = {}
            if filters:
                for field in cls.fields:
                    if field.name in filters:
                        filter_queries[field.name] = get_filter_value(filters, field)
            filter_query = filter_queries or None
            context = None
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            filter_query = None
            context = None
            space = space or cls.space
        else:
            raise ValueError("'api' must be either 'query', or 'core'")
        return client.list(cls, space=space, from_index=from_index, size=size, api=api,
                           scope=scope, resolved=resolved, filter=filter_query)

    @classmethod
    def count(cls, client, api="query", scope="released"):
        return client.count(cls, api=api, scope=scope)

    def _build_existence_query(self):
        if self.existence_query_fields is None:
            return None

        query_fields = []
        for field_name in self.existence_query_fields:
            for field in self.fields:
                if field.name == field_name:
                    query_fields.append(field)
                    break
        if len(query_fields) < 1:
            raise Exception("Empty existence query for class {}".format(self.__class__.__name__))
        return {
            field.name: field.serialize(getattr(self, field.name), None, for_query=True)
            for field in query_fields
        }

    def exists(self, client, space=None):
        """Check if this object already exists in the KnowledgeGraph"""
        if self.id:
            # Since the KG now allows user-specified IDs we can't assume that the presence of
            # an id means the object exists
            data = client.instance_from_full_uri(self.id, use_cache=True,
                                                 scope="latest", resolved=False)
            if space:
                key = "https://core.kg.ebrains.eu/vocab/meta/space"
                if key in data and data[key] == space:
                    return True
                else:
                    return False
            else:
                return bool(data)
        else:
            query_filter = self._build_existence_query()

            if query_filter is None:
                # if there's no existence query and no ID, we allow
                # duplicate entries
                return False
            else:
                query_cache_key = generate_cache_key(query_filter, space)
                if query_cache_key in self.save_cache[self.__class__]:
                    # Because the KnowledgeGraph is only eventually consistent, an instance
                    # that has just been written to Nexus may not appear in the query.
                    # Therefore we cache the query when creating an instance and
                    # where exists() returns True
                    self.id = self.save_cache[self.__class__][query_cache_key]
                    return True

                instances = client.query(self.query_label, filter=query_filter,
                                        space=space, size=1, scope="latest")
                if instances:
                    self.id = instances[0].data()["@id"]
                    KGObjectV3.save_cache[self.__class__][query_cache_key] = self.id
                return bool(instances)

    def _updated_data(self, data):
        updated_data = {}
        for key, value in data.items():
            if key not in self.data:
                if value is not None:
                    logger.info(f"new field '{key}' with value {value}")  # todo: change to debug
                    updated_data[key] = value
            elif self.data[key] != value:
                existing = self.data[key]
                if not (
                    isinstance(existing, list)
                    and len(existing) == 1
                    and isinstance(existing[0], dict)
                    and existing[0] == value
                ): # we treat a list containing a single dict as equivalent to that dict
                    logger.info(f"change to field '{key}' from {existing} to {value}")
                    updated_data[key] = value
        return updated_data

    def _build_data(self, client, all_fields=False):
        if self.fields:
            data = {}
            for field in self.fields:
                if field.intrinsic:
                    value = getattr(self, field.name)
                    if all_fields or field.required or value is not None:
                        serialized = field.serialize(value, client, with_type=False)
                        if field.path in data:
                            if isinstance(data[field.path], list):
                                data[field.path].append(serialized)
                            else:
                                data[field.path] = [data[field.path], serialized]
                        else:
                            data[field.path] = serialized
            return data
        else:
            raise NotImplementedError("to be implemented by child classes")

    def save(self, client, space=None):
        if space is None:
            if self.space is None:
                space = self.__class__.space
            else:
                space = self.space
        if self.exists(client, space=space):
            # update
            data = self._build_data(client, all_fields=True)
            updated_data = self._updated_data(data)
            if updated_data:
                logger.info(f"Updating - {self.__class__.__name__}(id={self.id})")
                self.data.update(data)
                client.update_instance(self.uuid, updated_data)
            else:
                logger.info(f"Not updating {self.__class__.__name__}(id={self.id}), unchanged")
        else:
            # create new
            data = self._build_data(client)
            logger.info("Creating instance with data {}".format(data))
            data["@context"] = self.context
            data["@type"] = self.type
            instance_data = client.create_new_instance(space=space or self.__class__.space, data=data, instance_id=self.uuid)
            self.id = instance_data["@id"]
        # not handled yet: save existing object to new space - requires changing uuid
        logger.debug("Updating cache for object {}. Current state: {}".format(self.id, self._build_data(client)))
        KGObjectV3.object_cache[self.id] = self

    def delete(self, client):
        """Deprecate"""
        client.delete_instance(self.id)
        if self.id in KGObjectV3.object_cache:
            KGObjectV3.object_cache.pop(self.id)

    @classmethod
    def by_name(cls, name, client, match="equals", all=False,
                space=None, scope="released", resolved=False):
        return client.by_name(cls, name, match=match, all=all, space=space,
                              scope="released", resolved=resolved)

    def resolve(self, client, use_cache=True):
        """To avoid having to check if a child attribute is a proxy or a real object,
        a real object resolves to itself.
        """
        return self

    @classmethod
    def set_strict_mode(cls, value, field_name=None):
        if value not in (True, False):
            raise ValueError("value should be either True or False")
        if field_name:
            for field in cls.fields:
                if field.name == field_name:
                    field.strict_mode = value
                    return
            raise ValueError("No such field: {}".format(field_name))
        else:
            for field in cls.fields:
                field.strict_mode = value

    def show(self, max_width=None):
        if not have_tabulate:
            raise Exception("You need to install the tabulate module to use the `show()` method")
        data = [("id", self.id)] + [(field.name, getattr(self, field.name, None))
                                    for field in self.fields]
        if max_width:
            value_column_width = max_width - max(len(item[0]) for item in data)

            def fit_column(value):
                strv = str(value)
                if len(strv) > value_column_width:
                    strv = strv[:value_column_width - 4] + " ..."
                return strv
            data = [(k, fit_column(v)) for k, v in data]
        print(tabulate(data, tablefmt="plain"))
        #return tabulate(data, tablefmt='html') - also see  https://bitbucket.org/astanin/python-tabulate/issues/57/html-class-options-for-tables

    @classmethod
    def generate_query(cls, query_type, space, client, resolved=False, top_level=True,
                       field_names_used=None, parents=None):
        query_label = cls.get_query_label(query_type, space)
        if top_level:
            fields = [
                {
                    "path": "@id",
                    "filter": {
                        "op": "equals",
                        "parameter": "id"
                    }
                },
                {
                    "path": "https://core.kg.ebrains.eu/vocab/meta/space",
                    "filter": {
                        "op": "EQUALS",
                        "value": space
                    },
                    "propertyName": "query:space"
                }
            ]
        else:
            fields = [{"path": "@id"}]
        fields.append({"path": "@type"})
        if field_names_used is None:
            field_names_used = []

        for field in cls.fields:
            # set parents to avoid infinite recursion
            if top_level:
                # reset for each field
                parents = set([cls])
            else:
                parents.add(cls)

            if field.intrinsic:
                field_definition = {
                    "propertyName": field.path,
                    "path": expand_uri(field.path, cls.context, client)[0],
                }
                field_names_used.append(field.path)
                if top_level:
                    if field.name == "name":
                        field_definition["sort"] = True
                        if field.required:
                            field_definition["required"] = True

                if any(issubclass(_type, KGObjectV3) for _type in field.types):

                    if not top_level and field.path in field_names_used:
                        field_definition["propertyName"] = "{}__{}".format(cls.__name__, field.path)
                    if field.multiple:
                        field_definition["ensureOrder"] = True

                    field_definition["structure"] = [
                        {"path": "@id"},
                        {"path": "@type"}
                    ]

                    if resolved and not parents.intersection(set(field.types)):
                        #               ^^^ avoid recursion to types seen previously
                        #print("    resolving.... (parents={}, field.types={})".format(parents, field.types))
                        subfield_map = {}
                        for child_cls in field.types:
                            if issubclass(child_cls, KGObjectV3):
                                subfields = child_cls.generate_query(
                                    query_type, space, client, resolved=resolved,
                                    top_level=False, field_names_used=field_names_used,
                                    parents=copy(parents))  # use a copy to keep the original for the next iteration
                                subfield_map.update(
                                    {subfield_defn.get("propertyName", subfield_defn["path"]): subfield_defn
                                    for subfield_defn in subfields}
                                )
                        field_definition["structure"] = list(subfield_map.values())

                # here we add a filter for top-level fields
                if field.types[0] in (int, float, bool, datetime, date):
                    op = "EQUALS"
                else:
                    op = "CONTAINS"
                if top_level:
                    field_definition["filter"] = {  # don't filter on datetime,  ...
                        "op": op,
                        "parameter": field.name
                    }

                fields.append(field_definition)

            # todo: add proxy reverse links for non-intrinsic fields?
            #       (proxy because otherwise we risk returning the entire graph!)
        if top_level:
            query = {
                "@context": {
                    "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
                    "query": "https://schema.hbp.eu/myQuery/",
                    "propertyName": {
                        "@id": "propertyName",
                        "@type": "@id"
                    },
                    "merge": {
                        "@type": "@id",
                        "@id": "merge"
                    },
                    "path": {
                        "@id": "path",
                        "@type": "@id"
                    }
                },
                "meta": {
                    "type": cls.type[0],   # ? e.g. "https://openminds.ebrains.eu/core/ModelVersion",
                    "name": query_label,
                    "description": "Automatically generated by fairgraph"
                },
                "structure": fields,
            }
            return query
        else:
            return fields

    @classmethod
    def get_query_label(cls, query_type, space):
        return f"fg-{cls.__name__}-{query_type}-{space}"

    @classmethod
    def store_queries(cls, space, client):
        # todo: we don't necessarily have to store the queries in the same space they're querying
        #       might be useful to have some queries that span multiple spaces, e.g. 'model' + 'myspace'
        for query_type, resolved in (("simple", False), ("resolved", True)):
            query_label = cls.get_query_label(query_type, space)
            query_definition = cls.generate_query(query_type, space, client, resolved=resolved)
            try:
                client.store_query(query_label, query_definition, space=space)
            except HTTPError as err:
                if err.response.status_code == 401:
                    warnings.warn("Unable to store query with id '{}': {}".format(
                        query_label, err.response.text))
                else:
                    raise

    @classmethod
    def retrieve_query(cls, query_type, space, client):
        query_label = cls.get_query_label(query_type, space)
        return client.retrieve_query(query_label)

    def is_released(self, client):
        """Release status of the node"""
        return client.is_released(self.id)

    def release(self, client):
        """Release this node (make it available in public search)."""
        return client.release(self.id)

    def unrelease(self, client):
        """Urelease this node (remove it from public search)."""
        return client.unrelease(self.id)


class KGProxyV3(object):
    """docstring"""

    def __init__(self, cls, uri):
        if isinstance(cls, str):
            self.cls = lookup(cls)
        elif cls is None:
            self.cls = lookup_by_id(uri)
        else:
            self.cls = cls
        self.id = uri

    @property
    def type(self):
        try:
            return self.cls.type
        except AttributeError as err:
            raise AttributeError(f"{err} self.cls={self.cls}")

    @property
    def classes(self):
        # For consistency with KGQuery interface
        if isinstance(self.cls, (list, tuple)):
            return self.cls
        else:
            return [self.cls]

    def resolve(self, client, scope="released", use_cache=True):
        """docstring"""
        if use_cache and self.id in KGObjectV3.object_cache:
            obj = KGObjectV3.object_cache[self.id]
            #if obj:
            #    logger.debug("Retrieving object {} from cache. Status: {}".format(self.id, obj._build_data(client)))
            return obj
        else:
            if len(self.classes) > 1:
                obj = None
                for cls in self.classes:
                    obj = cls.from_uri(self.id, client, scope=scope)
                    if obj is not None:
                        break
            else:
                obj = self.cls.from_uri(self.id, client, scope=scope)
            if obj is None:
                raise Exception("Cannot resolve proxy object")
            KGObjectV3.object_cache[self.id] = obj
            return obj

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.classes!r}, {self.id!r})'.format(self=self))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.cls == other.cls and self.id == other.id

    def __ne__(self, other):
        return (not isinstance(other, self.__class__)
                or self.cls != other.cls
                or self.id != other.id)

    @property
    def uuid(self):
        return self.id.split("/")[-1]

    def delete(self, client):
        """Delete the instance which this proxy represents"""
        obj = self.resolve(client, scope="latest")
        if obj:
            obj.delete(client)


class KGQueryV3(object):
    """docstring"""

    def __init__(self, classes, filter):
        self.classes = []
        for cls in as_list(classes):
            if isinstance(cls, str):
                self.classes.append(lookup(cls))
            else:
                self.classes.append(cls)
        self.filter = filter

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.classes!r}, {self.filter!r})'.format(self=self))

    def resolve(self, client, size=10000, from_index=0, space=None,
                scope="released", use_cache=True, resolved=False):
        if resolved:
            query_type = "resolved"
        else:
            query_type = "simple"
        objects = []
        for cls in self.classes:
            instances = client.query(
                query_label=cls.get_query_label(query_type, space),
                filter=self.filter,
                size=size,
                from_index=from_index,
                scope=scope)
            objects.extend(cls.from_kg_instance(instance_data, client)
                           for instance_data in instances)
        for obj in objects:
            KGObjectV3.object_cache[obj.id] = obj
        if len(objects) == 1:
            return objects[0]
        else:
            return objects

    def count(self, client, space=None, scope="released"):
        n = 0
        for cls in self.classes:
            n += client.count(space=space, filter=self.filter, scope=scope)
        return n


def build_kgv3_object(possible_classes, data, resolved=False, client=None):
    """
    Build a KGObject, a KGProxy, or a list of such, based on the data provided.

    This takes care of the JSON-LD quirk that you get a list if there are multiple
    objects, but you get the object directly if there is only one.

    Returns `None` if data is None.
    """
    if data is None:
        return None

    if not isinstance(data, list):
        if not isinstance(data, dict):
            raise ValueError("data must be a list or dict")
        if "@list" in data:
            assert len(data) == 1
            data = data["@list"]
        else:
            data = [data]

    objects = []
    for item in data:
        if item is None:
            logger.error(f"Unexpected null. possible_classes={possible_classes} data={data}")
            continue
        logger.debug(f"Building {possible_classes} from {item.get('@id', 'not a node')}")
        if possible_classes is None:
            raise NotImplementedError

        assert isinstance(possible_classes, (list, tuple))
        assert all(issubclass(item, KGObjectV3) for item in possible_classes)
        if len(possible_classes) > 1:
            if "@type" in item:
                for cls in possible_classes:
                    if item["@type"] == cls.type:
                        kg_cls = cls
                        break
            else:
                kg_cls = possible_classes

        else:
            kg_cls = possible_classes[0]

        if "@id" in item and item["@id"].startswith("http"):
            # here is where we check the "resolved" keyword,
            # and return an actual object if we have the data
            # or resolve the proxy if we don't
            if resolved:
                try:
                    obj = kg_cls.from_kg_instance(item, client, resolved=resolved)
                except (ValueError, KeyError) as err:
                    # to add: emit a warning
                    logger.warning("Error in building {}: {}".format(kg_cls.__name__, err))
                    obj = KGProxyV3(kg_cls, item["@id"]).resolve(
                        client,
                        # todo: provide space and scope
                        resolved=resolved)
            else:
                if "@type" in item and item["@type"] is not None and kg_cls not in as_list(
                        lookup_type(item["@type"])):
                    logger.warning(f"Mismatched types: {kg_cls} <> {item['@type']}")
                    raise Exception("mismatched types")
                    obj = None
                else:
                    obj = KGProxyV3(kg_cls, item["@id"])
        else:
            # todo: add a logger.warning that we have dud data
            obj = None

        if obj is not None:
            objects.append(obj)

    if len(objects) == 1:
        return objects[0]
    else:
        return objects
