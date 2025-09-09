"""
Structured information on an electrode.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import Electrode as OMElectrode
from fairgraph import KGObject


class Electrode(KGObject, OMElectrode):
    """
    Structured information on an electrode.
    """

    type_ = "https://openminds.om-i.org/types/Electrode"
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
            "openminds.latest.ephys.ElectrodeUsage",
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
        conductor_material=None,
        description=None,
        device_type=None,
        digital_identifier=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
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
            conductor_material=conductor_material,
            description=description,
            device_type=device_type,
            digital_identifier=digital_identifier,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            is_part_of=is_part_of,
            manufacturers=manufacturers,
            owners=owners,
            serial_number=serial_number,
            usage=usage,
        )


# cast openMINDS instances to their fairgraph subclass
Electrode.set_error_handling(None)
for key, value in OMElectrode.__dict__.items():
    if isinstance(value, OMElectrode):
        fg_instance = Electrode.from_jsonld(value.to_jsonld())
        fg_instance._space = Electrode.default_space
        setattr(Electrode, key, fg_instance)
Electrode.set_error_handling("log")
