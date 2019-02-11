"""

"""

from nar.base import KGObject, KGProxy, KGQuery, cache, as_list
from nar.data import FileAssociation, CSCSFile


class MINDSObject(KGObject):
    """docstring"""
    context = [
        "https://nexus-int.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0",
        {
            "schema": "http://schema.org/",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "prov": "http://www.w3.org/ns/prov#",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "minds": 'https://schema.hbp.eu/'
        }
    ]

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        #assert cls.type[0] in D["@type"]
        data = {}
        for key, value in D.items():
            if key.startswith('http://hbp.eu/minds'):
                name = key.split("#")[1]
            elif key.startswith('https://schema.hbp.eu/minds/'):
                name = key.split('https://schema.hbp.eu/minds/')[1]
            elif key.startswith('http://schema.org/'):
                name = key.split('http://schema.org/')[1]
            elif key in ("http://www.w3.org/ns/prov#qualifiedAssociation", "prov:qualifiedAssociation"):
                name = "associated_with"
            elif ":" in key:
                name = key.split(":")[1]
            else:
                name = None
            if name in cls.property_names:
                if name in obj_types:
                    if isinstance(value, list):
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value]
                    elif "@list" in value:
                        assert len(value) == 1
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value['@list']]
                    else:
                        data[name] = KGProxy(obj_types[name], value["@id"])
                else:
                    data[name] = value
        data["id"] = D["@id"]
        data["instance"] = instance
        return cls(**data)

    def save(self, client, exists_ok=True):
        """docstring"""
        if self.instance:
            data = self.instance.data
        else:
            data = {
                "@context": self.context,
                "@type": self.type
            }
        for property_name in self.property_names:
            if hasattr(self, property_name):
                if property_name in ("name", "description"):
                    property_url = "http://schema.org/" + property_name
                elif property_name == "associated_with":
                    property_url = "http://www.w3.org/ns/prov#qualifiedAssociation"
                else:
                    property_url = "https://schema.hbp.eu/" + property_name

                value = getattr(self, property_name)
                if isinstance(value, (str, int, float)):  # todo: extend with other simple types
                    data[property_url] = value
                elif isinstance(value, (KGObject, KGProxy)):
                    data[property_url] = {
                        "@id": value.id,
                        "@type": value.type
                    }
                elif isinstance(value, (list, tuple)) and len(value) > 0 and isinstance(value[0], KGObject):
                    data[property_url] = [{
                        "@id": item.id,
                        "@type": item.type
                    } for item in value]
                else:
                    raise NotImplementedError("Can't handle {}".format(type(value)))
        self._save(data, client, exists_ok)


class Dataset(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v1.0.0"
    #type = ["https://schema.hbp.eu/Dataset"]
    type = ["minds:Dataset"]
    property_names = ["activity", "component", "contributors", "created_at", "datalink",
                      "embargo_status", "formats", "license", "owners", "parcellation",
                      "publications", "release_date", "specimen_group",
                      "description", "name", "associated_with"]


class Activity(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v1.0.0"
    #type = ["https://schema.hbp.eu/Activity"]
    type = ["minds:Activity"]
    property_names = ["created_at", "ethics", "methods", "preparation", "protocols",
                      "description", "name", "associated_with"]


class Method(MINDSObject):
    """docstring"""
    path = "minds/experiment/method/v1.0.0"
    #type = ["https://schema.hbp.eu/ExperimentMethod"]
    type = ["minds:ExperimentMethod"]
    property_names = ["name", "associated_with"]


class SpecimenGroup(MINDSObject):
    """docstring"""
    path = "minds/core/specimengroup/v1.0.0"
    type = ["minds:SpecimenGroup"]
    property_names = ["created_at", "subjects", "name", "associated_with"]


class MINDSSubject(MINDSObject):
    """docstring"""
    # name qualified to avoid clash with nsg:Subject
    # pending addition of namespaces to registry
    path = "minds/experiment/subject/v1.0.0"
    #type = ["https://schema.hbp.eu/ExperimentSubject"]
    type = ["minds:ExperimentSubject"]
    property_names = ["age", "age_category", "causeOfDeath", "samples", "sex", "species",
                     "strains", "name", "associated_with"]


class License(MINDSObject):
    """docstring"""
    #path = "minds/core/licensetype/v1.0.0"
    type = ["minds:LicenseType"]
    property_names = ["name", "associated_with"]


class EmbargoStatus(MINDSObject):
    """docstring"""
    path = "minds/core/embargostatus/v1.0.0"
    #type = ["https://schema.hbp.eu/EmbargoStatus"]
    type = ["minds:EmbargoStatus"]
    property_names = ["name", "associated_with"]


class Sample(MINDSObject):
    """docstring"""
    path = "minds/experiment/sample/v1.0.0"
    #type = ["https://schema.hbp.eu/ExperimentSample"]
    type = ["minds:ExperimentSample"]
    property_names = ["name", "methods", "parcellationAtlas", "parcellationRegion",
                      "associated_with"]

    def get_files(self, client):
        query = {
            "path": "linkinginstance:to",
            "op": "eq",
            "value": self.id
        }
        context = {
            "minds": "https://schema.hbp.eu/minds/",
            "linkinginstance": "https://schema.hbp.eu/linkinginstance/",
        }
        links = KGQuery(FileAssociation, query, context).resolve(client)
        return [CSCSFile.from_uri(link.from_["@id"], client) for link in as_list(links)]


class Person(MINDSObject):
    """docstring"""
    path = "minds/core/person/v1.0.0"
    type = ["minds:Person"]
    property_names = ["name"]


class PLAComponent(MINDSObject):
    """docstring"""
    path = "minds/core/placomponent/v1.0.0"
    type = ["minds:PLAComponent"]
    property_names = ["name", "description"]

    @property
    def datasets(self):
        query = {
            "path": "minds:component",
            "op": "eq",
            "value": self.id
        }
        context = {
            "minds": "https://schema.hbp.eu/minds/"
        }
        return KGQuery(Dataset, query, context)


class AgeCategory(MINDSObject):
    path = "minds/core/agecategory/v1.0.0"
    type = ["minds:Agecategory"]
    property_names = ["name"]


class Sex(MINDSObject):
    path = "minds/core/sex/v1.0.0"
    type = ["minds:Sex"]
    property_names = ["name"]


class Species(MINDSObject):
    path = "minds/core/species/v1.0.0"
    type = ["minds:Species"]
    property_names = ["name"]


class ParcellationRegion(MINDSObject):
    path = "minds/core/parcellationregion/v1.0.0"
    type = ["minds:Parcellationregion"]
    property_names = ["name"]


# Alias some classes to reflect names used in KG Search
Project = PLAComponent


# todo: integrate this into the registry
obj_types = {
    "dataset": Dataset,
    "activity": Activity,
    "methods": Method,
    "specimen_group": SpecimenGroup,
    "subjects": MINDSSubject,
    "license": License,
    "embargo_status": EmbargoStatus,
    "samples": Sample,
    "owners": Person,
    "contributors": Person,
    "component": PLAComponent,
    "age_category": AgeCategory,
    "sex": Sex,
    "species": Species,
    "parcellationRegion": ParcellationRegion
}
