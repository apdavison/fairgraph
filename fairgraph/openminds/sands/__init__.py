import sys
import inspect
from fairgraph.kgobject import KGObject
from fairgraph.embedded import EmbeddedMetadata

from .mathematicalShapes.ellipse import Ellipse
from .mathematicalShapes.rectangle import Rectangle
from .mathematicalShapes.circle import Circle
from .non_atlas.custom_coordinate_space import CustomCoordinateSpace
from .non_atlas.custom_annotation import CustomAnnotation
from .non_atlas.custom_anatomical_entity import CustomAnatomicalEntity
from .miscellaneous.anatomical_target_position import AnatomicalTargetPosition
from .miscellaneous.viewer_specification import ViewerSpecification
from .miscellaneous.qualitative_relation_assessment import QualitativeRelationAssessment
from .miscellaneous.quantitative_relation_assessment import QuantitativeRelationAssessment
from .miscellaneous.coordinate_point import CoordinatePoint
from .miscellaneous.single_color import SingleColor
from .atlas.parcellation_entity import ParcellationEntity
from .atlas.common_coordinate_space import CommonCoordinateSpace
from .atlas.parcellation_terminology import ParcellationTerminology
from .atlas.common_coordinate_space_version import CommonCoordinateSpaceVersion
from .atlas.parcellation_terminology_version import ParcellationTerminologyVersion
from .atlas.brain_atlas import BrainAtlas
from .atlas.atlas_annotation import AtlasAnnotation
from .atlas.brain_atlas_version import BrainAtlasVersion
from .atlas.parcellation_entity_version import ParcellationEntityVersion


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)
    ]


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, EmbeddedMetadata) and obj.__module__.startswith(__name__)
    ]


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required field is not provided).
            Possible values: "error", "warning", "log", None
    """
    for cls in list_kg_classes() + list_embedded_metadata_classes():
        cls.set_error_handling(value)
