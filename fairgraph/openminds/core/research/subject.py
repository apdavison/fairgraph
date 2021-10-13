"""
Structured information on a subject.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class Subject(KGObjectV3):
    """
    Structured information on a subject.
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Subject"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("is_part_of", "openminds.core.SubjectGroup", "vocab:isPartOf", multiple=True, required=False,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("studied_states", "openminds.core.SubjectState", "vocab:studiedState", multiple=True, required=True,
              doc="Reference to a point in time at which the subject was studied in a particular mode or condition."),
        Field("biological_sex", "openminds.controlledterms.BiologicalSex", "vocab:biologicalSex", multiple=False, required=True,
              doc="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the subject within a particular product."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("phenotype", "openminds.controlledterms.Phenotype", "vocab:phenotype", multiple=False, required=False,
              doc="Physical expression of one or more genes of an organism."),
        Field("species", "openminds.controlledterms.Species", "vocab:species", multiple=False, required=True,
              doc="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective."),
        Field("strain", "openminds.controlledterms.Strain", "vocab:strain", multiple=False, required=False,
              doc="Group of presumed common ancestry with physiological but usually not morphological distinctions."),
        
    ]
    existence_query_fields = ('lookup_label',)

