"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import PublicationVolume
from fairgraph import KGObject


class PublicationVolume(KGObject, PublicationVolume):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/PublicationVolume"
    default_space = "livepapers"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_parts",
            ["openminds.latest.publications.PublicationIssue", "openminds.latest.publications.ScholarlyArticle"],
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
    ]
    existence_query_properties = ("is_part_of", "volume_number")

    def __init__(
        self, has_parts=None, is_part_of=None, volume_number=None, id=None, data=None, space=None, scope=None
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            has_parts=has_parts,
            is_part_of=is_part_of,
            volume_number=volume_number,
        )
