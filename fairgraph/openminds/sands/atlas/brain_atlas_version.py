"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import BrainAtlasVersion
from fairgraph import KGObject


from datetime import date
from openminds import IRI


class BrainAtlasVersion(KGObject, BrainAtlasVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlasVersion"
    default_space = "atlas"
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
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.ProtocolExecution",
            ],
            ["input", "inputData"],
            reverse=["input_data", "inputs"],
            multiple=True,
            description="reverse of input_data, inputs",
        ),
        Property(
            "is_old_version_of",
            "openminds.latest.sands.BrainAtlasVersion",
            "isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            description="reverse of 'is_new_version_of'",
        ),
        Property(
            "is_part_of",
            [
                "openminds.latest.core.Project",
                "openminds.latest.core.ResearchProductGroup",
                "openminds.latest.core.SoftwareVersion",
            ],
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "is_version_of",
            "openminds.latest.sands.BrainAtlas",
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
        abbreviation=None,
        accessibility=None,
        authors=None,
        comments=None,
        coordinate_space=None,
        copyright=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_terminology=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_input_to=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        license=None,
        major_version_identifier=None,
        ontology_identifier=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        type=None,
        used_specimens=None,
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
            abbreviation=abbreviation,
            accessibility=accessibility,
            authors=authors,
            comments=comments,
            coordinate_space=coordinate_space,
            copyright=copyright,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_terminology=has_terminology,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_input_to=is_input_to,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            license=license,
            major_version_identifier=major_version_identifier,
            ontology_identifier=ontology_identifier,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            type=type,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
