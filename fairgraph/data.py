"""

"""

# Copyright 2018-2020 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from urllib.request import urlretrieve
from pathlib import Path
from datetime import datetime

from fairgraph.base_v2 import KGObject
from .fields import Field


class DataObject(KGObject):
    """docstring"""
    pass


class FileAssociation(DataObject):
    namespace = "cscs"
    _path = "/core/fileassociation/v1.0.0"
    type = ["cscs:Fileassociation", "https://schema.hbp.eu/LinkingInstance"]
    fields = (
        Field("name", str, "http://schema.org/name"),
        Field("from", KGObject, "'https://schema.hbp.eu/linkinginstance/from"),
        Field("to", KGObject, "'https://schema.hbp.eu/linkinginstance/to")
    )

    @property
    def from_(self):
        """Return the 'from' property of the file association

        (note trailing underscore since 'from' is a reserved word in Python
        """
        return getattr(self, "from")


class CSCSFile(DataObject):
    namespace = "cscs"
    _path = "/core/file/v1.0.0"
    type = ["hbp:File"]
    context = [
        {
            "hbp": "https://schema.hbp.eu/cscs/",
            "schema": "http://schema.org/"
        },
        "https://nexus.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0"
    ]
    fields = (
        Field("name", str, "schema:name"),
        Field("absolute_path", str, "hbp:absolute_path"),
        Field("byte_size", int, "hbp:byte_size"),
        Field("content_type", str, "hbp:content_type"),
        Field("last_modified", datetime, "hbp:last_modified"),
        Field("relative_path", str, "hbp:relative_path")
    )

    def download(self, base_dir=".", preserve_relative_path=True):
        local_filename = Path(base_dir)
        if preserve_relative_path:
            local_filename = local_filename / self.relative_path
        else:
            local_filename = local_filename / self.name
        local_filename.parent.mkdir(parents=True, exist_ok=True)
        local_filename, headers = urlretrieve(self.absolute_path, local_filename)
        return local_filename
