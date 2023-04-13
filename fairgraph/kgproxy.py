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

from .registry import lookup
from .errors import ResolutionFailure
from .caching import object_cache
from .base import Resolvable, RepresentsSingleObject


logger = logging.getLogger("fairgraph")


class KGProxy(Resolvable, RepresentsSingleObject):
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

    def release(self, client, with_children=False):
        """Release this node (make it available in public search)."""
        if not self.is_released(client, with_children=with_children):
            if with_children:
                for child in self.children(client):
                    if not child.is_released(client, with_children=False):
                        client.release(child.id)
            return client.release(self.id)
