"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ViewerSpecification
from fairgraph import EmbeddedMetadata


class ViewerSpecification(EmbeddedMetadata, ViewerSpecification):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ViewerSpecification"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        additional_remarks=None,
        anchor_points=None,
        camera_position=None,
        preferred_display_color=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            additional_remarks=additional_remarks,
            anchor_points=anchor_points,
            camera_position=camera_position,
            preferred_display_color=preferred_display_color,
        )
