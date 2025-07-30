"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import AnatomicalTargetPosition
from fairgraph import EmbeddedMetadata


class AnatomicalTargetPosition(EmbeddedMetadata, AnatomicalTargetPosition):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/AnatomicalTargetPosition"
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
