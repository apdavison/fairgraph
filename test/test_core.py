# encoding: utf-8
"""
Tests of fairgraph.core module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

from datetime import datetime
from fairgraph.base_v2 import KGQuery, KGProxy, as_list
from fairgraph.commons import QuantitativeValue, Species, Strain, Sex, Age, Address
from fairgraph.core import Subject, Organization, Person

from .utils import kg_client, MockKGObject, test_data_lookup, BaseTestKG
try:
    from pyxus.resources.entity import Instance
    have_pyxus = True
except ImportError:
    have_pyxus = False

import pytest


test_data_lookup.update({
    "/v0/data/neuralactivity/core/collection/v0.1.0/": "test/test_data/nexus/core/collection_list_0_10.json",
    "/v0/data/neuralactivity/core/identifier/v0.1.0/": "test/test_data/nexus/core/identifier_list_0_10.json",
    "/v0/data/neuralactivity/core/organization/v0.1.0/": "test/test_data/nexus/core/organization_list_0_10.json",
    "/v0/data/neuralactivity/core/person/v0.1.0/": "test/test_data/nexus/core/person_list_0_10.json",
    "/v0/data/neuralactivity/core/protocol/v0.1.0/": "test/test_data/nexus/core/protocol_list_0_10.json",
    "/v0/data/neuralactivity/core/subject/v0.1.2/": "test/test_data/nexus/core/subject_list_0_10.json",
})


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestSubject(BaseTestKG):
    class_under_test = Subject

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_round_trip(self, kg_client):
        obj1 = Subject(name="Mickey", species=Species("Mus musculus"),
                       strain=Strain("129/Sv"), sex=Sex("male"),
                       age=Age(QuantitativeValue(20, "days"), "Post-natal"),
                       death_date=datetime(1960, 1, 1))
        instance = Instance(Subject.path, obj1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "http://fake_uuid_9ab2227fe1"
        instance.data["@type"] = Subject.type
        obj2 = Subject.from_kg_instance(instance, kg_client)
        for field in ("name", "species", "strain", "sex", "age", "death_date"):
            assert getattr(obj1, field) == getattr(obj2, field)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestOrganization(BaseTestKG):
    class_under_test = Organization

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_round_trip(self, kg_client):
        obj1 = Organization(name="NeuroPSI",
                            address=Address(locality="Saclay", country="France"),
                            parent=KGProxy(Organization, "http://fake_uuid_00481be7a1"))
        instance = Instance(Organization.path, obj1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "http://fake_uuid_7bb3c1e78b"
        instance.data["@type"] = Organization.type
        obj2 = Organization.from_kg_instance(instance, kg_client)
        for field in ("name", "address", "parent"):
            assert getattr(obj1, field) == getattr(obj2, field)

    def test_build_data(self, kg_client):
        obj1 = Organization(name="NeuroPSI",
                            address=Address(locality="Saclay", country="France"),
                            parent=KGProxy(Organization, "http://fake_uuid_00481be7a1"))
        expected = {
            "name": "NeuroPSI",
            "address": {
                "@type": "schema:PostalAddress",
                "addressLocality": "Saclay",
                "addressCountry": "France"
            },
            "parentOrganization": {
                "@type": ["nsg:Organization"],
                "@id": "http://fake_uuid_00481be7a1"
            }
        }
        assert obj1._build_data(kg_client) == expected


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestPerson(BaseTestKG):
    class_under_test = Person

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_list_with_filter(self, kg_client):
        people = Person.list(kg_client, api="nexus", family_name="da Vinci", size=10)
        assert isinstance(people, Person)
        people = Person.list(kg_client, api="nexus", given_name="Katherine", size=10)
        assert isinstance(people, Person)
        people = Person.list(kg_client, api="nexus", given_name="Horatio", size=10)
        assert len(people) == 0

    def test_round_trip(self, kg_client):
        p1 = Person("Hamilton", "Margaret", "margaret.hamilton@nasa.gov",
                    KGProxy(Organization, "http://fake_uuid_855fead8"))
        instance = Instance(Person.path, p1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "http://fake_uuid_8ab3dc739b"
        instance.data["@type"] = Person.type
        p2 = Person.from_kg_instance(instance, kg_client)
        for field in ("family_name", "given_name", "email", "affiliation", "full_name"):
            assert getattr(p1, field) == getattr(p2, field)

    def test_exists(self, kg_client):
        p1 = Person("Hamilton", "Margaret", "margaret.hamilton@nasa.gov",
                    KGProxy(Organization, "http://fake_uuid_855fead8"),
                    id="http://fake_uuid_8ab3dc739b")
        assert p1.exists(kg_client, api="nexus")
        p2 = Person("James", "Bond", "fictional@example.com")
        p2_exists = p2.exists(kg_client, api="nexus")
        assert not p2_exists
        p3_noid = Person("Johnson", "Katherine", "katherine.johnson@nasa.gov")
        p3_exists = p3_noid.exists(kg_client, api="nexus")
        assert p3_exists

    def test_existence_query(self):
        obj = Person("Johnson", "Katherine")
        expected = {
            "op": "and",
            "value": [
                {
                    "path": "schema:familyName",
                    "op": "eq",
                    "value": "Johnson"
                },
                {
                    "path": "schema:givenName",
                    "op": "eq",
                    "value": "Katherine"
                }
            ]
        }
        generated = obj._build_existence_query(api="nexus")
        assert expected == generated

    def test_get_context(self, kg_client):
        p1 = Person("Hamilton", "Margaret", "margaret.hamilton@nasa.gov",
                    KGProxy(Organization, "http://fake_uuid_855fead8"),
                    id="http://fake_uuid_8ab3dc739b")
        context = p1.get_context(kg_client)
        assert context == Person.context

    def test_uuid(self, kg_client):
        obj = Person("Johnson", "Katherine", "katherine.johnson@nasa.gov",
                     id="https://nexus.humanbrainproject.org/v0/data/neuralactivity/core/person/v0.1.0/02be7e84-af91-4481-a7c1-1ec204eaeab8")

        assert obj.uuid == "02be7e84-af91-4481-a7c1-1ec204eaeab8"

        assert obj.uri_from_uuid(obj.uuid, kg_client) == obj.id

    def test_from_uuid_empty_uuid(self, kg_client):
        with pytest.raises(ValueError):
            Person.from_uuid("", kg_client)

    def test_from_uuid_invalid_uuid(self, kg_client):
        with pytest.raises(ValueError):
            Person.from_uuid("02be7e84-af91-4481-a7c1-1ec204eaeab", kg_client, api="nexus")

    def test_save_new(self, kg_client, monkeypatch):
        new_p = Person("Ride", "Sally", "sally.ride@nasa.gov")
        monkeypatch.setattr(Person, "exists", lambda self, kg_client, api='any': False)
        new_p.save(kg_client)
