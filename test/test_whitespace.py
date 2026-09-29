"""
Tests for `fairgraph.utility.whitespace`, and for its use when saving objects.

Only property values are normalized, when saving. Queries (existence queries and filters) are used as given.
"""

import pytest
from openminds import IRI

from fairgraph.kgproxy import KGProxy
import fairgraph.openminds.core as omcore
import fairgraph.openminds.v4.core as omcore4
import fairgraph.openminds.v5.core as omcore5
from fairgraph.utility import ActivityLog
from fairgraph.utility.whitespace import normalize_property_value, normalize_whitespace

from .utils import MockKGResponse, clear_caches, mock_client

BILBO_ID = "https://kg.ebrains.eu/api/instances/12345678-90ab-cdef-0123-4567890abcde"


def _seed_bilbo(mock_client, given_name="Bilbo", family_name="Baggins"):
    mock_client.instances[BILBO_ID] = {
        "@id": BILBO_ID,
        "@type": ["https://openminds.om-i.org/types/Person"],
        "https://core.kg.ebrains.eu/vocab/meta/space": "common",
        "https://openminds.om-i.org/props/givenName": given_name,
        "https://openminds.om-i.org/props/familyName": family_name,
    }


class TestNormalizeWhitespace:
    prop = omcore.Person.get_property("given_name")

    def test_strips_both_ends(self):
        assert normalize_whitespace("  Bilbo\t\n", self.prop) == "Bilbo"

    def test_leaves_internal_whitespace_alone(self):
        assert normalize_whitespace(" Bilbo  Baggins\nof Bag End ", self.prop) == "Bilbo  Baggins\nof Bag End"

    def test_all_whitespace_becomes_empty(self):
        assert normalize_whitespace(" \t ", self.prop) == ""


class TestNormalizePropertyValue:
    single = omcore.Person.get_property("given_name")
    multiple = omcore.Person.get_property("alternate_names")
    not_text = omcore.Person.get_property("contact_information")

    def test_single_value(self):
        assert normalize_property_value(self.single, " Bilbo ") == "Bilbo"

    def test_list(self):
        assert normalize_property_value(self.multiple, [" Barrel-rider ", "Ringbearer"]) == [
            "Barrel-rider",
            "Ringbearer",
        ]

    def test_tuple_stays_a_tuple(self):
        assert normalize_property_value(self.multiple, (" a ", "b ")) == ("a", "b")

    def test_none(self):
        assert normalize_property_value(self.single, None) is None

    def test_non_str_items_pass_through(self):
        proxy = KGProxy(omcore.ContactInformation, "https://kg.ebrains.eu/api/instances/abc")
        assert normalize_property_value(self.multiple, [" a ", proxy]) == ["a", proxy]

    def test_property_that_does_not_take_text_is_untouched(self):
        proxy = KGProxy(omcore.ContactInformation, "https://kg.ebrains.eu/api/instances/abc")
        assert normalize_property_value(self.not_text, proxy) is proxy

    def test_iri_is_untouched(self):
        prop = omcore.File.get_property("iri")
        iri = IRI("http://example.org/file ")
        assert normalize_property_value(prop, iri) is iri

    def test_all_whitespace_becomes_empty(self):
        assert normalize_property_value(self.single, "  ") == ""


@pytest.mark.parametrize("module", [omcore4, omcore5], ids=["v4", "v5"])
def test_text_properties_have_the_formatting_information_that_future_normalization_relies_on(module):
    """
    A later version of `normalize_whitespace` is intended to treat single-line and multi-line
    text differently, using `Property.formatting` and `Property.multiline`.
    """
    n_checked = 0
    for name in dir(module):
        cls = getattr(module, name)
        if not (isinstance(cls, type) and hasattr(cls, "properties")):
            continue
        for prop in cls.properties:
            if str in prop.types:
                n_checked += 1
                assert prop.formatting in ("text/plain", "text/markdown"), f"{name}.{prop.name}"
                assert isinstance(prop.multiline, bool), f"{name}.{prop.name}"
    assert n_checked > 0


class TestNormalizeText:
    def test_strips_text_properties_in_place(self):
        person = omcore.Person(given_name=" Bilbo ", family_name="Baggins\n", alternate_names=[" Barrel-rider "])
        person._normalize_text()
        assert person.given_name == "Bilbo"
        assert person.family_name == "Baggins"
        assert person.alternate_names == ["Barrel-rider"]

    def test_embedded_nodes_are_normalized(self):
        file = omcore.File(
            name="foo.txt",
            iri=IRI("http://example.org/foo.txt"),
            hash=omcore.Hash(algorithm=" SHA-1 ", digest=" abc "),
        )
        file._normalize_text()
        assert file.hash.algorithm == "SHA-1"
        assert file.hash.digest == "abc"

    def test_linked_objects_are_not_normalized(self):
        child = omcore.Person(given_name=" Frodo ", family_name="Baggins")
        dataset_version = omcore.DatasetVersion(custodians=[child], version_identifier=" v1 ")
        dataset_version._normalize_text()
        assert dataset_version.version_identifier == "v1"
        assert child.given_name == " Frodo "


class TestSave:
    def test_new_object_is_saved_stripped(self, mock_client, clear_caches):
        person = omcore.Person(given_name=" Bilbo ", family_name="Baggins ")
        person.save(mock_client, space="common")
        (data,) = mock_client.instances.values()
        assert data["https://openminds.om-i.org/props/givenName"] == "Bilbo"
        assert data["https://openminds.om-i.org/props/familyName"] == "Baggins"
        # the local object now matches what is in the KG
        assert person.given_name == "Bilbo"
        assert person.family_name == "Baggins"

    def test_synonym_lists_are_saved_stripped(self, mock_client, clear_caches):
        person = omcore.Person(given_name="Bilbo", family_name="Baggins", alternate_names=[" Barrel-rider "])
        person.save(mock_client, space="common")
        (data,) = mock_client.instances.values()
        assert data["https://openminds.om-i.org/props/alternateName"] == ["Barrel-rider"]

    def test_untrimmed_new_object_finds_stored_object_and_creates_no_duplicate(self, mock_client, clear_caches):
        _seed_bilbo(mock_client)
        person = omcore.Person(given_name="Bilbo ", family_name=" Baggins")
        log = ActivityLog()
        person.save(mock_client, space="common", activity_log=log)
        assert person.id == BILBO_ID
        assert len(mock_client.instances) == 1
        assert [entry.type for entry in log.entries] == ["no-op"]
        assert mock_client.updates == []

    def test_stored_untrimmed_value_is_not_matched_exactly(self, mock_client, clear_caches):
        _seed_bilbo(mock_client, given_name="Bilbo ")
        # the value is stripped before saving, and an exact match does not ignore whitespace in the KG
        person = omcore.Person(given_name="Bilbo", family_name="Baggins")
        person.save(mock_client, space="common")
        assert person.id != BILBO_ID
        assert len(mock_client.instances) == 2

    def test_stored_untrimmed_value_is_matched_with_existence_match_contains(self, mock_client, clear_caches):
        _seed_bilbo(mock_client, given_name="Bilbo ")
        person = omcore.Person(given_name=" Bilbo", family_name="Baggins")
        person.save(mock_client, space="common", existence_match="contains")
        assert person.id == BILBO_ID
        assert len(mock_client.instances) == 1

    def test_loaded_object_with_untrimmed_stored_value_is_repaired(self, mock_client, clear_caches):
        _seed_bilbo(mock_client, given_name="Bilbo ")
        person = omcore.Person.from_id(BILBO_ID, mock_client)
        assert person.given_name == "Bilbo "  # loading does not strip
        assert person.remote_data["https://openminds.om-i.org/props/givenName"] == "Bilbo "
        log = ActivityLog()
        person.save(mock_client, space="common", activity_log=log)
        assert [entry.type for entry in log.entries] == ["update"]
        ((instance_id, payload),) = mock_client.updates
        assert instance_id == BILBO_ID.split("/")[-1]
        assert payload["https://openminds.om-i.org/props/givenName"] == "Bilbo"

    def test_linked_child_is_left_alone_when_not_recursive(self, mock_client, clear_caches):
        child = omcore.Person(id=BILBO_ID, given_name=" Frodo ", family_name="Baggins")
        parent = omcore.DatasetVersion(custodians=[child], version_identifier=" v1 ")
        parent.save(mock_client, space="dataset", recursive=False)
        assert parent.version_identifier == "v1"
        assert child.given_name == " Frodo "


class TestExists:
    def test_existence_query_is_not_stripped(self):
        person = omcore.Person(given_name="Bilbo ", family_name=" Baggins")
        query = person._build_existence_query()
        assert query == {"given_name": "Bilbo ", "family_name": " Baggins"}

    def test_exists_does_not_strip_and_does_not_change_the_object(self, mock_client, clear_caches):
        _seed_bilbo(mock_client)
        person = omcore.Person(given_name="Bilbo ", family_name=" Baggins")
        assert not person.exists(mock_client)
        assert person.given_name == "Bilbo "
        assert person.family_name == " Baggins"


def test_loading_does_not_strip_remote_data():
    data = {
        "@id": BILBO_ID,
        "@type": ["https://openminds.om-i.org/types/Person"],
        "https://openminds.om-i.org/props/givenName": "Bilbo ",
        "https://openminds.om-i.org/props/familyName": " Baggins",
    }
    person = omcore.Person.from_jsonld(data)
    assert person.given_name == "Bilbo "
    assert person.family_name == " Baggins"


def test_filter_values_are_not_stripped(mock_client):
    queries = []

    def record_query(query, **kwargs):
        queries.append(query)
        return MockKGResponse([])

    mock_client.query = record_query
    omcore.Person.list(mock_client, family_name="Baggins ")
    filter_values = [prop["filter"]["value"] for prop in queries[0]["structure"] if "value" in prop.get("filter", {})]
    assert filter_values == ["Baggins "]
