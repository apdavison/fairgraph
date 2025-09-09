"""
Structured information on a computational model (version level).
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ModelVersion as OMModelVersion
from fairgraph import KGObject

from fairgraph.errors import ResolutionFailure
from .model import Model
from datetime import date
from openminds import IRI


class ModelVersion(KGObject, OMModelVersion):
    """
    Structured information on a computational model (version level).
    """

    type_ = "https://openminds.om-i.org/types/ModelVersion"
    default_space = "model"
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
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Simulation",
            ],
            "input",
            reverse="inputs",
            multiple=True,
            description="reverse of 'inputs'",
        ),
        Property(
            "is_location_of",
            "openminds.latest.core.ServiceLink",
            "dataLocation",
            reverse="data_location",
            multiple=True,
            description="reverse of 'data_location'",
        ),
        Property(
            "is_old_version_of",
            "openminds.latest.core.ModelVersion",
            "isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            description="reverse of 'is_new_version_of'",
        ),
        Property(
            "is_output_of",
            "openminds.latest.computation.Optimization",
            "output",
            reverse="outputs",
            multiple=True,
            description="reverse of 'outputs'",
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
            "openminds.latest.core.Model",
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
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("full_name", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        accessibility=None,
        comments=None,
        configuration=None,
        copyright=None,
        custodians=None,
        description=None,
        developers=None,
        digital_identifier=None,
        entry_point=None,
        formats=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        input_data=None,
        is_alternative_version_of=None,
        is_input_to=None,
        is_location_of=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_output_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        licenses=None,
        other_contributions=None,
        output_data=None,
        publication=None,
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
            accessibility=accessibility,
            comments=comments,
            configuration=configuration,
            copyright=copyright,
            custodians=custodians,
            description=description,
            developers=developers,
            digital_identifier=digital_identifier,
            entry_point=entry_point,
            formats=formats,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            input_data=input_data,
            is_alternative_version_of=is_alternative_version_of,
            is_input_to=is_input_to,
            is_location_of=is_location_of,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_output_of=is_output_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            licenses=licenses,
            other_contributions=other_contributions,
            output_data=output_data,
            publication=publication,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )

    def is_version_of(self, client):
        parents = Model.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]


# cast openMINDS instances to their fairgraph subclass
ModelVersion.set_error_handling(None)
for key, value in OMModelVersion.__dict__.items():
    if isinstance(value, OMModelVersion):
        fg_instance = ModelVersion.from_jsonld(value.to_jsonld())
        fg_instance._space = ModelVersion.default_space
        setattr(ModelVersion, key, fg_instance)
ModelVersion.set_error_handling("log")
