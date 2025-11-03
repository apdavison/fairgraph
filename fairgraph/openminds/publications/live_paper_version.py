"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import LivePaperVersion as OMLivePaperVersion
from fairgraph import KGObject

from fairgraph.errors import ResolutionFailure
from .live_paper import LivePaper
from datetime import date
from datetime import datetime
from openminds import IRI


class LivePaperVersion(KGObject, OMLivePaperVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/LivePaperVersion"
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
            "has_parts",
            "openminds.latest.publications.LivePaperSection",
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
        Property(
            "is_old_version_of",
            "openminds.latest.publications.LivePaperVersion",
            "isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            description="reverse of 'is_new_version_of'",
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
            "is_version_of",
            "openminds.latest.publications.LivePaper",
            "hasVersion",
            reverse="has_versions",
            multiple=True,
            description="reverse of 'has_versions'",
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
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("short_name", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        about=None,
        accessibility=None,
        authors=None,
        comments=None,
        copyright=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_parts=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        license=None,
        modification_date=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        version_identifier=None,
        version_innovation=None,
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
            about=about,
            accessibility=accessibility,
            authors=authors,
            comments=comments,
            copyright=copyright,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_parts=has_parts,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            license=license,
            modification_date=modification_date,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )

    def is_version_of(self, client):
        parents = LivePaper.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
