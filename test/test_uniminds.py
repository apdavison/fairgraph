from .utils import BaseTestKG, kg_client, test_data_lookup

from fairgraph.uniminds import (
    AbstractionLevel,
    AgeCategory,
    BrainStructure,
    CellularTarget,
    Country,
    Dataset,
    Disability,
    Doi,
    EmbargoStatus,
    EthicsApproval,
    EthicsAuthority,
    ExperimentalPreparation,
    File,
    FileAssociation,
    FileBundle,
    FileBundleGroup,
    FundingInformation,
    Genotype,
    Handedness,
    HBPComponent,
    License,
    Method,
    MethodCategory,
    MimeType,
    ModelFormat,
    ModelInstance,
    ModelScope,
    Organization,
    Person,
    Project,
    Publication,
    PublicationId,
    PublicationIdType,
    Sex,
    Species,
    Strain,
    StudyTarget,
    StudyTargetSource,
    StudyTargetType,
    Subject,
    SubjectGroup,
    TissueSample
)

test_data_lookup.update({})


class TestAbstractionLevel(BaseTestKG):
    class_under_test = AbstractionLevel


class TestAgeCategory(BaseTestKG):
    class_under_test = AgeCategory


class TestBrainStructure(BaseTestKG):
    class_under_test = BrainStructure


class TestCellularTarget(BaseTestKG):
    class_under_test = CellularTarget


class TestCountry(BaseTestKG):
    class_under_test = Country


class TestDataset(BaseTestKG):
    class_under_test = Dataset


class TestDisability(BaseTestKG):
    class_under_test = Disability


class TestDoi(BaseTestKG):
    class_under_test = Doi


class TestEmbargoStatus(BaseTestKG):
    class_under_test = EmbargoStatus


class TestEthicsApproval(BaseTestKG):
    class_under_test = EthicsApproval


class TestEthicsAuthority(BaseTestKG):
    class_under_test = EthicsAuthority


class TestExperimentalPreparation(BaseTestKG):
    class_under_test = ExperimentalPreparation


class TestFile(BaseTestKG):
    class_under_test = File


class TestFileAssociation(BaseTestKG):
    class_under_test = FileAssociation


class TestFileBundle(BaseTestKG):
    class_under_test = FileBundle


class TestFileBundleGroup(BaseTestKG):
    class_under_test = FileBundleGroup


class TestFundingInformation(BaseTestKG):
    class_under_test = FundingInformation


class TestGenotype(BaseTestKG):
    class_under_test = Genotype


class TestHandedness(BaseTestKG):
    class_under_test = Handedness


class TestHbpComponent(BaseTestKG):
    class_under_test = HBPComponent


class TestLicense(BaseTestKG):
    class_under_test = License


class TestMethod(BaseTestKG):
    class_under_test = Method


class TestMethodCategory(BaseTestKG):
    class_under_test = MethodCategory


class TestMimeType(BaseTestKG):
    class_under_test = MimeType


class TestModelFormat(BaseTestKG):
    class_under_test = ModelFormat


class TestModelInstance(BaseTestKG):
    class_under_test = ModelInstance


class TestModelScope(BaseTestKG):
    class_under_test = ModelScope


class TestOrganization(BaseTestKG):
    class_under_test = Organization


class TestPerson(BaseTestKG):
    class_under_test = Person


class TestProject(BaseTestKG):
    class_under_test = Project


class TestPublication(BaseTestKG):
    class_under_test = Publication


class TestPublicationId(BaseTestKG):
    class_under_test = PublicationId


class TestPublicationIdType(BaseTestKG):
    class_under_test = PublicationIdType


class TestSex(BaseTestKG):
    class_under_test = Sex


class TestSpecies(BaseTestKG):
    class_under_test = Species


class TestStrain(BaseTestKG):
    class_under_test = Strain


class TestStudyTarget(BaseTestKG):
    class_under_test = StudyTarget


class TestStudyTargetSource(BaseTestKG):
    class_under_test = StudyTargetSource


class TestStudyTargetType(BaseTestKG):
    class_under_test = StudyTargetType


class TestSubject(BaseTestKG):
    class_under_test = Subject


class TestSubjectGroup(BaseTestKG):
    class_under_test = SubjectGroup


class TestTissueSample(BaseTestKG):
    class_under_test = TissueSample
