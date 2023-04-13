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

from .registry import Registry
from .utility import as_list  # temporary for backwards compatibility (a lot of code imports it from here)

logger = logging.getLogger("fairgraph")


class Resolvable: # all

    def resolve(self, client, scope=None, use_cache=True, follow_links=0):
        pass



class ContainsMetadata(metaclass=Registry):  # KGObject and EmbeddedMetadata

    def to_jsonld(self, normalized=True, follow_links=False, include_empty_fields=False):
        pass

    @classmethod
    def from_jsonld(cls, data, client):
        pass

    def save(self, client, space=None, recursive=True, activity_log=None, replace=False, ignore_auth_errors=False):
        pass

    @classmethod
    def set_strict_mode(cls, value, field_names=None):
        pass

    @classmethod
    def generate_query_properties(cls, filter_keys=None, follow_links=0):
        pass


class RepresentsSingleObject:  # KGObject, KGProxy
    pass


class SupportsQuerying:  # KGObject, KGQuery
    pass


class IRI:

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