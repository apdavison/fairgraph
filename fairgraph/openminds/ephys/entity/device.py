"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Device(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Device"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the device."),
        Field("device_type", "openminds.controlledterms.DeviceType", "vocab:deviceType", multiple=False, required=True,
              doc="no description available"),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the device within a particular product."),
        Field("manufacturer", str, "vocab:manufacturer", multiple=False, required=True,
              doc="no description available"),
        Field("model_name", str, "vocab:modelName", multiple=False, required=True,
              doc="no description available"),
        Field("parameter_sets", "openminds.core.ParameterSet", "vocab:parameterSet", multiple=True, required=False,
              doc="Manner, position, or direction in which digital or physical properties are set to determine a particular function, characteristics or behavior of something."),
        Field("serial_number", str, "vocab:serialNumber", multiple=False, required=False,
              doc="no description available"),
        Field("software", "openminds.core.SoftwareVersion", "vocab:software", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('device_type', 'internal_identifier', 'manufacturer', 'model_name')
