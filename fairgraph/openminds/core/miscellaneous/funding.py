"""
Structured information on used funding.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Funding as OMFunding
from fairgraph import KGObject


class Funding(KGObject, OMFunding):
    """
    Structured information on used funding.
    """

    type_ = "https://openminds.om-i.org/types/Funding"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "funded",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.publications.ScholarlyArticle",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "funding",
            reverse="funding",
            multiple=True,
            description="reverse of 'funding'",
        ),
    ]
    existence_query_properties = ("funder",)

    def __init__(
        self,
        acknowledgement=None,
        award_number=None,
        award_title=None,
        funded=None,
        funder=None,
        id=None,
        data=None,
        space=None,
        release_status=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            release_status=release_status,
            data=data,
            acknowledgement=acknowledgement,
            award_number=award_number,
            award_title=award_title,
            funded=funded,
            funder=funder,
        )
