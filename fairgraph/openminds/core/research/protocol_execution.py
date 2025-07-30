"""
Structured information on a protocol execution.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ProtocolExecution
from fairgraph import KGObject


from datetime import datetime, time


class ProtocolExecution(KGObject, ProtocolExecution):
    """
    Structured information on a protocol execution.
    """

    type_ = "https://openminds.ebrains.eu/core/ProtocolExecution"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "based_on_protocol_execution",
            ["openminds.latest.sands.AtlasAnnotation", "openminds.latest.sands.CustomAnnotation"],
            "criteria",
            reverse="criteria",
            multiple=True,
            description="reverse of 'criteria'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        based_on_protocol_execution=None,
        behavioral_protocols=None,
        custom_property_sets=None,
        description=None,
        end_time=None,
        inputs=None,
        is_part_of=None,
        outputs=None,
        performed_by=None,
        preparation_design=None,
        protocols=None,
        start_time=None,
        study_targets=None,
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
            lookup_label=lookup_label,
            based_on_protocol_execution=based_on_protocol_execution,
            behavioral_protocols=behavioral_protocols,
            custom_property_sets=custom_property_sets,
            description=description,
            end_time=end_time,
            inputs=inputs,
            is_part_of=is_part_of,
            outputs=outputs,
            performed_by=performed_by,
            preparation_design=preparation_design,
            protocols=protocols,
            start_time=start_time,
            study_targets=study_targets,
        )
