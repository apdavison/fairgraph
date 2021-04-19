"""
Structured information on the relation between one anatomical entity and another.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class AnatomicalEntityRelation(KGObject):
    """
    Structured information on the relation between one anatomical entity and another.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/AnatomicalEntityRelation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("criteria", "openminds.core.ProtocolExecution", "vocab:criteria", multiple=False, required=False,
              doc="Aspects or standards on which a judgement or decision is based."),
        Field("criteria_quality_type", "openminds.controlledTerms.CriteriaQualityType", "vocab:criteriaQualityType", multiple=False, required=True,
              doc="Distinct class that defines how the judgement or decision was made for a particular criteria."),
        Field("in_relation_to", "openminds.sands.AnatomicalEntity", "vocab:inRelationTo", multiple=False, required=True,
              doc="Reference to a related element."),
        Field("qualitative_overlap", "openminds.controlledTerms.QualitativeOverlap", "vocab:qualitativeOverlap", multiple=False, required=True,
              doc="Semantic characterization of how much two things occupy the same space."),
        Field("quantitative_overlap", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:quantitativeOverlap", multiple=False, required=False,
              doc="Numerical characterization of how much two things occupy the same space."),
        
    ]
    existence_query_fields = ('name',)