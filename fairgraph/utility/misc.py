"""
Miscellaneous helper functions
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
import hashlib
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..kgobject import KGObject

ATTACHMENT_SIZE_LIMIT = 1024 * 1024  # 1 MB


def as_list(obj: Union[None, KGObject, dict, str, list, tuple]) -> list:
    """
    Converts the input obj into a list.

    Args:
        obj: The input object to be converted to a list.

    Returns:
        list: A list - see Notes below.

    Raises:
        TypeError: If the input obj cannot be converted to a list.

    Notes:
        - If obj is None, it returns an empty list.
        - If obj is a dict or a str, it returns a list containing obj.
        - If obj is a list or a tuple, it returns a list with the same elements as obj.
        - If obj is not any of the above, it tries to convert obj into a list. If it fails due to a TypeError, it raises a TypeError with an appropriate error message.
    """
    if obj is None:
        return []
    elif isinstance(obj, (dict, str)):
        return [obj]
    try:
        L = list(obj)
    except TypeError:
        L = [obj]
    return L


def invert_dict(D):
    newD = {}
    for key, value in D.items():
        newD[value] = key
    return newD


def sha1sum(filename):
    BUFFER_SIZE = 128 * 1024
    h = hashlib.sha1()
    with open(filename, "rb") as fp:
        while True:
            data = fp.read(BUFFER_SIZE)
            if not data:
                break
            h.update(data)
    return h.hexdigest()
