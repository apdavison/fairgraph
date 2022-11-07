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
from copy import copy
import logging
from uuid import UUID
from warnings import warn

from requests.exceptions import HTTPError
try:
    from tabulate import tabulate
    have_tabulate = True
except ImportError:
    have_tabulate = False
from .utility import (compact_uri, expand_uri, as_list)
from .registry import Registry, generate_cache_key, lookup, lookup_by_id, lookup_type, lookup_by_iri
from .queries import QueryProperty, Query, Filter
from .errors import ResolutionFailure


logger = logging.getLogger("fairgraph")


def get_filter_value(filters, field):
    value = filters[field.name]
    def is_valid(val):
        return (isinstance(val, (IRI, UUID, *field.types))
                or (isinstance(val, KGProxy) and val.cls in field.types))
    if isinstance(value, list) and len(value) > 0:
        valid_type = all(is_valid(item) for item in value)
        have_multiple = True
    else:
        valid_type = is_valid(value)
        have_multiple = False
    if not valid_type:
        if field.name == "hash":  # bit of a hack
            filter_value = value
        elif isinstance(value, str) and value.startswith("http"):  # for @id
            filter_value = value
        else:
            raise TypeError("{} must be of type {}".format(field.name, field.types))
    filter_items = []
    for item in as_list(value):
        if isinstance(item, IRI):
            filter_item = item.value
        elif hasattr(item, "id"):
            filter_item = item.id
        elif isinstance(item, UUID):
            # todo: consider using client.uri_from_uuid()
            # would require passing client as arg
            filter_item = f"https://kg.ebrains.eu/api/instances/{item}"
        elif isinstance(item, str) and "+" in item:  # workaround for KG bug
            invalid_char_index = item.index("+")
            if invalid_char_index < 3:
                raise ValueError(f"Cannot use {item} as filter, contains invalid characters")
            filter_item = item[:invalid_char_index]
            warn(f"Truncating filter value {item} --> {filter_item}")
        else:
            filter_item = item
        filter_items.append(filter_item)
    if have_multiple:
        return filter_items
    else:
        return filter_items[0]


def normalize_filter(cls, filter_dict):
    filter_queries = {}
    for field in cls.fields:
        if field.name in filter_dict:
            filter_queries[field.name] = get_filter_value(filter_dict, field)
    return filter_queries


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
                        warn(msg)
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

    @property
    def space(self):
        return None

    @property
    def default_space(self):
        return None

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ")"
        return template.format(self=self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.to_jsonld() == other.to_jsonld()

    def to_jsonld(self, client=None, with_type=False):
        data = {
            "@type": self.type
        }
        for field in self.fields:
            value = getattr(self, field.name)
            if value is not None:
                data[field.path] = field.serialize(value, client, with_type=with_type)
        return data

    @classmethod
    def from_jsonld(cls, data, client, resolved=False):
        if "@id" in data:
            #raise Exception("Expected embedded metadata, but received @id: " + str(data))
            warn("Expected embedded metadata, but received @id")
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

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False):
        for field in self.fields:
            if field.intrinsic:
                values = getattr(self, field.name)
                for value in as_list(values):
                    if isinstance(value, (KGObject, EmbeddedMetadata)):
                        if value.space:
                            target_space = value.space
                        elif value.__class__.default_space == "controlled" and value.exists(client) and value.space == "controlled":
                            continue
                        elif space is None and self.space is not None:
                            target_space = self.space
                        else:
                            target_space = space
                        if target_space == "controlled":
                            if value.exists(client) and value.space == "controlled":
                                continue
                            else:
                                raise Exception("Cannot write to controlled space")
                        value.save(client, space=target_space, recursive=True,
                                    activity_log=activity_log)

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

    @classmethod
    def generate_query_property(cls, field, client, filter_parameter=None, use_type_filter=False):

        expanded_path = expand_uri(field.path, cls.context, client)[0]

        if filter_parameter:
            property = QueryProperty(
                expanded_path,
                name=field.path,
                filter=Filter("CONTAINS", parameter=filter_parameter),
                ensure_order=field.multiple,
                properties=[
                    QueryProperty("@type")
                ])
        else:
            property = QueryProperty(
                expanded_path,
                name=field.path,
                properties=[
                    QueryProperty("@type")
                ])

        if use_type_filter:
            property.type_filter = cls.type
            property.name = f"{property.name}__{cls.__name__}"

        properties = []
        for subfield in cls.fields:
            if subfield.intrinsic:
                if any(issubclass(_type, EmbeddedMetadata) for _type in subfield.types):
                    for child_cls in subfield.types:
                        properties.append(
                            child_cls.generate_query_property(
                                subfield, client,
                                use_type_filter=bool(len(subfield.types) > 1)
                            )
                        )
                elif any(issubclass(_type, KGObject) for _type in subfield.types):
                    for child_cls in subfield.types[:1]:
                        properties.append(
                            child_cls.generate_query_property(
                                subfield, client
                            )
                        )
                else:
                    expanded_subpath = expand_uri(subfield.path, cls.context, client)[0]
                    properties.append(
                        QueryProperty(expanded_subpath,
                                      name=subfield.path,
                                      ensure_order=subfield.multiple))

        property.properties.extend(properties)
        return property

    def resolve(self, client, scope="released", use_cache=True, follow_links=0):
        if follow_links > 0:
            for field in self.fields:
                if issubclass(field.types[0], (KGObject, EmbeddedMetadata)):
                    values = getattr(self, field.name)
                    resolved_values = []
                    for value in as_list(values):
                        if isinstance(value, (KGProxy, KGQuery, EmbeddedMetadata)):
                            try:
                                resolved_value = value.resolve(
                                    client, scope=scope, use_cache=use_cache,
                                    follow_links=follow_links - 1)
                            except ResolutionFailure as err:
                                warn(str(err))
                                resolved_values.append(value)
                            else:
                                resolved_values.append(resolved_value)
                        elif isinstance(value, KGObject):  # already resolved
                            resolved_values.append(value)
                    if isinstance(values, (KGProxy, KGObject)):
                        assert len(resolved_values) == 1
                        resolved_values = resolved_values[0]
                    elif values is None:
                        assert len(resolved_values) == 0
                        resolved_values = None
                    setattr(self, field.name, resolved_values)
        return self


class KGObject(object, metaclass=Registry):
    """Base class for Knowledge Graph objects"""
    object_cache = {}  # for caching based on object ids
    save_cache = defaultdict(dict)  # for caching based on queries
    fields = []
    existence_query_fields = ["name"]
    # Note that this default value of existence_query_fields should in
    # many cases be over-ridden.
    # It assumes that "name" is unique within instances of a given type,
    # which may often not be the case.

    def __init__(self, id=None, data=None, space=None, scope=None, **properties):
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
                        warn(msg)
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
        self.scope = scope

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ", space={self.space}, id={self.id})"
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
            "@id": data["@id"],
            "@type": compact_uri(data["@type"], cls.context),
            "@context": data.get("@context", cls.context)
        }
        for key, value in data.items():
            if "__" in key:
                key, type_filter = key.split("__")
                normalised_key = compact_uri(key, cls.context)
                value = [item for item in as_list(value)
                         if item["@type"][0].endswith(type_filter)]
                if normalised_key in D:
                    D[normalised_key].extend(value)
                else:
                    D[normalised_key] = value
            elif key[0] != "@":
                normalised_key = compact_uri(key, cls.context)
                D[normalised_key] = value

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
            # sometimes queries put single items in a list, this removes the enclosing list
            if (not field.multiple) and isinstance(data_item, (list, tuple)) and len(data_item) == 1:
                data_item = data_item[0]
            deserialized_data[field.name] = field.deserialize_v3(data_item, client, resolved=resolved)
        # if cls.__name__ == "ModelVersion":
        #     raise Exception()
        return deserialized_data

    @classmethod
    def from_kg_instance(cls, data, client, scope=None, resolved=False):
        deserialized_data = cls._deserialize_data(data, client, resolved=resolved)
        return cls(id=data["@id"], data=data, scope=scope, **deserialized_data)

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
            return cls.from_kg_instance(data, client, scope=scope, resolved=resolved)

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

    @classmethod
    def from_alias(cls, alias, client, space=None, scope="released", resolved=False):
        if "alias" not in cls.field_names:
            raise AttributeError(f"{cls.__name__} doesn't have an 'alias' field")
        candidates = as_list(
            cls.list(client, size=20, from_index=0, api="query",
                     scope=scope, resolved=resolved, space=space, alias=alias))
        if len(candidates) == 0:
            return None
        elif len(candidates) == 1:
            return candidates[0]
        else:  # KG query does a "contains" lookup, so can get multiple results
            for candidate in candidates:
                if candidate.alias == alias:
                    return candidate
            warn("Multiple objects found with a similar alias, but none match exactly."
                 "Returning the first one found.")
            return candidates[0]

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
    def _get_query_definition(cls, client, normalized_filters, space=None, resolved=False):
        if resolved:
            query_type = "resolved"
        else:
            query_type = "simple"
        if normalized_filters is None:
            filter_keys = None
        else:
            filter_keys = normalized_filters.keys()
        query_label = cls.get_query_label(query_type, space, filter_keys)
        query = client.retrieve_query(query_label)
        if query is None:
            query = cls.generate_query(query_type, space, client=client, filter_keys=filter_keys, resolved=resolved)
            client.store_query(query_label, query, space=space)
        return query

    @classmethod
    def list(cls, client, size=100, from_index=0, api="auto",
             scope="released", resolved=False, space=None, **filters):
        """List all objects of this type in the Knowledge Graph"""

        if api == "auto":
            if filters:
                api = "query"
            else:
                api = "core"

        if api == "query":
            normalized_filters = normalize_filter(cls, filters) or None
            query = cls._get_query_definition(client, normalized_filters, space, resolved)
            instances = client.query(
                normalized_filters, query["@id"],
                space=space,
                from_index=from_index, size=size,
                scope=scope
            ).data
            for instance in instances:
                instance["@context"] = cls.context
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            instances = client.list(
                cls.type,
                space=space,
                from_index=from_index, size=size,
                scope=scope
            ).data
        else:
            raise ValueError("'api' must be either 'query', 'core', or 'auto'")

        return [cls.from_kg_instance(instance, client, scope=scope, resolved=resolved)
                for instance in instances]

    @classmethod
    def count(cls, client, api="auto", scope="released", space=None, **filters):
        if api == "auto":
            if filters:
                api = "query"
            else:
                api = "core"
        if api == "query":
            normalized_filters = normalize_filter(cls, filters) or None
            query = cls._get_query_definition(client, normalized_filters, space, resolved=False)
            response = client.query(normalized_filters, query["@id"], space=space,
                                    from_index=0, size=1, scope=scope)
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            response = client.list(cls.type, space=space, scope=scope, from_index=0, size=1)
        return response.total

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

    def __eq__(self, other):
        return not self.__ne__(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if self.id and other.id and self.id != other.id:
            return True
        for field in self.fields:
            val_self = getattr(self, field.name)
            val_other = getattr(other, field.name)
            if val_self != val_other:
                return True
        return False

    def diff(self, other):
        differences = defaultdict(dict)
        if not isinstance(other, self.__class__):
            differences["type"] = (self.__class__, other.__class__)
        else:
            if self.id != other.id:
                differences["id"] = (self.id, other.id)
            for field in self.fields:
                val_self = getattr(self, field.name)
                val_other = getattr(other, field.name)
                if val_self != val_other:
                    differences["fields"][field.name] = (val_self, val_other)
        return differences

    def exists(self, client):
        """Check if this object already exists in the KnowledgeGraph"""

        if self.id:
            # Since the KG now allows user-specified IDs we can't assume that the presence of
            # an id means the object exists
            data = client.instance_from_full_uri(self.id, use_cache=True,
                                                 scope=self.scope or "in progress", resolved=False)
            # todo: revisit this. Maybe need to query both "released" and "latest/in progress" scopes
            if self.data is None:
                self.data = data
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
                try:
                    query_cache_key = generate_cache_key(query_filter)
                except TypeError as err:
                    raise TypeError(f"Error in generating cache key for {self.__class__.__name__} object: {err}")
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

                normalized_filters = normalize_filter(self.__class__, query_filter) or None
                query = self.__class__._get_query_definition(client, normalized_filters, resolved=False)
                instances = client.query(normalized_filters, query["@id"], size=1,
                                         scope="in progress").data

                if instances:
                    self.id = instances[0]["@id"]
                    KGObject.save_cache[self.__class__][query_cache_key] = self.id

                    if self.data is None:
                        self.data = instances[0]
                    self._update(instances[0], client)
                return bool(instances)

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

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False):
        if recursive:
            for field in self.fields:
                if field.intrinsic:
                    values = getattr(self, field.name)
                    for value in as_list(values):
                        if isinstance(value, (KGObject, EmbeddedMetadata)):
                            if value.space:
                                target_space = value.space
                            elif value.__class__.default_space == "controlled" and value.exists(client) and value.space == "controlled":
                                continue
                            elif space is None and self.space is not None:
                                target_space = self.space
                            else:
                                target_space = space
                            if target_space == "controlled":
                                if value.exists(client) and value.space == "controlled":
                                    continue
                                else:
                                    raise Exception("Cannot write to controlled space")
                            value.save(client, space=target_space, recursive=True,
                                       activity_log=activity_log)
        if space is None:
            if self.space is None:
                space = self.__class__.default_space
            else:
                space = self.space
        logger.info(f"Saving a {self.__class__.__name__} in space {space}")
        if self.exists(client):
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
                        warn("Removing storage size from update because this field is currently locked by the KG")
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
                data,
                space or self.__class__.default_space,
                instance_id=self.uuid)
            self.id = instance_data["@id"]
            self.data = instance_data
            if activity_log:
                activity_log.update(item=self, delta=data, space=self.space, entry_type="create")
        # not handled yet: save existing object to new space - requires changing uuid
        logger.debug("Updating cache for object {}. Current state: {}".format(self.id, self._build_data(client)))
        KGObject.object_cache[self.id] = self

    def delete(self, client, ignore_not_found=True):
        """Deprecate"""
        client.delete_instance(self.uuid, ignore_not_found=ignore_not_found)
        if self.id in KGObject.object_cache:
            KGObject.object_cache.pop(self.id)

    @classmethod
    def by_name(cls, name, client, match="equals", all=False,
                space=None, scope="released", resolved=False):
        # todo: implement 'match'
        objects = cls.list(client, space=space, scope=scope, resolved=resolved, api="query", name=name)
        if len(objects) == 0:
            return None
        elif len(objects) == 1:
            return objects[0]
        elif all:
            return objects
        else:
            warn("Multiple objects with the same name, returning the first. "
                "Use 'all=True' to retrieve them all")
            return objects[0]

    def resolve(self, client, scope=None, use_cache=True, follow_links=0):
        """To avoid having to check if a child attribute is a proxy or a real object,
        a real object resolves to itself.
        """
        use_scope = scope or self.scope or "released"
        if follow_links > 0:
            for field in self.fields:
                if issubclass(field.types[0], (KGObject, EmbeddedMetadata)):
                    values = getattr(self, field.name)
                    resolved_values = []
                    for value in as_list(values):
                        if isinstance(value, (KGProxy, KGQuery, EmbeddedMetadata)):
                            try:
                                resolved_value = value.resolve(
                                    client, scope=use_scope, use_cache=use_cache,
                                    follow_links=follow_links - 1)
                            except ResolutionFailure as err:
                                warn(str(err))
                                resolved_values.append(value)
                            else:
                                resolved_values.append(resolved_value)
                        elif isinstance(value, KGObject):  # already resolved
                            resolved_values.append(value)
                    if isinstance(values, (KGProxy, KGObject)):
                        assert len(resolved_values) == 1
                        resolved_values = resolved_values[0]
                    elif values is None:
                        assert len(resolved_values) == 0
                        resolved_values = None
                    setattr(self, field.name, resolved_values)
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
        data = [("id", self.id), ("space", self.space)] + [
                (field.name, str(getattr(self, field.name, None))) for field in self.fields]
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
    def generate_query_property(cls, field, client, filter_parameter=None, name=None):

        expanded_path = expand_uri(field.path, cls.context, client)[0]

        if filter_parameter:
            filter = Filter("CONTAINS", parameter=filter_parameter)  # should be "EQUALS" for consistency, here we use "CONTAINS" for backwards compatibility
        else:
            filter = None
        property = QueryProperty(
            expanded_path,
            name=name or field.path,
            ensure_order=field.multiple,
            properties=[
                QueryProperty("@id", filter=filter),
                QueryProperty("@type")
            ])

        return property

    @classmethod
    def generate_query(cls, query_type, space, client, filter_keys=None, resolved=False):
        """

        query_type: "simple" or "resolved"
        """
        if resolved:
            raise NotImplementedError("todo")

        query_label = cls.get_query_label(query_type, space, filter_keys)
        if space == "myspace":
            real_space = client._private_space
        else:
            real_space = space
        query = Query(
            node_type=cls.type[0],
            label=query_label,
            space=real_space,
            properties=[
                QueryProperty("@type"),
            ]
        )
        if filter_keys is None:
            filter_keys = []
        for field in cls.fields:
            if field.intrinsic:
                if field.types[0] in (int, float, bool, datetime, date):
                    op = "EQUALS"
                else:
                    op = "CONTAINS"
                if field.name in filter_keys:
                    filter_parameter = field.name
                else:
                    filter_parameter = None
                expanded_path = expand_uri(field.path, cls.context, client)[0]
                if any(issubclass(_type, EmbeddedMetadata) for _type in field.types):
                    for child_cls in field.types:
                        property = child_cls.generate_query_property(
                            field, client,
                            filter_parameter=field.name,
                            use_type_filter=bool(len(field.types) > 1)
                        )
                        query.properties.append(property)
                elif any(issubclass(_type, KGObject) for _type in field.types):
                    for child_cls in field.types[:1]:
                        # take only the first entry, since we don't use type filters
                        # for KGObject where resolved=False
                        if field.name in filter_keys:
                            property = child_cls.generate_query_property(
                                field, client,
                                filter_parameter=field.name,
                                name=field.multiple and f"Q{field.name}" or None
                            )
                            property.required = True
                            query.properties.append(property)
                            if field.multiple:
                                # if filtering by a field that can have multiple values,
                                # the first property will return only the elements in the array
                                # that match, so we add a second property with the same path
                                # to get the full array
                                property = child_cls.generate_query_property(field, client)
                                query.properties.append(property)
                        else:
                            property = child_cls.generate_query_property(field, client)
                            query.properties.append(property)
                else:
                    property = QueryProperty(expanded_path,
                                             name=field.path,
                                             ensure_order=field.multiple)
                    if field.name == "name":
                        property.sorted = True
                    if field.name in filter_keys:
                        property.required = True
                        property.filter=Filter(op, parameter=field.name)
                    query.properties.append(property)
        return query.serialize()

    @classmethod
    def get_query_label(cls, query_type, space, filter_keys=None):
        if space and "private" in space:  # temporary work-around
            label = f"fg-{cls.__name__}-{query_type}-myspace"
        else:
            label = f"fg-{cls.__name__}-{query_type}-{space}"
        if filter_keys:
            label += f"-filters-{'-'.join(sorted(filter_keys))}"
        return label

    @classmethod
    def store_queries(cls, space, client):
        #for query_type, resolved in (("simple", False), ("resolved", True)):
        for query_type, resolved in (("simple", False),):  # temporary until resolved is reimplemented
            query_label = cls.get_query_label(query_type, space)
            query_definition = cls.generate_query(query_type, space, client, resolved=resolved)
            try:
                client.store_query(query_label, query_definition, space=space or cls.default_space)
            except HTTPError as err:
                if err.response.status_code == 401:
                    warn("Unable to store query with id '{}': {}".format(
                        query_label, err.response.text))
                else:
                    raise

    @classmethod
    def retrieve_query(cls, query_type, space, client, filter_keys=None):
        query_label = cls.get_query_label(query_type, space, filter_keys)
        return client.retrieve_query(query_label)

    def children(self, client, follow_links=0):
        if follow_links:
            self.resolve(client, follow_links=follow_links)
        all_children = []
        for field in self.fields:
            if field.is_link:
                children = as_list(getattr(self, field.name))
                all_children.extend(children)
                if follow_links:
                    for child in children:
                        all_children.extend(child.children(client))
        return all_children

    def is_released(self, client, with_children=False):
        """Release status of the node"""
        return client.is_released(self.id, with_children=with_children)

    def release(self, client, with_children=False):
        """Release this node (make it available in public search)."""
        if not self.is_released(client, with_children=with_children):
            if with_children:
                for child in self.children(client):
                    if not child.is_released(client, with_children=False):
                        client.release(child.id)
            return client.release(self.id)

    def unrelease(self, client, with_children=False):
        """Un-release this node (remove it from public search)."""
        response = client.unrelease(self.id)
        if with_children:
            for child in self.children(client):
                client.unrelease(child.id)
        return response


class KGProxy(object):
    """docstring"""

    def __init__(self, cls, uri, preferred_scope="released"):
        if isinstance(cls, str):
            self.cls = lookup(cls)
        elif cls is None:
            self.cls = lookup_by_id(uri)
        else:
            self.cls = cls
        self.id = uri
        self.preferred_scope = preferred_scope

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

    def resolve(self, client, scope=None, use_cache=True, follow_links=0):
        """docstring"""
        if use_cache and self.id in KGObject.object_cache:
            obj = KGObject.object_cache[self.id]
            #if obj:
            #    logger.debug("Retrieving object {} from cache. Status: {}".format(self.id, obj._build_data(client)))
        else:
            scope = scope or self.preferred_scope
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
                raise ResolutionFailure(f"Cannot resolve proxy object of type {self.cls} with id {self.uuid}")
            KGObject.object_cache[self.id] = obj
        if follow_links > 0:
            return obj.resolve(
                client, scope=scope, use_cache=use_cache,
                follow_links=follow_links
            )
        else:
            return obj

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.classes!r}, {self.id!r})'.format(self=self))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and set(self.classes).intersection(other.classes) and self.id == other.id

    def __ne__(self, other):
        return (not isinstance(other, self.__class__)
                or set(self.classes).isdisjoint(other.classes)
                or self.id != other.id)

    @property
    def uuid(self):
        return self.id.split("/")[-1]

    def delete(self, client, ignore_not_found=True):
        """Delete the instance which this proxy represents"""
        obj = self.resolve(client, scope="in progress")
        if obj:
            obj.delete(client, ignore_not_found=ignore_not_found)
        elif not ignore_not_found:
            raise ResolutionFailure("Couldn't resolve object to delete")

    def is_released(self, client, with_children=False):
        """Release status of the node"""
        return client.is_released(self.id, with_children=with_children)


class KGQuery(object):
    """docstring"""

    def __init__(self, classes, filter, preferred_scope="released"):
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
                scope=None, use_cache=True, resolved=False,
                follow_links=0):
        scope = scope or self.preferred_scope
        if resolved:
            query_type = "resolved"
        else:
            query_type = "simple"
        objects = []
        for cls in self.classes:
            normalized_filters = normalize_filter(cls, self.filter) or None
            query = cls._get_query_definition(client, normalized_filters, space, resolved)
            instances = client.query(
                normalized_filters,
                query["@id"],
                space=space,
                size=size,
                from_index=from_index,
                scope=scope).data
            objects.extend(cls.from_kg_instance(instance_data, client)
                           for instance_data in instances)
        for obj in objects:
            KGObject.object_cache[obj.id] = obj

        if follow_links > 0:
            for obj in objects:
                obj.resolve(
                    client, scope=scope, use_cache=use_cache,
                    follow_links=follow_links
                )

        if len(objects) == 1:
            return objects[0]
        else:
            return objects

    def count(self, client, space=None, scope=None):
        scope = scope or self.preferred_scope
        n = 0
        for cls in self.classes:
            n += cls.count(client, api="query", scope=scope,
                           space=space, **self.filter)
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
        assert all(issubclass(item, KGObject) for item in possible_classes)
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
                    obj = KGProxy(kg_cls, item["@id"]).resolve(
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
                    obj = KGProxy(kg_cls, item["@id"])
        else:
            # todo: add a logger.warning that we have dud data
            obj = None

        if obj is not None:
            objects.append(obj)

    if len(objects) == 1:
        return objects[0]
    else:
        return objects
