"""

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


import logging
from warnings import warn

from .utility import expand_uri, as_list, normalize_data
from .queries import QueryProperty
from .errors import ResolutionFailure
from .base import Resolvable, ContainsMetadata, RepresentsSingleObject
from .kgobject import KGObject

logger = logging.getLogger("fairgraph")


class EmbeddedMetadata(ContainsMetadata, Resolvable):

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
        return cls.from_kg_instance(data, client)

    @classmethod
    def from_kg_instance(cls, data, client):
        if "@id" in data:
            warn("Expected embedded metadata, but received @id")
            return None
        deserialized_data = cls._deserialize_data(data, client)
        return cls(data=data, **deserialized_data)

    @classmethod
    def _deserialize_data(cls, data, client):
        D = {
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

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False):
        for field in self.fields:
            if field.intrinsic:
                values = getattr(self, field.name)
                for value in as_list(values):
                    if isinstance(value, ContainsMetadata):
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
                if issubclass(field.types[0], ContainsMetadata):
                    values = getattr(self, field.name)
                    resolved_values = []
                    for value in as_list(values):
                        if isinstance(value, Resolvable):
                            if isinstance(value, KGObject):  # already resolved
                                resolved_values.append(value)
                            else:
                                try:
                                    resolved_value = value.resolve(
                                        client, scope=scope, use_cache=use_cache,
                                        follow_links=follow_links - 1)
                                except ResolutionFailure as err:
                                    warn(str(err))
                                    resolved_values.append(value)
                                else:
                                    resolved_values.append(resolved_value)
                    if isinstance(values, RepresentsSingleObject):
                        assert len(resolved_values) == 1
                        resolved_values = resolved_values[0]
                    elif values is None:
                        assert len(resolved_values) == 0
                        resolved_values = None
                    setattr(self, field.name, resolved_values)
        return self
