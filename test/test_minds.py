
from datetime import datetime
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


test_data_lookup.update({
    "/v0/data/minds/core/activity/v1.0.0/": "test/test_data/nexus/minds/activity_list_0_10.json",
    "/v0/data/minds/core/agecategory/v1.0.0/": "test/test_data/nexus/minds/agecategory_list_0_10.json",
    "/v0/data/minds/core/dataset/v1.0.0/": "test/test_data/nexus/minds/dataset_list_0_10.json",
    "/v0/data/minds/core/embargostatus/v1.0.0/": "test/test_data/nexus/minds/embargostatus_list_0_10.json",
    "/v0/data/minds/ethics/approval/v1.0.0/": "test/test_data/nexus/minds/ethicsapproval_list_0_10.json",
    "/v0/data/minds/ethics/authority/v1.0.0/": "test/test_data/nexus/minds/ethicsauthority_list_0_10.json",
    "/v0/data/minds/core/file/v0.0.4/": "test/test_data/nexus/minds/file_list_0_10.json",
    "/v0/data/minds/core/fileassociation/v1.0.0/": "test/test_data/nexus/minds/fileassociation_list_0_10.json",
    "/v0/data/minds/core/format/v1.0.0/": "test/test_data/nexus/minds/format_list_0_10.json",
    "/v0/data/minds/core/licensetype/v1.0.0/": "test/test_data/nexus/minds/license_list_0_10.json",
    "/v0/data/minds/experiment/method/v1.0.0/": "test/test_data/nexus/minds/method_list_0_10.json",
    "/v0/data/minds/core/modality/v1.0.0/": "test/test_data/nexus/minds/modality_list_0_10.json",
    "/v0/data/minds/core/parcellationatlas/v1.0.0/": "test/test_data/nexus/minds/parcellationatlas_list_0_10.json",
    "/v0/data/minds/core/parcellationregion/v1.0.0/": "test/test_data/nexus/minds/parcellationregion_list_0_10.json",
    "/v0/data/minds/core/person/v1.0.0/": "test/test_data/nexus/minds/person_list_0_10.json",
    "/v0/data/minds/core/placomponent/v1.0.0/": "test/test_data/nexus/minds/placomponent_list_0_10.json",
    "/v0/data/minds/core/preparation/v1.0.0/": "test/test_data/nexus/minds/preparation_list_0_10.json",
    "/v0/data/minds/experiment/protocol/v1.0.0/": "test/test_data/nexus/minds/protocol_list_0_10.json",
    "/v0/data/minds/core/publication/v1.0.0/": "test/test_data/nexus/minds/publication_list_0_10.json",
    "/v0/data/minds/core/referencespace/v1.0.0/": "test/test_data/nexus/minds/referencespace_list_0_10.json",
    "/v0/data/minds/prov/role/v1.0.0/": "test/test_data/nexus/minds/role_list_0_10.json",
    "/v0/data/minds/experiment/sample/v1.0.0/": "test/test_data/nexus/minds/sample_list_0_10.json",
    "/v0/data/minds/core/sex/v1.0.0/": "test/test_data/nexus/minds/sex_list_0_10.json",
    "/v0/data/minds/core/softwareagent/v1.0.0/": "test/test_data/nexus/minds/softwareagent_list_0_10.json",
    "/v0/data/minds/core/species/v1.0.0/": "test/test_data/nexus/minds/species_list_0_10.json",
    "/v0/data/minds/core/specimengroup/v1.0.0/": "test/test_data/nexus/minds/specimengroup_list_0_10.json",
    "/v0/data/minds/experiment/subject/v1.0.0/": "test/test_data/nexus/minds/subject_list_0_10.json",

    #"/query/minds/core/dataset/v1.0.0/fgResolvedModified/instances": "test/test_data/kgquery/minds/dataset_list_resolved_0_10.json",
    "/query/minds/core/dataset/v1.0.0/fgResolved/instances": "test/test_data/kgquery/minds/dataset_list_resolved_0_10.json",
    "/api/releases/minds/core/dataset/v1.0.0/bd78a096-6804-4655-83e7-38286ba59671": "test/test_data/releases/released.json"
})


class TestActivity(BaseTestKG):
    class_under_test = Activity

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestAgeCategory(BaseTestKG):
    class_under_test = AgeCategory

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 5, len(objects)


class TestDataset(BaseTestKG):
    class_under_test = Dataset

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_from_id_kgquery_resolved(self, kg_client):
        uuid = "bd78a096-6804-4655-83e7-38286ba59671"
        dataset = Dataset.from_id(uuid, kg_client, api="query", scope="latest", resolved=True)
        assert dataset.uuid == uuid
        assert dataset.activity.ethics_authority.name == "Veterinary Office, Canton of Zurich, Switzerland"
        assert dataset.activity.preparation.name == "In vivo"
        #assert dataset.activity.protocols[0].name == 'Synchrotron radiation based X-ray tomography'
        assert dataset.release_date == datetime(2017, 11, 1, 0, 0)
        assert dataset.embargo_status.name == "Free"
        assert dataset.license.name == "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International"
        assert dataset.parcellation_region.alias == "Neocortex"
        assert dataset.parcellation_region.species.name == "Rattus norvegicus"
        assert dataset.specimen_group.subjects.age_category.name == "Adult"

class TestEmbargoStatus(BaseTestKG):
    class_under_test = EmbargoStatus

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 3, len(objects)


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


class TestLicense(BaseTestKG):
    class_under_test = License

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 3, len(objects)


class TestMethod(BaseTestKG):
    class_under_test = Method

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestModality(BaseTestKG):
    class_under_test = Modality

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 0, len(objects)


class TestFormat(BaseTestKG):
    class_under_test = Format

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestPLAComponent(BaseTestKG):
    class_under_test = PLAComponent

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestParcellationRegion(BaseTestKG):
    class_under_test = ParcellationRegion

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestParcellationAtlas(BaseTestKG):
    class_under_test = ParcellationAtlas

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 7, len(objects)


class TestPerson(BaseTestKG):
    class_under_test = Person

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestPreparation(BaseTestKG):
    class_under_test = Preparation

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 5, len(objects)


class TestPLAComponent(BaseTestKG):
    class_under_test = PLAComponent

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestProtocol(BaseTestKG):
    class_under_test = Protocol

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestPublication(BaseTestKG):
    class_under_test = Publication

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestReferenceSpace(BaseTestKG):
    class_under_test = ReferenceSpace

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestRole(BaseTestKG):
    class_under_test = Role

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 1, len(objects)


class TestSample(BaseTestKG):
    class_under_test = Sample

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestSex(BaseTestKG):
    class_under_test = Sex

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 4, len(objects)


class TestSoftwareAgent(BaseTestKG):
    class_under_test = SoftwareAgent

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 1, len(objects)


class TestSpecies(BaseTestKG):
    class_under_test = Species

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestSpecimenGroup(BaseTestKG):
    class_under_test = SpecimenGroup

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestSubject(BaseTestKG):
    class_under_test = Subject

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)
