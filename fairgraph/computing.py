
import sys, inspect
from .base_v2 import KGObject, cache, build_kg_object, Distribution, as_list
from .fields import Field
from .software import Software

DEFAULT_NAMESPACE = "neuromorphic"


class HardwareSystem(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/computing/hardware/v0.1.0"
    type = ["prov:Entity", "nsg:HardwareSystem"]  # maybe rename "ComputingHardwareSystem"
    context =  {
        "name": "schema:name",
        "description": "schema:description",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "schema": "http://schema.org/"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("description", str, "description")
    )

#class HardwareConfiguration(KGObject):
#    pass


class ComputingEnvironment(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/computing/environment/v0.1.0"
    type = ["prov:Entity", "nsg:ComputingEnvironment"]
    context = {
        "name": "schema:name",
        "description": "schema:description",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "dcterms": "http://purl.org/dc/terms/",
        "schema": "http://schema.org/",
        "hasPart": "dcterms:hasPart",
        "softwareRequirements": "schema:softwareRequirements",
        "hardwareConfiguration": "nsg:hardwareConfiguration"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("hardware", HardwareSystem, "hasPart", required=True),
        #Field("config", HardwareConfiguration, "hardwareConfiguration"),
        Field("config", str, "hardwareConfiguration"),
        Field("software", Software, "softwareRequirements", multiple=True),  # libraries, executables, compilers...
        Field("description", str, "description")
    )
    # todo: add identifier? Uniqueness should be based on all fields except description
    # but that will make for complex queries


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
