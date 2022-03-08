"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class AtlasAnnotation(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/AtlasAnnotation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("annotation_type", "openminds.controlledterms.AnnotationType", "vocab:annotationType", multiple=False, required=False,
              doc="no description available"),
        Field("best_view_point", "openminds.sands.CoordinatePoint", "vocab:bestViewPoint", multiple=False, required=False,
              doc="Coordinate point from which you get the best view of something."),
        Field("criteria", "openminds.core.ProtocolExecution", "vocab:criteria", multiple=False, required=False,
              doc="Aspects or standards on which a judgement or decision is based."),
        Field("criteria_quality_type", "openminds.controlledterms.CriteriaQualityType", "vocab:criteriaQualityType", multiple=False, required=True,
              doc="Distinct class that defines how the judgement or decision was made for a particular criteria."),
        Field("display_color", str, "vocab:displayColor", multiple=False, required=False,
              doc="Preferred coloring."),
        Field("inspired_bys", "openminds.core.File", "vocab:inspiredBy", multiple=True, required=False,
              doc="Reference to an inspiring element."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the atlas annotation within a particular product."),
        Field("laterality", "openminds.controlledterms.Laterality", "vocab:laterality", multiple=True, required=False,
              doc="Differentiation between a pair of lateral homologous parts of the body."),
        Field("visualized_in", "openminds.core.File", "vocab:visualizedIn", multiple=False, required=False,
              doc="Reference to an image in which something is visible."),

    ]
