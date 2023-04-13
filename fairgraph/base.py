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


from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Dict, List, Union, Any
from typing_extensions import TypeAlias
from copy import copy
import logging
from warnings import warn

from .registry import Registry
from .queries import QueryProperty
from .errors import ResolutionFailure, AuthorizationError
from .utility import (
    as_list,  # temporary for backwards compatibility (a lot of code imports it from here)
    expand_uri,
    normalize_data,
)

if TYPE_CHECKING:
    from .client import KGClient
    from .fields import Field
    from .utility import ActivityLog

logger = logging.getLogger("fairgraph")

JSONdict = Dict[str, Any]  # see https://github.com/python/typing/issues/182 for some possible improvements


class Resolvable:  # all
    def resolve(
        self,
        client: KGClient,
        scope: Optional[str] = None,
        use_cache: bool = True,
        follow_links: int = 0,
    ):
        pass


class ContainsMetadata(Resolvable, metaclass=Registry):  # KGObject and EmbeddedMetadata
    fields: List[Field]
    context: Dict[str, str]
    type_: List[str]
    scope: Optional[str]
    space: Union[str, None]
    default_space: Union[str, None]
    remote_data: Optional[JSONdict]

    def __init__(self, data: Optional[Dict] = None, **properties):
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
                raise NameError(
                    f"""{self.__class__.__name__} does not have fields named "{'", "'.join(properties_copy)}"."""
                )

        # we store the original remote data in `_raw_remote_data`
        # and a normalized version in `remote_data`
        self._raw_remote_data = data  # for debugging
        self.remote_data = {}
        if data:
            self.remote_data = self.to_jsonld(include_empty_fields=True, follow_links=False)

    def to_jsonld(
        self,
        normalized: bool = True,
        follow_links: bool = False,
        include_empty_fields: bool = False,
    ):
        if self.fields:
            data: JSONdict = {"@type": self.type_}
            if hasattr(self, "id") and self.id:
                data["@id"] = self.id
            for field in self.fields:
                if field.intrinsic:
                    expanded_path = field.expanded_path
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

    @classmethod
    def from_jsonld(cls, data: JSONdict, client: KGClient, scope: Optional[str] = None):
        if scope:
            return cls.from_kg_instance(data, client, scope)
        else:
            return cls.from_kg_instance(data, client)

    @classmethod
    def from_kg_instance(cls, data: JSONdict, client: KGClient, scope: Optional[str] = None) -> ContainsMetadata:
        pass

    def save(
        self,
        client: KGClient,
        space: Optional[str] = None,
        recursive: bool = True,
        activity_log: Optional[ActivityLog] = None,
        replace: bool = False,
        ignore_auth_errors: bool = False,
    ):
        pass

    @classmethod
    def set_strict_mode(cls, value: bool, field_names: Optional[Union[str, List[str]]] = None):
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
    def generate_query_properties(cls, filter_keys: Optional[List[str]] = None, follow_links: int = 0):
        if filter_keys is None:
            filter_keys = []
        properties = [QueryProperty("@type")]
        for field in cls.fields:
            if field.intrinsic:
                properties.extend(
                    field.get_query_properties(use_filter=field.name in filter_keys, follow_links=follow_links)
                )
        return properties

    @classmethod
    def _deserialize_data(cls, data: JSONdict, client: KGClient, include_id: bool = False):
        # normalize data by expanding keys
        D = {"@type": data["@type"]}
        if include_id:
            D["@id"] = data["@id"]
        for key, value in data.items():
            if "__" in key:
                key, type_filter = key.split("__")
                normalised_key = expand_uri(key, cls.context)
                value = [item for item in as_list(value) if item["@type"][0].endswith(type_filter)]
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

    def resolve(
        self,
        client: KGClient,
        scope: Optional[str] = None,
        use_cache: bool = True,
        follow_links: int = 0,
    ):
        """To avoid having to check if a child attribute is a proxy or a real object,
        a real object resolves to itself.
        """
        use_scope = scope or self.scope or "released"
        if follow_links > 0:
            for field in self.fields:
                if issubclass(field.types[0], ContainsMetadata):
                    values = getattr(self, field.name)
                    resolved_values: List[Any] = []
                    for value in as_list(values):
                        if isinstance(value, Resolvable):
                            if isinstance(value, ContainsMetadata) and isinstance(value, RepresentsSingleObject):
                                # i.e. isinstance(value, KGObject) - already resolved
                                resolved_values.append(value)
                            else:
                                try:
                                    resolved_value = value.resolve(
                                        client,
                                        scope=use_scope,
                                        use_cache=use_cache,
                                        follow_links=follow_links - 1,
                                    )
                                except ResolutionFailure as err:
                                    warn(str(err))
                                    resolved_values.append(value)
                                else:
                                    resolved_values.append(resolved_value)
                    if isinstance(values, RepresentsSingleObject):
                        assert len(resolved_values) == 1
                        setattr(self, field.name, resolved_values[0])
                    elif values is None:
                        assert len(resolved_values) == 0
                        setattr(self, field.name, None)
                    else:
                        setattr(self, field.name, resolved_values)
        return self


class RepresentsSingleObject(Resolvable):  # KGObject, KGProxy
    id: Optional[str]
    remote_data: Optional[JSONdict]

    def children(self, client: KGClient, follow_links: int = 0) -> List[RepresentsSingleObject]:
        pass

    def is_released(self, client: KGClient, with_children: bool = False) -> bool:
        """Release status of the node"""
        try:
            return client.is_released(self.id, with_children=with_children)
        except AuthorizationError:
            # for unprivileged users
            if self.remote_data and "https://core.kg.ebrains.eu/vocab/meta/firstReleasedAt" in self.remote_data:
                return True
            return False

    def release(self, client: KGClient, with_children: bool = False):
        """Release this node (make it available in public search)."""
        if not self.is_released(client, with_children=with_children):
            if with_children:
                for child in self.children(client):
                    if not child.is_released(client, with_children=False):
                        client.release(child.id)
            return client.release(self.id)

    def unrelease(self, client: KGClient, with_children: bool = False):
        """Un-release this node (remove it from public search)."""
        response = client.unrelease(self.id)
        if with_children:
            for child in self.children(client):
                client.unrelease(child.id)
        return response


class SupportsQuerying:  # KGObject, KGQuery
    pass


class IRI:
    def __init__(self, value: Union[str, IRI]):
        if isinstance(value, IRI):
            iri = value.value
        else:
            iri = value
        if not iri.startswith("http"):
            raise ValueError("Invalid IRI")
        self.value: str = iri

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value

    def __repr__(self):
        return f"IRI({self.value})"

    def __str__(self):
        return self.value

    def to_jsonld(self):
        return self.value
