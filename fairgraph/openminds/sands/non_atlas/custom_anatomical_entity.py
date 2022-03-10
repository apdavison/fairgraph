"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class CustomAnatomicalEntity(KGObject):
    """

    """
    default_space = "spatial"
    type = ["https://openminds.ebrains.eu/sands/CustomAnatomicalEntity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the custom anatomical entity."),
        Field("has_annotations", "openminds.sands.CustomAnnotation", "vocab:hasAnnotation", multiple=True, required=False,
              doc="no description available"),
        Field("related_uberon_term", "openminds.controlledterms.UBERONParcellation", "vocab:relatedUBERONTerm", multiple=False, required=False,
              doc="no description available"),
        Field("relation_assessments", ["openminds.sands.QualitativeRelationAssessment", "openminds.sands.QuantitativeRelationAssessment"], "vocab:relationAssessment", multiple=True, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('name',)
