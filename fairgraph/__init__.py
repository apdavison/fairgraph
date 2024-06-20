"""
Python client for the EBRAINS Knowledge Graph

Authors: Andrew Davison et al., CNRS (see authors.rst)


Copyright 2018-2024 CNRS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from openminds import IRI
from .client import KGClient
from .kgobject import KGObject
from .embedded import EmbeddedMetadata
from .kgproxy import KGProxy
from .kgquery import KGQuery


__version__ = "0.12.0"

# from . import (
#    base, client, errors, utility, openminds)
