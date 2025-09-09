"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import AnatomicalTargetPosition as OMAnatomicalTargetPosition
from fairgraph import EmbeddedMetadata


class AnatomicalTargetPosition(EmbeddedMetadata, OMAnatomicalTargetPosition):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/AnatomicalTargetPosition"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        additional_remarks=None,
        anatomical_targets=None,
        spatial_locations=None,
        target_identification_type=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            additional_remarks=additional_remarks,
            anatomical_targets=anatomical_targets,
            spatial_locations=spatial_locations,
            target_identification_type=target_identification_type,
        )


# cast openMINDS instances to their fairgraph subclass
AnatomicalTargetPosition.set_error_handling(None)
for key, value in OMAnatomicalTargetPosition.__dict__.items():
    if isinstance(value, OMAnatomicalTargetPosition):
        fg_instance = AnatomicalTargetPosition.from_jsonld(value.to_jsonld())
        fg_instance._space = AnatomicalTargetPosition.default_space
        setattr(AnatomicalTargetPosition, key, fg_instance)
AnatomicalTargetPosition.set_error_handling("log")
