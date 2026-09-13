import pytest

import fairgraph.openminds.controlled_terms as terms
import fairgraph.openminds.core as omcore
from test.utils import mock_client, kg_client, skip_if_no_connection, skip_if_using_production_server


def test_initialization():
    for cls in terms.list_kg_classes():
        obj = cls(name="foo")


@skip_if_no_connection
def test_exists(kg_client):
    obj = terms.AgeCategory.adult
    assert obj.space == "controlled"
    assert obj.exists(kg_client)


def test_by_name_without_client_searches_the_instance_library():
    mouse = terms.Species.by_name("Mus musculus")
    assert mouse.id == "https://openminds.om-i.org/instances/species/musMusculus"
    assert terms.Species.by_name("house mouse") == mouse  # synonyms are searched too


def test_by_name_without_client_returns_none_when_nothing_matches():
    # https://github.com/HumanBrainProject/fairgraph/issues/130
    assert terms.Species.by_name("definitely not a species") is None
    assert terms.Species.by_name("mus musculus") is None  # the search is case-sensitive by default


def test_by_name_without_client_honours_case_sensitive():
    assert terms.Species.by_name("mus musculus", case_sensitive=False).name == "Mus musculus"


def test_by_name_without_client_honours_match():
    assert terms.Species.by_name("musculus", match="contains").name == "Mus musculus"
    assert terms.Species.by_name("the species Mus musculus", match="within").name == "Mus musculus"


def test_by_name_without_client_returns_deduplicated_list():
    # "Mus musculus" is indexed under both its name and its synonyms
    found = terms.Species.by_name("Mus musculus", all=True)
    assert [obj.id for obj in found] == ["https://openminds.om-i.org/instances/species/musMusculus"]


def test_by_name_rejects_an_unknown_match_type():
    with pytest.raises(ValueError):
        terms.Species.by_name("Mus musculus", match="approximately")


def test_by_name_without_instance_library_returns_none():
    # Person has no instance library, so there is nothing to search without a client
    assert omcore.Person.by_name("Smith") is None


def test_by_name_with_client(mock_client):
    assert terms.Species.by_name("Mus musculus", mock_client).name == "Mus musculus"
    # the Nazgûl's fell beasts have never been formally described
    assert terms.Species.by_name("Nazgulia membranacea", mock_client) is None


def test_by_name_with_client_requires_a_name_like_property(mock_client):
    with pytest.raises(AttributeError):
        omcore.DOI.by_name("10.25493/ANYTHING", mock_client)
