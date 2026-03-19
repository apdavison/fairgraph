# encoding: utf-8
"""
Tests for fairgraph.collection module.
"""

import os
import pytest
from unittest.mock import MagicMock, patch, mock_open, call
from fairgraph.collection import Collection
from fairgraph.errors import AuthenticationError
from fairgraph.utility import ActivityLog


def _make_mock_node_class(name="MockNode"):
    """Create a MockNode class with the given name."""

    class MockNode:
        def __init__(self, node_id):
            self.id = node_id

        def save(self, client, space=None, recursive=False, ignore_duplicates=False, activity_log=None):
            pass

    MockNode.__name__ = name
    MockNode.__qualname__ = name
    return MockNode


MockNode = _make_mock_node_class()


def _make_collection_with_nodes(nodes):
    """Create a Collection with mock sorted nodes (bypassing openMINDS internals)."""
    collection = Collection.__new__(Collection)
    collection._nodes = {}
    for node in nodes:
        collection._nodes[node.id] = node
    # Patch sort_nodes_for_upload to return our nodes directly
    collection.sort_nodes_for_upload = lambda: nodes
    return collection


class TestCollectionLoad:

    def test_load_imports_fairgraph_openminds(self, tmp_path):
        collection = _make_collection_with_nodes([])
        # Patch import_module and super().load() to avoid actual file I/O
        with patch("fairgraph.collection.import_module") as mock_import:
            with patch.object(collection, "sort_nodes_for_upload", return_value=[]):
                # Call load - it should import fairgraph.openminds then call super().load
                with patch("openminds.Collection.load") as mock_super_load:
                    collection.load(str(tmp_path))
                    mock_import.assert_called_once_with("fairgraph.openminds")
                    mock_super_load.assert_called_once()


class TestCollectionUpload:

    def test_upload_returns_activity_log(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        result = collection.upload(mock_client, default_space="myspace")

        assert isinstance(result, ActivityLog)

    def test_upload_saves_normal_nodes(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        with patch.object(node, "save") as mock_save:
            collection.upload(mock_client, default_space="myspace")
            mock_save.assert_called_once()

    def test_upload_skips_openminds_instances(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # This node's id starts with the openMINDS prefix and should be skipped
        node = MockNode("https://openminds.om-i.org/instances/ageCategory/juvenile")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        with patch.object(node, "save") as mock_save:
            collection.upload(mock_client, default_space="myspace")
            mock_save.assert_not_called()

    def test_upload_reads_skip_log(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node1 = MockNode("https://example.com/instances/001")
        node2 = MockNode("https://example.com/instances/002")
        collection = _make_collection_with_nodes([node1, node2])

        # Write node1's id to the skip log
        skip_log = tmp_path / ".kg_upload_log.txt"
        skip_log.write_text(node1.id + "\n")

        mock_client = MagicMock()
        with patch.object(node1, "save") as mock_save1:
            with patch.object(node2, "save") as mock_save2:
                collection.upload(mock_client, default_space="myspace")
                mock_save1.assert_not_called()  # should be skipped
                mock_save2.assert_called_once()  # should be saved

    def test_upload_writes_to_skip_log(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        collection.upload(mock_client, default_space="myspace")

        skip_log = tmp_path / ".kg_upload_log.txt"
        assert skip_log.exists()
        content = skip_log.read_text()
        assert node.id in content

    def test_upload_stops_on_authentication_error(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node1 = MockNode("https://example.com/instances/001")
        node2 = MockNode("https://example.com/instances/002")
        collection = _make_collection_with_nodes([node1, node2])
        mock_client = MagicMock()

        with patch.object(node1, "save", side_effect=AuthenticationError("expired")):
            with patch.object(node2, "save") as mock_save2:
                collection.upload(mock_client, default_space="myspace")
                mock_save2.assert_not_called()

    def test_upload_retries_on_500_error(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        call_count = [0]

        def flaky_save(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                raise Exception("500 Internal Server Error")

        with patch.object(node, "save", side_effect=flaky_save):
            with patch("fairgraph.collection.sleep") as mock_sleep:
                collection.upload(mock_client, default_space="myspace")
                mock_sleep.assert_called_once_with(5)

        assert call_count[0] == 2  # called twice: once failing, once succeeding

    def test_upload_reraises_non_500_exception(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        with patch.object(node, "save", side_effect=Exception("404 Not Found")):
            with pytest.raises(Exception, match="404"):
                collection.upload(mock_client, default_space="myspace")

    def test_upload_uses_space_map(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        ClassA = _make_mock_node_class("ClassA")
        ClassB = _make_mock_node_class("ClassB")
        node_a = ClassA("https://example.com/instances/a")
        node_b = ClassB("https://example.com/instances/b")
        collection = _make_collection_with_nodes([node_a, node_b])
        mock_client = MagicMock()
        space_map = {ClassA: "space-alpha", ClassB: "space-beta"}

        saved_spaces = []

        def capture_save(*args, space=None, **kwargs):
            saved_spaces.append(space)

        with patch.object(node_a, "save", side_effect=capture_save):
            with patch.object(node_b, "save", side_effect=capture_save):
                collection.upload(mock_client, space_map=space_map)

        assert "space-alpha" in saved_spaces
        assert "space-beta" in saved_spaces

    def test_upload_verbosity_2_prints(self, tmp_path, monkeypatch, capsys):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        collection.upload(mock_client, default_space="myspace", verbosity=2)

        captured = capsys.readouterr()
        assert "%" in captured.out  # progress percentage

    def test_upload_verbosity_1_tqdm_missing_warns(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        with patch("fairgraph.collection.import_module", side_effect=ImportError("no tqdm")):
            with pytest.warns(UserWarning, match="tqdm"):
                collection.upload(mock_client, default_space="myspace", verbosity=1)

    def test_upload_verbosity_1_tqdm_present(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        node = MockNode("https://example.com/instances/001")
        collection = _make_collection_with_nodes([node])
        mock_client = MagicMock()

        mock_tqdm_module = MagicMock()
        mock_tqdm_module.tqdm.side_effect = lambda x: x  # return nodes unchanged

        with patch("fairgraph.collection.import_module", return_value=mock_tqdm_module):
            collection.upload(mock_client, default_space="myspace", verbosity=1)

        mock_tqdm_module.tqdm.assert_called_once()
