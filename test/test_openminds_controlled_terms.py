import fairgraph.openminds.controlled_terms as terms
from test.utils import mock_client, kg_client, skip_if_no_connection, skip_if_using_production_server


def test_initialization():
    for cls in terms.list_kg_classes():
        obj = cls(name="foo")


@skip_if_no_connection
def test_exists(kg_client):
    obj = terms.AgeCategory.adult
    assert obj.space == "controlled"
    assert obj.exists(kg_client)
