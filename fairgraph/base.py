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
from .utility import (compact_uri, expand_uri, as_list, normalize_data)
from .registry import Registry, generate_cache_key, lookup, lookup_type
from .queries import QueryProperty, Query, Filter
from .errors import ResolutionFailure, AuthorizationError, ResourceExistsError


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
            raise TypeError("{} must be of type {}, not {}".format(field.name, field.types, type(value)))
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

    def to_jsonld(self):
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
        self._raw_remote_data = data

    @property
    def space(self):
        return None

    @property
    def default_space(self):
        return None

    def _get_remote_data(self):
        return self._data

    def _set_remote_data(self, value):
        self._data = normalize_data(value, self.context)

    data = property(fget=_get_remote_data, fset=_set_remote_data)

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ")"
        return template.format(self=self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.to_jsonld() == other.to_jsonld()

    def to_jsonld(self, normalized=True, follow_links=False, include_empty_fields=False):
        data = {
            "@type": self.type_
        }
        for field in self.fields:
            assert field.intrinsic
            expanded_path = expand_uri(field.path, self.context)
            value = getattr(self, field.name)
            if include_empty_fields or field.required or value is not None:
                data[expanded_path] = field.serialize(value, follow_links=follow_links)
        if normalized:
            return normalize_data(data, self.context)
        else:
            return data

    @classmethod
    def from_jsonld(cls, data, client):
        if "@id" in data:
            #raise Exception("Expected embedded metadata, but received @id: " + str(data))
            warn("Expected embedded metadata, but received @id")
            return None

        args = {}
        for field in cls.fields:
            expanded_path = expand_uri(field.path, cls.context)
            data_item = data.get(field.path, data.get(expanded_path))
            args[field.name] = field.deserialize(data_item, client)
        return cls(data=data, **args)

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

    # @classmethod
    # def generate_query_property(cls, field, filter_parameter=None, use_type_filter=True, follow_links=0):

    #     expanded_path = expand_uri(field.path, cls.context)

    #     if filter_parameter:
    #         property = QueryProperty(
    #             expanded_path,
    #             name=field.path,
    #             filter=Filter("CONTAINS", parameter=filter_parameter),
    #             ensure_order=field.multiple,
    #             properties=[
    #                 QueryProperty("@type")
    #             ])
    #     else:
    #         property = QueryProperty(
    #             expanded_path,
    #             name=field.path,
    #             properties=[
    #                 QueryProperty("@type")
    #             ])

    #     if use_type_filter and len(field._types) > 1:
    #         property.type_filter = cls.type_
    #         property.name = f"{property.name}__{cls.__name__}"

    #     properties = []
    #     for subfield in cls.fields:
    #         if subfield.intrinsic:
    #             if any(issubclass(_type, EmbeddedMetadata) for _type in subfield.types):
    #                 for child_cls in subfield.types:
    #                     properties.append(
    #                         child_cls.generate_query_property(
    #                             subfield,
    #                             follow_links=follow_links
    #                         )
    #                     )
    #             elif any(issubclass(_type, KGObject) for _type in subfield.types):
    #                 for child_cls in subfield.types:
    #                     properties.append(
    #                         child_cls.generate_query_property(
    #                             subfield,
    #                             follow_links=follow_links
    #                         )
    #                     )
    #             else:
    #                 expanded_subpath = expand_uri(subfield.path, cls.context)
    #                 properties.append(
    #                     QueryProperty(expanded_subpath,
    #                                   name=subfield.path,
    #                                   ensure_order=subfield.multiple))

    #     property.properties.extend(properties)
    #     #breakpoint()
    #     return property

    @classmethod
    def generate_query_properties(cls, filter_keys=None, follow_links=0):
        if filter_keys is None:
            filter_keys = []
        properties=[
            QueryProperty("@type")
        ]
        for field in cls.fields:
            if field.intrinsic:
                properties.extend(
                    field.get_query_properties(
                        use_filter=field.name in filter_keys,
                        follow_links=follow_links
                    )
                )
        return properties

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

        # we store the original remote data in `_raw_remote_data`
        # and a normalized version in `remote_data`
        self._raw_remote_data = data  # for debugging
        self.remote_data = {}
        if data:
            self.remote_data = self.to_jsonld(include_empty_fields=True, follow_links=False)
        self.scope = scope
        self.allow_update = True

    def __repr__(self):
        template_parts = ("{}={{self.{}!r}}".format(field.name, field.name)
                            for field in self.fields if getattr(self, field.name) is not None)
        template = "{self.__class__.__name__}(" + ", ".join(template_parts) + ", space={self.space}, id={self.id})"
        return template.format(self=self)

    @property
    def space(self):
        if self._raw_remote_data:
            if "https://schema.hbp.eu/myQuery/space" in self._raw_remote_data:
                self._space = self._raw_remote_data["https://schema.hbp.eu/myQuery/space"]
            elif "https://core.kg.ebrains.eu/vocab/meta/space" in self._raw_remote_data:
                self._space = self._raw_remote_data["https://core.kg.ebrains.eu/vocab/meta/space"]
        return self._space

    @classmethod
    def _deserialize_data(cls, data, client):
        # normalize data by expanding keys
        D = {
            "@id": data["@id"],
            "@type": data["@type"]
        }
        for key, value in data.items():
            if "__" in key:
                key, type_filter = key.split("__")
                normalised_key = expand_uri(key, cls.context)
                value = [item for item in as_list(value)
                         if item["@type"][0].endswith(type_filter)]
                if normalised_key in D:
                    D[normalised_key].extend(value)
                else:
                    D[normalised_key] = value
            elif key.startswith("Q"):  # for 'Q' fields in data from queries
                D[key] = value
            elif key[0] != "@":
                normalised_key = expand_uri(key, cls.context)
                D[normalised_key] = value

        for otype in expand_uri(as_list(cls.type_), cls.context):
            if otype not in D["@type"]:
                raise TypeError("type mismatch {} - {}".format(otype, D["@type"]))
        deserialized_data = {}
        for field in cls.fields:
            expanded_path = expand_uri(field.path, cls.context)
            if field.intrinsic:
                data_item = D.get(expanded_path)
            else:
                data_item = D["@id"]
            # sometimes queries put single items in a list, this removes the enclosing list
            if (not field.multiple) and isinstance(data_item, (list, tuple)) and len(data_item) == 1:
                data_item = data_item[0]
            deserialized_data[field.name] = field.deserialize(data_item, client)
        return deserialized_data

    @classmethod
    def from_kg_instance(cls, data, client, scope=None):
        deserialized_data = cls._deserialize_data(data, client)
        return cls(id=data["@id"], data=data, scope=scope, **deserialized_data)

    # @classmethod
    # def _fix_keys(cls, data):
    #     """
    #     The KG Query API does not allow the same field name to be used twice in a document.
    #     This is a problem when resolving linked nodes which use the same field names
    #     as the 'parent'. As a workaround, we prefix the field names in the linked node
    #     with the class name.
    #     This method removes this prefix.
    #     This feels like a kludge, and I'd be happy to find a better solution.
    #     """
    #     prefix = cls.__name__ + "__"
    #     for key in list(data):
    #         # need to use list() in previous line to avoid
    #         # "dictionary keys changed during iteration" error in Python 3.8+
    #         if key.startswith(prefix):
    #             fixed_key = key.replace(prefix, "")
    #             data[fixed_key] = data.pop(key)
    #     return data

    @classmethod
    def from_uri(cls, uri, client, use_cache=True, scope="released"):
        data = client.instance_from_full_uri(uri, use_cache=use_cache, scope=scope)
        if data is None:
            return None
        else:
            return cls.from_kg_instance(data, client, scope=scope)

    @classmethod
    def from_uuid(cls, uuid, client, use_cache=True, scope="released"):
        logger.info("Attempting to retrieve {} with uuid {}".format(cls.__name__, uuid))
        if len(uuid) == 0:
            raise ValueError("Empty UUID")
        try:
            val = UUID(uuid, version=4)  # check validity of uuid
        except ValueError as err:
            raise ValueError("{} - {}".format(err, uuid))
        uri = cls.uri_from_uuid(uuid, client)
        return cls.from_uri(uri, client, use_cache=use_cache, scope=scope)

    @classmethod
    def from_id(cls, id, client, use_cache=True, scope="released"):
        if hasattr(cls, "type_") and cls.type_:
            if id.startswith("http"):
                return cls.from_uri(id, client, use_cache=use_cache, scope=scope)
            else:
                return cls.from_uuid(id, client, use_cache=use_cache, scope=scope)
        else:
            if id.startswith("http"):
                uri = id
            else:
                uri = client.uri_from_uuid(id)
            data = client.instance_from_full_uri(uri, use_cache=use_cache, scope=scope)
            cls_from_data = lookup_type(data["@type"])
            return cls_from_data.from_kg_instance(data, client, scope=scope)

    @classmethod
    def from_alias(cls, alias, client, space=None, scope="released"):
        if "alias" not in cls.field_names:
            raise AttributeError(f"{cls.__name__} doesn't have an 'alias' field")
        candidates = as_list(
            cls.list(client, size=20, from_index=0, api="query",
                     scope=scope, space=space, alias=alias))
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
    def _get_query_definition(cls, client, normalized_filters, space=None, follow_links=0, use_stored_query=False):
        if follow_links:
            query_type = f"resolved-{follow_links}"
        else:
            query_type = "simple"
        if normalized_filters is None:
            filter_keys = None
        else:
            filter_keys = normalized_filters.keys()
        query = None
        if use_stored_query:
            query_label = cls.get_query_label(query_type, space, filter_keys)
            query = client.retrieve_query(query_label)
        if query is None:
            query = cls.generate_query(
                query_type, space, client=client,
                filter_keys=filter_keys, follow_links=follow_links)
            if use_stored_query:
                client.store_query(query_label, query, space=space)
        return query

    @classmethod
    def list(cls, client, size=100, from_index=0, api="auto",
             scope="released", space=None,
             follow_links=0, **filters):
        """List all objects of this type in the Knowledge Graph"""

        if api == "auto":
            if filters:
                api = "query"
            else:
                api = "core"

        if api == "query":
            normalized_filters = normalize_filter(cls, filters) or None
            query = cls._get_query_definition(client, normalized_filters, space, follow_links=follow_links)
            instances = client.query(
                normalized_filters, query,
                space=space,
                from_index=from_index, size=size,
                scope=scope
            ).data
            for instance in instances:
                instance["@context"] = cls.context
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            if follow_links:
                raise NotImplementedError("Following links with api='core' not yet implemented")
            instances = client.list(
                cls.type_,
                space=space,
                from_index=from_index, size=size,
                scope=scope
            ).data
        else:
            raise ValueError("'api' must be either 'query', 'core', or 'auto'")

        return [cls.from_kg_instance(instance, client, scope=scope)
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
            query = cls._get_query_definition(client, normalized_filters, space)
            response = client.query(normalized_filters, query, space=space,
                                    from_index=0, size=1, scope=scope)
        elif api == "core":
            if filters:
                raise ValueError("Cannot use filters with api='core'")
            response = client.list(cls.type_, space=space, scope=scope, from_index=0, size=1)
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
        query = {}
        for field in query_fields:
            value = field.serialize(getattr(self, field.name), follow_links=False)
            if isinstance(value, dict) and "@id" in value:
                value = value["@id"]
            query[field.name] = value
        return query

    def _update_empty_fields(self, data, client):
        """Replace any empty fields (value None) with the supplied data"""
        cls = self.__class__
        deserialized_data = cls._deserialize_data(data, client)
        for field in cls.fields:
            current_value = getattr(self, field.name, None)
            if current_value is None:
                value = deserialized_data[field.name]
                setattr(self, field.name, value)
        for key, value in data.items():
            expanded_path = expand_uri(key, cls.context)
            self.remote_data[expanded_path] = data[key]

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
                                                 scope=self.scope or "any",
                                                 require_full_data=False)
            if self._raw_remote_data is None:
                self._raw_remote_data = data
            obj_exists = bool(data)
            if obj_exists:
                self._update_empty_fields(data, client)  # also updates `remote_data`
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
                    if cached_obj and cached_obj.remote_data:
                        self._raw_remote_data = cached_obj._raw_remote_data
                        self.remote_data = cached_obj.remote_data  # copy or update needed?
                    return True

                normalized_filters = normalize_filter(self.__class__, query_filter) or None
<<<<<<< HEAD
                query = self.__class__._get_query_definition(client, normalized_filters, resolved=False)
                instances = client.query(normalized_filters, query, size=1, scope="any").data
=======
                query = self.__class__._get_query_definition(client, normalized_filters)
                instances = client.query(normalized_filters, query, size=1,
                                         scope="any").data
>>>>>>> abc63c9 (Remove "resolved" keyword argument and replace (partially) with "follow_links".)

                if instances:
                    self.id = instances[0]["@id"]
                    KGObject.save_cache[self.__class__][query_cache_key] = self.id
                    self._update_empty_fields(instances[0], client)  # also updates `remote_data`
                return bool(instances)

    def modified_data(self):
        current_data = self.to_jsonld(include_empty_fields=True, follow_links=False)
        modified_data = {}
        for key, current_value in current_data.items():
            if not key.startswith("@"):
                assert key.startswith("http")  # keys should all be expanded by this point
                remote_value = self.remote_data.get(key, None)
                if current_value != remote_value:
                    modified_data[key] = current_value
        return modified_data

    def to_jsonld(self, normalized=True, follow_links=False, include_empty_fields=False):
        if self.fields:
            data = {
                "@type": self.type_
            }
            if self.id:
                data["@id"] = self.id
            for field in self.fields:
                if field.intrinsic:
                    expanded_path = expand_uri(field.path, self.context)
                    value = getattr(self, field.name)
                    if include_empty_fields or field.required or value is not None:
                        serialized = field.serialize(value, follow_links=follow_links)
                        if expanded_path in data:
                            if isinstance(data[expanded_path], list):
                                data[expanded_path].append(serialized)
                            else:
                                data[expanded_path] = [data[expanded_path], serialized]
                        else:
                            data[expanded_path] = serialized
            if normalized:
                return normalize_data(data, self.context)
            else:
                return data
        else:
            raise NotImplementedError("to be implemented by child classes")

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False, ignore_auth_errors=False):
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
            if not self.allow_update:
                logger.info(f"  - not updating {self.__class__.__name__}(id={self.id}), update not allowed by user")
                if activity_log:
                    activity_log.update(item=self, delta=None, space=space, entry_type="no-op")
            else:
                # update
                local_data = self.to_jsonld()
                if replace:
                    logger.info(f"  - replacing - {self.__class__.__name__}(id={self.id})")
                    if activity_log:
                        activity_log.update(item=self, delta=local_data, space=space, entry_type="replacement")
                    try:
                        client.replace_instance(self.uuid, local_data)
                        # what does this return? Can we use it to update `remote_data`?
                    except AuthorizationError as err:
                        if ignore_auth_errors:
                            logger.error(str(err))
                        else:
                            raise
                    else:
                        self.remote_data = local_data
                else:
                    modified_data = self.modified_data()
                    if modified_data:
                        logger.info(f"  - updating - {self.__class__.__name__}(id={self.id}) - fields changed: {modified_data.keys()}")
                        skip_update = False
                        if "vocab:storageSize" in modified_data:
                            warn("Removing storage size from update because this field is currently locked by the KG")
                            modified_data.pop("vocab:storageSize")
                            skip_update = len(modified_data) == 0

                        if skip_update:
                            if activity_log:
                                activity_log.update(item=self, delta=None, space=space, entry_type="no-op")
                        else:
                            try:
                                client.update_instance(self.uuid, modified_data)
                            except AuthorizationError as err:
                                if ignore_auth_errors:
                                    logger.error(str(err))
                                else:
                                    raise
                            else:
                                self.remote_data = local_data
                            if activity_log:
                                activity_log.update(item=self, delta=modified_data, space=space, entry_type="update")
                    else:
                        logger.info(f"  - not updating {self.__class__.__name__}(id={self.id}), unchanged")
                        if activity_log:
                            activity_log.update(item=self, delta=None, space=space, entry_type="no-op")
        else:
            # create new
            local_data = self.to_jsonld()
            logger.info("  - creating instance with data {}".format(local_data))
            try:
                instance_data = client.create_new_instance(
                    local_data,
                    space or self.__class__.default_space,
                    instance_id=self.uuid)
            except (AuthorizationError, ResourceExistsError) as err:
                if ignore_auth_errors:
                    logger.error(str(err))
                    if activity_log:
                        activity_log.update(item=self, delta=local_data, space=self.space, entry_type="create-error")
                else:
                    raise
            else:
                self.id = instance_data["@id"]
                self._raw_remote_data = instance_data
                self.remote_data = local_data
                if activity_log:
                    activity_log.update(item=self, delta=instance_data, space=self.space, entry_type="create")
        # not handled yet: save existing object to new space - requires changing uuid
        if self.id:
            logger.debug("Updating cache for object {}. Current state: {}".format(self.id, self.to_jsonld()))
            KGObject.object_cache[self.id] = self
        else:
            logger.warning("Object has no id - see log for the underlying error")

    def delete(self, client, ignore_not_found=True):
        """Deprecate"""
        client.delete_instance(self.uuid, ignore_not_found=ignore_not_found)
        if self.id in KGObject.object_cache:
            KGObject.object_cache.pop(self.id)

    @classmethod
    def by_name(cls, name, client, match="equals", all=False,
                space=None, scope="released"):
        objects = cls.list(client, space=space, scope=scope, api="query", name=name)
        if match == "equals":
            objects = [obj for obj in objects if obj.name == name]
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

    # @classmethod
    # def generate_query_property(cls, field, filter_parameter=None, name=None,
    #                             use_type_filter=True, follow_links=0):

    #     expanded_path = expand_uri(field.path, cls.context)

    #     if filter_parameter:
    #         filter = Filter("CONTAINS", parameter=filter_parameter)  # should be "EQUALS" for consistency, here we use "CONTAINS" for backwards compatibility
    #     else:
    #         filter = None

    #     children = []
    #     if follow_links > 0:
    #         for child_field in cls.fields:
    #             if child_field.intrinsic:
    #                 expanded_child_path = expand_uri(child_field.path, cls.context)
    #                 if any(issubclass(_type, EmbeddedMetadata) for _type in child_field.types):
    #                     for child_cls in child_field.types:
    #                         child_property = child_cls.generate_query_property(
    #                             child_field,
    #                             follow_links=follow_links - 1
    #                         )
    #                         children.append(child_property)
    #                 elif any(issubclass(_type, KGObject) for _type in child_field.types):
    #                     if follow_links > 1:
    #                         include_types = child_field.types
    #                         use_type_filter = True
    #                     else:
    #                         include_types = child_field.types[0:1]
    #                         use_type_filter = False
    #                     for child_cls in include_types:
    #                         child_property = child_cls.generate_query_property(
    #                             child_field,
    #                             use_type_filter=use_type_filter,
    #                             follow_links=follow_links - 1)
    #                         children.append(child_property)
    #                 else:
    #                     child_property = QueryProperty(expanded_child_path,
    #                                                    name=child_field.path,
    #                                                    ensure_order=child_field.multiple)
    #                     if child_field.name == "name":
    #                         child_property.sorted = True
    #                     children.append(child_property)

    #     property = QueryProperty(
    #         expanded_path,
    #         name=name or field.path,
    #         ensure_order=field.multiple,
    #         properties=[
    #             QueryProperty("@id", filter=filter),
    #             QueryProperty("@type")
    #         ] + children)

    #     if use_type_filter and len(field.types) > 1:
    #         property.type_filter = cls.type_[0]
    #         property.name = f"{property.name}__{cls.__name__}"

    #     return property

    @classmethod
    def generate_query_properties(cls, filter_keys=None, follow_links=0):
        if filter_keys is None:
            filter_keys = []
        properties=[
            QueryProperty("@type")
        ]
        for field in cls.fields:
            if field.intrinsic:
                properties.extend(
                    field.get_query_properties(
                        use_filter=field.name in filter_keys,
                        follow_links=follow_links
                    )
                )
        return properties

    @classmethod
    def generate_query(cls, query_type, space, client, filter_keys=None, follow_links=0):
        """

        query_type: "simple" or "resolved-n"
        """

        query_label = cls.get_query_label(query_type, space, filter_keys)
        if space == "myspace":
            real_space = client._private_space
        else:
            real_space = space
        query = Query(
            node_type=cls.type_[0],
            label=query_label,
            space=real_space,
            properties=cls.generate_query_properties(filter_keys, follow_links=follow_links)
        )
        # for field in cls.fields:
        #     if field.intrinsic:
        #         if field.types[0] in (int, float, bool, datetime, date):
        #             op = "EQUALS"
        #         else:
        #             op = "CONTAINS"
        #         if field.name in filter_keys:
        #             filter_parameter = field.name
        #         else:
        #             filter_parameter = None
        #         expanded_path = expand_uri(field.path, cls.context)
        #         if any(issubclass(_type, EmbeddedMetadata) for _type in field.types):
        #             for child_cls in field.types:
        #                 property = child_cls.generate_query_property(
        #                     field,
        #                     filter_parameter=filter_parameter,
        #                     follow_links=follow_links
        #                 )
        #                 query.properties.append(property)
        #         elif any(issubclass(_type, KGObject) for _type in field.types):
        #             if query_type == "simple":  # equivalent: if follow_links == 0
        #                 types_slice = slice(None, 1, None)
        #                 # take only the first entry, since we don't use type filters
        #                 # for KGObject where we're not following links
        #                 use_type_filter = False
        #             else:
        #                 types_slice = slice(None)
        #                 use_type_filter = True
        #             for child_cls in field.types[types_slice]:
        #                 if field.name in filter_keys:
        #                     property = child_cls.generate_query_property(
        #                         field,
        #                         filter_parameter=filter_parameter,
        #                         use_type_filter=use_type_filter,
        #                         name=field.multiple and f"Q{field.name}" or None
        #                     )
        #                     property.required = True
        #                     query.properties.append(property)
        #                     if field.multiple:
        #                         # if filtering by a field that can have multiple values,
        #                         # the first property will return only the elements in the array
        #                         # that match, so we add a second property with the same path
        #                         # to get the full array
        #                         property = child_cls.generate_query_property(
        #                             field,
        #                             use_type_filter=use_type_filter,
        #                             follow_links=follow_links)
        #                         query.properties.append(property)
        #                 else:
        #                     property = child_cls.generate_query_property(
        #                         field,
        #                         follow_links=follow_links,
        #                         use_type_filter=use_type_filter)
        #                     query.properties.append(property)
        #         else:
        #             property = QueryProperty(expanded_path,
        #                                      name=field.path,
        #                                      ensure_order=field.multiple)
        #             if field.name == "name":
        #                 property.sorted = True
        #             if field.name in filter_keys:
        #                 property.required = True
        #                 property.filter=Filter(op, parameter=field.name)
        #             query.properties.append(property)
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
        for query_type, follow_links in (("simple", 0), ("resolved-1", 1)):
            query_label = cls.get_query_label(query_type, space)
            query_definition = cls.generate_query(query_type, space, client, follow_links=follow_links)
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
        try:
            return client.is_released(self.id, with_children=with_children)
        except AuthorizationError:
            # for unprivileged users
            if "https://core.kg.ebrains.eu/vocab/meta/firstReleasedAt" in self.remote_data:
                return True
            return False

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

    def export(self, path, single_file=False):
        """
        Export metadata as files in JSON-LD format.

        If any objects do not have IDs, these will be generated.

        If `single_file` is False, then `path` must be the path to a directory,
        and each object will be exported as a file named for the object ID.

        If `single_file` is True, then `path` should be the path to a file
        with extension ".jsonld". This file will contain metadata for all objects.
        """
        raise NotImplementedError("todo")


class KGProxy(object):
    """docstring"""

    def __init__(self, cls, uri, preferred_scope="released"):
        if isinstance(cls, str):
            self.cls = lookup(cls)
        else:
            self.cls = cls
        self.id = uri
        self.preferred_scope = preferred_scope

    @property
    def type(self):
        try:
            return self.cls.type_
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
        try:
            obj = self.resolve(client, scope="in progress")
        except ResolutionFailure as err:
            logger.warning(str(err))
            obj = None
        if obj:
            obj.delete(client, ignore_not_found=ignore_not_found)
        elif not ignore_not_found:
            raise ResolutionFailure("Couldn't resolve object to delete")

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
                scope=None, use_cache=True, follow_links=0):
        scope = scope or self.preferred_scope
        if follow_links > 0:
            query_type = f"resolved-{follow_links}"
        else:
            query_type = "simple"
        objects = []
        for cls in self.classes:
            normalized_filters = normalize_filter(cls, self.filter) or None
            query = cls._get_query_definition(client, normalized_filters, space, follow_links=follow_links)
            instances = client.query(
                normalized_filters,
                query,
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


def is_resolved(item):
    return set(item.keys()) not in (set(["@id", "@type"]), set(["@id"]))


def build_kg_object(possible_classes, data, client=None):
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
                    if item["@type"] == cls.type_:
                        kg_cls = cls
                        break
            else:
                kg_cls = possible_classes

        else:
            kg_cls = possible_classes[0]

        if "@id" in item:
            # the following line is only relevant to test data,
            # for real data it is always an expanded uri
            item["@id"] = expand_uri(item["@id"], {"kg": "https://kg.ebrains.eu/api/instances/"})
            if is_resolved(item):
                try:
                    obj = kg_cls.from_kg_instance(item, client)
                except (ValueError, KeyError) as err:
                    # to add: emit a warning
                    logger.warning("Error in building {}: {}".format(kg_cls.__name__, err))
                    obj = KGProxy(kg_cls, item["@id"]).resolve(client)
                    # todo: provide space and scope
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

"""
fp = open(path_expected, "w")
json.dump(generated, fp, indent=2)
fp.close()
"""