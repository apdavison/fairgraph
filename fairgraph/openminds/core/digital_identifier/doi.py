"""
Structured information about a digital object identifier, as standardized by the International Organization for Standardization.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import DOI as OMDOI
from fairgraph import KGObject


class DOI(KGObject, OMDOI):
    """
    Structured information about a digital object identifier, as standardized by the International Organization for Standardization.
    """

    type_ = "https://openminds.om-i.org/types/DOI"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            ["openminds.latest.core.BehavioralProtocol", "openminds.latest.core.Protocol"],
            "describedIn",
            reverse="described_in",
            multiple=True,
            description="reverse of 'described_in'",
        ),
        Property(
            "identifies",
            [
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.WorkflowRecipe",
                "openminds.latest.core.Dataset",
                "openminds.latest.core.MetaDataModel",
                "openminds.latest.core.Model",
                "openminds.latest.core.Software",
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.LivePaper",
                "openminds.latest.publications.ScholarlyArticle",
                "openminds.latest.sands.BrainAtlas",
                "openminds.latest.sands.CommonCoordinateSpace",
                "openminds.latest.specimen_prep.SlicingDevice",
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
        describes=None,
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
            describes=describes,
            identifier=identifier,
            identifies=identifies,
            related_to=related_to,
        )


# cast openMINDS instances to their fairgraph subclass
DOI.set_error_handling(None)
for key, value in OMDOI.__dict__.items():
    if isinstance(value, OMDOI):
        fg_instance = DOI.from_jsonld(value.to_jsonld())
        fg_instance._space = DOI.default_space
        setattr(DOI, key, fg_instance)
DOI.set_error_handling("log")
