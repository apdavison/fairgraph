"""
Normalization of the whitespace in the text values that fairgraph writes to, and queries for in, the Knowledge Graph.
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
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from openminds.properties import Property


def normalize_whitespace(value: str, prop: Property) -> str:
    """
    Normalize the whitespace in a text value, for storage in the Knowledge Graph.

    Args:
        value: the text to normalize.
        prop: the openMINDS property that the text is a value of.
    """
    # Currently this only removes leading and trailing whitespace. It takes the property (rather than
    # just the string) so that internal whitespace can later be handled differently for single-line
    # and multi-line properties (using ``prop.multiline`` and ``prop.formatting``) by changing only this function.
    return value.strip()


def normalize_property_value(prop: Property, value: Any) -> Any:
    """
    Normalize the whitespace in the value(s) of a property, if it holds text.

    Values of properties that do not accept text are returned unchanged, as are ``None``
    and any items of a list that are not strings (IRIs, dates, nodes, proxies...).
    An all-whitespace string becomes an empty string.
    """
    if str not in prop.types:
        return value
    if isinstance(value, str):
        return normalize_whitespace(value, prop)
    elif isinstance(value, (list, tuple)):
        items = [normalize_whitespace(item, prop) if isinstance(item, str) else item for item in value]
        return tuple(items) if isinstance(value, tuple) else items
    return value
