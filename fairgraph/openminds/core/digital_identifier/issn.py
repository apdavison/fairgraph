"""
An International Standard Serial Number of the ISSN International Centre.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ISSN
from fairgraph import KGObject


class ISSN(KGObject, ISSN):
    """
    An International Standard Serial Number of the ISSN International Centre.
    """

    type_ = "https://openminds.ebrains.eu/core/ISSN"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            "openminds.latest.publications.Periodical",
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

    def __init__(self, identifier=None, identifies=None, related_to=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            identifier=identifier,
            identifies=identifies,
            related_to=related_to,
        )
