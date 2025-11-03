"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import DiseaseModel as OMDiseaseModel
from fairgraph import KGObject


from openminds import IRI


class DiseaseModel(KGObject, OMDiseaseModel):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/DiseaseModel"
    default_space = "controlled"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
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
            "keyword",
            reverse="keywords",
            multiple=True,
            description="reverse of 'keywords'",
        ),
        Property(
            "is_modeled_by",
            "openminds.latest.core.Strain",
            "diseaseModel",
            reverse="disease_models",
            multiple=True,
            description="reverse of 'disease_models'",
        ),
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "specimen_state",
            [
                "openminds.latest.core.SubjectGroupState",
                "openminds.latest.core.SubjectState",
                "openminds.latest.core.TissueSampleCollectionState",
                "openminds.latest.core.TissueSampleState",
            ],
            "pathology",
            reverse="pathologies",
            multiple=True,
            description="reverse of 'pathologies'",
        ),
        Property(
            "studied_in",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.Visualization",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "studyTarget",
            reverse="study_targets",
            multiple=True,
            description="reverse of 'study_targets'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        describes=None,
        description=None,
        interlex_identifier=None,
        is_modeled_by=None,
        is_used_to_group=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        specimen_state=None,
        studied_in=None,
        synonyms=None,
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
            name=name,
            definition=definition,
            describes=describes,
            description=description,
            interlex_identifier=interlex_identifier,
            is_modeled_by=is_modeled_by,
            is_used_to_group=is_used_to_group,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            specimen_state=specimen_state,
            studied_in=studied_in,
            synonyms=synonyms,
        )
