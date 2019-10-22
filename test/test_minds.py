from .utils import BaseTestKG, kg_client, test_data_lookup

from fairgraph.minds import (
    Activity,
    AgeCategory,
    Dataset,
    EmbargoStatus,
    EthicsApproval,
    EthicsAuthority,
    File,
    FileAssociation,
    License,
    MINDSObject,
    Method,
    Modality,
    Format,
    PLAComponent,
    ParcellationRegion,
    ParcellationAtlas,
    Person,
    Preparation,
    PLAComponent,
    Protocol,
    Publication,
    ReferenceSpace,
    Role,
    Sample,
    Sex,
    SoftwareAgent,
    Species,
    SpecimenGroup,
    Subject)


test_data_lookup.update({})


class TestActivity(BaseTestKG):
    class_under_test = Activity


class TestAgeCategory(BaseTestKG):
    class_under_test = AgeCategory


class TestDataset(BaseTestKG):
    class_under_test = Dataset


class TestEmbargoStatus(BaseTestKG):
    class_under_test = EmbargoStatus


class TestEthicsApproval(BaseTestKG):
    class_under_test = EthicsApproval


class TestEthicsAuthority(BaseTestKG):
    class_under_test = EthicsAuthority


class TestFile(BaseTestKG):
    class_under_test = File


class TestFileAssociation(BaseTestKG):
    class_under_test = FileAssociation


class TestLicense(BaseTestKG):
    class_under_test = License


class TestMethod(BaseTestKG):
    class_under_test = Method


class TestModality(BaseTestKG):
    class_under_test = Modality


class TestFormat(BaseTestKG):
    class_under_test = Format


class TestPLAComponent(BaseTestKG):
    class_under_test = PLAComponent


class TestParcellationRegion(BaseTestKG):
    class_under_test = ParcellationRegion


class TestParcellationAtlas(BaseTestKG):
    class_under_test = ParcellationAtlas


class TestPerson(BaseTestKG):
    class_under_test = Person


class TestPreparation(BaseTestKG):
    class_under_test = Preparation


class TestPLAComponent(BaseTestKG):
    class_under_test = PLAComponent


class TestProtocol(BaseTestKG):
    class_under_test = Protocol


class TestPublication(BaseTestKG):
    class_under_test = Publication


class TestReferenceSpace(BaseTestKG):
    class_under_test = ReferenceSpace


class TestRole(BaseTestKG):
    class_under_test = Role


class TestSample(BaseTestKG):
    class_under_test = Sample


class TestSex(BaseTestKG):
    class_under_test = Sex


class TestSoftwareAgent(BaseTestKG):
    class_under_test = SoftwareAgent


class TestSpecies(BaseTestKG):
    class_under_test = Species


class TestSpecimenGroup(BaseTestKG):
    class_under_test = SpecimenGroup


class TestSubject(BaseTestKG):
    class_under_test = Subject
