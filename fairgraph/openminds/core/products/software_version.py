"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import SoftwareVersion
from fairgraph import KGObject

from fairgraph.errors import ResolutionFailure
from .software import Software
from datetime import date
from openminds import IRI


class SoftwareVersion(KGObject, SoftwareVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SoftwareVersion"
    default_space = "software"
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
            "is_input_to",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "input",
            reverse="inputs",
            multiple=True,
            description="reverse of 'inputs'",
        ),
        Property(
            "is_old_version_of",
            "openminds.latest.core.SoftwareVersion",
            "isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            description="reverse of 'is_new_version_of'",
        ),
        Property(
            "is_part_of",
            [
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.Project",
                "openminds.latest.core.ResearchProductGroup",
                "openminds.latest.core.Setup",
                "openminds.latest.core.WebServiceVersion",
            ],
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "is_version_of",
            "openminds.latest.core.Software",
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
        Property(
            "publication",
            "openminds.latest.publications.LivePaperVersion",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
        Property(
            "used_in",
            ["openminds.latest.computation.Environment", "openminds.latest.computation.SoftwareAgent"],
            "software",
            reverse="software",
            multiple=True,
            description="reverse of 'software'",
        ),
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("short_name", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        accessibility=None,
        application_categories=None,
        comments=None,
        copyright=None,
        custodians=None,
        description=None,
        developers=None,
        devices=None,
        digital_identifier=None,
        features=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_parts=None,
        homepage=None,
        how_to_cite=None,
        input_formats=None,
        is_alternative_version_of=None,
        is_input_to=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        languages=None,
        learning_resources=None,
        licenses=None,
        operating_systems=None,
        other_contributions=None,
        output_formats=None,
        programming_languages=None,
        publication=None,
        related_publications=None,
        release_date=None,
        repository=None,
        requirements=None,
        short_name=None,
        support_channels=None,
        used_in=None,
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
            accessibility=accessibility,
            application_categories=application_categories,
            comments=comments,
            copyright=copyright,
            custodians=custodians,
            description=description,
            developers=developers,
            devices=devices,
            digital_identifier=digital_identifier,
            features=features,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_parts=has_parts,
            homepage=homepage,
            how_to_cite=how_to_cite,
            input_formats=input_formats,
            is_alternative_version_of=is_alternative_version_of,
            is_input_to=is_input_to,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            languages=languages,
            learning_resources=learning_resources,
            licenses=licenses,
            operating_systems=operating_systems,
            other_contributions=other_contributions,
            output_formats=output_formats,
            programming_languages=programming_languages,
            publication=publication,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            requirements=requirements,
            short_name=short_name,
            support_channels=support_channels,
            used_in=used_in,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )

    def is_version_of(self, client):
        parents = Software.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
