"""
This module provides the KGQuery class, which represents one or more
KGObjects identified by a range of possible types and by some of their
metadata, but whose specific identifier(s) is/are not known.
"""

# Copyright 2018-2024 CNRS

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
import logging
from typing import Dict, List, Optional, Union, Any, TYPE_CHECKING

from openminds.registry import lookup

from .utility import as_list, expand_filter
from .caching import object_cache
from .base import Resolvable, SupportsQuerying

if TYPE_CHECKING:
    from .client import KGClient
    from .kgobject import KGObject

logger = logging.getLogger("fairgraph")


class KGQuery(Resolvable, SupportsQuerying):
    """
    Representation of one or more KGObjects identified by a range of possible types
    and by some of their metadata, but whose specific identifier(s) is/are not known.

    It is possible that no KGObjects match the types/metadata.

    Args:
        classes (list of KGObject subclasses): a list of types to query.
        filter (dict): key:value pairs that should be matched. All pairs must match.
        preferred_scope (str): The preferred scope used to resolve the query.
            Valid values are "released", "in progress", or "any".

    Example:
        >>> import fairgraph.openminds.core as omcore
        >>> from fairgraph.utility import as_list
        >>> query = KGQuery([omcore.Person], {"family_name": "Amunts"})
        >>> people = as_list(query.resolve(kg_client))
        >>> len(people)
        1
        >>> people[0].family_name
        Amunts
    """

    def __init__(
        self,
        classes: Union[str, KGObject, List[Union[str, KGObject]]],
        filter: Dict[str, str],
        preferred_scope: str = "released",
    ):
        self.classes: List[KGObject] = []
        for cls in as_list(classes):
            if isinstance(cls, str):
                resolved_cls = lookup(cls)
                assert isinstance(resolved_cls, KGObject)
                self.classes.append(resolved_cls)
            else:
                self.classes.append(cls)
        self.filter = filter
        self.preferred_scope = preferred_scope

    def __repr__(self):
        return "{self.__class__.__name__}(" "{self.classes!r}, {self.filter!r})".format(self=self)

    def resolve(
        self,
        client: KGClient,
        size: int = 10000,
        from_index: int = 0,
        space: Optional[str] = None,
        scope: Optional[str] = None,
        use_cache: bool = True,
        follow_links: Optional[Dict[str, Any]] = None,
    ):
        """
        Retrieve the full metadata for the KGObject(s) represented by this query object.

        Args:
            client: a KGClient
            from_index: The index of the first result to include in the response.
            size: The maximum number of results to include in the response.
            space: If specified, queries only in the given space.
            scope (str, optional): The scope of the query. Valid values are "released", "in progress", or "any".
                If not provided, the "preferred_scope" provided when creating the proxy object will be used.
            use_cache (bool): Whether to use cached data if they exist. Defaults to True.
            follow_links (dict): The links in the graph to follow. Defaults to None.

        Returns:
            a KGObject instance, of the appropriate subclass.
        """
        scope = scope or self.preferred_scope
        objects: List[KGObject] = []
        for cls in self.classes:
            if hasattr(cls, "generate_query"):
                # if cls is EmbeddedMetadata we cannot query it
                query = cls.generate_query(client=client, filters=self.filter, space=space, follow_links=follow_links)
                instances = client.query(
                    query=query,
                    size=size,
                    from_index=from_index,
                    scope=scope,
                ).data
                objects.extend(cls.from_kg_instance(instance_data, client) for instance_data in instances)
        for obj in objects:
            object_cache[obj.id] = obj

        if follow_links:
            for obj in objects:
                obj.resolve(client, scope=scope, use_cache=use_cache, follow_links=follow_links)

        if len(objects) == 1:
            return objects[0]
        else:
            return objects

    def count(self, client: KGClient, space: Optional[str] = None, scope: Optional[str] = None):
        """
        Return the number of objects that would be returned by resolving this query.
        """
        scope = scope or self.preferred_scope
        n = 0
        for cls in self.classes:
            n += cls.count(client, api="query", scope=scope, space=space, **self.filter)
        return n
