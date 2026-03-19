# encoding: utf-8
"""
Tests for fairgraph.kgproxy module.
"""

import pytest
from unittest.mock import MagicMock, patch
from fairgraph.kgproxy import KGProxy
from fairgraph.caching import object_cache
from fairgraph.errors import ResolutionFailure

from test.test_base import MockKGObject, MockKGObject2

URI = "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234"


@pytest.fixture(autouse=True)
def clear_object_cache():
    """Clear the object cache before each test."""
    object_cache.clear()
    yield
    object_cache.clear()


class TestKGProxyResolve:

    def test_resolve_uses_cache(self):
        proxy = KGProxy(MockKGObject, URI)
        cached_obj = MagicMock()
        object_cache[URI] = cached_obj
        mock_client = MagicMock()

        result = proxy.resolve(mock_client)

        assert result is cached_obj
        mock_client.instance_from_full_uri.assert_not_called()

    def test_resolve_cache_miss_success(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_obj = MagicMock()
        mock_client = MagicMock()

        with patch.object(MockKGObject, "from_uri", return_value=mock_obj):
            result = proxy.resolve(mock_client, use_cache=False)

        assert result is mock_obj
        assert object_cache[URI] is mock_obj

    def test_resolve_cache_miss_all_classes_fail(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_client = MagicMock()

        with patch.object(MockKGObject, "from_uri", side_effect=TypeError("wrong type")):
            with pytest.raises(ResolutionFailure):
                proxy.resolve(mock_client, use_cache=False)

    def test_resolve_with_follow_links(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_obj = MagicMock()
        mock_resolved = MagicMock()
        mock_obj.resolve.return_value = mock_resolved
        mock_client = MagicMock()

        with patch.object(MockKGObject, "from_uri", return_value=mock_obj):
            result = proxy.resolve(mock_client, use_cache=False, follow_links={"some_prop": {}})

        mock_obj.resolve.assert_called_once()
        assert result is mock_resolved

    def test_resolve_uses_preferred_release_status(self):
        proxy = KGProxy(MockKGObject, URI, preferred_release_status="in progress")
        mock_obj = MagicMock()
        mock_client = MagicMock()

        with patch.object(MockKGObject, "from_uri", return_value=mock_obj) as mock_from_uri:
            proxy.resolve(mock_client, use_cache=False)
            mock_from_uri.assert_called_once()
            call_kwargs = mock_from_uri.call_args.kwargs
            assert call_kwargs.get("release_status") == "in progress"

    def test_resolve_explicit_release_status_overrides(self):
        proxy = KGProxy(MockKGObject, URI, preferred_release_status="released")
        mock_obj = MagicMock()
        mock_client = MagicMock()

        with patch.object(MockKGObject, "from_uri", return_value=mock_obj) as mock_from_uri:
            proxy.resolve(mock_client, use_cache=False, release_status="in progress")
            mock_from_uri.assert_called_once()
            call_kwargs = mock_from_uri.call_args.kwargs
            assert call_kwargs.get("release_status") == "in progress"


class TestKGProxyDelete:

    def test_delete_success(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_obj = MagicMock()
        mock_client = MagicMock()

        with patch.object(proxy, "resolve", return_value=mock_obj):
            proxy.delete(mock_client)

        mock_obj.delete.assert_called_once_with(mock_client, ignore_not_found=True)

    def test_delete_resolution_failure_ignore(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_client = MagicMock()

        with patch.object(proxy, "resolve", side_effect=ResolutionFailure("not found")):
            proxy.delete(mock_client, ignore_not_found=True)  # should not raise

    def test_delete_resolution_failure_raise(self):
        proxy = KGProxy(MockKGObject, URI)
        mock_client = MagicMock()

        with patch.object(proxy, "resolve", side_effect=ResolutionFailure("not found")):
            with pytest.raises(ResolutionFailure):
                proxy.delete(mock_client, ignore_not_found=False)


class TestKGProxyClsProperty:

    def test_cls_single_class(self):
        proxy = KGProxy(MockKGObject, URI)
        assert proxy.cls is MockKGObject

    def test_cls_multiple_classes_raises(self):
        proxy = KGProxy([MockKGObject, MockKGObject2], URI)
        with pytest.raises(AttributeError):
            _ = proxy.cls


class TestKGProxyTypeProperty:

    def test_type_with_class_missing_type_(self):
        # A class without type_ attribute should cause AttributeError to be re-raised
        class NoTypeClass:
            pass

        proxy = KGProxy.__new__(KGProxy)
        proxy.classes = [NoTypeClass]
        proxy.id = URI

        with pytest.raises(AttributeError):
            _ = proxy.type
