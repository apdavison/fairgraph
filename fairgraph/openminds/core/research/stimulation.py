"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class Stimulation(KGObjectV3):
    """
    
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Stimulation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("stimulation_approach", "openminds.controlledterms.StimulationApproach", "vocab:stimulationApproach", multiple=False, required=True,
              doc="no description available"),
        Field("stimulus_type", "openminds.controlledterms.StimulusType", "vocab:stimulusType", multiple=False, required=True,
              doc="no description available"),
        
    ]
    existence_query_fields = ('stimulation_approach', 'stimulus_type')

