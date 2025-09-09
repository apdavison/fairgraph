"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CommonCoordinateSpaceVersion as OMCommonCoordinateSpaceVersion
from fairgraph import KGObject


from datetime import date
from openminds import IRI


class CommonCoordinateSpaceVersion(KGObject, OMCommonCoordinateSpaceVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommonCoordinateSpaceVersion"
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
            "is_coordinate_space_of",
            ["openminds.latest.sands.BrainAtlasVersion", "openminds.latest.sands.CustomAnnotation"],
            "coordinateSpace",
            reverse="coordinate_space",
            multiple=True,
            description="reverse of 'coordinate_space'",
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
            "openminds.latest.sands.CommonCoordinateSpaceVersion",
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
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "is_version_of",
            "openminds.latest.sands.CommonCoordinateSpace",
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
    existence_query_properties = (
        "accessibility",
        "anatomical_axes_orientation",
        "axes_origins",
        "full_documentation",
        "native_unit",
        "release_date",
        "short_name",
        "version_identifier",
        "version_innovation",
    )

    def __init__(
        self,
        name=None,
        alias=None,
        abbreviation=None,
        accessibility=None,
        anatomical_axes_orientation=None,
        authors=None,
        axes_origins=None,
        comments=None,
        copyright=None,
        custodians=None,
        default_images=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_coordinate_space_of=None,
        is_input_to=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_used_to_group=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        license=None,
        native_unit=None,
        ontology_identifiers=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
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
            anatomical_axes_orientation=anatomical_axes_orientation,
            authors=authors,
            axes_origins=axes_origins,
            comments=comments,
            copyright=copyright,
            custodians=custodians,
            default_images=default_images,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_coordinate_space_of=is_coordinate_space_of,
            is_input_to=is_input_to,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_used_to_group=is_used_to_group,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            license=license,
            native_unit=native_unit,
            ontology_identifiers=ontology_identifiers,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )


# cast openMINDS instances to their fairgraph subclass
CommonCoordinateSpaceVersion.set_error_handling(None)
for key, value in OMCommonCoordinateSpaceVersion.__dict__.items():
    if isinstance(value, OMCommonCoordinateSpaceVersion):
        fg_instance = CommonCoordinateSpaceVersion.from_jsonld(value.to_jsonld())
        fg_instance._space = CommonCoordinateSpaceVersion.default_space
        setattr(CommonCoordinateSpaceVersion, key, fg_instance)
CommonCoordinateSpaceVersion.set_error_handling("log")
