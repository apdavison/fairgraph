# encoding: utf-8
"""
Tests of fairgraph.base_v2 module.
"""

from datetime import date, datetime
from uuid import UUID
from fairgraph.base_v2 import KGQuery, KGProxy, as_list, Distribution, build_kg_object
from fairgraph.base_v3 import EmbeddedMetadata, KGObject
from fairgraph.fields import Field
from fairgraph.commons import QuantitativeValue
from fairgraph.core import Person

from .utils import kg_client

try:
    from pyxus.resources.entity import Instance
    have_pyxus = True
except ImportError:
    have_pyxus = False


import pytest

@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestDistribution(object):

    def test_to_jsonld(self, kg_client):
        obj = Distribution(location="http://example.com/data.dat",
                           size=123,  # bytes
                           digest="abcdef",
                           digest_method="sha1",
                           content_type="application/foo",
                           original_file_name="data.dat")
        data = obj.to_jsonld(kg_client)
        expected_data = {
            "@context": "https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0",
            "contentSize": {"unit": "byte", "value": 123},
            "digest": {"algorithm": "sha1", "value": "abcdef"},
            "downloadURL": "http://example.com/data.dat",
            "mediaType": "application/foo",
            "originalFileName": "data.dat"}
        assert data == expected_data

    def test_from_jsonld(self, kg_client):
        data = {
            "@context": "https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0",
            "contentSize": {"unit": "byte", "value": 456},
            "digest": {"algorithm": "sha1", "value": "a1b2c3"},
            "downloadURL": "http://example.com/data2.dat",
            "mediaType": "application/bar",
            "originalFileName": "data2.dat"
        }
        obj = Distribution.from_jsonld(data)
        assert obj.size == 456
        assert obj.content_type == "application/bar"
        assert obj.digest == "a1b2c3"
        assert obj.digest_method == "sha1"
        assert obj.location == "http://example.com/data2.dat"

    def test_from_jsonld_minimal(self, kg_client):
        data = {
            "@context": "https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0",
            "downloadURL": "http://example.com/data2.dat",
        }
        obj = Distribution.from_jsonld(data)
        assert obj.size is None
        assert obj.content_type is None
        assert obj.digest is None
        assert obj.digest_method is None
        assert obj.location == "http://example.com/data2.dat"


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestModuleFunctions(object):

    def test_build_kg_object(self, kg_client):
        obj = build_kg_object(Person, {"@id": "http://fake_uuid_a8575fdd19"})
        assert isinstance(obj, KGProxy)

        obj = build_kg_object(
            Person, {"@list": [{"@id": "http://fake_uuid_a8575fdd19"}]})
        assert isinstance(obj, KGProxy)

        obj = build_kg_object(Person,
                              [{"@id": "http://fake_uuid_a8575fdd19"},
                               {"@id": "http://fake_uuid_91ddf5758a"}])
        assert isinstance(obj, list)
        assert isinstance(obj[1], KGProxy)

        obj = build_kg_object(
            Distribution, {"downloadURL": "http://example.com/data.dat"})
        assert isinstance(obj, Distribution)

        with pytest.raises(ValueError):
            build_kg_object(tuple, {"@id": "http://fake_uuid_a8575fdd19"})

        with pytest.raises(ValueError):
            build_kg_object(Person, "abcde")

        obj = build_kg_object(
            None, {"@id": "http://fake_uuid_a8575fdd19", "@type": Person.type})
        assert isinstance(obj, KGProxy)
        assert obj.type == Person.type


class MockEmbeddedObject(EmbeddedMetadata):
    type = ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "mock": "https://openminds.ebrains.eu/mock/"
    }
    fields = [
        Field("a_string", str, "vocab:aString",
              multiple=False, required=False),
        Field("a_date", date, "vocab:aDate", multiple=False, required=False),
        Field("a_number", float, "vocab:aNumber",
              multiple=False, required=True),
    ]


class MockKGObject2(KGObject):
    default_space = "mock"
    type = ["https://openminds.ebrains.eu/mock/MockKGObject2"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "mock": "https://openminds.ebrains.eu/mock/"
    }
    fields = [
        Field("a", int, "vocab:A", multiple=False, required=True)
    ]


class MockKGObject(KGObject):
    default_space = "mock"
    type = ["https://openminds.ebrains.eu/mock/MockKGObject"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "mock": "https://openminds.ebrains.eu/mock/"
    }
    fields = [
        Field("a_required_string", str, "vocab:aRequiredString",
              multiple=False, required=True),
        Field("a_required_list_of_strings", str,
              "vocab:aRequiredListOfStrings", multiple=True, required=True),
        Field("an_optional_string", str, "vocab:anOptionalString",
              multiple=False, required=False),
        Field("an_optional_list_of_strings", str,
              "vocab:anOptionalListOfStrings", multiple=True, required=False),
        Field("a_required_datetime", datetime,
              "vocab:aRequiredDateTime", multiple=False, required=True),
        Field("a_required_list_of_datetimes", datetime,
              "vocab:aRequiredListOfDateTimes", multiple=True, required=True),
        Field("an_optional_datetime", datetime,
              "vocab:anOptionalDateTime", multiple=False, required=False),
        Field("an_optional_list_of_datetimes", datetime,
              "vocab:anOptionalListOfDateTimes", multiple=True, required=False),
        Field("a_required_linked_object", ["test_base.MockKGObject", MockKGObject2],
              "vocab:aRequiredLinkedObject", multiple=False, required=True),
        Field("a_required_list_of_linked_objects", ["test_base.MockKGObject", MockKGObject2],
              "vocab:aRequiredListOfLinkedObjects", multiple=True, required=True),
        Field("an_optional_linked_object", MockKGObject2,
              "vocab:anOptionalLinkedObject", multiple=False, required=False),
        Field("an_optional_list_of_linked_objects", ["test_base.MockKGObject", MockKGObject2],
              "vocab:anOptionalListOfLinkedObjects", multiple=True, required=False),
        Field("a_required_embedded_object", MockEmbeddedObject,
              "vocab:aRequiredEmbeddedObject", multiple=False, required=True),
        Field("a_required_list_of_embedded_objects", MockEmbeddedObject,
              "vocab:aRequiredListOfEmbeddedObjects", multiple=True, required=True),
        Field("an_optional_embedded_object", MockEmbeddedObject,
              "vocab:anOptionalEmbeddedObject", multiple=False, required=False),
        Field("an_optional_list_of_embedded_objects", MockEmbeddedObject,
              "vocab:anOptionalListOfEmbeddedObjects", multiple=True, required=False),
    ]
    existence_query_fields = ("a_required_string", "a_required_datetime",
                              "a_required_linked_object", "a_required_embedded_object")


ID_NAMESPACE = "https://kg.ebrains.eu/api/instances/"


class TestKGObject(object):
    object_counter = 0

    def _construct_embedded_object_required_fields(self, n):
        return MockEmbeddedObject(a_number=float(n))

    def _construct_object_required_fields(self):
        return MockKGObject(
            id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000002",
            a_required_string="apple",
            a_required_list_of_strings=["banana", "pear"],
            a_required_datetime=datetime(1789, 7, 14),
            a_required_list_of_datetimes=[datetime(1900, 1, 1), datetime(2000, 1, 1)],
            a_required_linked_object=MockKGObject2(a=1234, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"),
            a_required_list_of_linked_objects=[
                MockKGObject2(a=2345, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000002345"),
                MockKGObject2(a=3456, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000003456")
            ],
            a_required_embedded_object=self._construct_embedded_object_required_fields(41),
            a_required_list_of_embedded_objects=[
                self._construct_embedded_object_required_fields(42),
                self._construct_embedded_object_required_fields(43)
            ]
        )

    def _construct_object_all_fields(self):
        return MockKGObject(
            id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001",
            a_required_string="apple",
            a_required_list_of_strings=["banana", "pear"],
            an_optional_string="melon",
            an_optional_list_of_strings=["plum, peach, apricot"],
            a_required_datetime=datetime(1789, 7, 14),
            a_required_list_of_datetimes=[datetime(1900, 1, 1), datetime(2000, 1, 1)],
            an_optional_datetime=datetime(1605, 11, 5),
            an_optional_list_of_datetimes=[datetime(1899, 12, 31), datetime(1999, 12, 31)],
            a_required_linked_object=self._construct_object_required_fields(),
            a_required_list_of_linked_objects=[
                self._construct_object_required_fields(),
                self._construct_object_required_fields()
            ],
            an_optional_linked_object=MockKGObject2(a=123, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000123"),
            an_optional_list_of_linked_objects=[
                MockKGObject2(a=1234, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"),
                self._construct_object_required_fields()
            ],
            a_required_embedded_object=self._construct_embedded_object_required_fields(-1),
            a_required_list_of_embedded_objects=[
                self._construct_embedded_object_required_fields(100),
                self._construct_embedded_object_required_fields(200),
            ],
            an_optional_embedded_object=self._construct_embedded_object_required_fields(17),
            an_optional_list_of_embedded_objects=[
                self._construct_embedded_object_required_fields(18),
                self._construct_embedded_object_required_fields(19),
            ]
        )

    def test_construct_object_all_fields(self):
        obj = self._construct_object_all_fields()
        assert obj.a_required_string == "apple"
        assert obj.an_optional_datetime == datetime(1605, 11, 5)
        assert isinstance(obj.a_required_linked_object, MockKGObject)
        assert obj.a_required_linked_object.a_required_linked_object.a == 1234
        assert obj.an_optional_list_of_embedded_objects[1].a_number == 19.0

    def test_uuid(self):
        obj = self._construct_object_required_fields()
        # this should probably be a UUID object but it"s not at present
        assert obj.uuid == "00000000-0000-0000-0000-000000000002"

    def test_build_existence_query(self):
        obj = self._construct_object_all_fields()
        expected = {
            "a_required_datetime": "1789-07-14T00:00:00",
            "a_required_embedded_object": {
                "@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"],
                "vocab:aNumber": -1.0
            },
            "a_required_linked_object": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002",
            "a_required_string": "apple"
        }
        assert obj._build_existence_query() == expected

    def test_build_data_all_fields(self):
        obj = self._construct_object_all_fields()
        expected = {
            "vocab:aRequiredDateTime": "1789-07-14T00:00:00",
            "vocab:aRequiredEmbeddedObject": {
                "@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"],
                "vocab:aNumber": -1.0
            },
            "vocab:aRequiredLinkedObject": {
                "@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002",
            },
            "vocab:aRequiredListOfDateTimes": ["1900-01-01T00:00:00", "2000-01-01T00:00:00"],
            "vocab:aRequiredListOfEmbeddedObjects": [
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 100.0},
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 200.0}],
            "vocab:aRequiredListOfLinkedObjects": [
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002"},
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002"}
            ],
            "vocab:aRequiredListOfStrings": ["banana", "pear"],
            "vocab:aRequiredString": "apple",
            "vocab:anOptionalDateTime": "1605-11-05T00:00:00",
            "vocab:anOptionalEmbeddedObject": {
                "@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"],
                "vocab:aNumber": 17.0
            },
            "vocab:anOptionalLinkedObject": {
                "@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000123"
            },
            "vocab:anOptionalListOfDateTimes": ["1899-12-31T00:00:00", "1999-12-31T00:00:00"],
            "vocab:anOptionalListOfEmbeddedObjects": [
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 18.0},
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 19.0}],
            "vocab:anOptionalListOfLinkedObjects": [
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"},
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002"}],
            "vocab:anOptionalListOfStrings": "plum, peach, apricot",
            "vocab:anOptionalString": "melon"}
        assert obj._build_data(client=None, all_fields=True) == expected

    def test_updated_data(self):
        obj = self._construct_object_all_fields()
        obj.data = obj._build_data(client=None, all_fields=True)
        expected = {}
        assert obj._updated_data(obj.data) == expected

        obj.a_required_string = "pomme"
        obj.an_optional_list_of_embedded_objects = [
            self._construct_embedded_object_required_fields(-18),
            self._construct_embedded_object_required_fields(19),
        ]
        expected = {
            "vocab:aRequiredString": "pomme",
            "vocab:anOptionalListOfEmbeddedObjects": [
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": -18},
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 19}
            ]
        }
        new_data = obj._build_data(client=None, all_fields=True)
        assert obj._updated_data(new_data) == expected

    def test_update(self):
        obj = self._construct_object_required_fields()
        assert obj.an_optional_datetime == None
        new_data = {
            "@id": obj.id,
            "@type": obj.type,
            "vocab:aRequiredListOfString": ["kumquat", "bilberry"],
            "vocab:anOptionalDateTime": "1789-07-14T00:00:00"
        }
        obj._update(new_data, client=None, resolved=False)
        assert obj.a_required_list_of_strings == ["banana", "pear"]  # unchanged because already set
        assert obj.an_optional_datetime == datetime(1789, 7, 14)

    @pytest.mark.filterwarnings("ignore:Field")  # ignore expected warning from strict_mode False
    def test_exists__it_does_exist(self):
        orig_object = self._construct_object_required_fields()
        class MockClient:
            def instance_from_full_uri(self, id, use_cache=True, scope="in progress", resolved=False):
                data = orig_object._build_data(client=None, all_fields=True)
                data["https://core.kg.ebrains.eu/vocab/meta/space"] = "collab-foobar"
                data["@id"] = orig_object.id
                data["@context"] = orig_object.context
                data["@type"] = orig_object.type
                return data
        MockKGObject.set_strict_mode(False)  # stop the constructor from complaining
        new_obj = MockKGObject(id=orig_object.id, a_required_list_of_strings=["coconut"], an_optional_string="lime")
        MockKGObject.set_strict_mode(True)
        assert new_obj.a_required_list_of_strings == ["coconut"]
        assert new_obj.data is None
        assert new_obj.a_required_embedded_object == None

        assert new_obj.exists(MockClient()) and new_obj.space == "collab-foobar"  # has the side-effect of setting .data

        assert new_obj.a_required_embedded_object == MockEmbeddedObject(a_number=41.0)
        expected = {
            "@context": MockKGObject.context,
            "@id": orig_object.id,
            "@type": MockKGObject.type,
            "https://core.kg.ebrains.eu/vocab/meta/space": "collab-foobar",
            "vocab:aRequiredDateTime": "1789-07-14T00:00:00",
            "vocab:aRequiredEmbeddedObject": {
                "@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"],
                "vocab:aNumber": 41.0
            },
            "vocab:aRequiredLinkedObject": {
                "@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"
            },
            "vocab:aRequiredListOfDateTimes": ["1900-01-01T00:00:00",
                                               "2000-01-01T00:00:00"],
            "vocab:aRequiredListOfEmbeddedObjects": [
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 42.0},
                {"@type": ["https://openminds.ebrains.eu/mock/MockEmbeddedObject"], "vocab:aNumber": 43.0}],
            "vocab:aRequiredListOfLinkedObjects": [
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000002345"},
                {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000003456"}
            ],
            "vocab:aRequiredListOfStrings": ["banana", "pear"],  # still the same value, represents what is thought to be in the KG
            "vocab:aRequiredString": "apple",
            "vocab:anOptionalDateTime": None,
            "vocab:anOptionalEmbeddedObject": None,
            "vocab:anOptionalLinkedObject": None,
            "vocab:anOptionalListOfDateTimes": None,
            "vocab:anOptionalListOfEmbeddedObjects": None,
            "vocab:anOptionalListOfLinkedObjects": None,
            "vocab:anOptionalListOfStrings": None,
            "vocab:anOptionalString": None}
        assert new_obj.data == expected
        assert new_obj.a_required_list_of_strings == ["coconut"]
        assert new_obj.an_optional_string == "lime"
        assert new_obj.a_required_datetime == datetime(1789, 7, 14)

        expected = {
            "vocab:aRequiredListOfStrings": "coconut",  # note no square brackets, single item in list. Is this desired?
            "vocab:anOptionalString": "lime"
        }
        assert new_obj._updated_data(new_obj._build_data(client=None, all_fields=True)) == expected



    def test_exists__it_does_not_exist(self):
        pass
