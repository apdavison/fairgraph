"""
Representations of metadata fields

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


import warnings
from datetime import date, datetime
from collections.abc import Iterable, Mapping

from dateutil import parser as date_parser

from .registry import lookup
from .base import (KGObject, KGProxy, KGQuery, MockKGObject, Distribution,
                   StructuredMetadata, IRI, build_kg_object)


class Field(object):
    """Representation of a metadata field"""

    def __init__(self, name, types, path, required=False, default=None, multiple=False,
                 strict=True, reverse=None, doc=""):
        self.name = name
        if isinstance(types, (type, str)):
            self._types = (types,)
        else:
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
            self.name, self._types, self.path, self.required, self.multiple)

    @property
    def types(self):
        if not self._resolved_types:
            self._types = tuple(
                [lookup(obj) if isinstance(obj, str) else obj
                 for obj in self._types]
            )
            self._resolved_types = True
        return self._types

    def check_value(self, value):
        def check_single(item):
            if not isinstance(item, self.types):
                if not (isinstance(item, (KGProxy, KGQuery))
                        and any(issubclass(cls, _type) for _type in self.types for cls in item.classes)):
                    if not isinstance(item, MockKGObject):  # this check could be stricter
                        if item is None and self.required:
                            errmsg = "Field '{}' is required but was not provided.".format(
                                     self.name)
                        else:
                            errmsg = "Field '{}' should be of type {}, not {}".format(
                                     self.name, self.types, type(item))
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

    def serialize(self, value, client, for_query=False):
        def serialize_single(value):
            if isinstance(value, (str, int, float, dict)):
                return value
            elif hasattr(value, "to_jsonld"):
                return value.to_jsonld(client)
            elif isinstance(value, (KGObject, KGProxy)):
                if for_query:
                    return value.id
                else:
                    return {
                        "@id": value.id,
                        "@type": value.type
                    }
            elif isinstance(value, (datetime, date)):
                return value.isoformat()
            elif value is None:
                return None
            else:
                raise ValueError("don't know how to serialize this value")
        if isinstance(value, (list, tuple)):
            if self.multiple:
                value = [serialize_single(item) for item in value]
                if len(value) == 1:
                    return value[0]
                else:
                    return value
            else:
                return value
        else:
            return serialize_single(value)

    def deserialize(self, data, client, resolved=False):

        if data is None:
            return data
        try:
            if not self.intrinsic:
                query_filter = {
                    "nexus": {
                        "path": self.path[1:],  # remove initial ^
                        "op": "eq",  # OR? "eq" if self.multiple else "in",  # maybe ok for 1:n and n:1, but not n:n
                        "value": data
                    },
                    "query": {
                        self.reverse: data
                    }
                }
                # context_key = query_filter["path"].split(":")[0]  # e.g. --> 'prov', 'nsg'
                # query_context = {context_key: TODO: lookup contexts}
                query_context = {
                    "prov": "http://www.w3.org/ns/prov#",
                    "schema": "http://schema.org/",
                    "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
                }
                return KGQuery(self.types, query_filter, query_context)
            if Distribution in self.types:
                return build_kg_object(Distribution, data)
            elif issubclass(self.types[0], (KGObject, StructuredMetadata)):
                if len(self.types) > 1 or self.types[0] == KGObject:
                    return build_kg_object(None, data, resolved=resolved, client=client)
                return build_kg_object(self.types[0], data, resolved=resolved, client=client)
            elif self.types[0] in (datetime, date):
                return date_parser.parse(data)
            elif self.types[0] == IRI:
                return data["@id"]
            elif self.types[0] == int:
                if isinstance(data, str):
                    return int(data)
                elif isinstance(data, Iterable):
                    return [int(item) for item in data]
                else:
                    return int(data)
            else:
                return data
        except Exception as err:
            if self.strict_mode:
                raise
            else:
                warnings.warn(str(err))
                return None
