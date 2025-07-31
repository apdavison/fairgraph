"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import Recording
from fairgraph import KGObject


class Recording(KGObject, Recording):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Recording"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "next_recording",
            "openminds.latest.ephys.Recording",
            "previousRecording",
            reverse="previous_recording",
            multiple=True,
            description="reverse of 'previous_recording'",
        ),
    ]
    existence_query_properties = ("channels", "data_location", "recorded_with", "sampling_frequency")

    def __init__(
        self,
        name=None,
        additional_remarks=None,
        channels=None,
        data_location=None,
        internal_identifier=None,
        next_recording=None,
        previous_recording=None,
        recorded_with=None,
        sampling_frequency=None,
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
            additional_remarks=additional_remarks,
            channels=channels,
            data_location=data_location,
            internal_identifier=internal_identifier,
            next_recording=next_recording,
            previous_recording=previous_recording,
            recorded_with=recorded_with,
            sampling_frequency=sampling_frequency,
        )
