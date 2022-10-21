"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Measurement(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/core/Measurement"]
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
        Field("measured_with", ["openminds.ephys.ElectrodeArrayUsage", "openminds.ephys.ElectrodeUsage", "openminds.ephys.PipetteUsage"], "vocab:measuredWith", multiple=False, required=False,
              doc="no description available"),
        Field("timestamp", datetime, "vocab:timestamp", multiple=False, required=False,
              doc="no description available"),
        Field("values", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:value", multiple=True, required=True,
              doc="Entry for a property."),

    ]
