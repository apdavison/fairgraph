"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.specimen_prep import SlicingDevice as OMSlicingDevice
from fairgraph import KGObject


class SlicingDevice(KGObject, OMSlicingDevice):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SlicingDevice"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_part_of",
            "openminds.latest.core.Setup",
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "usage",
            "openminds.latest.specimen_prep.SlicingDeviceUsage",
            "device",
            reverse="device",
            multiple=True,
            description="reverse of 'device'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        name=None,
        lookup_label=None,
        description=None,
        device_type=None,
        digital_identifier=None,
        is_part_of=None,
        manufacturers=None,
        owners=None,
        serial_number=None,
        usage=None,
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
            lookup_label=lookup_label,
            description=description,
            device_type=device_type,
            digital_identifier=digital_identifier,
            is_part_of=is_part_of,
            manufacturers=manufacturers,
            owners=owners,
            serial_number=serial_number,
            usage=usage,
        )


# cast openMINDS instances to their fairgraph subclass
SlicingDevice.set_error_handling(None)
for key, value in OMSlicingDevice.__dict__.items():
    if isinstance(value, OMSlicingDevice):
        fg_instance = SlicingDevice.from_jsonld(value.to_jsonld())
        fg_instance._space = SlicingDevice.default_space
        setattr(SlicingDevice, key, fg_instance)
SlicingDevice.set_error_handling("log")
