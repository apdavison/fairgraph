"""
Casting of openMINDS library instances to their fairgraph subclasses.
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

from openminds.base import LinkedNodeEmbedding

from ..base import ErrorHandling


def initialise_instances(class_list):
    """Cast openMINDS instances to their fairgraph subclass"""
    from .. import openminds as fg_openminds  # local import avoids a circular import at load time

    node_lookup = {}
    recast_instances = []

    # Many library instances are intentionally incomplete, and validation runs on every
    # attribute assignment (including the deep, cross-class re-validation triggered while
    # resolving links). Suppress validation handling globally — covering both linked and
    # embedded classes — for the whole initialisation, then restore the default, so that
    # `import fairgraph` produces no output.
    fg_openminds.set_error_handling(None)
    try:
        # Phase 1: shallow recast of each openMINDS instance to its fairgraph subclass.
        # Serialising with embed_linked_nodes=NEVER emits links as {"@id": ...} rather than
        # embedding them, so the (potentially cyclic) instance graph is never traversed;
        # linked attributes are deserialised into KGProxy objects to be resolved in phase 2.
        for cls in class_list:
            # find parent openMINDS class
            for parent_cls in cls.__mro__[1:]:
                if parent_cls.__name__ == cls.__name__:
                    # could also do this by looking for issubclass(parent_cls, openminds.Node)
                    break
            for key, value in parent_cls.__dict__.items():
                if isinstance(value, parent_cls):
                    fg_instance = cls.from_jsonld(value.to_jsonld(embed_linked_nodes=LinkedNodeEmbedding.NEVER))
                    fg_instance._space = cls.default_space
                    setattr(cls, key, fg_instance)
                    if fg_instance.id is not None:
                        node_lookup[fg_instance.id] = fg_instance
                    recast_instances.append(fg_instance)

        # Phase 2: replace the temporary KGProxy links with the actual recast objects,
        # so the library instances reference each other as fairgraph objects. Any link
        # pointing outside the recast set is left as a KGProxy (resolvable from the KG later).
        for fg_instance in recast_instances:
            fg_instance._resolve_links(node_lookup)
    finally:
        fg_openminds.set_error_handling(ErrorHandling.log)
