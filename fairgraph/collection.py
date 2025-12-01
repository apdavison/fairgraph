"""
This module provides the Collection class, an extension to the openMINDS Collection
that knows how to upload metadata to the KG.
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

from importlib import import_module
import os
from time import sleep
from uuid import uuid4
from warnings import warn

from openminds import Collection as OMCollection
from .utility import ActivityLog
from .errors import AuthenticationError


class Collection(OMCollection):
    """
    A collection of metadata nodes that can be saved to
    and loaded from disk, and uploaded to the KG.

    Args
    ----

    *nodes (LinkedMetadata):
        Nodes to store in the collection when creating it.
        Child nodes that are referenced from the explicitly
        listed nodes will also be added.
    """

    def load(self, *paths):
        import_module("fairgraph.openminds")
        super().load(*paths)

    def upload(self, client, default_space=None, space_map=None, verbosity=0):
        nodes_to_save = [
            node
            for node in self.sort_nodes_for_upload()
            if not node.id.startswith("https://openminds.om-i.org/instances")
        ]
        activity_log = ActivityLog()

        if verbosity == 1:
            try:
                tqdm = import_module("tqdm")
            except ImportError:
                warn("Unable to show progress bar, please install tqdm")
            else:
                nodes_to_save = tqdm.tqdm(nodes_to_save)

        if os.path.exists(".kg_upload_log.txt"):
            with open(".kg_upload_log.txt") as fp:
                skip = fp.read().strip().split("\n")
        else:
            skip = None

        for i, node in enumerate(nodes_to_save):
            if not (skip and node.id in skip):
                if verbosity == 2:
                    print(f"[{100*i//len(nodes_to_save)}%] Saving {node.__class__.__name__} {node.id}")
                if space_map:
                    target_space = space_map.get(node.__class__, default_space)
                else:
                    target_space = default_space
                original_node_id = node.id
                try:
                    node.save(
                        client, space=target_space, recursive=False, ignore_duplicates=True, activity_log=activity_log
                    )
                except AuthenticationError as err:
                    # client.refresh()
                    print(err)
                    break
                except Exception as err:
                    if "500" in str(err):
                        sleep(5)
                        node.save(
                            client,
                            space=target_space,
                            recursive=False,
                            ignore_duplicates=True,
                            activity_log=activity_log,
                        )
                    else:
                        raise
                else:
                    with open(".kg_upload_log.txt", "a") as fp:
                        fp.write(f"{original_node_id}\n")

        return activity_log
