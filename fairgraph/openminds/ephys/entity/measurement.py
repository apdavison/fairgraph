"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Measurement(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/ephys/Measurement"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the measurement."),
        Field("devices", ["openminds.ephys.Device", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"], "vocab:device", multiple=True, required=False,
              doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function."),
        Field("measured_quantity", "openminds.controlledterms.MeasuredQuantity", "vocab:measuredQuantity", multiple=False, required=False,
              doc="no description available"),
        Field("timestamp", datetime, "vocab:timestamp", multiple=False, required=True,
              doc="no description available"),
        Field("values", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:value", multiple=True, required=True,
              doc="Entry for a property."),

    ]
