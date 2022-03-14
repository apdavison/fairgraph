"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ElectrodeArray(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/ElectrodeArray"]
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
        Field("electrodes", "openminds.ephys.Electrode", "vocab:electrodes", multiple=True, required=True,
              doc="Elements in a semiconductor device that emits or collects electrons or holes or controls their movements."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the electrode array within a particular product."),

    ]
    existence_query_fields = ('electrodes', 'internal_identifier')
