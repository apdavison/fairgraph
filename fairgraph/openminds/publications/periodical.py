"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class Periodical(KGObject):
    """
    <description not available>
    """

    default_space = "livepapers"
    type_ = "https://openminds.ebrains.eu/publications/Periodical"
    properties = [
        Property("abbreviation", str, "vocab:abbreviation", doc="no description available"),
        Property(
            "digital_identifier",
            "openminds.core.ISSN",
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the periodical.",
        ),
    ]
    reverse_properties = [
        Property(
            "has_parts",
            "openminds.publications.PublicationVolume",
            "^vocab:isPartOf",
            reverse="is_part_of",
            multiple=True,
            doc="reverse of 'is_part_of'",
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
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            abbreviation=abbreviation,
            digital_identifier=digital_identifier,
            has_parts=has_parts,
        )
