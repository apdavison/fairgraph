"""
An International Standard Book Number of the International ISBN Agency.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ISBN
from fairgraph import KGObject


class ISBN(KGObject, ISBN):
    """
    An International Standard Book Number of the International ISBN Agency.
    """

    type_ = "https://openminds.ebrains.eu/core/ISBN"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "cited_in",
            [
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.ScholarlyArticle",
            ],
            "citedPublication",
            reverse="cited_publications",
            multiple=True,
            description="reverse of 'cited_publications'",
        ),
        Property(
            "identifies",
            [
                "openminds.latest.publications.Book",
                "openminds.latest.sands.BrainAtlas",
                "openminds.latest.sands.CommonCoordinateSpace",
            ],
            "digitalIdentifier",
            reverse="digital_identifier",
            multiple=True,
            description="reverse of 'digital_identifier'",
        ),
        Property(
            "related_to",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "relatedPublication",
            reverse="related_publications",
            multiple=True,
            description="reverse of 'related_publications'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(
        self,
        cited_in=None,
        identifier=None,
        identifies=None,
        related_to=None,
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
            cited_in=cited_in,
            identifier=identifier,
            identifies=identifies,
            related_to=related_to,
        )
