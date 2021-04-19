"""

"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class ParcellationTerminology(KGObject):
    """
    
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/ParcellationTerminology"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("anatomical_entitys", "openminds.sands.AnatomicalEntity", "vocab:anatomicalEntity", multiple=True, required=True,
              doc="Physical component of a body, organ, or tissue."),
        Field("defined_ins", "openminds.core.File", "vocab:definedIn", multiple=True, required=False,
              doc="Reference to a file instance in which something is stored."),
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the parcellation terminology."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the parcellation terminology."),
        
    ]
    existence_query_fields = ('name',)