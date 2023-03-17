"""
Structured information about a measurement performed during a scientific experiment.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Measurement(EmbeddedMetadata):
    """
    Structured information about a measurement performed during a scientific experiment.
    """
    type_ = ["https://openminds.ebrains.eu/core/Measurement"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("measured_quantity", "openminds.controlledterms.MeasuredQuantity", "vocab:measuredQuantity", multiple=False, required=True,
              doc="no description available"),
        Field("measured_with", ["openminds.ephys.ElectrodeArrayUsage", "openminds.ephys.ElectrodeUsage", "openminds.ephys.PipetteUsage", "openminds.specimenprep.SlicingDeviceUsage"], "vocab:measuredWith", multiple=False, required=False,
              doc="no description available"),
        Field("timestamp", datetime, "vocab:timestamp", multiple=False, required=False,
              doc="no description available"),
        Field("values", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:value", multiple=True, required=True,
              doc="Entry for a property."),

    ]

    def __init__(self, additional_remarks=None, measured_quantity=None, measured_with=None, timestamp=None, values=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, additional_remarks=additional_remarks, measured_quantity=measured_quantity, measured_with=measured_with, timestamp=timestamp, values=values)