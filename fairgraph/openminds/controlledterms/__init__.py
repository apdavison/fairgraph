import sys
import inspect
from fairgraph.kgobject import KGObject
from fairgraph.embedded import EmbeddedMetadata

from .difference_measure import DifferenceMeasure
from .programming_language import ProgrammingLanguage
from .stimulation_technique import StimulationTechnique
from .measured_quantity import MeasuredQuantity
from .laterality import Laterality
from .auditory_stimulus_type import AuditoryStimulusType
from .software_application_category import SoftwareApplicationCategory
from .service import Service
from .age_category import AgeCategory
from .semantic_data_type import SemanticDataType
from .preparation_type import PreparationType
from .organism_substance import OrganismSubstance
from .criteria_quality_type import CriteriaQualityType
from .anatomical_identification_type import AnatomicalIdentificationType
from .operating_system import OperatingSystem
from .operating_device import OperatingDevice
from .experimental_approach import ExperimentalApproach
from .breeding_type import BreedingType
from .subject_attribute import SubjectAttribute
from .device_type import DeviceType
from .uberon_parcellation import UBERONParcellation
from .software_feature import SoftwareFeature
from .cell_type import CellType
from .type_of_uncertainty import TypeOfUncertainty
from .genetic_strain_type import GeneticStrainType
from .electrical_stimulus_type import ElectricalStimulusType
from .model_abstraction_level import ModelAbstractionLevel
from .olfactory_stimulus_type import OlfactoryStimulusType
from .learning_resource_type import LearningResourceType
from .annotation_criteria_type import AnnotationCriteriaType
from .ethics_assessment import EthicsAssessment
from .organ import Organ
from .technique import Technique
from .tactile_stimulus_type import TactileStimulusType
from .chemical_mixture_type import ChemicalMixtureType
from .qualitative_overlap import QualitativeOverlap
from .anatomical_axes_orientation import AnatomicalAxesOrientation
from .analysis_technique import AnalysisTechnique
from .molecular_entity import MolecularEntity
from .meta_data_model_type import MetaDataModelType
from .species import Species
from .file_usage_role import FileUsageRole
from .anatomical_plane import AnatomicalPlane
from .biological_sex import BiologicalSex
from .data_type import DataType
from .stimulation_approach import StimulationApproach
from .model_scope import ModelScope
from .optical_stimulus_type import OpticalStimulusType
from .cranial_window_reinforcement_type import CranialWindowReinforcementType
from .term_suggestion import TermSuggestion
from .disease import Disease
from .setup_type import SetupType
from .terminology import Terminology
from .handedness import Handedness
from .tissue_sample_type import TissueSampleType
from .organism_system import OrganismSystem
from .contribution_type import ContributionType
from .product_accessibility import ProductAccessibility
from .cranial_window_construction_type import CranialWindowConstructionType
from .biological_order import BiologicalOrder
from .educational_level import EducationalLevel
from .visual_stimulus_type import VisualStimulusType
from .language import Language
from .cell_culture_type import CellCultureType
from .action_status_type import ActionStatusType
from .unit_of_measurement import UnitOfMeasurement
from .file_bundle_grouping import FileBundleGrouping
from .disease_model import DiseaseModel
from .patch_clamp_variation import PatchClampVariation
from .colormap import Colormap
from .file_repository_type import FileRepositoryType
from .atlas_type import AtlasType
from .subcellular_entity import SubcellularEntity
from .annotation_type import AnnotationType
from .gustatory_stimulus_type import GustatoryStimulusType
from .tissue_sample_attribute import TissueSampleAttribute


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)
    ]


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, EmbeddedMetadata) and obj.__module__.startswith(__name__)
    ]


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required field is not provided).
            Possible values: "error", "warning", "log", None
    """
    for cls in list_kg_classes() + list_embedded_metadata_classes():
        cls.set_error_handling(value)
