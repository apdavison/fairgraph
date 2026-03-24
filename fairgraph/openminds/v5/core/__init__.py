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
    SpecimenAge,
    NumericalProperty,
    SubjectGroupState,
    SpecimenWeight,
    PropertyValueList,
)
from .products import (
    Interface,
    Dataset,
    Project,
    DatasetVersion,
    Service,
    SoftwareVersion,
    MetaDataModelVersion,
    Model,
    Software,
    Setup,
    HardwareProduct,
    MetaDataModel,
    InterfaceVersion,
    ModelVersion,
)
from .digital_identifier import (
    ISSN,
    IdentifiersDotOrgID,
    DOI,
    RORID,
    GenericIdentifier,
    RRID,
    ORCID,
    ISBN,
    StockNumber,
    LEI,
    ISNI,
    HANDLE,
    SWHID,
)
from .miscellaneous import (
    Membership,
    QuantitativeValue,
    Location,
    Funding,
    ResearchProductGroup,
    WebResource,
    Accessibility,
    GeoCoordinates,
    Dependency,
    QuantitativeValueRange,
    QuantitativeValueArray,
    Comment,
)
from .actors import Contribution, AccountInformation, Consortium, Affiliation, Organization, ContactInformation, Person
from .data import (
    ServiceLink,
    UsageAgreement,
    ContentTypePattern,
    Copyright,
    GridImage,
    LocalFile,
    FileArchive,
    Hash,
    GridImageStack,
    ContentType,
    FilePathPattern,
    FileRepository,
    License,
    File,
    FileBundle,
    FileRepositoryStructure,
    GridVolume,
    GridVolumeSequence,
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
