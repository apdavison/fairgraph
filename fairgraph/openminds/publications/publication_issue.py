"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class PublicationIssue(KGObject):
    """
    <description not available>
    """

    default_space = "livepapers"
    type_ = "https://openminds.ebrains.eu/publications/PublicationIssue"
    properties = [
        Property(
            "is_part_of",
            "openminds.publications.PublicationVolume",
            "vocab:isPartOf",
            required=True,
            doc="Reference to the ensemble of multiple things or beings.",
        ),
        Property("issue_number", str, "vocab:issueNumber", required=True, doc="no description available"),
    ]
    reverse_properties = [
        Property(
            "has_parts",
            "openminds.publications.ScholarlyArticle",
            "^vocab:isPartOf",
            reverse="is_part_of",
            multiple=True,
            doc="reverse of 'is_part_of'",
        ),
    ]
    existence_query_properties = ("is_part_of", "issue_number")

    def __init__(self, has_parts=None, is_part_of=None, issue_number=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            has_parts=has_parts,
            is_part_of=is_part_of,
            issue_number=issue_number,
        )
