"""
Structured information on a used license.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import License
from fairgraph import KGObject


from openminds import IRI


class License(KGObject, License):
    """
    Structured information on a used license.
    """

    type_ = "https://openminds.ebrains.eu/core/License"
    default_space = "controlled"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_applied_to",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.publications.ScholarlyArticle",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "license",
            reverse="license",
            multiple=True,
            description="reverse of 'license'",
        ),
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("alias",)

    def __init__(
        self,
        name=None,
        alias=None,
        full_name=None,
        is_applied_to=None,
        legal_code=None,
        short_name=None,
        webpages=None,
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
            full_name=full_name,
            is_applied_to=is_applied_to,
            legal_code=legal_code,
            short_name=short_name,
            webpages=webpages,
        )
