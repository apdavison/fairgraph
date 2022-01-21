# encoding: utf-8
"""
Metadata about, or related to, software
"""

# Copyright 2018-2020 CNRS and Universität Trier

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import logging
from datetime import date
import inspect
from dateutil import parser as date_parser
from .base_v2 import KGObject, IRI, cache, KGProxy, build_kg_object, Distribution, as_list, KGQuery, OntologyTerm
from .fields import Field
from .core import Organization, Person
from .commons import License

logger = logging.getLogger("fairgraph")

DEFAULT_NAMESPACE = "softwarecatalog"


class SoftwareCategory(OntologyTerm):
    iri_map = {
        "application": "https://www.wikidata.org/wiki/Q166142",
        "plug-in": "https://www.wikidata.org/wiki/Q184148"
    }


class OperatingSystem(OntologyTerm):
    iri_map = {
        "Linux": "http://dbpedia.org/resource/Linux",
        "MacOS": "http://dbpedia.org/resource/MacOS",
        "Windows": "http://dbpedia.org/resource/Microsoft_Windows",
        "Windows XP": "http://dbpedia.org/resource/Windows_XP",
        "Windows Vista": "http://dbpedia.org/resource/Windows_Vista",
        "Windows 7": "http://dbpedia.org/resource/Windows_7",
        "Windows 10": "http://dbpedia.org/resource/Windows_10"
    }


class ProgrammingLanguage(OntologyTerm):
    iri_map = {
        "Python": "https://www.wikidata.org/wiki/Q28865",
        "C++": "https://www.wikidata.org/wiki/Q2407",
        "C": "https://www.wikidata.org/wiki/Q15777",
        "Java": "https://www.wikidata.org/wiki/Q251",
        "Perl": "https://www.wikidata.org/wiki/Q42478",
        "Javascript": "https://www.wikidata.org/wiki/Q2005"
    }


class SoftwareFeatureCategory(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/software/softwarefeaturecategory/v1.0.0"
    type = ["hbpsc:Softwarefeaturecategory"]

    context = {
        "schema": "http://schema.org/",
        "hbpsc": "https://schema.hbp.eu/softwarecatalog/",
        "name": "schema:name",
        "identifier": "schema:identifier",
        "description": "schema:description",
        "parentCategory": "schema:parentCategory"
    }

    fields = (
        Field("identifier", str, "identifier"),
        Field("name", str, "name", required=True),
        Field("description", str, "description"),
        Field("parent", "software.SoftwareFeatureCategory", "parentCategory")
    )


class SoftwareFeature(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/software/softwarefeature/v1.0.0"
    type = ["hbpsc:Softwarefeature"]

    context = {
        "schema": "http://schema.org/",
        "hbpsc": "https://schema.hbp.eu/softwarecatalog/",
        "name": "schema:name",
        "identifier": "schema:identifier",
        "description": "schema:description",
        "category": "schema:category"
    }

    fields = (
        Field("name", str, "name", required=True),
        Field("description", str, "name"),
        Field("category", SoftwareFeatureCategory, "category"),
        Field("identifier", str, "identifier")
    )


class Keyword(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/options/keyword/v1.0.0"
    type = ["hbpsc:Keyword"]

    context = {
        "schema": "http://schema.org/",
        "hbpsc": "https://schema.hbp.eu/softwarecatalog/",
        "name": "schema:name",
        "identifier": "schema:identifier"
    }

    fields = (
        Field("name", str, "name", required=True),
        Field("identifier", str, "identifier")
    )


class Software(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/software/software/v1.0.0"
    type = ["hbpsc:Software"]

    context = {
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "hbpsc": "https://schema.hbp.eu/softwarecatalog/",
        "prov": "http://www.w3.org/ns/prov#",
        "schema": "http://schema.org/",
        "name": "schema:name",
        "description": "schema:description",
        "citation": "schema:citation",
        "dateCreated": "schema:dateCreated",
        "applicationCategory": "schema:applicationCategory",
        "license": "schema:license",
        "operatingSystem": "schema:operatingSystem",
        "releaseNotes": "schema:releaseNotes",
        "softwareRequirements": "schema:softwareRequirements",
        "headline": "schema:headline",
        "wasAttributedTo": "prov:wasAttributedTo",
        "copyrightHolder": "schema:copyrightHolder",
        "url": "schema:url",
        "documentation": "schema:documentation",
        "softwareHelp": "schema:softwareHelp",
        "programmingLanguage": "schema:programmingLanguage",
        "funder": "schema:funder",
        "hasPart": "schema:hasPart",
        "isAccessibleForFree": "schema:isAccessibleForFree",
        "image": "schema:image",
        "keywords": "schema:keywords",
        "version": "schema:version",
        "feature": "schema:feature",
        "code": "schema:code",
        "author": "schema:author",
    }

    fields = (
        Field("name", str, "name", required=True),
        Field("description", str, "description"),
        Field("citation", str, "citation"),
        Field("release_date", date, "dateCreated"),
        Field("categories", SoftwareCategory, "applicationCategory"),
        Field("license", License, "license", multiple=True),
        Field("operating_system", OperatingSystem, "operatingSystem", multiple=True),
        Field("release_notes", IRI, "releaseNotes"),
        #Field("screenshots")
        Field("requirements", str, "softwareRequirements"),
        Field("summary", str, "headline"),
        Field("contributors", Person, "author", multiple=True), #"wasAttributedTo"),
        Field("copyright", [Person, Organization], "copyrightHolder"),
        Field("homepage", IRI, "url"),
        Field("documentation", IRI, "documentation"),
        Field("help", IRI, "softwareHelp"),
        Field("source_code", IRI, "code"),
        Field("programming_languages", ProgrammingLanguage, "programmingLanguage", multiple=True),
        Field("funding", Organization, "funder", multiple=True),
        Field("components", "software.Software", "hasPart", multiple=True),
        Field("is_free", bool, "isAccessibleForFree"),
        #Field("image", IRI, "image", multiple=True),
        Field("keywords", Keyword, "keywords", multiple=True),  # todo: add Keyword class
        Field("version", str, "version", required=True),
        #Field("device"),
        Field("features", SoftwareFeature, "feature", multiple=True),
        #Field("input_formats", str, ),
        #Field("output_formats", str),
        #Field("languages"),
        #Field("project", SoftwareProject, )
    )


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
