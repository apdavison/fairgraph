"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import MolecularEntity as OMMolecularEntity
from fairgraph import KGObject


from openminds import IRI


class MolecularEntity(KGObject, OMMolecularEntity):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MolecularEntity"
    default_space = "controlled"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "composes",
            [
                "openminds.latest.chemicals.ChemicalSubstance",
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
            ],
            ["insulatorMaterial", "material", "molecularEntity"],
            reverse=["insulator_material", "material", "molecular_entity"],
            multiple=True,
            description="reverse of insulator_material, material, molecular_entity",
        ),
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
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "labels",
            "openminds.latest.ephys.PipetteUsage",
            "labelingCompound",
            reverse="labeling_compound",
            multiple=True,
            description="reverse of 'labeling_compound'",
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
        composes=None,
        definition=None,
        describes=None,
        description=None,
        interlex_identifier=None,
        is_used_to_group=None,
        knowledge_space_link=None,
        labels=None,
        preferred_ontology_identifier=None,
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
            composes=composes,
            definition=definition,
            describes=describes,
            description=description,
            interlex_identifier=interlex_identifier,
            is_used_to_group=is_used_to_group,
            knowledge_space_link=knowledge_space_link,
            labels=labels,
            preferred_ontology_identifier=preferred_ontology_identifier,
            studied_in=studied_in,
            synonyms=synonyms,
        )
