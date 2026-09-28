"""
Utility functions and classes used throughout fairgraph, grouped by theme.

All public names are re-exported here, so they can be imported from ``fairgraph.utility``.
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

from .misc import ATTACHMENT_SIZE_LIMIT, as_list, invert_dict, sha1sum
from .jsonld import JSONdict, expand_uri, compact_uri, normalize_data, expand_filter
from .activity_log import LogEntry, ActivityLog
from .terms_of_use import TERMS_OF_USE, accepted_terms_of_use, in_notebook
from .initialisation import initialise_instances
from .deprecation import handle_scope_keyword
