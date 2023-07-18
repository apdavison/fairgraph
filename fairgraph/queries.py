"""
This module provides Python classes to assist in writing Knowledge Graph queries.
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
from typing import Optional, List, Any, Dict


class Filter:
    """
    A filter for querying Knowledge Graph nodes.

    Args:
        operation (str): The operation for the filter. Options are:
            ("CONTAINS", "EQUALS", "IS_EMPTY", "STARTS_WITH", "ENDS_WITH", "REGEX")
        parameter (str, optional): A parameter name for the filter.
        value (str, optional): The value to filter on.

    Methods:
        serialize: Returns a dictionary containing the serialized filter.

    """

    def __init__(self, operation: str, parameter: Optional[str] = None, value: Optional[str] = None):
        self.operation = operation
        self.parameter = parameter
        self.value = value

    def serialize(self):
        data = {"op": self.operation}
        if self.parameter:
            data["parameter"] = self.parameter
        if self.value:
            data["value"] = self.value
        return data


class QueryProperty:
    """
    A property for a Knowledge Graph query.

    Args:
        path (URI): The path of the property as a URI.
        name (str, optional): The name of the property to be used in the returned results.
        filter (Filter, optional): A filter based on the property.
        sorted (bool, optional): Whether to sort the results based on the property. Defaults to False.
        required (bool, optional): Whether the property is required. Defaults to False.
        ensure_order (bool, optional): Whether to ensure the ordering of results is maintained. Defaults to False.
        properties (List[QueryProperty], optional): A list of sub-properties.
        type_filter (URI, optional): Ensure that only objects that match the given type URI are returned.
        reverse (bool, optional): Whether the link defined by the path should be followed in the reverse direction. Defaults to False.
        expect_single (bool, optional): Whether to expect a single element in the result. Defaults to False.

    Methods:
        add_property: Adds a sub-property to the QueryProperty object.
        serialize: Returns a dictionary containing the serialized QueryProperty.

    Example:
        >>> p = QueryProperty(
        ...    "https://openminds.ebrains.eu/vocab/fullName",
        ...    name="full_name",
        ...    filter=Filter("CONTAINS", parameter="name"),
        ...    sorted=True,
        ...    required=True
        ... )
    """

    def __init__(
        self,
        path: str,
        name: Optional[str] = None,
        filter: Optional[Filter] = None,
        sorted: bool = False,
        required: bool = False,
        ensure_order: bool = False,
        properties: Optional[List[QueryProperty]] = None,
        type_filter: Optional[str] = None,
        reverse: bool = False,
        expect_single: bool = False,
    ):
        self.path = path
        self.name = name
        self.filter = filter
        self.sorted = sorted
        self.required = required
        self.ensure_order = ensure_order
        self.properties = properties or []
        self.type_filter = type_filter
        self.reverse = reverse
        self.expect_single = expect_single

        for property in self.properties:
            if property.sorted:
                raise ValueError("Sorting is only allowed on the root level of a query.")

    def __repr__(self):
        return f"QueryProperty({self.path}, name={self.name})"

    def add_property(self, property: QueryProperty):
        assert isinstance(property, QueryProperty)
        if property.sorted:
            raise ValueError("Sorting is only allowed on the root level of a query.")
        self.properties.append(property)

    def serialize(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "path": self.path,
        }
        if self.name:
            data["propertyName"] = self.name
        if self.filter:
            data["filter"] = self.filter.serialize()
        if self.sorted:
            data["sort"] = True
        if self.required:
            data["required"] = True
        if self.ensure_order:
            data["ensureOrder"] = True
        if self.properties:
            data["structure"] = [property.serialize() for property in self.properties]
        if self.type_filter or self.reverse:
            data["path"] = {"@id": data["path"]}
            if self.type_filter:
                data["path"]["typeFilter"] = {"@id": self.type_filter}
            if self.reverse:
                data["path"]["reverse"] = True
        if self.expect_single:
            data["singleValue"] = "FIRST"
        return data


class Query:
    """
    A Python representation of an EBRAINS Knowledge Graph query,
    which can be serialized to the JSON-LD used by the kg-core query API.

    Args:
        node_type (URI): The URI of the node type to query.
        label (str, optional): A label for this query.
        space (Optional[str], optional): The KG space to query.
        properties (Optional[List[QueryProperty]], optional): A list of QueryProperty
            objects representing the properties to include in the results.

    Methods:
        add_property: Adds a QueryProperty object to the list of properties to include.
        serialize: Returns a JSON-LD representation of the query, suitable for sending to the KG.

    Example:
        >>> q = Query(
        ...    node_type="https://openminds.ebrains.eu/core/ModelVersion",
        ...    label="fg-testing-modelversion",
        ...    space="model",
        ...    properties=[
        ...        QueryProperty("@type"),
        ...        QueryProperty(
        ...            "https://openminds.ebrains.eu/vocab/fullName",
        ...            name="vocab:fullName",
        ...            filter=Filter("CONTAINS", parameter="name"),
        ...            sorted=True,
        ...            required=True,
        ...        ),
        ...        QueryProperty(
        ...            "https://openminds.ebrains.eu/vocab/versionIdentifier",
        ...            name="vocab:versionIdentifier",
        ...            filter=Filter("EQUALS", parameter="version"),
        ...            required=True,
        ...        ),
        ...        QueryProperty(
        ...            "https://openminds.ebrains.eu/vocab/format",
        ...            name="vocab:format",
        ...            ensure_order=True,
        ...            properties=[
        ...                QueryProperty("@id", filter=Filter("EQUALS", parameter="format")),
        ...                QueryProperty("@type"),
        ...            ],
        ...        )
        ...     )
    """

    def __init__(
        self,
        node_type: str,
        label: Optional[str] = None,
        space: Optional[str] = None,
        properties: Optional[List[QueryProperty]] = None,
    ):
        self.node_type = node_type
        self.label = label
        self.space = space
        self.properties = [QueryProperty("@id", filter=Filter("EQUALS", parameter="id"))]
        if space:
            self.properties.append(
                QueryProperty(
                    "https://core.kg.ebrains.eu/vocab/meta/space",
                    name="query:space",
                    filter=Filter("EQUALS", value=self.space),
                )
            )
        else:
            self.properties.append(QueryProperty("https://core.kg.ebrains.eu/vocab/meta/space", name="query:space"))
        if properties:
            self.properties.extend(properties)

    def add_property(self, property: QueryProperty):
        assert isinstance(property, QueryProperty)
        self.properties.append(property)

    def serialize(self) -> Dict[str, Any]:
        query = {
            "@context": {
                "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
                "query": "https://schema.hbp.eu/myQuery/",
                "propertyName": {"@id": "propertyName", "@type": "@id"},
                "merge": {"@type": "@id", "@id": "merge"},
                "path": {"@id": "path", "@type": "@id"},
            },
            "meta": {
                "type": self.node_type,
                "description": "Automatically generated by fairgraph",
            },
            "structure": [property.serialize() for property in self.properties],
        }
        if self.label:
            query["meta"]["name"] = self.label
        return query


# todo: I think only one property can have "sort": True - need to check this
