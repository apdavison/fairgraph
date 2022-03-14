"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Electrode(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Electrode"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("amplifiers", "openminds.ephys.Device", "vocab:amplifier", multiple=True, required=False,
              doc="no description available"),
        Field("electrode_contacts", "openminds.ephys.ElectrodeContact", "vocab:electrodeContact", multiple=True, required=True,
              doc="Not shielded part of a conductor that is used to establish electrical contact with a nonmetallic part of a circuit."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the electrode within a particular product."),

    ]
    existence_query_fields = ('electrode_contacts', 'internal_identifier')
