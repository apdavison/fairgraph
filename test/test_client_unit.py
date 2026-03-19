# encoding: utf-8
"""
Unit tests for fairgraph.client module (no real KG connection needed).
"""

import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from uuid import UUID

from fairgraph.client import KGClient
from fairgraph.errors import AuthenticationError, AuthorizationError, ResourceExistsError


@pytest.fixture
def bare_client():
    """
    Build a KGClient without calling __init__ (which requires kg-core connection).
    Manually set the attributes that the methods under test depend on.
    """
    client = KGClient.__new__(KGClient)
    client._kg_client = MagicMock()
    client._kg_client_builder = MagicMock()
    client.__kg_admin_client = None
    client.host = "core.kg-ppd.ebrains.eu"
    client._user_info = None
    client.cache = {}
    client._query_cache = {}
    client.accepted_terms_of_use = False
    client._migrated = True  # avoid the migration check in _check_response
    return client


def _make_error_response(code, message="error"):
    """Create a mock response with an error."""
    response = MagicMock()
    response.error = MagicMock()
    response.error.code = code
    response.error.message = message
    response.total = 0
    response.data = []
    return response


def _make_ok_response(data=None):
    """Create a mock response without an error."""
    response = MagicMock()
    response.error = None
    response.data = data or []
    response.total = len(data) if data else 0
    response.size = len(data) if data else 0
    return response


class TestCheckResponse:

    def test_403_raises_authorization_error(self, bare_client):
        response = _make_error_response(403)
        with pytest.raises(AuthorizationError):
            bare_client._check_response(response)

    def test_401_raises_authentication_error(self, bare_client):
        response = _make_error_response(401)
        with pytest.raises(AuthenticationError):
            bare_client._check_response(response)

    def test_404_with_ignore_not_found_returns_response(self, bare_client):
        response = _make_error_response(404)
        result = bare_client._check_response(response, ignore_not_found=True)
        assert result is response

    def test_404_without_ignore_raises(self, bare_client):
        response = _make_error_response(404)
        with pytest.raises(Exception):
            bare_client._check_response(response, ignore_not_found=False)

    def test_409_raises_resource_exists(self, bare_client):
        response = _make_error_response(409)
        with pytest.raises(ResourceExistsError):
            bare_client._check_response(response)

    def test_500_raises_generic_exception(self, bare_client):
        response = _make_error_response(500)
        with pytest.raises(Exception):
            bare_client._check_response(response)

    def test_no_error_returns_response(self, bare_client):
        response = _make_ok_response(data=[{"@id": "https://example.com/1"}])
        result = bare_client._check_response(response)
        assert result is response

    def test_multiple_results_with_expected_instance_id_causes_error(self, bare_client):
        response = MagicMock()
        response.error = None
        response.total = 5
        response.data = [{"@id": "a"}, {"@id": "b"}]
        response.size = 2
        # When an instance_id is specified but multiple results come back,
        # a synthetic 404 error should be injected
        bare_client._check_response(response, expected_instance_id="some-uuid", ignore_not_found=True)
        # After the call, response.error should have been set and data cleared
        assert response.data == []


class TestInstanceFromFullUri:

    def test_uses_cache_when_available(self, bare_client):
        uri = "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"
        cached_data = {"@id": uri, "@type": "SomeType"}
        bare_client.cache[uri] = cached_data

        result = bare_client.instance_from_full_uri(uri)

        assert result is cached_data
        bare_client._kg_client.instances.get_by_id.assert_not_called()


class TestUriUuidConversion:

    def test_uri_from_uuid(self, bare_client):
        namespace = "https://kg.ebrains.eu/api/instances/"
        bare_client._kg_client.instances._kg_config.id_namespace = namespace
        uuid = "00000000-0000-0000-0000-000000001234"
        result = bare_client.uri_from_uuid(uuid)
        assert result == f"{namespace}{uuid}"

    def test_uuid_from_uri(self, bare_client):
        namespace = "https://kg.ebrains.eu/api/instances/"
        bare_client._kg_client.instances._kg_config.id_namespace = namespace
        uuid_str = "00000000-0000-0000-0000-000000001234"
        uri = f"{namespace}{uuid_str}"
        result = bare_client.uuid_from_uri(uri)
        assert str(result) == uuid_str


class TestUserInfo:

    def test_user_info_caches_result(self, bare_client):
        user_data = {"name": "Test User"}
        mock_response = MagicMock()
        mock_response.data = user_data
        mock_response.error = None
        bare_client._kg_client.users.my_info.return_value = mock_response

        result1 = bare_client.user_info()
        result2 = bare_client.user_info()

        assert result1 == user_data
        assert result2 == user_data
        bare_client._kg_client.users.my_info.assert_called_once()

    def test_user_info_401_raises(self, bare_client):
        mock_response = MagicMock()
        mock_response.data = None
        mock_response.error = MagicMock()
        mock_response.error.code = 401
        bare_client._kg_client.users.my_info.return_value = mock_response

        with pytest.raises(AuthenticationError):
            bare_client.user_info()
