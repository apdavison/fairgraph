"""
Structured information on an image annotation.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class Annotation(KGObject):
    """
    Structured information on an image annotation.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/Annotation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("best_view_point", "openminds.sands.CoordinatePoint", "vocab:bestViewPoint", multiple=False, required=False,
              doc="Coordinate point from which you get the best view of something."),
        Field("criteria", "openminds.core.ProtocolExecution", "vocab:criteria", multiple=False, required=False,
              doc="Aspects or standards on which a judgement or decision is based."),
        Field("criteria_quality_type", "openminds.controlledTerms.CriteriaQualityType", "vocab:criteriaQualityType", multiple=False, required=True,
              doc="Distinct class that defines how the judgement or decision was made for a particular criteria."),
        Field("display_colors", int, "vocab:displayColor", multiple=True, required=False,
              doc="Preferred coloring."),
        Field("inspired_bys", "openminds.sands.Image", "vocab:inspiredBy", multiple=True, required=False,
              doc="Reference to an inspiring element."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the annotation within a particular product."),
        Field("lateralitys", "openminds.controlledTerms.Laterality", "vocab:laterality", multiple=True, required=True,
              doc="Differentiation between a pair of lateral homologous parts of the body."),
        Field("naming_terms", "openminds.sands.AnatomicalEntity", "vocab:namingTerm", multiple=True, required=True,
              doc="Word or expression that has a precise meaning within a science, art, profession, or subject."),
        Field("related_parcellation_terms", "openminds.sands.AnatomicalEntity", "vocab:relatedParcellationTerm", multiple=True, required=False,
              doc="no description available"),
        Field("visualized_in", "openminds.sands.Image", "vocab:visualizedIn", multiple=False, required=False,
              doc="Reference to an image in which something is visible."),
        
    ]
    existence_query_fields = ('name',)