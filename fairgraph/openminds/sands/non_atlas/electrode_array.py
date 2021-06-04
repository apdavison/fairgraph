"""
Structured information on an electrode array.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class ElectrodeArray(KGObjectV3):
    """
    Structured information on an electrode array.
    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/sands/ElectrodeArray"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("electrodess", "openminds.sands.Electrode", "vocab:electrodes", multiple=True, required=True,
              doc="Elements in a semiconductor device that emits or collects electrons or holes or controls their movements."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the electrode array within a particular product."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = None