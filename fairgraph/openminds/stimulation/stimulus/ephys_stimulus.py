"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class EphysStimulus(KGObject):
    """ """

    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/stimulation/EphysStimulus"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "type",
            "openminds.controlledterms.ElectricalStimulusType",
            "vocab:type",
            doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
        ),
        Field(
            "is_stimulus_fors",
            "openminds.stimulation.StimulationActivity",
            "^vocab:stimulus",
            reverse="stimulus",
            multiple=True,
            doc="reverse of 'stimulus'",
        ),
    ]
    existence_query_fields = ()

    def __init__(self, type=None, is_stimulus_fors=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id, space=space, scope=scope, data=data, type=type, is_stimulus_fors=is_stimulus_fors
        )
