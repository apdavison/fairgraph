"""
Shims for deprecated keywords.
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
import warnings


def handle_scope_keyword(scope, release_status):
    """
    The keyword 'scope' has been renamed 'release_status',
    use of 'scope' is deprecated but still accepted.
    """
    if scope in ("released", "in progress", "any"):
        warnings.warn(
            "The keyword 'scope' is deprecated, and will be removed in version 1.0; it has been renamed to 'release_status'",
            DeprecationWarning,
            stacklevel=2,
        )
        return scope
    else:
        return release_status
