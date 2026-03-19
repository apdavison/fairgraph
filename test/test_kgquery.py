# encoding: utf-8
"""
Tests for fairgraph.kgquery module.
"""

import pytest
from unittest.mock import MagicMock, patch
from fairgraph.kgquery import KGQuery
from fairgraph.caching import object_cache

from test.test_base import MockKGObject, MockKGObject2


@pytest.fixture(autouse=True)
def clear_object_cache():
    object_cache.clear()
    yield
    object_cache.clear()


def _make_instance_data(n):
    return {
        "@id": f"https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-{n:012d}",
        "@type": MockKGObject.type_,
        "https://openminds.ebrains.eu/vocab/aRequiredString": f"obj{n}",
        "https://openminds.ebrains.eu/vocab/aRequiredListOfStrings": ["x"],
        "https://openminds.ebrains.eu/vocab/aRequiredDateTime": "2000-01-01T00:00:00",
        "https://openminds.ebrains.eu/vocab/aRequiredListOfDateTimes": ["2000-01-01T00:00:00"],
        "https://openminds.ebrains.eu/vocab/aRequiredLinkedObject": {
            "@id": f"https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-{n+100:012d}"
        },
        "https://openminds.ebrains.eu/vocab/aRequiredListOfLinkedObjects": [
            {"@id": f"https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-{n+100:012d}"}
        ],
        "https://openminds.ebrains.eu/vocab/aRequiredEmbeddedObject": {
            "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
            "https://openminds.ebrains.eu/vocab/aNumber": float(n),
        },
        "https://openminds.ebrains.eu/vocab/aRequiredListOfEmbeddedObjects": [
            {
                "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
                "https://openminds.ebrains.eu/vocab/aNumber": float(n),
            }
        ],
    }


class TestKGQueryResolve:

    def _make_query_and_client(self, num_results):
        query = KGQuery([MockKGObject], {"a_required_string": "foo"})
        mock_client = MagicMock()
        instance_data_list = [_make_instance_data(i) for i in range(1, num_results + 1)]
        mock_response = MagicMock()
        mock_response.data = instance_data_list
        mock_query = MagicMock()

        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            mock_client.query.return_value = mock_response
            return query, mock_client

    def test_resolve_returns_single_object_for_one_result(self):
        query, mock_client = self._make_query_and_client(1)
        mock_query = MagicMock()
        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            result = query.resolve(mock_client)
        assert isinstance(result, MockKGObject)

    def test_resolve_returns_list_for_multiple_results(self):
        query, mock_client = self._make_query_and_client(2)
        mock_query = MagicMock()
        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            result = query.resolve(mock_client)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_resolve_returns_empty_list_for_no_results(self):
        query = KGQuery([MockKGObject], {"a_required_string": "foo"})
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = []
        mock_query = MagicMock()
        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            mock_client.query.return_value = mock_response
            result = query.resolve(mock_client)
        assert result == []

    def test_resolve_populates_object_cache(self):
        query, mock_client = self._make_query_and_client(1)
        mock_query = MagicMock()
        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            result = query.resolve(mock_client)
        uri = result.id
        assert uri in object_cache

    def test_resolve_with_follow_links_calls_obj_resolve(self):
        query, mock_client = self._make_query_and_client(1)
        mock_query = MagicMock()
        with patch.object(MockKGObject, "generate_query", return_value=mock_query):
            with patch.object(MockKGObject, "resolve") as mock_resolve:
                query.resolve(mock_client, follow_links={"some_prop": {}})
                mock_resolve.assert_called_once()


class TestKGQueryCount:

    def test_count_delegates_to_cls_count(self):
        query = KGQuery([MockKGObject], {"a_required_string": "foo"})
        mock_client = MagicMock()
        with patch.object(MockKGObject, "count", return_value=5) as mock_count:
            result = query.count(mock_client)
        assert result == 5
        mock_count.assert_called_once()

    def test_count_multi_class_sums(self):
        query = KGQuery([MockKGObject, MockKGObject2], {})
        mock_client = MagicMock()
        with patch.object(MockKGObject, "count", return_value=3):
            with patch.object(MockKGObject2, "count", return_value=7):
                result = query.count(mock_client)
        assert result == 10


class TestKGQueryRepr:

    def test_repr_does_not_crash(self):
        query = KGQuery([MockKGObject], {"a_required_string": "foo"})
        r = repr(query)
        assert "KGQuery" in r
        assert "MockKGObject" in r
