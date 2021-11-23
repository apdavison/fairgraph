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
from urllib.parse import SplitResultBytes
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
from .errors import NoQueryFound


logger = logging.getLogger("fairgraph")


class IRI(object):

    def __init__(self, value):
        if isinstance(value, IRI):
            value = value.value
        if not value.startswith("http"):
            raise ValueError("Invalid IRI")
        self.value = value

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value

    def __repr__(self):
        return f"IRI({self.value})"

    def __str__(self):
        return self.value

    def to_jsonld(self, client):
        return self.value


class EmbeddedMetadata(object, metaclass=Registry):

    def __init__(self, data=None, **properties):
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
        self.data = data

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ")"
        return template.format(self=self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.to_jsonld() == other.to_jsonld()

    def to_jsonld(self, client=None):
        data = {
            "@type": self.type
        }
        for field in self.fields:
            value = getattr(self, field.name)
            if value is not None:
                data[field.path] = field.serialize(value, client)
        return data

    @classmethod
    def from_jsonld(cls, data, client, resolved=False):
        if "@id" in data:
            #raise Exception("Expected embedded metadata, but received @id: " + str(data))
            warnings.warn("Expected embedded metadata, but received @id")
            return None

        D = {
            compact_uri(key, cls.context): value
            for key, value in data.items() if key[0] != "@"
        }
        args = {}
        for field in cls.fields:
            data_item = D.get(field.path)
            args[field.name] = field.deserialize_v3(data_item, client, resolved=resolved)
        return cls(data=D, **args)

    @classmethod
    def set_strict_mode(cls, value, field_names=None):
        if value not in (True, False):
            raise ValueError("value should be either True or False")
        if field_names:
            for field_name in as_list(field_names):
                found = False
                for field in cls.fields:
                    if field.name == field_name:
                        field.strict_mode = value
                        found = True
                        break
                if not found:
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
        properties_copy = copy(properties)
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
            else:
                properties_copy.pop(field.name)
            if value is None:
                value = field.default
                if callable(value):
                    value = value()
            elif isinstance(value, (list, tuple)) and len(value) == 0:  # empty list
                value = None
            field.check_value(value)
            setattr(self, field.name, value)
        if len(properties_copy) > 0:
            if len(properties_copy) == 1:
                raise NameError(f'{self.__class__.__name__} does not have a field named "{list(properties_copy)[0]}".')
            else:
                raise NameError(f"""{self.__class__.__name__} does not have fields named "{'", "'.join(properties_copy)}".""")

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
    def _deserialize_data(cls, data, client, resolved=False):
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
                #print("Warning: type mismatch {} - {}".format(otype, D["@type"]))
                raise TypeError("type mismatch {} - {}".format(otype, D["@type"]))
        deserialized_data = {}
        for field in cls.fields:
            if field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            deserialized_data[field.name] = field.deserialize_v3(data_item, client, resolved=resolved)
        # if cls.__name__ == "ModelVersion":
        #     raise Exception()
        return deserialized_data

    @classmethod
    def from_kg_instance(cls, data, client, resolved=False):
        deserialized_data = cls._deserialize_data(data, client, resolved=resolved)
        return cls(id=data["@id"], data=data, **deserialized_data)

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
                if field.name == "hash":  # bit of a hack
                    filter_value = value
                else:
                    raise TypeError("{} must be of type {}".format(field.name, field.types))
            if hasattr(value, "iri"):
                filter_value = value.iri
            elif isinstance(value, IRI):
                filter_value = value.value
            elif hasattr(value, "id"):
                filter_value = value.id
            else:
                filter_value = value
            return filter_value

        space = space or cls.default_space
        if api == "query":
            filter_queries = {}
            if filters:
                for field in cls.fields:
                    if field.name in filters:
                        filter_queries[field.name] = get_filter_value(filters, field)
            filter_query = filter_queries or None
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            filter_query = None
        else:
            raise ValueError("'api' must be either 'query', or 'core'")
        return client.list(cls, space=space, from_index=from_index, size=size, api=api,
                           scope=scope, resolved=resolved, filter=filter_query)

    @classmethod
    def count(cls, client, api="core", scope="released"):
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

    def _update(self, data, client, resolved=False):
        """Replace any empty fields (value None) with the supplied data"""
        cls = self.__class__
        if self.data:
            self.data.update(data)
        deserialized_data = cls._deserialize_data(data, client, resolved=resolved)
        for field in cls.fields:
            current_value = getattr(self, field.name, None)
            if current_value is None:
                setattr(self, field.name, deserialized_data[field.name])

    def exists(self, client, space=None):
        """Check if this object already exists in the KnowledgeGraph"""
        if self.id:
            # Since the KG now allows user-specified IDs we can't assume that the presence of
            # an id means the object exists
            data = client.instance_from_full_uri(self.id, use_cache=True,
                                                 scope="latest", resolved=False)
            if self.data is None:
                self.data = data

            if space:
                key = "https://core.kg.ebrains.eu/vocab/meta/space"
                if data and key in data:
                    if data[key] == space:
                        obj_exists = True
                     # following 2 lines are a temporary workaround
                    elif space == "myspace" and data[key] == client._private_space:
                        obj_exists = True
                    else:
                        obj_exists = False
                else:
                    obj_exists = False
            else:
                obj_exists = bool(data)
            if obj_exists:
                self._update(data, client)
            return obj_exists
        else:
            query_filter = self._build_existence_query()

            if query_filter is None:
                # if there's no existence query and no ID, we allow
                # duplicate entries
                return False
            else:
                space = space or self.default_space
                query_cache_key = generate_cache_key(query_filter, space)
                if query_cache_key in self.save_cache[self.__class__]:
                    # Because the KnowledgeGraph is only eventually consistent, an instance
                    # that has just been written to the KG may not appear in the query.
                    # Therefore we cache the query when creating an instance and
                    # where exists() returns True
                    self.id = self.save_cache[self.__class__][query_cache_key]
                    cached_obj = self.object_cache.get(self.id)
                    if cached_obj and cached_obj.data:
                        self.data = cached_obj.data  # copy or update needed?
                    return True

                instances = self._query_simple(query_filter, space, client)
                if instances:
                    self.id = instances[0]["@id"]
                    KGObjectV3.save_cache[self.__class__][query_cache_key] = self.id

                    if self.data is None:
                        self.data = instances[0]
                    self._update(instances[0], client)
                return bool(instances)

    def _query_simple(self, query_filter, space, client):
        query_label = self.get_query_label("simple", space)
        try:
            instances = client.query(query_label, filter=query_filter, size=1, scope="latest")
        except NoQueryFound:
            query_definition = self.__class__.generate_query("simple", space, client, resolved=False)
            client.store_query(query_label, query_definition, space=space)
            instances = client.query(query_label, filter=query_filter, size=1, scope="latest")
        return instances

    def _updated_data(self, data):
        updated_data = {}
        for key, value in data.items():
            if self.data is None or key not in self.data:
                if value is not None:
                    logger.info(f"    - new field '{key}' with value {value}")  # todo: change to debug
                    updated_data[key] = value
            else:
                existing = self.data[key]
                if existing != value:
                    if (isinstance(existing, list) and len(existing) == 0 and value is None):
                        # we treat empty list and None as equivalent
                        pass
                    elif (
                        isinstance(existing, list)
                        and len(existing) == 1
                        and isinstance(existing[0], dict)
                        and existing[0] == value
                    ):
                        # we treat a list containing a single dict as equivalent to that dict
                        pass
                    else:
                        logger.info(f"    -  change to field '{key}' from {existing} to {value}")
                        updated_data[key] = value
        return updated_data

    def _build_data(self, client, all_fields=False):
        if self.fields:
            data = {}
            for field in self.fields:
                if field.intrinsic:
                    value = getattr(self, field.name)
                    if all_fields or field.required or value is not None:
                        serialized = field.serialize(value, client, with_type=True)
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

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False):
        if recursive:
            for field in self.fields:
                if field.intrinsic:
                    values = getattr(self, field.name)
                    for value in as_list(values):
                        if isinstance(value, KGObjectV3):
                            if value.space:
                                target_space = value.space
                            elif value.__class__.default_space == "controlled" and value.exists(client, space="controlled"):
                                continue
                            elif space is None and self.space is not None:
                                target_space = self.space
                            else:
                                target_space = space
                            value.save(client, space=target_space, recursive=True,
                                       activity_log=activity_log)
                        # todo: handle EmbeddedMetadata object that _contain_ KGObjects (e.g. QuantitativeValue->UnitOfMeasurement)
        if space is None:
            if self.space is None:
                space = self.__class__.default_space
            else:
                space = self.space
        logger.info(f"Saving a {self.__class__.__name__} in space {space}")
        if self.exists(client, space=space):
            # update
            data = self._build_data(client, all_fields=True)
            if replace:
                logger.info(f"  - replacing - {self.__class__.__name__}(id={self.id})")
                if activity_log:
                    activity_log.update(item=self, delta=data, space=space, entry_type="replacement")
                client.replace_instance(self.uuid, data)
            else:
                updated_data = self._updated_data(data)
                if updated_data:
                    logger.info(f"  - updating - {self.__class__.__name__}(id={self.id}) - fields changed: {updated_data.keys()}")
                    if self.data is None:
                        self.data = data
                    else:
                        self.data.update(data)

                    skip_update = False
                    if "vocab:storageSize" in updated_data:
                        warnings.warn("Removing storage size from update because this field is currently locked by the KG")
                        updated_data.pop("vocab:storageSize")
                        skip_update = len(updated_data) == 0

                    if skip_update:
                        if activity_log:
                            activity_log.update(item=self, delta=None, space=space, entry_type="no-op")
                    else:
                        updated_data["@context"] = self.context
                        client.update_instance(self.uuid, updated_data)
                        if activity_log:
                            updated_data.pop("@context")
                            activity_log.update(item=self, delta=updated_data, space=space, entry_type="update")
                else:
                    logger.info(f"  - not updating {self.__class__.__name__}(id={self.id}), unchanged")
                    if activity_log:
                        activity_log.update(item=self, delta=None, space=space, entry_type="no-op")
        else:
            # create new
            data = self._build_data(client)
            logger.info("  - creating instance with data {}".format(data))
            data["@context"] = self.context
            data["@type"] = self.type
            instance_data = client.create_new_instance(
                space=space or self.__class__.default_space,
                data=data,
                instance_id=self.uuid)
            self.id = instance_data["@id"]
            self._space = space or self.__class__.default_space
            if activity_log:
                activity_log.update(item=self, delta=data, space=self.space, entry_type="create")
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

    def resolve(self, client, scope="released", use_cache=True):
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
        data = [("id", self.id)] + [(field.name, str(getattr(self, field.name, None)))
                                    for field in self.fields]
        if max_width:
            value_column_width = max_width - max(len(item[0]) for item in data)

            def fit_column(value):
                strv = value
                if len(strv) > value_column_width:
                    strv = strv[:value_column_width - 4] + " ..."
                return strv
            data = [(k, fit_column(v)) for k, v in data]
        print(tabulate(data, tablefmt="plain"))
        #return tabulate(data, tablefmt='html') - also see  https://bitbucket.org/astanin/python-tabulate/issues/57/html-class-options-for-tables

    @classmethod
    def generate_query(cls, query_type, space, client, resolved=False, top_level=True,
                       field_names_used=None, parents=None):
        """

        query_type: "simple" or "resolved"

        Fields top_level, field_names_used and parents should not be specified,
        they are used only for recursion.
        """

        query_label = cls.get_query_label(query_type, space)
        if space == "myspace":
            real_space = client._private_space
        else:
            real_space = space
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
                        "value": real_space
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
                                    parents=copy(parents)  # use a copy to keep the original for the next iteration
                                )
                                subfield_map.update(
                                    {subfield_defn.get("propertyName", subfield_defn["path"]): subfield_defn
                                    for subfield_defn in subfields}
                                )
                        field_definition["structure"] = list(subfield_map.values())

                elif any(issubclass(_type, EmbeddedMetadata) for _type in field.types):
                    if not top_level and field.path in field_names_used:
                        field_definition["propertyName"] = "{}__{}".format(cls.__name__, field.path)
                    if field.multiple:
                        field_definition["ensureOrder"] = True
                    field_definition["structure"] = [{"path": "@type"}]
                    for child_cls in field.types:
                        for ch_field in child_cls.fields:
                            subfield_definition = {
                                "path": expand_uri(ch_field.path, child_cls.context, client)[0],
                                "propertyName": ch_field.path
                            }
                            if issubclass(child_cls, KGObjectV3):
                                subfield_definition["structure"] = {
                                    {"path": "@id"},
                                    {"path": "@type"}
                                }
                            field_definition["structure"].append(subfield_definition)

                # here we add a filter for top-level fields
                if field.types[0] in (int, float, bool, datetime, date):
                    op = "EQUALS"
                else:
                    op = "CONTAINS"
                if top_level:
                    filter = {
                        "op": op,
                        "parameter": field.name
                    }
                    id_elements = [elem for elem in field_definition.get("structure", [])
                                   if elem["path"] == "@id"]
                    if len(id_elements) > 0:
                        # if the field is itself an object, filter on the object's id
                        id_elements[0]["filter"] = filter
                    else:
                        field_definition["filter"] = filter

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
        if "private" in space:  # temporary work-around
            return f"fg-{cls.__name__}-{query_type}-myspace"
        else:
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
                    try:
                        obj = cls.from_uri(self.id, client, scope=scope)
                    except TypeError:
                        pass
                    else:
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

        if "@id" in item:
            item["@id"] = expand_uri(item["@id"], {"kg": "https://kg.ebrains.eu/api/instances/"})[0]
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


"""
id                    https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000000
inputs                [File(content='Demonstration data for validation framework', file_repository=FileRepository(hosted_by=KGProxyV3([<class 'fairgraph.openminds.core.actors.organization.Organization'>], 'https://kg.ebrains.eu/api/instances/7dfdd91f-3d05-424a-80bd-6d1d5dc11cd3'), iri=IRI(self.value), name='VF_paper_demo', repository_type=FileRepositoryType(name='Swift repository', id=https://kg.ebrains.eu/api/instances/25975e2e-f186-4c3f-9352-d460c6969761), id=https://kg.ebrains.eu/api/instances/4a10989f-fd9f-4068-b9c2-28d9a6d7342c), format=ContentType(name='application/json', id=https://kg.ebrains.eu/api/instances/ab0e7c0b-0cae-4a5a-9c75-a0323a3addfb), hash=Hash(algorithm='sha1', digest='716c29320b1e329196ce15d904f7d4e3c7c46685'), iri=IRI(self.value), name='InputResistance_data.json', storage_size=QuantitativeValue(value=34.0, unit=UnitOfMeasurement(name='bytes', id=None)), id=https://kg.ebrains.eu/api/instances/a50435e2-1a64-41c0-ba90-e52bf124a673), SoftwareVersion(name='Elephant', alias='Elephant', version_identifier='0.10.0', id=https://kg.ebrains.eu/api/instances/deaf5b85-bd3d-4937-a1cf-cea45f6e2c2f)]
outputs               [File(content='Demonstration data for validation framework', file_repository=FileRepository(hosted_by=KGProxyV3([<class 'fairgraph.openminds.core.actors.organization.Organization'>], 'https://kg.ebrains.eu/api/instances/7dfdd91f-3d05-424a-80bd-6d1d5dc11cd3'), iri=IRI(self.value), name='VF_paper_demo', repository_type=FileRepositoryType(name='Swift repository', id=https://kg.ebrains.eu/api/instances/06b025ae-43d6-4e7c-8509-ce1eefb4acf6), id=https://kg.ebrains.eu/api/instances/27b8231a-88cf-4264-ace4-dd9fa45d9d60), format=ContentType(name='application/json', id=https://kg.ebrains.eu/api/instances/477faf0c-da36-4172-ad18-dfe44ad817d8), hash=Hash(algorithm='sha1', digest='716c29320b1e329196ce15d904f7d4e3c7c46685'), iri=IRI(self.value), name='InputResistance_data.json', storage_size=QuantitativeValue(value=34.0, unit=UnitOfMeasurement(name='bytes', id=None)), id=https://kg.ebrains.eu/api/instances/8859cc17-947b-4167-9e29-81a02868454a)]
environment           Environment(name='SpiNNaker default 2021-10-13', hardware=HardwareSystem(name='spinnaker', version='not specified', id=https://kg.ebrains.eu/api/instances/0a467c94-cdf8-41f6-bf86-386ce21749a2), configuration=[ParameterSet(context='hardware configuration for SpiNNaker 1M core machine', parameters=[StringParameter(name='parameter1', value='value1'), StringParameter(name='parameter2', value='value2')])], software=[SoftwareVersion(name='numpy', alias='numpy', version_identifier='1.19.3', id=https://kg.ebrains.eu/api/instances/a2252d99-2c16-4a96-9e99-5882675f4069), SoftwareVersion(name='neo', alias='neo', version_identifier='0.9.0', id=https://kg.ebrains.eu/api/instances/22f5ea2f-f7ee-40a8-b759-f3522fcc0b98), SoftwareVersion(name='spyNNaker', alias='spyNNaker', version_identifier='5.0.0', id=https://kg.ebrains.eu/api/instances/bfea4e9f-0ca1-4896-a046-3c31384c2328)], description='Default environment on SpiNNaker 1M core machine as of 2020-10-13 (not really, this is just for example purposes).', id=https://kg.ebrains.eu/api/instances/64f65fa0-7338-406c-9c5a-81545bc05299)
launch_configuration  LaunchConfiguration(name='LaunchConfiguration-268406ad70a3d2c41727a561547473b66950183a', executable='/usr/bin/python', arguments=['-Werror'], environment_variables=ParameterSet(context='environment variables', parameters=[StringParameter(name='COLLAB_ID', value='myspace')]), id=https://kg.ebrains.eu/api/instances/9677046e-2850-44ab-9086-45833f9ccef9)
started_by            Person(digital_identifiers=[ORCID(identifier='https://orcid.org/0000-0001-7405-0455', id=https://kg.ebrains.eu/api/instances/8bbe9569-de0c-4a62-93ef-ab4a60a5cf02)], family_name='Destexhe', given_name='Alain', id=https://kg.ebrains.eu/api/instances/ca4302b8-f130-4c8f-933f-35d9b2c7fbd4)
was_informed_by
status                ActionStatusType(name='queued', id=https://kg.ebrains.eu/api/instances/c3c089db-47aa-4bcd-9646-84b370c16bd3)
resource_usages
tags                  ['string']
description
ended_at_time         2021-05-28 16:32:58.597000+00:00
lookup_label
parameter_sets
started_at_time       2021-05-28 16:32:58.597000+00:00
study_targets
"""

"""
id                    https://kg.ebrains.eu/api/instances/9c87a285-0dae-4028-b417-9093ecfc9ddc
inputs                [File(content='Demonstration data for validation framework', file_repository=FileRepository(hosted_by=KGProxyV3([<class 'fairgraph.openminds.core.actors.organization.Organization'>], 'https://kg.ebrains.eu/api/instances/7dfdd91f-3d05-424a-80bd-6d1d5dc11cd3'), iri=IRI(self.value), name='VF_paper_demo', repository_type=FileRepositoryType(name='Swift repository', id=https://kg.ebrains.eu/api/instances/4d046ca8-be25-4c7f-b6d6-5b35bf3a3664), id=https://kg.ebrains.eu/api/instances/a1351964-ad28-4ce7-8ccd-b0418a8f615c), format=ContentType(name='application/json', id=https://kg.ebrains.eu/api/instances/be522f07-b61c-4167-a84f-773e8a8b92e7), hash=Hash(algorithm='sha1', digest='716c29320b1e329196ce15d904f7d4e3c7c46685'), iri=IRI(self.value), name='InputResistance_data.json', storage_size=QuantitativeValue(value=34.0, unit=UnitOfMeasurement(name='bytes', id=None)), id=https://kg.ebrains.eu/api/instances/db6971a6-ab1d-4e97-ad10-9ac77532f99f), SoftwareVersion(name='Elephant', alias='Elephant', version_identifier='0.10.0', id=https://kg.ebrains.eu/api/instances/ed290bed-3e8e-4cf1-b95a-85d98760e310)]
outputs               [File(content='Demonstration data for validation framework', file_repository=FileRepository(hosted_by=KGProxyV3([<class 'fairgraph.openminds.core.actors.organization.Organization'>], 'https://kg.ebrains.eu/api/instances/7dfdd91f-3d05-424a-80bd-6d1d5dc11cd3'), iri=IRI(self.value), name='VF_paper_demo', repository_type=FileRepositoryType(name='Swift repository', id=https://kg.ebrains.eu/api/instances/bdb2fdca-db72-48c7-867d-24de2e1adc37), id=https://kg.ebrains.eu/api/instances/63513a20-fa0e-4d84-b09c-6927470238f2), format=ContentType(name='application/json', id=https://kg.ebrains.eu/api/instances/87f6330b-8350-41c2-9a33-427d93e0969c), hash=Hash(algorithm='sha1', digest='716c29320b1e329196ce15d904f7d4e3c7c46685'), iri=IRI(self.value), name='InputResistance_data.json', storage_size=QuantitativeValue(value=34.0, unit=UnitOfMeasurement(name='bytes', id=None)), id=https://kg.ebrains.eu/api/instances/488bd6be-e1ec-4463-9e06-0e4c24a51882)]
environment           Environment(name='SpiNNaker default 2021-10-13', hardware=HardwareSystem(name='spinnaker', version='not specified', id=https://kg.ebrains.eu/api/instances/17f432ae-6876-4407-865b-b9a333114d64), configuration=[ParameterSet(context='hardware configuration for SpiNNaker 1M core machine', parameters=[StringParameter(name='parameter1', value='value1'), StringParameter(name='parameter2', value='value2')])], software=[SoftwareVersion(name='numpy', alias='numpy', version_identifier='1.19.3', id=https://kg.ebrains.eu/api/instances/36f290da-c68b-47b1-afd6-aedf643352a5), SoftwareVersion(name='neo', alias='neo', version_identifier='0.9.0', id=https://kg.ebrains.eu/api/instances/bef421f5-7cf5-45e5-9b4c-58a1b5503241), SoftwareVersion(name='spyNNaker', alias='spyNNaker', version_identifier='5.0.0', id=https://kg.ebrains.eu/api/instances/d21abc35-7245-4123-b3ea-b9bb7574e912)], description='Default environment on SpiNNaker 1M core machine as of 2020-10-13 (not really, this is just for example purposes).', id=https://kg.ebrains.eu/api/instances/9bbf37a3-3d11-42e0-9078-aad505ab5089)
launch_configuration  LaunchConfiguration(name='LaunchConfiguration-268406ad70a3d2c41727a561547473b66950183a', executable='/usr/bin/python', arguments=['-Werror'], environment_variables=ParameterSet(context='environment variables', parameters=[StringParameter(name='COLLAB_ID', value='myspace')]), id=https://kg.ebrains.eu/api/instances/2eb5e20c-6409-4aec-ab18-7d035c507ee0)
started_by            Person(digital_identifiers=[ORCID(identifier='https://orcid.org/0000-0001-7405-0455', id=https://kg.ebrains.eu/api/instances/e83b8bc0-b460-4217-ba4f-1fae41a5f1dc)], family_name='Destexhe', given_name='Alain', id=https://kg.ebrains.eu/api/instances/723830ad-2991-4ecd-878f-d16cc2ce2f89)
was_informed_by
status                ActionStatusType(name='queued', id=https://kg.ebrains.eu/api/instances/6f91e353-4207-4160-8ba8-c8da9ccea074)
resource_usages
tags                  ['string']
description
ended_at_time         2021-05-28 16:32:58.597000+00:00
lookup_label          Data analysis by Alain Destexhe on 2021-05-28T16:32:58.597000+00:00 [0000000]
parameter_sets
started_at_time       2021-05-28 16:32:58.597000+00:00
study_targets
"""