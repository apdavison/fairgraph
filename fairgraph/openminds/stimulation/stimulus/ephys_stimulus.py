"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class EphysStimulus(KGObject):
    """

    """
    default_space = "in-depth"
    type = ["https://openminds.ebrains.eu/stimulation/EphysStimulus"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("stimulus_type", "openminds.controlledterms.ElectricalStimulusType", "vocab:stimulusType", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ()
