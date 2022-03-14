"""
Metadata for entities that are used in multiple contexts (e.g. in both electrophysiology and in simulation).

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


from __future__ import unicode_literals
import sys
import inspect
import logging
from datetime import date
from .base_v2 import KGObject, KGQuery, as_list, Distribution
from .fields import Field

from .commons import Address, Species, Strain, Genotype, Sex, Age, QuantitativeValue, Handedness, Group


DEFAULT_NAMESPACE = None
# core is used everywhere, so it makes no sense to set a default namespace
# the namespace to be used in a given context should be set using "use_namespace()"


logger = logging.getLogger("fairgraph")


class Subject(KGObject):
    """The individual organism that is the subject of an experimental study."""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/subject/v0.1.2"
    type = ["nsg:Subject", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "value": "schema:value",
        "minValue": "schema:minValue",
        "maxValue": "schema:maxValue",
        "unitCode": "schema:unitCode",
        "label": "rdfs:label",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "species": "nsg:species",  # change from nsg:species to "http://dbpedia.org/ontology/Species" ?
        "strain": "nsg:strain",
        "age": "nsg:age",  # change from nsg:age to "http://dbpedia.org/ontology/age" ?
        "period": "nsg:period",
        "sex": "nsg:sex",
        "genotype": "nsg:genotype",
        "handedness": "nsg:handedness",
        "deathDate": "schema:deathDate",
        "group": "nsg:group",
        "providerId": "nsg:providerId"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("species", Species, "species", required=True),
        Field("strain", Strain, "strain"),
        Field("genotype", Genotype, "genotype"),
        Field("sex", Sex, "sex"),
        Field("handedness", Handedness, "handedness"),
        Field("age", Age, "age"),
        Field("death_date", date, "deathDate"),
        Field("group", Group, "group")
    )

    def __init__(self, name, species, age=None, sex=None, handedness=None, strain=None, genotype=None, death_date=None, group=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Organization(KGObject):
    """
    An organization associated with research data or models, e.g. a university, lab or department.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/core/organization/v0.1.0"
    type = ["nsg:Organization"]
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "parentOrganization": "schema:parentOrganization",
        "address": "schema:address",
        "addressLocality": "schema:addressLocality",
        "addressCountry": "schema:addressCountry",
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("address", Address, "address"),
        Field("parent", "core.Organization", "parentOrganization")
    )

    def __init__(self, name, address=None, parent=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Person(KGObject):
    """
    A person associated with research data or models, for example as an experimentalist,
    or a data analyst.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/core/person/v0.1.0"
    type = ["nsg:Person", "prov:Agent"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "familyName": "schema:familyName",
        "givenName": "schema:givenName",
        "email": "schema:email",
        "affiliation": "schema:affiliation"
    }
    fields = (
        Field("family_name", str, "familyName", required=True, doc="Family name / surname"),
        Field("given_name", str, "givenName", required=True, doc="Given name"),
        Field("email", str, "email", doc="e-mail address"),
        Field("affiliation", Organization, "affiliation",
              doc="Organization to which person belongs")
    )
    existence_query_fields = ("family_name", "given_name")

    def __init__(self, family_name, given_name, email=None,
                 affiliation=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @property
    def full_name(self):
        return f'{self.given_name} {self.family_name}'

    @classmethod
    def list(cls, client, size=100, api="query", scope="released", resolved=False, **filters):
        """List all objects of this type in the Knowledge Graph"""
        if api == 'nexus':
            context = {
                "schema": "http://schema.org/"
            }
            filter_queries = []
            for name, value in filters.items():
                if name in ("first_name", "given_name"):
                    filter_queries.append({
                        'path': 'schema:givenName',
                        'op': 'eq',
                        'value': value
                    })
                elif name in ("family_name", "last_name", "surname"):
                    filter_queries.append({
                        "path": "schema:familyName",
                        "op": "eq",
                        "value": value
                    })
                elif name == "email":
                    filter_queries.append({
                        "path": "schema:email",
                        "op": "eq",
                        "value": value
                    })
                else:
                    raise ValueError(f"The only supported filters are by first (given) name, last (family) name or email. You specified {name}")
            if len(filter_queries) == 0:
                return client.list(cls, size=size, api=api)
            elif len(filter_queries) == 1:
                filter_query = filter_queries[0]
            else:
                filter_query = {
                    "op": "and",
                    "value": filter_queries
                }
            filter_query = {"nexus": filter_query}
            return KGQuery(cls, filter_query, context).resolve(client, api=api, size=size)
        elif api == "query":
            return super(Person, cls).list(client, size=size, api=api,
                                           scope=scope, resolved=resolved, **filters)
        else:
            raise ValueError("'api' must be either 'nexus' or 'query'")

    @classmethod
    def me(cls, client, api="query", allow_multiple=False):
        """Return the Person who is currently logged-in.

        (the user associated with the token stored in the client).

        If the Person node does not exist in the KG, it will be created.
        """
        user_info = client.user_info()
        given_name = user_info["givenName"]
        family_name = user_info["familyName"]
        email = [entry["value"] for entry in user_info["emails"] if entry["primary"]][0]
        # first look for a node that matches name and primary email
        people = Person.list(client, api=api, scope="latest", family_name=family_name,
                             given_name=given_name, email=email, resolved=False)
        # if we don't find a node, try to match by any email
        if not people:
            for entry in user_info["emails"]:
                people.extend(Person.list(client, api=api, scope="latest", email=entry["value"],
                                          resolved=False))
        # if we still don't find a node, try to match by name
        if not people:
            people = Person.list(client, api=api, scope="latest", family_name=family_name,
                                 given_name=given_name, resolved=False)
        # otherwise, create a new node
        if people:
            if isinstance(people, list):
                if len(people) > 1:
                    if allow_multiple:
                        return people
                    else:
                        raise Exception("Found multiple entries. "
                                        "Use the 'allow_multiple' option to avoid this error.")
                else:
                    people = people[0]
            return people
        else:
            person = Person(family_name=family_name, given_name=given_name, email=email)
            # todo: add linked organization based on user_info affiliation
            person.save(client)
            return person


class Identifier(KGObject):
    namespace = "nexus"
    _path = "/schemaorgsh/identifier/v0.1.0"
    type = ["schema:Identifier"]


class Material(KGObject):
    """
    Metadata about a chemical product or other material used in an experimental protocol.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/core/material/v0.1.0"
    type = ["nsg:Material", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema: name",
        "reagentMolarWeight": "nsg:reagentMolarWeight",
        "reagentLinearFormula": "nsg:reagentLinearFormula",
        "reagentSKU": "schema:sku",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
            },
        "vendor": "nsg:reagentVendor"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("molar_weight", QuantitativeValue, "reagentMolarWeight"),
        Field("formula", str, "reagentLinearFormula"),
        Field("stock_keeping_unit", str, "reagentSKU"), # doi
        Field("reagent_distribution", Distribution, "distribution"),
        Field("vendor", Organization, "vendor")
        )

    def __init__(self, name, molar_weight=None, formula=None,
                        stock_keeping_unit=None, reagent_distribution=None, vendor=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Step(KGObject):
    """
    A step in an experimental protocol.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/core/protocol/v0.1.2"
    type = ["nsg:Step", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "previousStepName": "nsg:previousStepName",
        "sequenceNumber": "nsg:sequenceNumber",
        "identifier": "schema:identifier",
        "description": "schema:description",
        "version" : "nsg:version",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        },
        "material":"nsg:material",
        "wasAssociatedWith": "prov:wasAssociatedWith",
    }
    fields = (
        Field("name", (str, int), "name", required=True),
        Field("previous_step_name", (str, int), "previousStepName"),
        Field("sequence_number", int, "sequenceNumber"),
        Field("identifier", str, "identifier"), # doi
        Field("version", (str, int), "version"),
        Field("distribution", Distribution, "distribution"), # external link
        Field("description", str, "description"),
        Field("materials", Material, "material", multiple=True),
        Field("author", Person, "wasAssociatedWith", multiple=True),
        )

    def __init__(self, name, previous_step_name=None, sequence_number=None,
                 identifier=None, version=None, distribution=None,
                 description=None, materials=None, author=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Protocol(KGObject):
    """
    An experimental protocol.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/core/protocol/v0.1.2"
    type = ["nsg:Protocol", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "version" : "nsg:version",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        },
        "numberOfSteps": "nsg:numberOfSteps",
        "hasPart": "nsg:hasPart",
        "identifier": "nsg:identifier",
        "material":"nsg:material",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "datePublished": "nsg:datePublished"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("version", (str, int), "version"),
        Field("identifier", str, "identifier"), # DOI
        Field("distribution", Distribution, "distribution"), # external link
        Field("number_of_steps", int, "numberOfSteps"),
        Field("steps", Step, "hasPart", multiple=True),
        Field("materials", Material, "material", multiple=True),
        Field("author", Person, "wasAssociatedWith", multiple=True),
        Field("date_published", date, "datePublished")
        )

    def __init__(self, name, version=None, identifier=None, doi=None, distribution=None, number_of_steps=None,
    steps=None, materials=None, author=None, date_published=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Collection(KGObject):
    """A collection of other metadata objects"""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/collection/v0.1.0"
    type = ["nsg:Collection", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "size": "schema:size",
        "hadMember": "prov:hadMember"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("members", KGObject, "hadMember", required=True, multiple=True)
    )

    def __init__(self, name, members, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @property
    def size(self):
        return len(as_list(self.members))

    # def __repr__(self):
    #     return ('{self.__class__.__name__}('
    #             '{self.name!r}, {self.size!r}, {self.id})'.format(self=self))

    # @classmethod
    # @cache
    # def from_kg_instance(cls, instance, client, resolved=False):
    #     """
    #     docstring
    #     """
    #     D = instance.data
    #     for otype in cls.type:
    #         assert otype in D["@type"]

    #     return cls(name=D["name"],
    #                members=[KGProxy(None, member_uri["@id"])
    #                         for member_uri in D["hadMember"]],
    #                id=D["@id"],
    #                instance=instance)

    def _build_data(self, client, all_fields=False):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["size"] = len(as_list(self.members))
        data["hadMember"] = [{
            "@type": member.type,
            "@id": member.id
        } for member in as_list(self.members)]
        return data


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
