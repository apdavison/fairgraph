"""
core

"""

from .base import KGObject, KGProxy, cache
from .errors import ResourceExistsError
from .commons import Address, Species, Strain, Sex, Age


class Subject(KGObject):
    """docstring"""
    path = "neuralactivity/core/subject/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "label": "rdfs:label",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "species": "nsg:species",  # change from nsg:species to "http://dbpedia.org/ontology/Species" ?
        "strain": "nsg:strain",
        "age": "nsg:age",  # change from nsg:age to "http://dbpedia.org/ontology/age" ?
        "period": "nsg:period",
        "sex": "nsg:sex",
        "deathDate": "schema:deathDate",
        "providerId": "nsg:providerId"
    }

    def __init__(self, name, species, strain, sex, age, death_date, id=None):
        self.name = name
        self.species = species
        self.strain = strain
        self.sex = sex
        self.age = age
        self.death_date = death_date
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.species!r}, {self.strain!r}, {self.sex!r}, '
                f'{self.age!r}, {self.death_date!r}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        assert 'nsg:Subject' in D["@type"]
        return cls(D["name"], 
                   Species.from_jsonld(D["species"]), 
                   Strain.from_jsonld(D.get("strain", None)), 
                   Sex.from_jsonld(D["sex"]),
                   Age.from_jsonld(D["age"]),
                   D.get("deathDate", None), D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": Subject.context,
            "@type": "nsg:Subject",
        }
        data["name"] = self.name
        data["providerId"] = self.name
        data["species"] = self.species.to_jsonld()
        if self.strain:
            data["strain"] = self.strain.to_jsonld()
        if self.age:
            data["age"] = self.age.to_jsonld()
        if self.sex:
            data["sex"] = self.sex.to_jsonld()
        if self.death_date:
            data["deathDate"] = self.death_date
        self._save(data, client, exists_ok)


class Organization(KGObject):
    """docstring"""
    path = "neuralactivity/core/organization/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "parentOrganization": "schema:parentOrganization",
        "address": "schema:address",
        "addressLocality": "schema:addressLocality",
        "addressCountry": "schema:addressCountry",
    }

    def __init__(self, name, address, parent, id=None):
        self.name = name
        self.address = address
        self.parent = parent
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.address!r}, {self.parent}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        assert 'nsg:Organization' in D["@type"]
        if "parentOrganization" in D:
            parent = KGProxy(cls, D["parentOrganization"]["@id"])
        else:
            parent = None
        address = Address(D["address"]["addressLocality"], D["address"]["addressCountry"])
        return cls(D["name"], address, parent, id=D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": Organization.context,
            "@type": "nsg:Organization",
        }
        data["name"] = self.name
        data["address"] = {
            "@type": "schema:PostalAddress",
            "addressLocality": self.address.locality,
            "addressCountry": self.address.country
        }
        if self.parent:
            if self.parent.id is None:
                self.parent.save(client)
            data["parent"] = {
                "@type": "nsg:Organization",
                "@id": self.parent.id
            }
        self._save(data, client, exists_ok)


class Person(KGObject):
    """docstring"""
    path = "neuralactivity/core/person/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "familyName": "schema:familyName",
        "givenName": "schema:givenName",
        "email": "schema:email",
        "affiliation": "schema:affiliation"
    }

    def __init__(self, family_name, given_name, email, affiliation, id=None):
        self.family_name = family_name
        self.given_name = given_name
        self.email = email
        self.affiliation = affiliation
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.family_name!r}, {self.given_name!r}, {self.email}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        assert 'nsg:Person' in D["@type"]
        affiliation = KGProxy(Organization, D["affiliation"]["@id"])
        return cls(D["familyName"], D["givenName"], D.get("email", None),
                   affiliation, D["@id"])

    def exists(self, client):
        """Check if this Person already exists in the KnowledgeGraph"""
        if self.id:
            return True
        else:
            context = {"schema": "http://schema.org/"},
            query_filter = {
                "op": "and",
                "value": [
                    {
                        "path": "schema:familyName",
                        "op": "eq",
                        "value": self.family_name
                    },
                    {
                        "path": "schema:givenName",
                        "op": "eq",
                        "value": self.given_name
                    }
                ]
            }
            response = client.filter_query(self.path, query_filter, context)
            if response:
                self.id = response[0].data["@id"]
            return bool(response)

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": Person.context,
            "@type": "nsg:Person",
        }
        data["familyName"] = self.family_name
        data["givenName"] = self.given_name
        if self.email:
            data["email"] = self.email
        if self.affiliation:
            if self.affiliation.id is None:
                self.affiliation.save(client)
            data["affiliation"] = {
                "@type": "nsg:Organization",
                "@id": self.affiliation.id
            }
        self._save(data, client, exists_ok)
        
    def resolve(self, client):
        if hasattr(self.affiliation, "resolve"):
            self.affiliation = self.affiliation.resolve(client)
