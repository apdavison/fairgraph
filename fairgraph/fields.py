"""
Representations of metadata fields.
"""

# Copyright 2018-2023 CNRS

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
import warnings
import logging
from datetime import date, datetime
from collections.abc import Iterable, Mapping
from typing import Any, List, Optional, Tuple, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .client import KGClient

from dateutil import parser as date_parser

from .registry import lookup, lookup_type
from .utility import as_list
from .base import IRI, JSONdict
from .kgproxy import KGProxy
from .kgquery import KGQuery
from .kgobject import KGObject
from .embedded import EmbeddedMetadata
from .utility import expand_uri
from .queries import Filter, QueryProperty


logger = logging.getLogger("fairgraph")


global_context = {
    "vocab": "https://openminds.ebrains.eu/vocab/",
}


def is_resolved(item: JSONdict) -> bool:
    return set(item.keys()) not in (set(["@id", "@type"]), set(["@id"]))


def build_kg_object(
    possible_classes: Iterable[Union[EmbeddedMetadata, KGObject]],
    data: Optional[Union[JSONdict, List[JSONdict]]],
    client: Optional[KGClient] = None,
) -> Union[EmbeddedMetadata, KGObject, KGProxy, None, List[Union[EmbeddedMetadata, KGObject, KGProxy]]]:
    """
    Build a KGObject, an EmbeddedMetadata, a KGProxy, or a list of such, based on the data provided.

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
    assert isinstance(data, list)

    objects = []
    for item in data:
        if item is None:
            logger.error(f"Unexpected null. possible_classes={possible_classes} data={data}")
            continue
        logger.debug(f"Building {possible_classes} from {item.get('@id', 'not a node')}")
        if possible_classes is None:
            raise NotImplementedError

        assert isinstance(possible_classes, (list, tuple))
        assert all(issubclass(item, KGObject) for item in possible_classes) or all(
            issubclass(item, EmbeddedMetadata) for item in possible_classes
        )
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
                if "@type" in item and item["@type"] is not None and kg_cls not in as_list(lookup_type(item["@type"])):
                    logger.warning(f"Mismatched types: {kg_cls} <> {item['@type']}")
                    raise Exception("mismatched types")
                    obj = None
                else:
                    obj = KGProxy(kg_cls, item["@id"])
        elif "@type" in item:  # Embedded metadata
            obj = kg_cls.from_kg_instance(item, client)
        else:
            # todo: add a logger.warning that we have dud data
            obj = None

        if obj is not None:
            objects.append(obj)

    if len(objects) == 1:
        return objects[0]
    else:
        return objects


class Field(object):
    """
    Representation of a metadata field.

    Args:
        name (str): The name of the field.
        types (str, date, datetime, int, KGObject, EmbeddedMetadata): The types of values that the field can take.
        path (URI): The globally unique identifier of this field.
        required (bool, optional): Whether the field is required or not. Defaults to False.
        default (Any, optional): The default value of the field if it is not provided.
        multiple (bool, optional): Whether the field can have multiple values or not. Defaults to False.
        strict (bool, optional): Whether strict mode is enabled or not. Defaults to False.
        reverse (str, optional): The name of the reverse field, if any.
        doc (str, optional): The documentation of the field.

    The class also contains machinery for serialization into JSON-LD of values stored in fields in
    KGObjects and EmbeddedMetadata instances, and for de-serialization from JSON-LD into Python objects.
    """

    def __init__(
        self,
        name: str,
        types: Union[
            str,
            type,
            KGObject,
            EmbeddedMetadata,
            Iterable[Union[str, type, KGObject, EmbeddedMetadata]],
        ],
        path: str,
        required: bool = False,
        default: Any = None,
        multiple: bool = False,
        strict: bool = False,
        reverse: Optional[str] = None,
        doc: str = "",
    ):
        self.name = name
        self._types: Tuple[Union[str, type, KGObject, EmbeddedMetadata], ...]
        if isinstance(types, (type, str)):
            self._types = (types,)
        else:
            assert isinstance(types, Iterable)
            self._types = tuple(types)
        self._resolved_types = False
        # later, may need to use lookup() to turn strings into classes
        self.path = path
        self.required = required
        self.default = default
        self.multiple = multiple
        self.strict_mode = strict
        self.reverse = reverse
        self.doc = doc

    def __repr__(self):
        return "Field(name='{}', types={}, path='{}', required={}, multiple={})".format(
            self.name, self._types, self.path, self.required, self.multiple
        )

    @property
    def types(self):
        if not self._resolved_types:
            self._types = tuple([lookup(obj) if isinstance(obj, str) else obj for obj in self._types])
            self._resolved_types = True
        return self._types

    def check_value(self, value):
        def check_single(item):
            if not isinstance(item, self.types):
                if not (
                    isinstance(item, (KGProxy, KGQuery, EmbeddedMetadata))
                    and any(issubclass(cls, _type) for _type in self.types for cls in item.classes)
                ):
                    if item is None and self.required:
                        errmsg = "Field '{}' is required but was not provided.".format(self.name)
                    else:
                        errmsg = "Field '{}' should be of type {}, not {}".format(self.name, self.types, type(item))
                    if self.strict_mode:
                        raise ValueError(errmsg)
                    else:
                        warnings.warn(errmsg)

        if self.required or value is not None:
            if self.multiple and isinstance(value, Iterable) and not isinstance(value, Mapping):
                for item in value:
                    check_single(item)
            else:
                check_single(value)

    @property
    def intrinsic(self):
        """
        Return True If the field contains data that is directly stored in the instance,
        False if the field contains data that is obtained through a query
        """
        return not self.path.startswith("^")

    @property
    def is_link(self) -> bool:
        return issubclass(self.types[0], (KGObject, EmbeddedMetadata))

    @property
    def expanded_path(self) -> str:
        return expand_uri(self.path, global_context)

    def serialize(self, value: Any, follow_links: bool = False):
        """
        Serialize a value to JSON-LD.

        Args:
            value (any): The value to be serialized.
            follow_links (bool): If the value contains graph links, these links
                will be represented using "@id" (follow_links=False) or fully
                serialized recursively (follow_links=True).
        """

        def serialize_single(value):
            if isinstance(value, (str, int, float, dict)):
                return value
            elif isinstance(value, EmbeddedMetadata):
                return value.to_jsonld(follow_links=follow_links)
            elif isinstance(value, IRI):
                return value.to_jsonld()
            elif isinstance(value, KGObject):
                if follow_links:
                    return value.to_jsonld(follow_links=follow_links)
                else:
                    return {"@id": value.id}
            elif isinstance(value, KGProxy):
                return {"@id": value.id}
            elif isinstance(value, (datetime, date)):
                return value.isoformat()
            elif value is None:
                return None
            else:
                raise ValueError("don't know how to serialize this value")

        if isinstance(value, (list, tuple)):
            if self.multiple or not self.strict_mode:
                value = [serialize_single(item) for item in value]
                if len(value) == 1:
                    return value[0]
                else:
                    return value
            elif len(value) == 1:
                return serialize_single(value[0])
            elif self.strict_mode:
                raise AttributeError(f"Single item expected for field {self.name} but received multiple")
            else:
                return value
        else:
            return serialize_single(value)

    def deserialize(self, data: Union[JSONdict, List[JSONdict]], client: KGClient):
        """
        Deserialize a JSON-LD data structure into Python objects.

        Args:
            data: the JSON-LD data
            client: a KG client
        """
        assert self.intrinsic
        if data is None or data == []:
            return None
        try:
            if issubclass(self.types[0], (KGObject, EmbeddedMetadata)):
                return build_kg_object(self.types, data, client=client)
            elif self.types[0] in (datetime, date):
                if isinstance(data, str):
                    if data == "":  # seems like the KG Editor puts empty strings here rather than None?
                        return None
                    return date_parser.parse(data)
                elif isinstance(data, Iterable):
                    return [date_parser.parse(item) for item in data]
                else:
                    raise ValueError("expecting a string or list")
            elif self.types[0] == int:
                if isinstance(data, str):
                    return int(data)
                elif isinstance(data, Iterable):
                    return [int(item) for item in data]
                else:
                    return int(data)
            elif self.types[0] == IRI:
                return IRI(data)
            else:
                return data
        except Exception as err:
            if self.strict_mode:
                raise
            else:
                warnings.warn(str(err))
                return None

    def get_query_properties(self, use_filter=False, follow_links=0):
        """
        Generate one or more QueryProperty instances for this field,
        for use in constructing a KG query definition.
        """
        if use_filter:
            if self.types[0] in (int, float, bool, datetime, date):
                op = "EQUALS"
            else:
                op = "CONTAINS"
            filter = Filter(op, parameter=self.name)
        else:
            filter = None

        properties = []
        if any(issubclass(_type, EmbeddedMetadata) for _type in self.types):
            assert all(issubclass(_type, EmbeddedMetadata) for _type in self.types)
            for cls in self.types:
                if len(self.types) > 1:
                    property_name = f"{self.path}__{cls.__name__}"
                    type_filter = cls.type_[0]
                else:
                    property_name = self.path
                    type_filter = None
                properties.append(
                    QueryProperty(
                        self.expanded_path,
                        name=property_name,
                        filter=filter,
                        required=bool(filter),
                        type_filter=type_filter,
                        ensure_order=self.multiple,
                        properties=cls.generate_query_properties(filter_keys=None, follow_links=follow_links),
                    )
                )
        elif any(issubclass(_type, KGObject) for _type in self.types):
            assert all(issubclass(_type, KGObject) for _type in self.types)
            if follow_links > 0:
                for cls in self.types:
                    property_name = self.path
                    if len(self.types) > 1:
                        property_name = f"{self.path}__{cls.__name__}"
                        type_filter = cls.type_[0]
                    else:
                        type_filter = None

                    have_Q = False
                    if filter and self.multiple:
                        property_name = f"Q{self.name}"
                        if len(self.types) > 1:
                            property_name = f"{property_name}__{cls.__name__}"
                        # if filtering by a field that can have multiple values,
                        # the first property will return only the elements in the array
                        # that match, so we add a second property with the same path
                        # to get the full array
                        have_Q = True
                        properties.append(
                            QueryProperty(
                                self.expanded_path,
                                name=property_name,
                                required=bool(filter),
                                type_filter=None,
                                ensure_order=self.multiple,
                                properties=[
                                    QueryProperty("@id", filter=filter),
                                    QueryProperty("@type"),
                                ],
                            )
                        )
                    properties.append(
                        QueryProperty(
                            self.expanded_path,
                            name=property_name,
                            required=filter and not have_Q,
                            type_filter=type_filter,
                            ensure_order=self.multiple,
                            properties=[
                                QueryProperty("@id", filter=None if have_Q else filter),
                                *cls.generate_query_properties(filter_keys=None, follow_links=follow_links - 1),
                            ],
                        )
                    )
            else:
                have_Q = False
                if filter and self.multiple:
                    # if filtering by a field that can have multiple values,
                    # the first property will return only the elements in the array
                    # that match, so we add a second property with the same path
                    # to get the full array
                    have_Q = True
                    properties.append(
                        QueryProperty(
                            self.expanded_path,
                            name=f"Q{self.name}",
                            required=bool(filter),
                            type_filter=None,
                            ensure_order=self.multiple,
                            properties=[
                                QueryProperty("@id", filter=filter),
                                QueryProperty("@type"),
                            ],
                        )
                    )
                properties.append(
                    QueryProperty(
                        self.expanded_path,
                        name=self.path,
                        required=filter and not have_Q,
                        type_filter=None,
                        ensure_order=self.multiple,
                        properties=[
                            QueryProperty("@id", filter=None if have_Q else filter),
                            QueryProperty("@type"),
                        ],
                    )
                )
        else:
            properties.append(
                QueryProperty(
                    self.expanded_path,
                    name=self.path,
                    filter=filter,
                    required=bool(filter),
                    sorted=bool(self.name == "name"),
                    ensure_order=self.multiple,
                )
            )
        return properties
