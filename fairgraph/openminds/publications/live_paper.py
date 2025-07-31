"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import LivePaper
from fairgraph import KGObject


from openminds import IRI


class LivePaper(KGObject, LivePaper):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/LivePaper"
    default_space = "livepapers"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "comments",
            "openminds.latest.core.Comment",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
        Property(
            "is_part_of",
            ["openminds.latest.core.Project", "openminds.latest.core.ResearchProductGroup"],
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "learning_resources",
            "openminds.latest.publications.LearningResource",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
    ]
    aliases = {"name": "full_name", "versions": "has_versions", "alias": "short_name"}
    existence_query_properties = ("full_name", "short_name")

    def __init__(
        self,
        name=None,
        alias=None,
        authors=None,
        comments=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_name=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        is_part_of=None,
        learning_resources=None,
        short_name=None,
        versions=None,
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
            alias=alias,
            authors=authors,
            comments=comments,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_part_of=is_part_of,
            learning_resources=learning_resources,
            short_name=short_name,
            versions=versions,
        )
