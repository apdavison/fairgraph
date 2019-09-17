
import sys, inspect
from .base import KGObject, cache, build_kg_object, Distribution, as_list

DEFAULT_NAMESPACE = "neuromorphic"


class HardwareSystem(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/computing/hardware/v0.1.0"
    type = ["prov:Entity", "nsg:HardwareSystem"]  # maybe rename "ComputingHardwareSystem"
    context =  [
        "{{base}}/contexts/neurosciencegraph/core/data/v0.3.1",
        "{{base}}/contexts/nexus/core/resource/v0.3.0",
        {
            "name": "schema:name",
            "description": "schema:description",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "prov": "http://www.w3.org/ns/prov#",
            "schema": "http://schema.org/"
        }
    ]

    def __init__(self, name, description=None, id=None, instance=None):
        self.name = name
        self.description = description
        self.id = id
        self.instance = instance

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r}, '
                '{self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:HardwareSystem' in D["@type"]
        obj = cls(name=D["name"],
                  description=D.get("description"),
                  id=D["@id"], instance=instance)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = {
            "name": self.name,
        }
        if self.description:
            data["description"] = self.description
        return data


#class HardwareConfiguration(KGObject):
#    pass


class ComputingEnvironment(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/computing/environment/v0.1.0"
    type = ["prov:Entity", "nsg:ComputingEnvironment"]
    context =  [
        "{{base}}/contexts/neurosciencegraph/core/data/v0.3.1",
        "{{base}}/contexts/nexus/core/resource/v0.3.0",
        {
            "name": "schema:name",
            "description": "schema:description",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "prov": "http://www.w3.org/ns/prov#",
            "schema": "http://schema.org/",
            "used": "prov:used",
            "softwareRequirements": "schema:softwareRequirements",
            "hardwareConfiguration": "nsg:hardwareConfiguration"
        }
    ]

    def __init__(self, name, hardware, config=None, libraries=None, description=None, id=None, instance=None):

        self.name = name
        self.hardware = hardware
        self.config = config
        self.libraries = libraries or []  # maybe call this "runtime", since it could include the operating system, Python version, etc.
        self.description = description
        self.id = id
        self.instance = instance

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.hardware!r}, '
                '{self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:ComputingEnvironment' in D["@type"]
        obj = cls(name=D["name"],
                  hardware=build_kg_object(HardwareSystem,
                                           [item for item in D.get("used")
                                            if "nsg:HardwareSystem" in item["@type"]][0]),
                  #config=build_kg_object(HardwareConfiguration,
                  #                       [item for item in D.get("used")
                  #                        if "nsg:HardwareConfiguration" in item["@type"]][0]),
                  config=D.get("hardwareConfiguration"),
                  libraries=D.get("softwareRequirements"),   # schema should define a SoftwareRequirementShape
                  description=D.get("description"),
                  id=D["@id"], instance=instance)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = {
            "name": self.name,
            "used": [
                {"@id": self.hardware.id, "@type": self.hardware.type}
            ]
        }
        if self.description:
            data["description"] = self.description
        if self.config:
            #data["used"].append({"@id": self.config.id, "@type": self.config.type})
            data["hardwareConfiguration"] = self.config
        if self.libraries:
            data["softwareRequirements"] = self.libraries
        return data


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
