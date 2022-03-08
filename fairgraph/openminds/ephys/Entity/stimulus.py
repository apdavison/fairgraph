"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Stimulus(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Stimulus"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("stimulus_type", "openminds.controlledterms.StimulusType", "vocab:stimulusType", multiple=False, required=True,
              doc="no description available"),
        Field("stimulus_approach", "openminds.controlledterms.StimulationApproach", "vocab:stimulusApproach", multiple=False, required=True,
              doc="no description available"),
        Field("parameter_sets", "openminds.core.ParameterSet", "vocab:parameterSet", multiple=True, required=False,
              doc="Manner, position, or direction in which digital or physical properties are set to determine a particular function, characteristics or behavior of something."),
        Field("data_locations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:dataLocation", multiple=True, required=True,
              doc="no description available"),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),

    ]
    existence_query_fields = ('stimulus_type', 'stimulus_approach', 'data_locations')
