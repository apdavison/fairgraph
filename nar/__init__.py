"""
Python client for the Human Brain Project Neural Activity Resource

Author: Andrew Davison, CNRS, 2018


Copyright 2018 CNRS

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

import re
from .client import NARClient


def KnowledgeGraphEntity(schema):
    namespace = {
        "context": schema.data["@context"],
        "revision": schema.get_revision(),
        "version": schema.get_version(),
        "organisation": schema.get_organisation(),
        "domain": schema.get_domain(),
        "deprecated": schema.is_deprecated(),
    }
    for shape in schema["shapes"]:
        if hasattr(shape, "targetClass"):
            principal_shape = shape
            break
    name = re.sub(".*?:", "", principal_shape["targetClass"])
    # ...unfinished
    
    bases = (object,)
    return type(name, bases, namespace)


