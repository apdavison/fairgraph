"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ElectrodePlacementActivity(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/ElectrodePlacementActivity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("anesthesia", str, "vocab:anesthesia", multiple=False, required=True,
              doc="no description available"),
        Field("electrodes", ["openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray"], "vocab:electrodes", multiple=False, required=True,
              doc="Elements in a semiconductor device that emits or collects electrons or holes or controls their movements."),
        Field("input", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:input", multiple=False, required=False,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("output", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:output", multiple=False, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),

    ]
    existence_query_fields = ('anesthesia', 'electrodes')
