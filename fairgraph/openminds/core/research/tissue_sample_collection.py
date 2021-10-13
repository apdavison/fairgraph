"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class TissueSampleCollection(KGObjectV3):
    """
    
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/TissueSampleCollection"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("anatomical_locations", ["openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalLocation", multiple=True, required=False,
              doc="no description available"),
        Field("laterality", "openminds.controlledterms.Laterality", "vocab:laterality", multiple=True, required=False,
              doc="Differentiation between a pair of lateral homologous parts of the body."),
        Field("origins", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ"], "vocab:origin", multiple=True, required=True,
              doc="Source at which something begins or rises, or from which something derives."),
        Field("studied_states", "openminds.core.TissueSampleCollectionState", "vocab:studiedState", multiple=True, required=True,
              doc="Reference to a point in time at which the tissue sample collection was studied in a particular mode or condition."),
        Field("types", "openminds.controlledterms.TissueSampleType", "vocab:type", multiple=True, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("biological_sex", "openminds.controlledterms.BiologicalSex", "vocab:biologicalSex", multiple=True, required=True,
              doc="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the tissue sample collection within a particular product."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("phenotypes", "openminds.controlledterms.Phenotype", "vocab:phenotype", multiple=True, required=False,
              doc="Physical expression of one or more genes of an organism."),
        Field("quantity", int, "vocab:quantity", multiple=False, required=False,
              doc="Total amount or number of things or beings."),
        Field("species", "openminds.controlledterms.Species", "vocab:species", multiple=True, required=True,
              doc="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective."),
        Field("strains", "openminds.controlledterms.Strain", "vocab:strain", multiple=True, required=False,
              doc="Group of presumed common ancestry with physiological but usually not morphological distinctions."),
        
    ]
    existence_query_fields = ('lookup_label',)

