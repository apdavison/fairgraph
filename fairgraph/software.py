# encoding: utf-8
"""
Metadata about, or related to, software
"""

# Copyright 2018-2019 CNRS and Universität Trier

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import datetime
from dateutil import parser as date_parser
from .base import KGObject, cache, KGProxy, build_kg_object, Distribution, as_list, KGQuery, OntologyTerm
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


class Software(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/software/software/v0.1.1"
    type = ["prov:Entity", "nsg:Software"]

    context = {
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "schema": "http://schema.org/"
    }

    def __init__(self, name, version, summary=None, description=None, identifier=None,
                 citation=None, license=None, release_date=None, previous_version=None,
                 contributors=None, project=None, image=None, download_url=None,
                 access_url=None, categories=None, subcategories=None,
                 operating_system=None, release_notes=None, requirements=None, copyright=None,
                 components=None, part_of=None,
                 funding=None, languages=None, features=None, keywords=None, is_free=None,
                 homepage=None, documentation=None, help=None, id=None, instance=None):
        self.name = name
        self.version = version
        self.summary = summary
        self.description = description
        self.identifier = identifier
        self.citation = citation
        self.license = license
        self.release_date = release_date
        self.previous_version = previous_version
        self.contributors = contributors
        self.project = project
        self.image = image
        self.download_url = download_url
        self.access_url = access_url
        self.categories = categories
        self.subcategories = subcategories
        self.operating_system = operating_system
        self.release_notes = release_notes
        self.requirements = requirements
        self.copyright = copyright
        self.components = components
        self.part_of = part_of
        self.funding = funding
        self.languages = languages
        self.features = features
        self.keywords = keywords
        self.is_free = is_free
        self.homepage = homepage
        self.documentation = documentation
        self.help = help
        self.id = id
        self.instance = instance

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.version!r}, '
                '{self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, use_cache=True, resolved=False):
        D = instance.data
        assert 'nsg:Software' in D["@type"]
        obj = cls(name=D["schema:name"],
                  version=D["schema:version"],
                  summary=D.get("schema:headline"),
                  description=D.get("schema:description"),
                  #identifier=build_kg_object(Identifier, D .get("schema:identifier")),  # todo: implement commons.Identifier
                  citation=D.get("schema:citation"),
                  license=build_kg_object(License, D.get("schema:license")),
                  release_date=date_parser.parse(D.get("schema:dateCreated"))
                               if "schema:dateCreated" in D else None,
                  previous_version=build_kg_object(Software, D.get("prov:wasRevisionOf")),
                  contributors=build_kg_object(Person, D.get("prov:wasAttributedTo")),
                  #project=D.get(""),  # todo: add link to SoftwareProject to schema?
                  image=D["schema:image"]["@id"] if "schema:image" in D else None,
                  download_url=D["schema:distribution"].get("schema:downloadURL") if "schema:distribution" in D else None,
                  access_url=D["schema:distribution"].get("schema:accessURL") if "schema:distribution" in D else None,
                  categories=build_kg_object(SoftwareCategory, D.get("schema:applicationCategory")),
                  subcategories=build_kg_object(SoftwareCategory, D.get("schema:applicationSubCategory")),
                  operating_system=build_kg_object(OperatingSystem, D.get("schema:operatingSystem")),
                  release_notes=D.get("schema:releaseNotes"),  # should probably contain ["@id"] ?
                  requirements=D.get("schema:softwareRequirements"),
                  copyright=build_kg_object(Organization, D.get("schema:copyrightHolder")),
                  components=build_kg_object(Software, D.get("schema:hasPart")),
                  part_of=build_kg_object(Software, D.get("schema:partOf")),
                  funding=build_kg_object(Organization, D.get("schema:funder")),
                  languages=build_kg_object(ProgrammingLanguage, D.get("schema:programmingLanguage")),
                  #features=build_kg_object(SoftwareFeature, D.get("schema:feature")),  # todo: implement SoftwareFeature
                  keywords=D.get("schema:keywords"),
                  is_free=D.get("schema:isAccessibleForFree"),
                  homepage=D["schema:url"]["@id"] if "schema:url" in D else None,
                  documentation=D["schema:documentation"]["@id"] if "schema:documentation" in D else None,
                  help=D["schema:softwareHelp"]["@id"] if "schema:softwareHelp" in D else None,
                  id=D.get("@id"),
                  instance=instance)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["schema:name"] = self.name
        data["schema:version"] = self.version
        if self.summary:
            data["schema:headline"] = self.summary
        if self.description:
            data["schema:description"] = self.description
        if self.identifier:
            data["schema:identifier"] = self.identifier.to_jsonld()
        if self.citation:
            data["schema:citation"] = self.citation
        if self.license:
            data["schema:license"] = self.license.to_jsonld()
        if self.release_date:
            data["schema:dateCreated"] = self.release_date.isoformat()
            data["schema:copyrightYear"] = self.release_date.year
        if self.previous_version:
            data["prov:wasRevisionOf"] = {
                "@id": self.previous_version.id,
                "@type": self.previous_version.type
            }
        if self.contributors:
            data["prov:wasAttributedTo"] = [{
                    "@id": person.id,
                    "@type": person.type
                } for person in as_list(self.contributors)]
        if self.image:
            data["schema:image"] = {"@id": self.image}
        if self.download_url:
            data["schema:distribution"] = {
                "schema:downloadURL": {"@id": self.download_url}
            }
        if self.access_url:
            if "schema:distribution" not in data:
                data["schema:distribution"] = {}
            data["schema:distribution"]["schema:accessURL"] = {"@id": self.access_url}
        if self.categories:
            data["schema:applicationCategory"] = [cat.to_jsonld() for cat in as_list(self.categories)]
        if self.subcategories:
            data["schema:applicationSubCategory"] = [cat.to_jsonld() for cat in as_list(self.subcategories)]
        if self.operating_system:
            data["schema:operatingSystem"] = [os.to_jsonld()
                                              for os in as_list(self.operating_system)]
        if self.release_notes:
            data["schema:releaseNotes"] = self.release_notes
        if self.requirements:
            data["schema:softwareRequirements"] = self.requirements
        if self.copyright:
            data["schema:copyrightHolder"] = {
                "@id": self.copyright.id,
                "@type": self.copyright.type
            }
        if self.components:
            data["schema:hasPart"] = [{
                    "@id": part.id,
                    "@type": part.type
                } for part in as_list(self.components)]
        if self.part_of:
            data["schema:partOf"] = [{
                    "@id": parent.id,
                    "@type": parent.type
                } for parent in as_list(self.part_of)]
        if self.funding:
            data["schema:funder"] = [{
                    "@id": org.id,
                    "@type": org.type
                } for org in as_list(self.funding)]
        if self.languages:
            data["schema:programmingLanguage"] = [lang.to_jsonld() for lang in as_list(self.languages)]
        if self.features:
            data["schema:feature"] = [{
                    "@id": feature.id,
                    "@type": feature.type
                } for feature in as_list(self.features)]
        if self.keywords:
            data["schema:keywords"] = self.keywords
        if self.is_free:
            data["schema:isAccessibleForFree"] = self.is_free
        if self.homepage:
            data["schema:url"] = {"@id": self.homepage}
        if self.documentation:
            data["schema:documentation"] = {"@id": self.documentation}
        if self.help:
            data["schema:softwareHelp"] = {"@id": self.help}
        return data


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
