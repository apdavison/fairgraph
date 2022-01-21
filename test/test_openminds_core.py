
import json
import fairgraph.openminds.core as omcore
import pytest

from test.utils import generate_random_object


class MockKGClient:
    _private_space = "myspace_1234"
    pass


@pytest.fixture
def client():
    return MockKGClient()


def test_query_generation(client):
    for cls in omcore.list_kg_classes():
        generated = cls.generate_query("simple", "collab-foobar", client)
        with open(f"test/test_data/queries/openminds/core/{cls.__name__.lower()}_simple_query.json", "r") as fp:
            expected = json.load(fp)
        assert generated == expected
