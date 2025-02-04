"""
An International Standard Book Number of the International ISBN Agency.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ISBN(KGObject):
    """
    An International Standard Book Number of the International ISBN Agency.
    """

    default_space = "dataset"
    type_ = "https://openminds.ebrains.eu/core/ISBN"
    properties = [
        Property("identifier", str, "vocab:identifier", required=True, doc="Term or code used to identify the ISBN."),
    ]
    reverse_properties = [
        Property(
            "cited_in",
            [
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.ScholarlyArticle",
            ],
            "^vocab:citedPublication",
            reverse="cited_publications",
            multiple=True,
            doc="reverse of 'cited_publications'",
        ),
        Property(
            "identifies",
            ["openminds.publications.Book", "openminds.sands.BrainAtlas", "openminds.sands.CommonCoordinateSpace"],
            "^vocab:digitalIdentifier",
            reverse="digital_identifier",
            multiple=True,
            doc="reverse of 'digital_identifier'",
        ),
        Property(
            "related_to",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.ModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.LivePaperVersion",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:relatedPublication",
            reverse="related_publications",
            multiple=True,
            doc="reverse of 'related_publications'",
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
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            cited_in=cited_in,
            identifier=identifier,
            identifies=identifies,
            related_to=related_to,
        )
