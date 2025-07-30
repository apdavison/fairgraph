"""
Structured information on a person.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Person
from fairgraph import KGObject


class Person(KGObject, Person):
    """
    Structured information on a person.
    """

    type_ = "https://openminds.ebrains.eu/core/Person"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "activities",
            [
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "performedBy",
            reverse="performed_by",
            multiple=True,
            description="reverse of 'performed_by'",
        ),
        Property(
            "comments",
            "openminds.latest.core.Comment",
            "commenter",
            reverse="commenter",
            multiple=True,
            description="reverse of 'commenter'",
        ),
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
        Property(
            "started",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
                "openminds.latest.computation.WorkflowExecution",
            ],
            "startedBy",
            reverse="started_by",
            multiple=True,
            description="reverse of 'started_by'",
        ),
    ]
    existence_query_properties = ("given_name", "family_name")

    def __init__(
        self,
        activities=None,
        affiliations=None,
        alternate_names=None,
        associated_accounts=None,
        comments=None,
        contact_information=None,
        coordinated_projects=None,
        developed=None,
        digital_identifiers=None,
        family_name=None,
        funded=None,
        given_name=None,
        is_custodian_of=None,
        is_owner_of=None,
        is_provider_of=None,
        manufactured=None,
        published=None,
        started=None,
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
            activities=activities,
            affiliations=affiliations,
            alternate_names=alternate_names,
            associated_accounts=associated_accounts,
            comments=comments,
            contact_information=contact_information,
            coordinated_projects=coordinated_projects,
            developed=developed,
            digital_identifiers=digital_identifiers,
            family_name=family_name,
            funded=funded,
            given_name=given_name,
            is_custodian_of=is_custodian_of,
            is_owner_of=is_owner_of,
            is_provider_of=is_provider_of,
            manufactured=manufactured,
            published=published,
            started=started,
        )

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def me(cls, client, allow_multiple=False, follow_links=None):
        user_info = client.user_info()
        possible_matches = cls.list(
            client,
            scope="in progress",
            space="common",
            follow_links=follow_links,
            family_name=user_info.family_name,
            given_name=user_info.given_name,
        )
        if len(possible_matches) == 0:
            person = Person(family_name=user_info.family_name, given_name=user_info.given_name)
        elif len(possible_matches) == 1:
            person = possible_matches[0]
        elif allow_multiple:
            person = possible_matches
        else:
            raise Exception("Found multiple matches")
        return person
