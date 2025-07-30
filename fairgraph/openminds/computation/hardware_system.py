"""
Structured information about computing hardware.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import HardwareSystem
from fairgraph import KGObject


class HardwareSystem(KGObject, HardwareSystem):
    """
    Structured information about computing hardware.
    """

    type_ = "https://openminds.ebrains.eu/computation/HardwareSystem"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "used_by",
            "openminds.latest.computation.Environment",
            "hardware",
            reverse="hardware",
            multiple=True,
            description="reverse of 'hardware'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        description=None,
        used_by=None,
        version_identifier=None,
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
            description=description,
            used_by=used_by,
            version_identifier=version_identifier,
        )
