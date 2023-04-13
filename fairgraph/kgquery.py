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

from .utility import as_list
from .registry import lookup
from .caching import object_cache
from .base import Resolvable, SupportsQuerying


logger = logging.getLogger("fairgraph")


class KGQuery(Resolvable, SupportsQuerying):
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
            normalized_filters = cls.normalize_filter(self.filter) or None
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
            object_cache[obj.id] = obj

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
