import sys
import inspect
from ...base_v3 import KGObjectV3

from .programming_language import ProgrammingLanguage
from .laterality import Laterality
from .software_application_category import SoftwareApplicationCategory
from .service import Service
from .age_category import AgeCategory
from .semantic_data_type import SemanticDataType
from .preparation_type import PreparationType
from .criteria_quality_type import CriteriaQualityType
from .operating_system import OperatingSystem
from .operating_device import OperatingDevice
from .experimental_approach import ExperimentalApproach
from .device_type import DeviceType
from .uberon_parcellation import UBERONParcellation
from .software_feature import SoftwareFeature
from .cell_type import CellType
from .type_of_uncertainty import TypeOfUncertainty
from .model_abstraction_level import ModelAbstractionLevel
from .ethics_assessment import EthicsAssessment
from .organ import Organ
from .strain import Strain
from .technique import Technique
from .qualitative_overlap import QualitativeOverlap
from .anatomical_axes_orientation import AnatomicalAxesOrientation
from .meta_data_model_type import MetaDataModelType
from .species import Species
from .file_usage_role import FileUsageRole
from .biological_sex import BiologicalSex
from .data_type import DataType
from .stimulation_approach import StimulationApproach
from .model_scope import ModelScope
from .stimulus_type import StimulusType
from .term_suggestion import TermSuggestion
from .disease import Disease
from .terminology import Terminology
from .handedness import Handedness
from .tissue_sample_type import TissueSampleType
from .contribution_type import ContributionType
from .product_accessibility import ProductAccessibility
from .biological_order import BiologicalOrder
from .language import Language
from .action_status_type import ActionStatusType
from .unit_of_measurement import UnitOfMeasurement
from .file_bundle_grouping import FileBundleGrouping
from .disease_model import DiseaseModel
from .phenotype import Phenotype
from .file_repository_type import FileRepositoryType


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObjectV3) and obj.__module__.startswith(__name__)]
