"""
Metadata for data analysis pipelines
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



import os.path
import logging
from datetime import datetime, date
import sys
import inspect
import mimetypes
from .base_v2 import KGObject, Distribution, as_list, upload_attachment
from .fields import Field
from .core import Person

from .utility import ATTACHMENT_SIZE_LIMIT

logger = logging.getLogger("fairgraph")

DEFAULT_NAMESPACE = "modelvalidation"


class Analysis(KGObject):
    """
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/simulation/analysisactivity/v0.1.0" # to do: move from 'simulation' to 'dataanalysis'
    type = ["prov:Activity", "nsg:Activity", "nsg:AnalysisActivity"]  # todo: update schema, the latter should be "nsg:Analysis"
    context = [
        "{{base}}/contexts/neurosciencegraph/core/data/v0.3.1",
        "{{base}}/contexts/nexus/core/resource/v0.3.0",
        {
            "schema": "http://schema.org/",
            "name": "schema:name",
            "description": "schema:description",
            "identifier": "schema:identifier",
            "prov": "http://www.w3.org/ns/prov#",
            "generated": "prov:generated",
            "used": "prov:used",
            "dataUsed": "prov:used",
            "scriptUsed": "prov:used",
            "configUsed": "prov:used",
            "startedAtTime": "prov:startedAtTime",
            "endedAtTime": "prov:endedAtTime",
            "wasAssociatedWith": "prov:wasAssociatedWith",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "referenceData": "nsg:referenceData"
        }
    ]
    fields = (
        Field("name", str, "name", required=True),
        Field("description", str, "description"),
        Field("identifier", str, "identifier"),
        Field("input_data", KGObject, "dataUsed", multiple=True),
        Field("script", "analysis.AnalysisScript", "scriptUsed", multiple=True),
        Field("config", "analysis.AnalysisConfiguration", "configUsed", multiple=True),
        Field("timestamp", datetime,  "startedAtTime"),
        Field("end_timestamp",  datetime, "endedAtTime"),
        Field("result", "analysis.AnalysisResult", "generated", multiple=True),
        Field("started_by", Person, "wasAssociatedWith")
    )
    existence_query_fields = ("name", "timestamp")


class AnalysisConfiguration(KGObject):
    """
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/simulation/analysisconfiguration/v0.1.0"
    type = ["prov:Entity", "nsg:Entity", "nsg:AnalysisConfiguration"]
    context = {"schema": "http://schema.org/",
               "name": "schema:name",
               "description": "schema:description",
               "identifier": "schema:identifier",
               "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
               "distribution": "nsg:distribution"}
    fields = (
        Field("name", str, "name", required=True),
        Field("description", str, "description"),
        Field("identifier", str, "identifier"),
        Field("config_file", (Distribution, str), "distribution")
    )

    ## TODO : write the different cases: Distribution, dict, str

    def __init__(self,
                 name,
                 description=None,
                 identifier=None,
                 config_file=None,
                 id=None, instance=None):

        super(AnalysisConfiguration, self).__init__(
            name=name,
            description=description,
            identifier=identifier,
            config_file=config_file,
            id=id,
            instance=instance)
        self._file_to_upload = None
        if isinstance(config_file, str):
            if config_file.startswith("http"):
                self.config_file = Distribution(location=config_file)
            elif os.path.isfile(config_file):
                self._file_to_upload = config_file
                self.config_file = None
        elif config_file is not None:
            for rf in as_list(self.config_file):
                assert isinstance(rf, Distribution)

    def upload_attachment(self, file_path, client):
        upload_attachment(self, file_path, client)

    def save(self, client):
        super(AnalysisConfiguration, self).save(client)
        if self._file_to_upload:
            self.upload_attachment(self._file_to_upload, client)

    def download(self, local_directory, client):
        for rf in as_list(self.config_file):
            rf.download(local_directory, client)


class AnalysisResult(KGObject):
    """The result of a data analysis.

    For example a graph, a histogram, etc. The result is expected to be stored either in a local
    file or in a web-accessible location with a direct URL.

    Note that local results files smaller than 1 MB in size will be uploaded and stored within
    the Knowledge Graph. Larger files must be stored elsewhere.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/simulation/analysisresult/v1.0.0"
    type = ["prov:Entity", "nsg:Entity", "nsg:AnalysisResult"]
    context = [
        "{{base}}/contexts/neurosciencegraph/core/data/v0.3.1",
        "{{base}}/contexts/nexus/core/resource/v0.3.0",
        {
            "wasDerivedFrom": "prov:wasDerivedFrom",
            "generatedAtTime": "prov:generatedAtTime",
            "wasAttributedTo": "prov:wasAttributedTo",
            "wasGeneratedBy": "prov:wasGeneratedBy",
        }
    ]
    fields = (
        Field("name", str, "name", required=True),
        Field("result_file", (Distribution, str), "distribution"),
        Field("timestamp", datetime, "generatedAtTime", default=datetime.now),
        Field("derived_from", KGObject, "wasDerivedFrom", multiple=True),
        Field("attributed_to", Person, "wasAttributedTo"),
        Field("generated_by", Analysis, "wasGeneratedBy"),
        Field("description", str, "description"),
        #Field("data_type", str, "dataType", multiple=True),
    )
    existence_query_fields = ("name", "timestamp")

    def __init__(self, name, result_file=None, timestamp=None, derived_from=None,
                 attributed_to=None, generated_by=None,
                 description=None, id=None, instance=None):
        super(AnalysisResult, self).__init__(
            name=name, result_file=result_file, timestamp=timestamp, derived_from=derived_from,
            attributed_to=attributed_to, generated_by=generated_by,
            description=description, id=id, instance=instance
        )
        self._file_to_upload = None
        if isinstance(result_file, str):
            if result_file.startswith("http"):
                self.result_file = Distribution(location=result_file)
            elif os.path.isfile(result_file):
                self._file_to_upload = result_file
                self.result_file = None
        elif result_file is not None:
            for rf in as_list(self.result_file):
                assert isinstance(rf, Distribution)

    def save(self, client):
        super(AnalysisResult, self).save(client)
        if self._file_to_upload:
            self.upload_attachment(self._file_to_upload, client)

    def upload_attachment(self, file_path, client):
        import requests
        assert os.path.isfile(file_path)
        statinfo = os.stat(file_path)
        if statinfo.st_size > ATTACHMENT_SIZE_LIMIT:
            raise Exception(
                "File is too large to store directly in the KnowledgeGraph, please upload it to a Swift container")
        # todo, use the Nexus HTTP client directly for the following
        headers = client._nexus_client._http_client.auth_client.get_headers()
        content_type, encoding = mimetypes.guess_type(file_path, strict=False)
        response = requests.put("{}/attachment?rev={}".format(self.id, self.rev or 1),
                                headers=headers,
                                files={
                                    "file": (os.path.basename(file_path),
                                             open(file_path, "rb"),
                                             content_type)
        })
        if response.status_code < 300:
            logger.info("Added attachment {} to {}".format(file_path, self.id))
            self._file_to_upload = None
            self.result_file = Distribution.from_jsonld(response.json()["distribution"][0])
        else:
            raise Exception(str(response.content))

    def download(self, local_directory, client):
        for rf in as_list(self.result_file):
            rf.download(local_directory, client)

    def _build_data(self, client, all_fields=False):
        # workaround for what seems to be a bug in Nexus when derivedFrom is another AnalysisResult
        data = super(AnalysisResult, self)._build_data(client, all_fields=all_fields)
        if isinstance(self.derived_from, AnalysisResult):
            data["wasDerivedFrom"]["name"] = self.derived_from.name
        elif isinstance(self.derived_from, list):
            if len(self.derived_from) == 1:
                data["wasDerivedFrom"]["name"] = self.derived_from[0].name
            else:
                for i, item in enumerate(self.derived_from):
                    if isinstance(item, AnalysisResult):
                        data["wasDerivedFrom"][i]["name"] = item.name
        return data



class AnalysisScript(KGObject):
    """
    """
    namespace = DEFAULT_NAMESPACE
    type = ["prov:Entity", "nsg:Entity", "nsg:AnalysisScript"]
    _path = "/simulation/analysisscript/v0.1.0"
    context = {"schema": "http://schema.org/",
               "name": "schema:name",
               "identifier": "schema:identifier",
               "description": "schema:description",
               "license": "schema:license",
               "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
               "distribution": "nsg:distribution",
               "code_format": "nsg:code_format"}  # todo: add version field
    fields = (
        Field("name", str, "name", required=True),
        Field("identifier", str, "identifier"),
        Field("script_file", (Distribution, str), "distribution", multiple=True),
        Field("code_format", str, "code_format", multiple=True),
        Field("license", str, "license")
    )

    def __init__(self, name,
                 script_file=None,
                 code_format=None,
                 license=None,
                 identifier=None,
                 id=None,
                 instance=None):
        super(AnalysisScript, self).__init__(name=name,
                                             script_file=script_file,
                                             code_format=code_format,
                                             license=license,
                                             identifier=identifier,
                                             id=id,
                                             instance=instance)
        self._file_to_upload = None
        if isinstance(script_file, str):
            if script_file.startswith("http"):
                self.script_file = Distribution(location=script_file)
            elif os.path.isfile(script_file):
                self._file_to_upload = script_file
                self.script_file = None
        elif script_file is not None:
            for rf in as_list(self.script_file):
                assert isinstance(rf, Distribution)
        else:
            print('/!\ Need to provide a "script_file" argument, either a string path to a file (local or public on the web) or a Distribution object')

    def save(self, client):
        super(AnalysisScript, self).save(client)
        if self._file_to_upload:
            self.upload_attachment(self._file_to_upload, client)

    @property
    def script_location(self):
        if self.distribution:
            return self.distribution.location
        else:
            print('script attached to the KG entry, use the "download" method to fetch it')
            return None

    def upload_attachment(self, file_path, client):
        upload_attachment(self, file_path, client)

    def download(self, local_directory, client):
        for rf in as_list(self.script_file):
            rf.download(local_directory, client)


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
