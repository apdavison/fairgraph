"""
Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from fairgraph.base import IRI


class Consortium(KGObject):
    """
    Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
    """

    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Consortium"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    properties = [
        Property("name", str, "vocab:fullName", required=True, doc="Whole, non-abbreviated name of the consortium."),
        Property("alias", str, "vocab:shortName", doc="Shortened or fully abbreviated name of the consortium."),
        Property(
            "contact_information",
            "openminds.core.ContactInformation",
            "vocab:contactInformation",
            doc="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).",
        ),
        Property("homepage", IRI, "vocab:homepage", doc="Main website of the consortium."),
        Property(
            "coordinated_projects",
            "openminds.core.Project",
            "^vocab:coordinator",
            reverse="coordinators",
            multiple=True,
            doc="reverse of 'coordinator'",
        ),
        Property(
            "developed",
            [
                "openminds.computation.ValidationTest",
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipe",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.MetaDataModel",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.Model",
                "openminds.core.ModelVersion",
                "openminds.core.Software",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebService",
                "openminds.core.WebServiceVersion",
            ],
            "^vocab:developer",
            reverse="developers",
            multiple=True,
            doc="reverse of 'developer'",
        ),
        Property(
            "funded",
            "openminds.core.Funding",
            "^vocab:funder",
            reverse="funders",
            multiple=True,
            doc="reverse of 'funder'",
        ),
        Property(
            "has_members",
            "openminds.core.Affiliation",
            "^vocab:memberOf",
            reverse="member_of",
            multiple=True,
            doc="reverse of 'memberOf'",
        ),
        Property(
            "is_custodian_of",
            [
                "openminds.core.Dataset",
                "openminds.core.DatasetVersion",
                "openminds.publications.LivePaper",
                "openminds.publications.LivePaperVersion",
                "openminds.sands.BrainAtlas",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpace",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:custodian",
            reverse="custodians",
            multiple=True,
            doc="reverse of 'custodian'",
        ),
        Property(
            "is_owner_of",
            [
                "openminds.ephys.Electrode",
                "openminds.ephys.ElectrodeArray",
                "openminds.ephys.Pipette",
                "openminds.specimen_prep.SlicingDevice",
            ],
            "^vocab:owner",
            reverse="owners",
            multiple=True,
            doc="reverse of 'owner'",
        ),
        Property(
            "is_provider_of",
            "openminds.chemicals.ProductSource",
            "^vocab:provider",
            reverse="providers",
            multiple=True,
            doc="reverse of 'provider'",
        ),
        Property(
            "manufactured",
            "openminds.core.Setup",
            "^vocab:manufacturer",
            reverse="manufacturers",
            multiple=True,
            doc="reverse of 'manufacturer'",
        ),
        Property(
            "published",
            [
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.ScholarlyArticle",
            ],
            "^vocab:publisher",
            reverse="publishers",
            multiple=True,
            doc="reverse of 'publisher'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        alias=None,
        contact_information=None,
        homepage=None,
        coordinated_projects=None,
        developed=None,
        funded=None,
        has_members=None,
        is_custodian_of=None,
        is_owner_of=None,
        is_provider_of=None,
        manufactured=None,
        published=None,
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
            name=name,
            alias=alias,
            contact_information=contact_information,
            homepage=homepage,
            coordinated_projects=coordinated_projects,
            developed=developed,
            funded=funded,
            has_members=has_members,
            is_custodian_of=is_custodian_of,
            is_owner_of=is_owner_of,
            is_provider_of=is_provider_of,
            manufactured=manufactured,
            published=published,
        )
