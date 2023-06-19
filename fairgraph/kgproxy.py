"""
This module provides the KGProxy class, which represents a
KGObject whose type and identifier are known but whose other metadata
have not been retrieved from the KG.
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
import logging
from typing import List, Optional, Tuple, Union, Dict, Any, TYPE_CHECKING

from .registry import lookup
from .errors import ResolutionFailure
from .caching import object_cache
from .base import RepresentsSingleObject

if TYPE_CHECKING:
    from .client import KGClient
    from .kgobject import KGObject


logger = logging.getLogger("fairgraph")


class KGProxy(RepresentsSingleObject):
    """
    Representation of an KGObject whose type and identifier are known but whose
    other metadata have not been retrieved from the KG.

    Args:
        cls (str, KGObject): the type of the associated KG object, defined by a KGObject subclass
            or by the name of the subclass.
        uri (URI): The global identifier of the KG object.
        preferred_scope (str, optional): The preferred scope used to resolve the proxy.
            Valid values are "released", "in progress", or "any".

    Example:
        >>> import fairgraph.openminds
        >>> proxy = KGProxy("openminds.core.Person", "https://kg.ebrains.eu/api/instances/bd554312-9829-4148-8803-cb873d0b32f9")
        >>> person = proxy.resolve(kg_client)
        >>> type(person)
        <class 'fairgraph.openminds.core.actors.person.Person'>
        >>> person.given_name
        Andrew P.
    """

    # todo: rename uri to id, for consistency?

    def __init__(self, cls: Union[str, KGObject], uri: str, preferred_scope: str = "released"):
        self.cls: KGObject
        if isinstance(cls, str):
            resolved_cls = lookup(cls)
            if TYPE_CHECKING:
                assert isinstance(resolved_cls, KGObject)
            self.cls = resolved_cls
        else:
            self.cls = cls
        if TYPE_CHECKING:
            assert isinstance(self.cls, KGObject)
        self.id = uri
        self.preferred_scope = preferred_scope
        self.remote_data = None

    @property
    def type(self) -> List[str]:
        """
        Provide the global identifiers of the object type (as a list of URIs).
        """
        try:
            return self.cls.type_
        except AttributeError as err:
            raise AttributeError(f"{err} self.cls={self.cls}")

    @property
    def classes(self) -> Union[Tuple[KGObject], List[KGObject]]:
        """
        Provide the metadata class associated with this object in a list.

        This is provided for consistency with the KGQuery interface.
        """
        if isinstance(self.cls, (list, tuple)):
            return self.cls
        else:
            return [self.cls]

    def resolve(
        self,
        client: KGClient,
        scope: Optional[str] = None,
        use_cache: bool = True,
        follow_links: Optional[Dict[str, Any]] = None,
    ):
        """
        Retrieve the full metadata for the KGObject represented by this proxy.

        Args:
            client: a KGClient
            scope (str, optional): The scope of the lookup. Valid values are "released", "in progress", or "any".
                If not provided, the "preferred_scope" provided when creating the proxy object will be used.
            use_cache (bool): Whether to use cached data if they exist. Defaults to True.
            follow_links (dict): The links in the graph to follow. Defaults to None.

        Returns:
            a KGObject instance, of the appropriate subclass.
        """
        if use_cache and self.id in object_cache:
            obj = object_cache[self.id]
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
            object_cache[self.id] = obj
        if follow_links:
            return obj.resolve(client, scope=scope, use_cache=use_cache, follow_links=follow_links)
        else:
            return obj

    def __repr__(self):
        return "{self.__class__.__name__}(" "{self.classes!r}, {self.id!r})".format(self=self)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and set(self.classes).intersection(other.classes) and self.id == other.id
        )

    def __ne__(self, other):
        return (
            not isinstance(other, self.__class__) or set(self.classes).isdisjoint(other.classes) or self.id != other.id
        )

    @property
    def uuid(self) -> str:
        return self.id.split("/")[-1]

    def delete(self, client: KGClient, ignore_not_found: bool = True):
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
