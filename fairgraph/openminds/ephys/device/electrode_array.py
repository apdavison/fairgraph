"""
Structured information on an electrode array.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import ElectrodeArray
from fairgraph import KGObject


class ElectrodeArray(KGObject, ElectrodeArray):
    """
    Structured information on an electrode array.
    """

    type_ = "https://openminds.ebrains.eu/ephys/ElectrodeArray"
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
            "openminds.latest.ephys.ElectrodeArrayUsage",
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
        electrode_identifiers=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
        is_part_of=None,
        manufacturers=None,
        number_of_electrodes=None,
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
            electrode_identifiers=electrode_identifiers,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            is_part_of=is_part_of,
            manufacturers=manufacturers,
            number_of_electrodes=number_of_electrodes,
            owners=owners,
            serial_number=serial_number,
            usage=usage,
        )
