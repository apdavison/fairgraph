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
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("anatomical_locations", ["openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalLocation", multiple=True, required=False,
              doc="no description available"),
        Field("biological_sex", "openminds.controlledterms.BiologicalSex", "vocab:biologicalSex", multiple=False, required=False,
              doc="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce."),
        Field("cell_type", "openminds.controlledterms.CellType", "vocab:cellType", multiple=False, required=True,
              doc="no description available"),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the cell within a particular product."),
        Field("is_part_of", "openminds.core.TissueSampleCollection", "vocab:isPartOf", multiple=True, required=False,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("laterality", "openminds.controlledterms.Laterality", "vocab:laterality", multiple=True, required=False,
              doc="Differentiation between a pair of lateral homologous parts of the body."),
        Field("origin", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ"], "vocab:origin", multiple=False, required=True,
              doc="Source at which something begins or rises, or from which something derives."),
        Field("semantically_anchored_to", "openminds.controlledterms.UBERONParcellation", "vocab:semanticallyAnchoredTo", multiple=False, required=True,
              doc="Reference to a related anatomical structure without providing a quantitative proof of the claimed relation."),
        Field("species", ["openminds.controlledterms.Species", "openminds.core.Strain"], "vocab:species", multiple=False, required=True,
              doc="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective."),
        Field("studied_states", ["openminds.ephys.PatchedCell", "openminds.ephys.TissueSampleState"], "vocab:studiedState", multiple=True, required=True,
              doc="Reference to a point in time at which the cell was studied in a particular mode or condition."),
        Field("type", "openminds.controlledterms.TissueSampleType", "vocab:type", multiple=False, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]
    existence_query_fields = ('lookup_label',)
