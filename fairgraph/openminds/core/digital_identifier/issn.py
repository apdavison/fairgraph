"""
An International Standard Serial Number of the ISSN International Centre.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ISSN(KGObject):
    """
    An International Standard Serial Number of the ISSN International Centre.
    """

    default_space = "dataset"
    type_ = "https://openminds.ebrains.eu/core/ISSN"
    properties = [
        Property("identifier", str, "vocab:identifier", required=True, doc="Term or code used to identify the ISSN."),
    ]
    reverse_properties = [
        Property(
            "identifies",
            "openminds.publications.Periodical",
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

    def __init__(self, identifier=None, identifies=None, related_to=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            identifier=identifier,
            identifies=identifies,
            related_to=related_to,
        )
