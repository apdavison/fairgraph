"""
Handling of JSON-LD data: URI expansion/compaction, key normalization, and filter expansion.
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
from typing import Any, Dict, List, Tuple, Union

from .misc import as_list

JSONdict = Dict[str, Any]  # see https://github.com/python/typing/issues/182 for some possible improvements


def expand_uri(uri_list: Union[str, List[str]], context: Dict[str, Any]) -> Union[str, Tuple[str, ...]]:
    """
    Expands a URI or a list of URIs using a given context.

    Args:
        uri_list (Union[str, List[str]]): A URI or a list of URIs to be expanded.
        context (Dict[str, Any]): A dictionary containing a mapping of prefixes to base URLs.

    Returns:
        Union[str, Tuple[str, ...]]: An expanded URI or a tuple of expanded URIs.

    Raises:
        ValueError: If a prefix in the URI is not found in the context.

    Examples:
        >>> context = {'foaf': 'http://xmlns.com/foaf/0.1/'}
        >>> uri_list = 'foaf:Person'
        >>> expand_uri(uri_list, context)
        'http://xmlns.com/foaf/0.1/Person'

    """
    expanded_uris = []
    for uri in as_list(uri_list):
        if uri.startswith("http") or uri.startswith("@"):
            expanded_uris.append(uri)
        else:
            parts = uri.split(":")
            if len(parts) == 1:
                prefix = "@vocab"
                identifier = uri
            else:
                prefix, identifier = parts
            if prefix not in context:
                raise ValueError(f"prefix {prefix} not found in context")
            base_url = context[prefix]
            if not base_url.endswith("/"):
                base_url += "/"
            expanded_uris.append(f"{base_url}{identifier}")
    if isinstance(uri_list, str):
        return expanded_uris[0]
    else:
        return tuple(expanded_uris)


def compact_uri(
    uri_list: Union[str, List[str]], context: Dict[str, Any], strict: bool = False
) -> Union[str, Tuple[str, ...]]:
    """
    Compacts a URI or a list of URIs using a given context.

    Args:
        uri_list (Union[str, List[str]]): A URI or a list of URIs to be compacted.
        context (Dict[str, Any]): A dictionary containing a mapping of prefixes to base URLs.
        strict (bool, optional): Whether to raise an error if a URI cannot be compacted. Defaults to False.

    Returns:
        Union[str, Tuple[str, ...]]: A compacted URI or a tuple of compacted URIs.

    Raises:
        ValueError: If strict is True and a URI cannot be compacted.

    Examples:
        >>> context = {'foaf': 'http://xmlns.com/foaf/0.1/'}
        >>> uri_list = 'http://xmlns.com/foaf/0.1/Person'
        >>> compact_uri(uri_list, context)
        'foaf:Person'
    """
    compacted_uris = []
    for uri in as_list(uri_list):
        if uri.startswith("http"):
            found = False
            for prefix, base_url in context.items():
                if uri.startswith(base_url):
                    start = len(base_url)
                    identifier = uri[start:].strip("/")
                    if prefix == "@vocab":
                        compacted_uris.append(identifier)
                    else:
                        compacted_uris.append(f"{prefix}:{identifier}")
                    found = True
                    break
            if not found:
                if strict:
                    raise ValueError(f"Unable to compact {uri} with the provided context")
                else:
                    compacted_uris.append(uri)
        else:
            compacted_uris.append(uri)
    if isinstance(uri_list, str):
        return compacted_uris[0]
    else:
        return tuple(compacted_uris)


def normalize_data(data: Union[None, JSONdict], context: Dict[str, Any]) -> Union[None, JSONdict]:
    """
    Normalizes JSON-LD data using a given context.

    Args:
        data (Union[None, JSONdict]): A JSON-LD data dict to be normalized.
        context (Dict[str, Any]): A dictionary containing a mapping of prefixes to base URLs.

    Returns:
        Union[None, JSONdict]: A normalized JSON-LD data dict.

    Examples:
        >>> context = {'foaf': 'http://xmlns.com/foaf/0.1/'}
        >>> data = {
        ...     "foaf:name": "John Smith",
        ...     "foaf:age": 35,
        ...     "foaf:knows": {
        ...         "foaf:name": "Jane Doe",
        ...         "foaf:age": 25
        ...     }
        ... }
        >>> normalize_data(data, context)
        {
            "http://xmlns.com/foaf/0.1/name": "John Smith",
            "http://xmlns.com/foaf/0.1/age": 35,
            "http://xmlns.com/foaf/0.1/knows": {
                "http://xmlns.com/foaf/0.1/name": "Jane Doe",
                "http://xmlns.com/foaf/0.1/age": 25
            }
        }

    """
    if data is None:
        return data
    normalized: JSONdict = {}
    for key, value in data.items():
        assert isinstance(key, str)
        if key == "@context":
            continue
        elif key.startswith("Q"):
            expanded_key = key
        else:
            result = expand_uri(key, context)
            assert isinstance(result, str)  # for type checking
            expanded_key = result
        assert expanded_key.startswith("http") or expanded_key.startswith("@") or expanded_key.startswith("Q")

        if hasattr(value, "__len__") and len(value) == 0:
            pass
        elif expanded_key == "@id":
            if value.startswith("http"):
                # do not take local ids, e.g., those starting with "_"
                normalized[expanded_key] = value
        elif expanded_key == "@type":
            normalized[expanded_key] = value
        elif isinstance(value, (list, tuple)):
            normalized[expanded_key] = []
            for item in value:
                if isinstance(item, dict):
                    normalized[expanded_key].append(normalize_data(item, context))
                else:
                    normalized[expanded_key].append(item)
        elif isinstance(value, dict):
            normalized[expanded_key] = normalize_data(value, context)
        else:
            normalized[expanded_key] = value
    return normalized


def expand_filter(filter_dict: Dict[str, Any]):
    """
    Expand single-level filter specification (provided by user) into
    a multi-level dict as required by the query-generation machinery.

    Example:
    >>> filter = {
    ...    "developers__affiliations__member_of__alias": "CNRS",
    ...    "digital_identifier__identifier": "https://doi.org/some-doi"
    ... }
    >>> expand_filter(filter)
    {
        "developers": {
            "affiliations": {
                "member_of": {
                    "alias": "CNRS
                }
            }
        },
        "digital_identifier": {
            "identifier": "https://doi.org/some-doi"
        }
    }
    """
    expanded = {}
    for key, value in filter_dict.items():
        if hasattr(value, "items"):
            raise TypeError("Filter specifications should be a single-level dict, without nesting")
        local_path = expanded
        parts = key.split("__")
        for part in parts[:-1]:
            local_path[part] = {}
            local_path = local_path[part]
        local_path[parts[-1]] = value
    return expanded
