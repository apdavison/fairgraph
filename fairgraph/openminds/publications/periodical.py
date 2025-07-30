"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import Periodical
from fairgraph import KGObject


class Periodical(KGObject, Periodical):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/Periodical"
    default_space = "livepapers"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_parts",
            "openminds.latest.publications.PublicationVolume",
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
    ]
    existence_query_properties = ("abbreviation",)

    def __init__(
        self,
        name=None,
        abbreviation=None,
        digital_identifier=None,
        has_parts=None,
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
            abbreviation=abbreviation,
            digital_identifier=digital_identifier,
            has_parts=has_parts,
        )
