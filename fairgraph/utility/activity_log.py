"""
Logging of the changes made to Knowledge Graph objects.
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
from typing import Optional, TYPE_CHECKING

from .jsonld import JSONdict

if TYPE_CHECKING:
    from ..kgobject import KGObject


class LogEntry:
    """
    Represents an entry in an activity log.

    Attributes:
        cls (str): The name of the class of the Knowledge Grapg object.
        id (Optional[str]): The identifer of the object being logged.
        delta (Optional[JSONdict]): A dictionary containing the changes made to the object.
        space (Optional[str]): The Knowledge Graph space containing the object.
        type_ (str): The type of the log entry.
    """

    def __init__(
        self,
        cls: str,
        id: Optional[str],
        delta: Optional[JSONdict],
        space: Optional[str],
        type_: str,
    ):
        self.cls = cls
        self.id = id
        self.delta = delta
        self.space = space
        self.type = type_

    def __repr__(self):
        return f"{self.type}: {self.cls}({self.id}) in '{self.space}'"

    def as_dict(self):
        return {
            "cls": self.cls,
            "id": self.id,
            "delta": self.delta,
            "space": self.space,
            "type_": self.type
        }


class ActivityLog:
    """
    Represents a log of activities performed on Knowledge Graph objects.

    Attributes:
        entries (List[LogEntry]): A list of LogEntry objects representing the activities performed.
    """

    def __init__(self):
        self.entries = []

    def update(self, item: KGObject, delta: Optional[JSONdict], space: Optional[str], entry_type: str):
        """
        Adds a new log entry to the activity log.

        Args:
            item (KGObject): The object being logged.
            delta (Optional[JSONdict]): A dictionary containing the changes made to the object.
            space (Optional[str]): The Knowledge Graph space containing the object.
            entry_type (str): The type of the log entry.
        """
        self.entries.append(LogEntry(item.__class__.__name__, item.uuid, delta, space, entry_type))

    def __repr__(self):
        return "\n".join((str(entry) for entry in self.entries))
