"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CustomCoordinateSpace
from fairgraph import KGObject


class CustomCoordinateSpace(KGObject, CustomCoordinateSpace):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CustomCoordinateSpace"
    default_space = "spatial"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_coordinate_space_of",
            "openminds.latest.sands.CustomAnnotation",
            "coordinateSpace",
            reverse="coordinate_space",
            multiple=True,
            description="reverse of 'coordinate_space'",
        ),
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        anatomical_axes_orientation=None,
        axes_origins=None,
        default_images=None,
        is_coordinate_space_of=None,
        is_used_to_group=None,
        native_unit=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            anatomical_axes_orientation=anatomical_axes_orientation,
            axes_origins=axes_origins,
            default_images=default_images,
            is_coordinate_space_of=is_coordinate_space_of,
            is_used_to_group=is_used_to_group,
            native_unit=native_unit,
        )
