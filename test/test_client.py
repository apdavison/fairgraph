

from .utils_v3 import kg_client, skip_if_no_connection


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
