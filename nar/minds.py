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
        return (f'{self.__class__.__name__}('
                f'{self.name!r} {self.id!r})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        assert cls.type[0] in D["@type"]
        data = {}
        for key, value in D.items():
            if key.startswith('http://hbp.eu/minds'):
                name = key.split("#")[1]
            elif key.startswith('http://schema.org/'):
                name = key.split('http://schema.org/')[1]
            elif key == "http://www.w3.org/ns/prov#qualifiedAssociation":
                name = "associated_with"
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
        return cls(**data)


class Dataset(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v0.0.4"
    type = ["http://hbp.eu/minds#Dataset"]
    property_names = ["activity", "component", "contributors", "created_at", "datalink", 
                      "embargo_status", "formats", "license_id", "owners", "parcellation",
                      "publicationDOI", "publications", "reference_space", "specimen_group",
                      "description", "name", "associated_with"]


class Activity(MINDSObject):
    """docstring"""
    path = "minds/core/dataset/v0.0.4"
    type = ["http://hbp.eu/minds#Activity"]
    property_names = ["created_at", "ethics", "methods", "preparation", "protocols",
                      "description", "name", "associated_with"]


class Method(MINDSObject):
    """docstring"""
    path = "minds/experiment/method/v0.0.4"
    type = ["http://hbp.eu/minds#ExperimentMethod"]
    property_names = ["name", "associated_with"]


class SpecimenGroup(MINDSObject):
    """docstring"""
    path = "minds/core/specimengroup/v0.0.4"
    type = ["http://hbp.eu/minds#SpecimenGroup"]
    property_names = ["created_at", "subjects", "name", "associated_with"]


class MINDSSubject(MINDSObject):
    """docstring"""
    # name qualified to avoid clash with nsg:Subject
    # pending addition of namespaces to registry
    path = "minds/experiment/subject/v0.0.4"
    type = ["http://hbp.eu/minds#ExperimentSubject"]
    property_name = ["age", "age_category", "causeOfDeath", "samples", "sex", "species", 
                     "strains", "name", "associated_with"]


# todo: integrate this into the registry
obj_types = {
    "dataset": Dataset,
    "activity": Activity,
    "method": Method,
    "specimen_group": SpecimenGroup,
    "subject": MINDSSubject
}