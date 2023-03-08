"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class CustomAnnotation(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/CustomAnnotation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("anchor_point", "openminds.sands.CoordinatePoint", "vocab:anchorPoint", multiple=False, required=False,
              doc="no description available"),
        Field("coordinate_space", ["openminds.sands.CommonCoordinateSpaceVersion", "openminds.sands.CustomCoordinateSpace"], "vocab:coordinateSpace", multiple=False, required=True,
              doc="Two or three dimensional geometric setting."),
        Field("criteria", "openminds.core.ProtocolExecution", "vocab:criteria", multiple=False, required=False,
              doc="Aspects or standards on which a judgement or decision is based."),
        Field("criteria_quality_type", "openminds.controlledterms.CriteriaQualityType", "vocab:criteriaQualityType", multiple=False, required=True,
              doc="Distinct class that defines how the judgement or decision was made for a particular criteria."),
        Field("criteria_type", "openminds.controlledterms.AnnotationCriteriaType", "vocab:criteriaType", multiple=False, required=True,
              doc="no description available"),
        Field("inspired_bys", "openminds.core.File", "vocab:inspiredBy", multiple=True, required=False,
              doc="Reference to an inspiring element."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the custom annotation within a particular product."),
        Field("laterality", "openminds.controlledterms.Laterality", "vocab:laterality", multiple=True, required=False,
              doc="Differentiation between a pair of lateral homologous parts of the body."),
        Field("preferred_visualization", "openminds.sands.ViewerSpecification", "vocab:preferredVisualization", multiple=False, required=False,
              doc="no description available"),
        Field("specification", ["openminds.core.File", "openminds.core.PropertyValueList"], "vocab:specification", multiple=False, required=False,
              doc="Detailed and precise presentation of, or proposal for something."),
        Field("type", "openminds.controlledterms.AnnotationType", "vocab:type", multiple=False, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]
