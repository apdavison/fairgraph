"""

"""

from nar.base import KGObject, KGProxy, cache


class MINDSObject(KGObject):
    """docstring"""
    context = "https://nexus-int.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0"

    def __init__(self, id=None, instance=None, **properties):
        for key, value in properties.items():
            if key not in self.property_names:
                raise TypeError(f"{self.__class__.__name__} got an unexpected keyword argument {key}")
            else:
                setattr(self, key, value)
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r} {self.id!r})')
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))

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
                    else:
                        data[name] = KGProxy(obj_types[name], value["@id"])
                else:
                    data[name] = value
        data["id"] = D["@id"]
        data["instance"] = instance
        return cls(**data)


class Dataset(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v0.0.4"
    #type = ["http://hbp.eu/minds#Dataset"]
    type = ["hbp:Dataset"]
    property_names = ["activity", "component", "contributors", "created_at", "datalink", 
                      "embargo_status", "formats", "license", "owners", "parcellation",
                      "publications", "release_date", "specimen_group",
                      "description", "name", "associated_with"]


class Activity(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v0.0.4"
    #type = ["http://hbp.eu/minds#Activity"]
    type = ["hbp:Activity"]
    property_names = ["created_at", "ethics", "methods", "preparation", "protocols",
                      "description", "name", "associated_with"]


class Method(MINDSObject):
    """docstring"""
    path = "minds/experiment/method/v0.0.4"
    #type = ["http://hbp.eu/minds#ExperimentMethod"]
    type = ["hbp:ExperimentMethod"]
    property_names = ["name", "associated_with"]


class SpecimenGroup(MINDSObject):
    """docstring"""
    path = "minds/core/specimengroup/v0.0.4"
    #type = ["hbp:SpecimenGroup"]
    property_names = ["created_at", "subjects", "name", "associated_with"]


class MINDSSubject(MINDSObject):
    """docstring"""
    # name qualified to avoid clash with nsg:Subject
    # pending addition of namespaces to registry
    path = "minds/experiment/subject/v0.0.4"
    #type = ["http://hbp.eu/minds#ExperimentSubject"]
    type = ["hbp:ExperimentSubject"]
    property_names = ["age", "age_category", "causeOfDeath", "samples", "sex", "species", 
                     "strains", "name", "associated_with"]


class License(MINDSObject):
    """docstring"""
    #path = "minds/core/licensetype/v0.0.4"
    type = ["hbp:LicenseType"]
    property_names = ["name", "associated_with"]


class EmbargoStatus(MINDSObject):
    """docstring"""
    path = "minds/core/embargostatus/v0.0.4"
    #type = ["http://hbp.eu/minds#EmbargoStatus"]
    type = ["hbp:EmbargoStatus"]
    property_names = ["name", "associated_with"]


class Sample(MINDSObject):
    """docstring"""
    path = "minds/experiment/sample/v0.0.4"
    #type = ["http://hbp.eu/minds#ExperimentSample"]
    type = ["hbp:ExperimentSample"]
    property_names = ["name", "methods", "parcellation_atlas", "parcellation_region",
                      "associated_with"]


class Person(MINDSObject):
    """docstring"""
    path = "minds/core/person/v0.0.4"
    type = ["hbp:Person"]
    property_names = ["name"]


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
    "owners": Person
}