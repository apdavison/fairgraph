import sys
from fairgraph.openminds import (
    list_kg_classes as _lkgc,
    list_embedded_metadata_classes as _lemc,
    set_error_handling as _seh,
)

from .access_channel import AccessChannel
from .access_eligibility_type import AccessEligibilityType
from .access_form import AccessForm
from .access_process_type import AccessProcessType
from .action_status_type import ActionStatusType
from .age_category import AgeCategory
from .age_reference import AgeReference
from .analysis_technique import AnalysisTechnique
from .anatomical_axes_orientation import AnatomicalAxesOrientation
from .anatomical_cavity import AnatomicalCavity
from .anatomical_identification_type import AnatomicalIdentificationType
from .anatomical_plane import AnatomicalPlane
from .annotation_criteria_type import AnnotationCriteriaType
from .annotation_type import AnnotationType
from .atlas_type import AtlasType
from .auditory_stimulus_type import AuditoryStimulusType
from .biological_order import BiologicalOrder
from .biological_process import BiologicalProcess
from .biological_sex import BiologicalSex
from .breeding_type import BreedingType
from .cell_culture_type import CellCultureType
from .cell_type import CellType
from .chemical_mixture_type import ChemicalMixtureType
from .colormap import Colormap
from .communication_interface_type import CommunicationInterfaceType
from .communication_protocol import CommunicationProtocol
from .contribution_type import ContributionType
from .cranial_window_construction_type import CranialWindowConstructionType
from .cranial_window_reinforcement_type import CranialWindowReinforcementType
from .criteria_quality_type import CriteriaQualityType
from .data_type import DataType
from .dependency_impact import DependencyImpact
from .deployment_environment_type import DeploymentEnvironmentType
from .device_mounting_type import DeviceMountingType
from .device_type import DeviceType
from .difference_measure import DifferenceMeasure
from .disease import Disease
from .disease_model import DiseaseModel
from .educational_level import EducationalLevel
from .electrical_stimulus_type import ElectricalStimulusType
from .experimental_approach import ExperimentalApproach
from .external_body_region import ExternalBodyRegion
from .file_bundle_grouping import FileBundleGrouping
from .file_repository_type import FileRepositoryType
from .file_usage_role import FileUsageRole
from .genetic_strain_type import GeneticStrainType
from .gustatory_stimulus_type import GustatoryStimulusType
from .handedness import Handedness
from .language import Language
from .laterality import Laterality
from .learning_resource_type import LearningResourceType
from .measured_quantity import MeasuredQuantity
from .measured_signal_type import MeasuredSignalType
from .meta_data_model_type import MetaDataModelType
from .model_abstraction_level import ModelAbstractionLevel
from .model_scope import ModelScope
from .modification_consent_requirement import ModificationConsentRequirement
from .modification_constraint import ModificationConstraint
from .modification_form import ModificationForm
from .modification_scope import ModificationScope
from .molecular_entity import MolecularEntity
from .mri_fat_suppression_technique import MRIFatSuppressionTechnique
from .mri_parallel_acquisition_technique import MRIParallelAcquisitionTechnique
from .mri_pulse_sequence import MRIPulseSequence
from .mri_spoiling_technique import MRISpoilingTechnique
from .mri_weighting import MRIWeighting
from .muscular_structure import MuscularStructure
from .nervous_system_structure import NervousSystemStructure
from .olfactory_stimulus_type import OlfactoryStimulusType
from .operating_device import OperatingDevice
from .operating_system import OperatingSystem
from .operational_approach import OperationalApproach
from .optical_stimulus_type import OpticalStimulusType
from .organ import Organ
from .organ_system_structure import OrganSystemStructure
from .organism_substance import OrganismSubstance
from .organism_system import OrganismSystem
from .organization_type import OrganizationType
from .patch_clamp_variation import PatchClampVariation
from .payment_model_type import PaymentModelType
from .preparation_type import PreparationType
from .programming_language import ProgrammingLanguage
from .project_type import ProjectType
from .publication_status import PublicationStatus
from .pulse_shape import PulseShape
from .qualitative_overlap import QualitativeOverlap
from .semantic_data_type import SemanticDataType
from .setup_type import SetupType
from .signal_directionality import SignalDirectionality
from .skeletal_structure import SkeletalStructure
from .software_application_category import SoftwareApplicationCategory
from .software_feature import SoftwareFeature
from .sovereign_state import SovereignState
from .spatial_encoding import SpatialEncoding
from .species import Species
from .stimulation_approach import StimulationApproach
from .stimulation_technique import StimulationTechnique
from .subcellular_entity import SubcellularEntity
from .subject_attribute import SubjectAttribute
from .supranational_body import SupranationalBody
from .tactile_stimulus_type import TactileStimulusType
from .technique import Technique
from .term_suggestion import TermSuggestion
from .terminology import Terminology
from .tissue_sample_attribute import TissueSampleAttribute
from .tissue_sample_type import TissueSampleType
from .tissue_structure import TissueStructure
from .type_of_uncertainty import TypeOfUncertainty
from .unit_of_measurement import UnitOfMeasurement
from .vascular_structure import VascularStructure
from .visual_stimulus_type import VisualStimulusType
from .weight_type import WeightType


def list_kg_classes():
    """List all KG classes defined in this module"""
    return _lkgc(sys.modules[__name__])


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return _lemc(sys.modules[__name__])


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
    """
    _seh(value, sys.modules[__name__])
