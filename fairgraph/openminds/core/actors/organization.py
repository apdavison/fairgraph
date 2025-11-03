"""
An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Organization as OMOrganization
from fairgraph import KGObject


from openminds import IRI


class Organization(KGObject, OMOrganization):
    """
    An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)
    """

    type_ = "https://openminds.om-i.org/types/Organization"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "coordinated_projects",
            "openminds.latest.core.Project",
            "coordinator",
            reverse="coordinators",
            multiple=True,
            description="reverse of 'coordinators'",
        ),
        Property(
            "developed",
            [
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipe",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.MetaDataModel",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.Software",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebService",
                "openminds.latest.core.WebServiceVersion",
            ],
            "developer",
            reverse="developers",
            multiple=True,
            description="reverse of 'developers'",
        ),
        Property(
            "funded",
            "openminds.latest.core.Funding",
            "funder",
            reverse="funder",
            multiple=True,
            description="reverse of 'funder'",
        ),
        Property(
            "has_children",
            "openminds.latest.core.Organization",
            "hasParent",
            reverse="has_parents",
            multiple=True,
            description="reverse of 'has_parents'",
        ),
        Property(
            "has_members",
            "openminds.latest.core.Affiliation",
            "memberOf",
            reverse="member_of",
            multiple=True,
            description="reverse of 'member_of'",
        ),
        Property(
            "hosts",
            ["openminds.latest.core.FileRepository", "openminds.latest.publications.LivePaperResourceItem"],
            "hostedBy",
            reverse="hosted_by",
            multiple=True,
            description="reverse of 'hosted_by'",
        ),
        Property(
            "is_custodian_of",
            [
                "openminds.latest.core.Dataset",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.publications.LivePaper",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlas",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpace",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "custodian",
            reverse="custodians",
            multiple=True,
            description="reverse of 'custodians'",
        ),
        Property(
            "is_owner_of",
            [
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
                "openminds.latest.specimen_prep.SlicingDevice",
            ],
            "owner",
            reverse="owners",
            multiple=True,
            description="reverse of 'owners'",
        ),
        Property(
            "is_provider_of",
            "openminds.latest.chemicals.ProductSource",
            "provider",
            reverse="provider",
            multiple=True,
            description="reverse of 'provider'",
        ),
        Property(
            "manufactured",
            "openminds.latest.core.Setup",
            "manufacturer",
            reverse="manufacturers",
            multiple=True,
            description="reverse of 'manufacturers'",
        ),
        Property(
            "published",
            [
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.ScholarlyArticle",
            ],
            "publisher",
            reverse="publisher",
            multiple=True,
            description="reverse of 'publisher'",
        ),
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("full_name",)

    def __init__(
        self,
        name=None,
        alias=None,
        affiliations=None,
        coordinated_projects=None,
        developed=None,
        digital_identifiers=None,
        full_name=None,
        funded=None,
        has_children=None,
        has_members=None,
        has_parents=None,
        homepage=None,
        hosts=None,
        is_custodian_of=None,
        is_owner_of=None,
        is_provider_of=None,
        manufactured=None,
        published=None,
        short_name=None,
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
            affiliations=affiliations,
            coordinated_projects=coordinated_projects,
            developed=developed,
            digital_identifiers=digital_identifiers,
            full_name=full_name,
            funded=funded,
            has_children=has_children,
            has_members=has_members,
            has_parents=has_parents,
            homepage=homepage,
            hosts=hosts,
            is_custodian_of=is_custodian_of,
            is_owner_of=is_owner_of,
            is_provider_of=is_provider_of,
            manufactured=manufactured,
            published=published,
            short_name=short_name,
        )
