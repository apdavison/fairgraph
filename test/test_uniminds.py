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

test_data_lookup.update({
    "/v0/data/uniminds/options/abstractionlevel/v1.0.0/": "test/test_data/nexus/uniminds/abstractionlevel_list_0_10.json",
    "/v0/data/uniminds/options/agecategory/v1.0.0/": "test/test_data/nexus/uniminds/agecategory_list_0_10.json",
    "/v0/data/uniminds/options/brainstructure/v1.0.0/": "test/test_data/nexus/uniminds/brainstructure_list_0_10.json",
    "/v0/data/uniminds/options/cellulartarget/v1.0.0/": "test/test_data/nexus/uniminds/cellulartarget_list_0_10.json",
    "/v0/data/uniminds/options/country/v1.0.0/": "test/test_data/nexus/uniminds/country_list_0_10.json",
    "/v0/data/uniminds/core/dataset/v1.0.0/": "test/test_data/nexus/uniminds/dataset_list_0_10.json",
    "/v0/data/uniminds/options/disability/v1.0.0/": "test/test_data/nexus/uniminds/disability_list_0_10.json",
    "/v0/data/uniminds/options/doi/v1.0.0/": "test/test_data/nexus/uniminds/doi_list_0_10.json",
    "/v0/data/uniminds/options/embargostatus/v1.0.0/": "test/test_data/nexus/uniminds/embargostatus_list_0_10.json",
    "/v0/data/uniminds/core/ethicsapproval/v1.0.0/": "test/test_data/nexus/uniminds/ethicsapproval_list_0_10.json",
    "/v0/data/uniminds/options/ethicsauthority/v1.0.0/": "test/test_data/nexus/uniminds/ethicsauthority_list_0_10.json",
    "/v0/data/uniminds/options/experimentalpreparation/v1.0.0/": "test/test_data/nexus/uniminds/experimentalpreparation_list_0_10.json",
    "/v0/data/uniminds/core/file/v1.0.0/": "test/test_data/nexus/uniminds/file_list_0_10.json",
    "/v0/data/uniminds/core/fileassociation/v1.0.0/": "test/test_data/nexus/uniminds/fileassociation_list_0_10.json",
    "/v0/data/uniminds/core/filebundle/v1.0.0/": "test/test_data/nexus/uniminds/filebundle_list_0_10.json",
    "/v0/data/uniminds/options/filebundlegroup/v1.0.0/": "test/test_data/nexus/uniminds/filebundlegroup_list_0_10.json",
    "/v0/data/uniminds/core/fundinginformation/v1.0.0/": "test/test_data/nexus/uniminds/fundinginformation_list_0_10.json",
    "/v0/data/uniminds/options/genotype/v1.0.0/": "test/test_data/nexus/uniminds/genotype_list_0_10.json",
    "/v0/data/uniminds/core/hbpcomponent/v1.0.0/": "test/test_data/nexus/uniminds/hbpcomponent_list_0_10.json",
    "/v0/data/uniminds/options/handedness/v1.0.0/": "test/test_data/nexus/uniminds/handedness_list_0_10.json",
    "/v0/data/uniminds/options/license/v1.0.0/": "test/test_data/nexus/uniminds/license_list_0_10.json",
    "/v0/data/uniminds/core/method/v1.0.0/": "test/test_data/nexus/uniminds/method_list_0_10.json",
    "/v0/data/uniminds/options/methodcategory/v1.0.0/": "test/test_data/nexus/uniminds/methodcategory_list_0_10.json",
    "/v0/data/uniminds/options/mimetype/v1.0.0/": "test/test_data/nexus/uniminds/mimetype_list_0_10.json",
    "/v0/data/uniminds/options/modelformat/v1.0.0/": "test/test_data/nexus/uniminds/modelformat_list_0_10.json",
    "/v0/data/uniminds/core/modelinstance/v1.0.0/": "test/test_data/nexus/uniminds/modelinstance_list_0_10.json",
    "/v0/data/uniminds/options/modelscope/v1.0.0/": "test/test_data/nexus/uniminds/modelscope_list_0_10.json",
    "/v0/data/uniminds/options/organization/v1.0.0/": "test/test_data/nexus/uniminds/organization_list_0_10.json",
    "/v0/data/uniminds/core/person/v1.0.0/": "test/test_data/nexus/uniminds/person_list_0_10.json",
    "/v0/data/uniminds/core/project/v1.0.0/": "test/test_data/nexus/uniminds/project_list_0_10.json",
    "/v0/data/uniminds/core/publication/v1.0.0/": "test/test_data/nexus/uniminds/publication_list_0_10.json",
    "/v0/data/uniminds/options/publicationid/v1.0.0/": "test/test_data/nexus/uniminds/publicationid_list_0_10.json",
    "/v0/data/uniminds/options/publicationidtype/v1.0.0/": "test/test_data/nexus/uniminds/publicationidtype_list_0_10.json",
    "/v0/data/uniminds/options/sex/v1.0.0/": "test/test_data/nexus/uniminds/sex_list_0_10.json",
    "/v0/data/uniminds/options/species/v1.0.0/": "test/test_data/nexus/uniminds/species_list_0_10.json",
    "/v0/data/uniminds/options/strain/v1.0.0/": "test/test_data/nexus/uniminds/strain_list_0_10.json",
    "/v0/data/uniminds/core/studytarget/v1.0.0/": "test/test_data/nexus/uniminds/studytarget_list_0_10.json",
    "/v0/data/uniminds/options/studytargetsource/v1.0.0/": "test/test_data/nexus/uniminds/studytargetsource_list_0_10.json",
    "/v0/data/uniminds/options/studytargettype/v1.0.0/": "test/test_data/nexus/uniminds/studytargettype_list_0_10.json",
    "/v0/data/uniminds/core/subject/v1.0.0/": "test/test_data/nexus/uniminds/subject_list_0_10.json",
    "/v0/data/uniminds/core/subjectgroup/v1.0.0/": "test/test_data/nexus/uniminds/subjectgroup_list_0_10.json",
    "/v0/data/uniminds/core/tissuesample/v1.0.0/": "test/test_data/nexus/uniminds/tissuesample_list_0_10.json",
})


class TestAbstractionLevel(BaseTestKG):
    class_under_test = AbstractionLevel

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestAgeCategory(BaseTestKG):
    class_under_test = AgeCategory

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestBrainStructure(BaseTestKG):
    class_under_test = BrainStructure

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestCellularTarget(BaseTestKG):
    class_under_test = CellularTarget

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestCountry(BaseTestKG):
    class_under_test = Country

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestDataset(BaseTestKG):
    class_under_test = Dataset

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestDisability(BaseTestKG):
    class_under_test = Disability

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestDoi(BaseTestKG):
    class_under_test = Doi

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestEmbargoStatus(BaseTestKG):
    class_under_test = EmbargoStatus

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestEthicsApproval(BaseTestKG):
    class_under_test = EthicsApproval

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestEthicsAuthority(BaseTestKG):
    class_under_test = EthicsAuthority

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestExperimentalPreparation(BaseTestKG):
    class_under_test = ExperimentalPreparation

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 2, len(objects)


class TestFile(BaseTestKG):
    class_under_test = File

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestFileAssociation(BaseTestKG):
    class_under_test = FileAssociation

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestFileBundle(BaseTestKG):
    class_under_test = FileBundle

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestFileBundleGroup(BaseTestKG):
    class_under_test = FileBundleGroup

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestFundingInformation(BaseTestKG):
    class_under_test = FundingInformation

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestGenotype(BaseTestKG):
    class_under_test = Genotype

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestHandedness(BaseTestKG):
    class_under_test = Handedness

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestHbpComponent(BaseTestKG):
    class_under_test = HBPComponent

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestLicense(BaseTestKG):
    class_under_test = License

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestMethod(BaseTestKG):
    class_under_test = Method

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestMethodCategory(BaseTestKG):
    class_under_test = MethodCategory

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestMimeType(BaseTestKG):
    class_under_test = MimeType

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestModelFormat(BaseTestKG):
    class_under_test = ModelFormat

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestModelInstance(BaseTestKG):
    class_under_test = ModelInstance

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestModelScope(BaseTestKG):
    class_under_test = ModelScope

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestOrganization(BaseTestKG):
    class_under_test = Organization

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestPerson(BaseTestKG):
    class_under_test = Person

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestProject(BaseTestKG):
    class_under_test = Project

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestPublication(BaseTestKG):
    class_under_test = Publication

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestPublicationId(BaseTestKG):
    class_under_test = PublicationId

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestPublicationIdType(BaseTestKG):
    class_under_test = PublicationIdType

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestSex(BaseTestKG):
    class_under_test = Sex

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestSpecies(BaseTestKG):
    class_under_test = Species

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestStrain(BaseTestKG):
    class_under_test = Strain

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestStudyTarget(BaseTestKG):
    class_under_test = StudyTarget

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestStudyTargetSource(BaseTestKG):
    class_under_test = StudyTargetSource

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestStudyTargetType(BaseTestKG):
    class_under_test = StudyTargetType

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestSubject(BaseTestKG):
    class_under_test = Subject

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestSubjectGroup(BaseTestKG):
    class_under_test = SubjectGroup

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestTissueSample(BaseTestKG):
    class_under_test = TissueSample

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)
