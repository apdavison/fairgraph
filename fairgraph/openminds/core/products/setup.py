"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Setup
from fairgraph import KGObject


class Setup(KGObject, Setup):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/Setup"
    default_space = "dataset"
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
            "used_in",
            "openminds.latest.stimulation.StimulationActivity",
            "setup",
            reverse="setup",
            multiple=True,
            description="reverse of 'setup'",
        ),
    ]
    existence_query_properties = ("description", "has_parts", "name")

    def __init__(
        self,
        name=None,
        description=None,
        has_parts=None,
        is_part_of=None,
        location=None,
        manufacturers=None,
        types=None,
        used_in=None,
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
            has_parts=has_parts,
            is_part_of=is_part_of,
            location=location,
            manufacturers=manufacturers,
            types=types,
            used_in=used_in,
        )
