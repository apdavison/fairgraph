import sys
from fairgraph.openminds import (
    list_kg_classes as _lkgc,
    list_embedded_metadata_classes as _lemc,
    set_error_handling as _seh,
)

from .research import (
    ProtocolExecution,
    SubjectGroup,
    Subject,
    Strain,
    TissueSampleCollection,
    BehavioralProtocol,
    StringProperty,
    CustomPropertySet,
    TissueSampleState,
    SubjectState,
    TissueSample,
    Protocol,
    TissueSampleCollectionState,
    Configuration,
    NumericalProperty,
    SubjectGroupState,
    PropertyValueList,
)
from .products import (
    Dataset,
    Project,
    DatasetVersion,
    SoftwareVersion,
    MetaDataModelVersion,
    Model,
    Software,
    Setup,
    WebServiceVersion,
    MetaDataModel,
    WebService,
    ModelVersion,
)
from .digital_identifier import (
    ISSN,
    IdentifiersDotOrgID,
    DOI,
    RORID,
    RRID,
    ORCID,
    GRIDID,
    ISBN,
    StockNumber,
    HANDLE,
    SWHID,
)
from .miscellaneous import (
    QuantitativeValue,
    Funding,
    ResearchProductGroup,
    WebResource,
    QuantitativeValueRange,
    QuantitativeValueArray,
    Comment,
)
from .actors import Contribution, AccountInformation, Consortium, Affiliation, Organization, ContactInformation, Person
from .data import (
    ServiceLink,
    ContentTypePattern,
    Copyright,
    FileArchive,
    Hash,
    ContentType,
    FilePathPattern,
    FileRepository,
    License,
    File,
    FileBundle,
    FileRepositoryStructure,
    Measurement,
)


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
