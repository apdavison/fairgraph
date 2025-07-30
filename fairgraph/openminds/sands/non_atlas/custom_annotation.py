"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CustomAnnotation
from fairgraph import EmbeddedMetadata


class CustomAnnotation(EmbeddedMetadata, CustomAnnotation):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CustomAnnotation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        anchor_points=None,
        coordinate_space=None,
        criteria=None,
        criteria_quality_type=None,
        criteria_type=None,
        inspired_by=None,
        internal_identifier=None,
        lateralities=None,
        preferred_visualization=None,
        specification=None,
        type=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            anchor_points=anchor_points,
            coordinate_space=coordinate_space,
            criteria=criteria,
            criteria_quality_type=criteria_quality_type,
            criteria_type=criteria_type,
            inspired_by=inspired_by,
            internal_identifier=internal_identifier,
            lateralities=lateralities,
            preferred_visualization=preferred_visualization,
            specification=specification,
            type=type,
        )
