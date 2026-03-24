import sys
from fairgraph.openminds import (
    list_kg_classes as _lkgc,
    list_embedded_metadata_classes as _lemc,
    set_error_handling as _seh,
)

from .non_atlas import CustomAnnotation, CustomAnatomicalEntity, CustomCoordinateFramework
from .miscellaneous import (
    AnatomicalTargetPosition,
    ViewerSpecification,
    QualitativeRelationAssessment,
    CoordinatePoint,
    QuantitativeRelationAssessment,
    SingleColor,
)
from .atlas import (
    AnatomicalAtlas,
    ParcellationEntity,
    AnatomicalAtlasVersion,
    ParcellationTerminologyVersion,
    CommonCoordinateFramework,
    CommonCoordinateFrameworkVersion,
    ParcellationTerminology,
    AtlasAnnotation,
    ParcellationEntityVersion,
)
from .mathematical_shape import (
    Rhombus,
    Ellipsoid,
    Frustum,
    Cube,
    Triangle,
    RightPrism,
    Square,
    Trapezoid,
    Ellipse,
    RightCone,
    Kite,
    CircularSector,
    RegularPolygon,
    RightCylinder,
    EquilateralTriangle,
    Rectangle,
    IsoscelesTriangle,
    RightTriangle,
    Spheroid,
    Circle,
    Parallelogram,
    Sphere,
    CentroidalPyramid,
)


def list_kg_classes():
    """List all KG classes defined in this module"""
    return _lkgc(sys.modules[__name__])


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return _lemc(sys.modules[__name__])


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
    """
    _seh(value, sys.modules[__name__])
