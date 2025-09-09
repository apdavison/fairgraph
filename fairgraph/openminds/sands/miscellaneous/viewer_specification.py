"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ViewerSpecification as OMViewerSpecification
from fairgraph import EmbeddedMetadata


class ViewerSpecification(EmbeddedMetadata, OMViewerSpecification):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ViewerSpecification"
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


# cast openMINDS instances to their fairgraph subclass
ViewerSpecification.set_error_handling(None)
for key, value in OMViewerSpecification.__dict__.items():
    if isinstance(value, OMViewerSpecification):
        fg_instance = ViewerSpecification.from_jsonld(value.to_jsonld())
        fg_instance._space = ViewerSpecification.default_space
        setattr(ViewerSpecification, key, fg_instance)
ViewerSpecification.set_error_handling("log")
