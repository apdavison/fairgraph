

from .utils import kg_client, skip_if_no_connection


@skip_if_no_connection
def test_spaces(kg_client):
    result = kg_client.spaces()
    assert isinstance(result, list)
    for space in result:
        assert isinstance(space.name, str)
        assert not space.permissions


@skip_if_no_connection
def test_spaces_with_permissions(kg_client):
    result = kg_client.spaces(permissions=['RELEASE'])
    assert isinstance(result, list)
    for space in result:
        assert "RELEASE" in space.permissions


@skip_if_no_connection
def test_spaces_with_permissions_True(kg_client):
    result = kg_client.spaces(permissions=True)
    assert isinstance(result, list)
    for space in result:
        assert space.permissions


@skip_if_no_connection
def test_spaces_names_only(kg_client):
    result = kg_client.spaces(names_only=True)
    assert isinstance(result, list)
    assert all(isinstance(space, str) for space in result)


@skip_if_no_connection
def test_query_filter_by_space(kg_client):
    results = kg_client.query(
        filter=None,
        query_id="https://kg.ebrains.eu/api/instances/16b28f98-a8e0-488a-a130-59d53f7c9d00",
        instance_id=None,
        from_index=0,
        size=1000,
        scope="in progress",
        id_key="uri",
        space="model"
    )
    spaces = set(result["project_id"] for result in results.data)
    if len(spaces) > 0:  # not a great test, needs to be improved
        assert len(spaces) == 1
        assert "model" == list(spaces)[0]
