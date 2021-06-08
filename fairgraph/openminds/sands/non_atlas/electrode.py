"""
Structured information on an electrode.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class Electrode(KGObjectV3):
    """
    Structured information on an electrode.
    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/sands/Electrode"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("electrode_contacts", "openminds.sands.ElectrodeContact", "vocab:electrodeContact", multiple=True, required=True,
              doc="Not shielded part of a conductor that is used to establish electrical contact with a nonmetallic part of a circuit."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the electrode within a particular product."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ("lookup_label",)
