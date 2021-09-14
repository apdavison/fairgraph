import sys
import inspect
from ...base_v3 import KGObjectV3

from .research.subject_group import SubjectGroup
from .research.protocol_execution import ProtocolExecution
from .research.parameter_set import ParameterSet
from .research.behavioral_protocol import BehavioralProtocol
from .research.subject import Subject
from .research.numerical_parameter import NumericalParameter
from .research.tissue_sample_collection import TissueSampleCollection
from .research.stimulation import Stimulation
from .research.string_parameter import StringParameter
from .research.tissue_sample_state import TissueSampleState
from .research.subject_state import SubjectState
from .research.tissue_sample import TissueSample
from .research.tissue_sample_collection_state import TissueSampleCollectionState
from .research.protocol import Protocol
from .research.subject_group_state import SubjectGroupState
from .products.dataset import Dataset
from .products.project import Project
from .products.software_version import SoftwareVersion
from .products.dataset_version import DatasetVersion
from .products.meta_data_model_version import MetaDataModelVersion
from .products.model import Model
from .products.software import Software
from .products.meta_data_model import MetaDataModel
from .products.model_version import ModelVersion
from .miscellaneous.doi import DOI
from .miscellaneous.rorid import RORID
from .miscellaneous.isbn import ISBN
from .miscellaneous.quantitative_value import QuantitativeValue
from .miscellaneous.orcid import ORCID
from .miscellaneous.gridid import GRIDID
from .miscellaneous.funding import Funding
from .miscellaneous.quantitative_value_range import QuantitativeValueRange
from .miscellaneous.swhid import SWHID
from .miscellaneous.url import URL
from .actors.contribution import Contribution
from .actors.organization import Organization
from .actors.contact_information import ContactInformation
from .actors.affiliation import Affiliation
from .actors.person import Person
from .data.service_link import ServiceLink
from .data.copyright import Copyright
from .data.content_type_pattern import ContentTypePattern
from .data.file_repository import FileRepository
from .data.license import License
from .data.file import File
from .data.hash import Hash
from .data.file_path_pattern import FilePathPattern
from .data.content_type import ContentType
from .data.file_repository_structure import FileRepositoryStructure
from .data.file_bundle import FileBundle


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObjectV3) and obj.__module__.startswith(__name__)]
