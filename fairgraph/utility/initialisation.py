"""
Casting of openMINDS library instances to their fairgraph subclasses.

openMINDS Python provides library instances (controlled terms, brain atlases, licences, ...)
as class attributes of its classes, e.g. ``Species.mus_musculus``. fairgraph replaces these with
instances of the corresponding fairgraph classes. There are many thousands of library instances,
and most applications use only a few classes, so each class's instances are recast the first time
they are used: when one of them is accessed as a class attribute, or through ``instances()``
or ``by_name()``.
"""

# Copyright 2018-2026 CNRS and fairgraph authors and/or their employers

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

from collections import defaultdict
import threading

from openminds.base import LinkedNodeEmbedding

from ..base import validation_suppressed


class _RecastLookup(dict):
    """
    Lookup of recast library instances by id, for one openMINDS version
    (the v4 and v5 libraries share their ids).

    Looking up an instance of a class whose instances have not yet been recast recasts them,
    so that links between library instances of different classes can be resolved.
    """

    def __init__(self):
        super().__init__()
        self.owner_by_id = {}  # library instance id -> fairgraph class

    def get(self, key, default=None):
        if key not in self and key in self.owner_by_id:
            recast_instances(self.owner_by_id[key])
        return super().get(key, default)


_lock = threading.RLock()
_pending = {}  # fairgraph class -> openMINDS parent class, for classes whose instances have not yet been recast
_recast_lookups = defaultdict(_RecastLookup)  # openMINDS version -> lookup of recast instances


class _LibraryInstance:
    """Placeholder for a library instance, which recasts the instances of its class when first accessed."""

    def __init__(self, cls, name):
        self.cls = cls
        self.name = name

    def __get__(self, obj, owner):
        recast_instances(self.cls)
        return self.cls.__dict__[self.name]


def _instances(cls):
    recast_instances(cls)
    return [value for value in cls.__dict__.values() if isinstance(value, cls)]


def _find_openminds_parent(cls):
    for parent_cls in cls.__mro__[1:]:
        if parent_cls.__name__ == cls.__name__:
            # could also do this by looking for issubclass(parent_cls, openminds.Node)
            return parent_cls
    raise TypeError(f"{cls.__name__} has no openMINDS parent class")


def _recast_lookup(cls):
    # class_name has the form "openminds.<version>.<module>.<class>"
    return _recast_lookups[cls.class_name.split(".")[1]]


def register_instances(class_list):
    """
    Arrange for the openMINDS library instances of the given fairgraph classes
    to be recast to the fairgraph class the first time they are used.
    """
    with _lock:
        for cls in class_list:
            parent_cls = _find_openminds_parent(cls)
            owner_by_id = _recast_lookup(cls).owner_by_id
            names = [key for key, value in parent_cls.__dict__.items() if isinstance(value, parent_cls)]
            if not names:
                continue
            for key in names:
                setattr(cls, key, _LibraryInstance(cls, key))
                instance_id = getattr(parent_cls, key).id
                if instance_id is not None:
                    owner_by_id[instance_id] = cls
            cls.instances = classmethod(_instances)
            # stop the class using a by_name() lookup table built by its openMINDS parent
            cls._instance_lookup = None
            _pending[cls] = parent_cls


def recast_instances(cls):
    """
    Recast the openMINDS library instances of the given fairgraph class, if this has not already been done.

    Links to library instances of other classes are resolved to the recast objects,
    recasting the instances of those classes if necessary.
    Any link pointing outside the library is left as a KGProxy (resolvable from the KG later).
    """
    with _lock:
        parent_cls = _pending.pop(cls, None)
        if parent_cls is None:
            return
        recast_lookup = _recast_lookup(cls)
        try:
            # Many library instances are intentionally incomplete, and validation runs on every
            # attribute assignment (including the deep, cross-class re-validation triggered while
            # resolving links), so validation is switched off while recasting.
            with validation_suppressed():
                # Phase 1: shallow recast of each openMINDS instance to its fairgraph subclass.
                # Serialising with embed_linked_nodes=NEVER emits links as {"@id": ...} rather than
                # embedding them, so the (potentially cyclic) instance graph is never traversed;
                # linked attributes are deserialised into KGProxy objects to be resolved in phase 2.
                recast = []
                for key, value in parent_cls.__dict__.items():
                    if isinstance(value, parent_cls):
                        fg_instance = cls.from_jsonld(value.to_jsonld(embed_linked_nodes=LinkedNodeEmbedding.NEVER))
                        fg_instance._space = cls.default_space
                        setattr(cls, key, fg_instance)
                        if fg_instance.id is not None:
                            recast_lookup[fg_instance.id] = fg_instance
                        recast.append(fg_instance)

                # Phase 2: replace the temporary KGProxy links with the recast objects,
                # so the library instances reference each other as fairgraph objects.
                for fg_instance in recast:
                    fg_instance._resolve_links(recast_lookup)
        except BaseException:
            _pending[cls] = parent_cls
            raise


def initialise_instances(class_list):
    """Cast the openMINDS library instances of the given fairgraph classes to the fairgraph class, immediately"""
    register_instances(class_list)
    for cls in class_list:
        recast_instances(cls)
