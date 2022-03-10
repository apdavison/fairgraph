"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Cell(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Cell"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("semantically_anchored_to", "openminds.controlledterms.UBERONParcellation", "vocab:semanticallyAnchoredTo", multiple=False, required=True,
              doc="Reference to a related anatomical structure without providing a quantitative proof of the claimed relation."),
        Field("cell_type", "openminds.controlledterms.CellType", "vocab:cellType", multiple=False, required=True,
              doc="no description available"),
        Field("studied_states", ["openminds.ephys.PatchedCell", "openminds.ephys.TissueSampleState"], "vocab:studiedState", multiple=True, required=True,
              doc="Reference to a point in time at which the cell was studied in a particular mode or condition."),

    ]
    existence_query_fields = ('semantically_anchored_to', 'cell_type', 'studied_states')
