"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import RecordingActivity as OMRecordingActivity
from fairgraph import KGObject


from datetime import datetime, time


class RecordingActivity(KGObject, OMRecordingActivity):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RecordingActivity"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        custom_property_sets=None,
        description=None,
        devices=None,
        end_time=None,
        inputs=None,
        internal_identifier=None,
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
            custom_property_sets=custom_property_sets,
            description=description,
            devices=devices,
            end_time=end_time,
            inputs=inputs,
            internal_identifier=internal_identifier,
            is_part_of=is_part_of,
            outputs=outputs,
            performed_by=performed_by,
            preparation_design=preparation_design,
            protocols=protocols,
            start_time=start_time,
            study_targets=study_targets,
        )


# cast openMINDS instances to their fairgraph subclass
RecordingActivity.set_error_handling(None)
for key, value in OMRecordingActivity.__dict__.items():
    if isinstance(value, OMRecordingActivity):
        fg_instance = RecordingActivity.from_jsonld(value.to_jsonld())
        fg_instance._space = RecordingActivity.default_space
        setattr(RecordingActivity, key, fg_instance)
RecordingActivity.set_error_handling("log")
