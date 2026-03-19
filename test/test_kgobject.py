# encoding: utf-8
"""
Additional tests for fairgraph.kgobject module, focusing on uncovered branches.
"""

import pytest
from datetime import datetime
from unittest.mock import MagicMock, patch, call
from fairgraph.kgobject import KGObject
from fairgraph.errors import AuthorizationError, ResourceExistsError, CannotBuildExistenceQuery
from fairgraph.caching import object_cache, save_cache
from fairgraph.utility import ActivityLog

from test.test_base import MockKGObject, MockKGObject2, MockEmbeddedObject, ID_NAMESPACE


@pytest.fixture(autouse=True)
def clear_caches():
    object_cache.clear()
    save_cache.clear()
    yield
    object_cache.clear()
    save_cache.clear()


def _make_simple_obj(id=None, a_required_string="apple"):
    """Construct a minimal MockKGObject2 (only has 'a' property)."""
    return MockKGObject2(a=1, id=id)


def _make_full_obj(id=None):
    data = {
        "https://openminds.ebrains.eu/vocab/aRequiredDateTime": "1789-07-14T00:00:00",
        "https://openminds.ebrains.eu/vocab/aRequiredEmbeddedObject": {
            "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
            "https://openminds.ebrains.eu/vocab/aNumber": -1.0,
        },
        "https://openminds.ebrains.eu/vocab/aRequiredLinkedObject": {
            "@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002",
        },
        "https://openminds.ebrains.eu/vocab/aRequiredListOfDateTimes": ["1900-01-01T00:00:00"],
        "https://openminds.ebrains.eu/vocab/aRequiredListOfEmbeddedObjects": [
            {
                "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
                "https://openminds.ebrains.eu/vocab/aNumber": 100.0,
            }
        ],
        "https://openminds.ebrains.eu/vocab/aRequiredListOfLinkedObjects": [
            {"@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000002"},
        ],
        "https://openminds.ebrains.eu/vocab/aRequiredListOfStrings": ["banana"],
        "https://openminds.ebrains.eu/vocab/aRequiredString": "apple",
    }
    return MockKGObject(
        id=id or f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000002",
        data=data,
        a_required_string="apple",
        a_required_list_of_strings=["banana"],
        a_required_datetime=datetime(1789, 7, 14),
        a_required_list_of_datetimes=[datetime(1900, 1, 1)],
        a_required_linked_object=MockKGObject2(
            a=1234,
            id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234",
        ),
        a_required_list_of_linked_objects=[
            MockKGObject2(a=2345, id="https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000002345"),
        ],
        a_required_embedded_object=MockEmbeddedObject(a_number=-1.0),
        a_required_list_of_embedded_objects=[MockEmbeddedObject(a_number=100.0)],
    )


class TestKGObjectFromUuid:

    def test_from_uuid_empty_raises(self):
        mock_client = MagicMock()
        with pytest.raises(ValueError, match="Empty UUID"):
            MockKGObject2.from_uuid("", mock_client)

    def test_from_uuid_invalid_raises(self):
        mock_client = MagicMock()
        with pytest.raises(ValueError):
            MockKGObject2.from_uuid("not-a-uuid", mock_client)

    def test_from_uuid_valid(self):
        mock_client = MagicMock()
        uuid = "00000000-0000-0000-0000-000000001234"
        uri = f"{ID_NAMESPACE}{uuid}"
        mock_client.uri_from_uuid.return_value = uri
        mock_client.instance_from_full_uri.return_value = {
            "@id": uri,
            "@type": MockKGObject2.type_,
            "https://openminds.ebrains.eu/vocab/A": 42,
        }
        result = MockKGObject2.from_uuid(uuid, mock_client)
        assert result is not None
        assert result.a == 42


class TestKGObjectFromId:

    def test_from_id_with_uri_calls_from_uri(self):
        mock_client = MagicMock()
        uri = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234"
        with patch.object(MockKGObject2, "from_uri", return_value=None) as mock_from_uri:
            MockKGObject2.from_id(uri, mock_client)
            mock_from_uri.assert_called_once()
            assert mock_from_uri.call_args.args[0] == uri

    def test_from_id_with_uuid_calls_from_uuid(self):
        mock_client = MagicMock()
        uuid = "00000000-0000-0000-0000-000000001234"
        with patch.object(MockKGObject2, "from_uuid", return_value=None) as mock_from_uuid:
            MockKGObject2.from_id(uuid, mock_client)
            mock_from_uuid.assert_called_once()
            assert mock_from_uuid.call_args.args[0] == uuid


class TestKGObjectList:

    def test_list_api_query(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = [
            {
                "@id": f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001",
                "@type": MockKGObject2.type_,
                "https://openminds.ebrains.eu/vocab/A": 10,
            }
        ]
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            results = MockKGObject2.list(mock_client, api="query")

        assert len(results) == 1
        assert isinstance(results[0], MockKGObject2)

    def test_list_api_core(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = [
            {
                "@id": f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001",
                "@type": MockKGObject2.type_,
                "https://openminds.ebrains.eu/vocab/A": 10,
            }
        ]
        mock_client.list.return_value = mock_response

        results = MockKGObject2.list(mock_client, api="core")

        assert len(results) == 1
        mock_client.list.assert_called_once()

    def test_list_api_auto_with_filters_uses_query(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = []
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            MockKGObject2.list(mock_client, api="auto", a=1)

        mock_client.query.assert_called_once()
        mock_client.list.assert_not_called()

    def test_list_api_auto_without_filters_uses_core(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = []
        mock_client.list.return_value = mock_response

        MockKGObject2.list(mock_client, api="auto")

        mock_client.list.assert_called_once()
        mock_client.query.assert_not_called()

    def test_list_invalid_api_raises(self):
        mock_client = MagicMock()
        with pytest.raises(ValueError, match="'api' must be"):
            MockKGObject2.list(mock_client, api="invalid")

    def test_list_core_with_filters_raises(self):
        mock_client = MagicMock()
        with pytest.raises(ValueError, match="Cannot use filters"):
            MockKGObject2.list(mock_client, api="core", a=1)


class TestKGObjectCount:

    def test_count_api_query(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.total = 42
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            result = MockKGObject2.count(mock_client, api="query")

        assert result == 42

    def test_count_api_core(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.total = 17
        mock_client.list.return_value = mock_response

        result = MockKGObject2.count(mock_client, api="core")

        assert result == 17

    def test_count_api_auto_without_filters_uses_core(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.total = 5
        mock_client.list.return_value = mock_response

        result = MockKGObject2.count(mock_client, api="auto")

        mock_client.list.assert_called_once()
        assert result == 5

    def test_count_api_auto_with_filters_uses_query(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.total = 3
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            result = MockKGObject2.count(mock_client, api="auto", a=1)

        mock_client.query.assert_called_once()
        assert result == 3


class TestKGObjectSave:

    def test_save_creates_new_instance(self):
        """When object has no id, save() should create a new instance."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=99)
        MockKGObject2.set_error_handling("error")
        assert obj.id is None

        mock_client = MagicMock()
        new_id = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000009999"
        mock_client.create_new_instance.return_value = {
            "@id": new_id,
            "@type": MockKGObject2.type_,
            "https://openminds.ebrains.eu/vocab/A": 99,
        }

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False)

        assert obj.id == new_id
        mock_client.create_new_instance.assert_called_once()

    def test_save_updates_when_modified(self):
        """When object exists and has modified data, save() should update."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.update_instance.return_value = {}

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={
                "https://openminds.ebrains.eu/vocab/aRequiredString": "changed"
            }):
                obj.save(mock_client, space="mock", recursive=False)

        mock_client.update_instance.assert_called_once()
        mock_client.create_new_instance.assert_not_called()

    def test_save_noop_when_unchanged(self):
        """When object exists and data is unchanged, save() should not update."""
        obj = _make_full_obj()
        mock_client = MagicMock()

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={}):
                obj.save(mock_client, space="mock", recursive=False)

        mock_client.update_instance.assert_not_called()
        mock_client.create_new_instance.assert_not_called()

    def test_save_replace_mode(self):
        """With replace=True, save() should call replace_instance."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.replace_instance.return_value = {}

        with patch.object(obj, "exists", return_value=True):
            obj.save(mock_client, space="mock", recursive=False, replace=True)

        mock_client.replace_instance.assert_called_once()
        mock_client.update_instance.assert_not_called()

    def test_save_allow_update_false(self):
        """With allow_update=False, save() should not update existing object."""
        obj = _make_full_obj()
        obj.allow_update = False
        mock_client = MagicMock()

        with patch.object(obj, "exists", return_value=True):
            obj.save(mock_client, space="mock", recursive=False)

        mock_client.update_instance.assert_not_called()
        mock_client.replace_instance.assert_not_called()

    def test_save_ignore_auth_error_on_create(self):
        """With ignore_auth_errors=True, AuthorizationError on create is swallowed."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_client.create_new_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False, ignore_auth_errors=True)

        # No exception raised

    def test_save_raise_auth_error_on_create(self):
        """With ignore_auth_errors=False (default), AuthorizationError on create propagates."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_client.create_new_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=False):
            with pytest.raises(AuthorizationError):
                obj.save(mock_client, space="mock", recursive=False, ignore_auth_errors=False)

    def test_save_with_no_space_uses_default_space(self):
        """When space=None is passed, save() uses self.__class__.default_space."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=99)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        new_id = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000009999"
        mock_client.create_new_instance.return_value = {
            "@id": new_id,
            "@type": MockKGObject2.type_,
        }

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space=None, recursive=False)

        # Should have used MockKGObject2.default_space = "mock"
        call_args = mock_client.create_new_instance.call_args
        assert call_args[0][1] == "mock"  # second positional arg is space

    def test_save_creates_with_uri_uses_uuid_as_instance_id(self):
        """When object has an http id, save() passes uuid as instance_id."""
        uri = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000009999"
        obj = MockKGObject2(a=42, id=uri)
        mock_client = MagicMock()
        mock_client.create_new_instance.return_value = {
            "@id": uri,
            "@type": MockKGObject2.type_,
        }

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False)

        call_kwargs = mock_client.create_new_instance.call_args[1]
        assert call_kwargs.get("instance_id") == "00000000-0000-0000-0000-000000009999"

    def test_save_noop_with_activity_log_records_entry(self):
        """No-op save (unchanged data) records entry_type='no-op' in activity_log."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        activity_log = MagicMock()

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={}):
                obj.save(mock_client, space="mock", recursive=False, activity_log=activity_log)

        # activity_log.update should have been called with entry_type="no-op"
        activity_log.update.assert_called()
        call_kwargs = activity_log.update.call_args[1]
        assert call_kwargs.get("entry_type") == "no-op"

    def test_save_allow_update_false_with_activity_log(self):
        """allow_update=False records no-op in activity log."""
        obj = _make_full_obj()
        obj.allow_update = False
        mock_client = MagicMock()
        activity_log = MagicMock()

        with patch.object(obj, "exists", return_value=True):
            obj.save(mock_client, space="mock", recursive=False, activity_log=activity_log)

        activity_log.update.assert_called()
        call_kwargs = activity_log.update.call_args[1]
        assert call_kwargs.get("entry_type") == "no-op"

    def test_save_with_activity_log(self):
        """save() passes updates to activity_log when provided."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=99)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        new_id = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000009999"
        mock_client.create_new_instance.return_value = {
            "@id": new_id,
            "@type": MockKGObject2.type_,
        }
        activity_log = MagicMock()

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False, activity_log=activity_log)

        activity_log.update.assert_called()


class TestKGObjectDelete:

    def test_delete_removes_from_cache(self):
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        object_cache[obj.id] = obj
        mock_client = MagicMock()
        mock_client.delete_instance.return_value = None

        obj.delete(mock_client)

        assert obj.id not in object_cache
        mock_client.delete_instance.assert_called_once()

    def test_delete_not_in_cache(self):
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        mock_client = MagicMock()
        mock_client.delete_instance.return_value = None

        obj.delete(mock_client)  # should not raise

        mock_client.delete_instance.assert_called_once()


class TestKGObjectShow:

    def test_show_without_tabulate_raises(self):
        obj = _make_simple_obj()
        with patch("fairgraph.kgobject.have_tabulate", False):
            with pytest.raises(Exception, match="tabulate"):
                obj.show()

    def test_show_with_tabulate(self, capsys):
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        with patch("fairgraph.kgobject.have_tabulate", True):
            obj.show()
        captured = capsys.readouterr()
        assert "id" in captured.out


class TestKGObjectSpaceProperty:

    def test_space_reads_from_raw_remote_data_myquery(self):
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        obj._raw_remote_data = {"https://schema.hbp.eu/myQuery/space": "special-space"}
        assert obj.space == "special-space"

    def test_space_reads_from_raw_remote_data_core(self):
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        obj._raw_remote_data = {"https://core.kg.ebrains.eu/vocab/meta/space": "core-space"}
        assert obj.space == "core-space"


class TestKGObjectListFollowLinks:

    def test_list_core_with_follow_links_raises(self):
        mock_client = MagicMock()
        with pytest.raises(NotImplementedError):
            MockKGObject2.list(mock_client, api="core", follow_links={"some": {}})


class TestKGObjectSaveAuthError:

    def test_save_update_ignore_auth_error(self):
        """With ignore_auth_errors=True, AuthorizationError on update is swallowed."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.update_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={
                "https://openminds.ebrains.eu/vocab/aRequiredString": "changed"
            }):
                obj.save(mock_client, space="mock", recursive=False, ignore_auth_errors=True)

        # No exception raised

    def test_save_replace_ignore_auth_error(self):
        """With ignore_auth_errors=True, AuthorizationError on replace is swallowed."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.replace_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=True):
            obj.save(mock_client, space="mock", recursive=False, replace=True, ignore_auth_errors=True)

        # No exception raised

    def test_save_resource_exists_error_ignored(self):
        """ResourceExistsError on create should be handled like AuthorizationError."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_client.create_new_instance.side_effect = ResourceExistsError("already exists")

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False, ignore_auth_errors=True)

        # No exception raised


class TestKGObjectByName:

    def test_by_name_with_client_no_results(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = []
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            result = MockKGObject2.by_name("nonexistent", mock_client)

        assert result is None

    def test_by_name_without_client_no_instances_attr(self):
        # MockKGObject2 has no `instances` attr, so without client returns None
        result = MockKGObject2.by_name("something", client=None)
        assert result is None

    def test_by_name_without_client_with_instances_equals(self):
        """Test the elif hasattr(cls, 'instances') branch — used by controlled terms."""
        from fairgraph.openminds.controlled_terms import CellType
        CellType._instance_lookup = None  # force rebuild
        result = CellType.by_name("astrocyte", client=None)
        assert result is not None

    def test_by_name_without_client_with_instances_contains(self):
        """Test the match='contains' sub-branch of the instances lookup."""
        from fairgraph.openminds.controlled_terms import CellType
        CellType._instance_lookup = None
        results = CellType.by_name("astrocyte", client=None, match="contains", all=True)
        assert results is not None

    def test_by_name_without_client_with_instances_invalid_match(self):
        """Test that an invalid match value raises ValueError."""
        from fairgraph.openminds.controlled_terms import CellType
        CellType._instance_lookup = None
        with pytest.raises(ValueError, match="'match' must be"):
            CellType.by_name("astrocyte", client=None, match="invalid")

    def test_by_name_multiple_results_returns_first(self):
        """When multiple objects have same name, warn and return first."""
        mock_client = MagicMock()
        uri1 = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001"
        uri2 = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000002"
        mock_response = MagicMock()
        mock_response.data = [
            {"@id": uri1, "@type": MockKGObject2.type_, "https://openminds.ebrains.eu/vocab/A": 1},
            {"@id": uri2, "@type": MockKGObject2.type_, "https://openminds.ebrains.eu/vocab/A": 2},
        ]
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            with pytest.warns(UserWarning):
                result = MockKGObject2.by_name("1", mock_client, match="contains")

        # Result should be the first one
        assert result is not None

    def test_by_name_all_true_returns_list(self):
        """With all=True, returns all matching objects."""
        mock_client = MagicMock()
        uri1 = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001"
        uri2 = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000002"
        mock_response = MagicMock()
        mock_response.data = [
            {"@id": uri1, "@type": MockKGObject2.type_, "https://openminds.ebrains.eu/vocab/A": 1},
            {"@id": uri2, "@type": MockKGObject2.type_, "https://openminds.ebrains.eu/vocab/A": 2},
        ]
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(MockKGObject2, "generate_query", return_value=mock_query):
            result = MockKGObject2.by_name("1", mock_client, match="contains", all=True)

        assert isinstance(result, list)


class TestKGObjectDiff:

    def test_diff_same_objects(self):
        obj1 = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        obj2 = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        assert obj1.diff(obj2) == {}

    def test_diff_different_type(self):
        obj1 = MockKGObject2(a=1, id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        # Use a simple mock object of a different class
        obj2 = MagicMock(spec=object)
        obj2.__class__ = MagicMock  # clearly not MockKGObject2
        result = obj1.diff(obj2)
        assert "type" in result

    def test_diff_different_ids(self):
        obj1 = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001111")
        obj2 = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000002222")
        result = obj1.diff(obj2)
        assert "id" in result

    def test_diff_different_property(self):
        obj1 = MockKGObject2(a=1, id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        obj2 = MockKGObject2(a=99, id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        result = obj1.diff(obj2)
        assert "properties" in result
        assert "a" in result["properties"]


class TestKGObjectFromUri:

    def test_from_uri_returns_none_when_no_data(self):
        """from_uri returns None when client returns no instance data."""
        mock_client = MagicMock()
        mock_client.instance_from_full_uri.return_value = None
        uri = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234"
        result = MockKGObject2.from_uri(uri, mock_client)
        assert result is None


class TestKGObjectCountCore:

    def test_count_core_with_filters_raises(self):
        """count() with api='core' and filters should raise ValueError."""
        mock_client = MagicMock()
        with pytest.raises(ValueError, match="Cannot use filters"):
            MockKGObject2.count(mock_client, api="core", a=1)


class TestKGObjectExists:

    def test_exists_cannot_build_query_returns_false(self):
        """exists() returns False when _build_existence_query raises CannotBuildExistenceQuery."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        with patch.object(obj, "_build_existence_query", side_effect=CannotBuildExistenceQuery):
            result = obj.exists(mock_client)
        assert result is False

    def test_exists_save_cache_hit(self):
        """exists() returns True immediately when query result is cached in save_cache."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=99)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        query_filter = {"a": 99}
        cached_uri = f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234"
        from fairgraph.caching import generate_cache_key
        cache_key = generate_cache_key(query_filter)
        save_cache[MockKGObject2][cache_key] = cached_uri

        with patch.object(obj, "_build_existence_query", return_value=query_filter):
            result = obj.exists(mock_client)

        assert result is True
        assert obj.id == cached_uri
        # client.query should NOT have been called (cache hit)
        mock_client.query.assert_not_called()

    def test_exists_connection_error_returns_false(self):
        """exists() returns False and warns on RemoteDisconnected ConnectionError."""
        from requests.exceptions import ConnectionError as RequestsConnectionError
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_client.query.side_effect = RequestsConnectionError("RemoteDisconnected: blah")
        mock_query = MagicMock()

        with patch.object(obj, "_build_existence_query", return_value={"a": 1}):
            with patch.object(MockKGObject2, "generate_minimal_query", return_value=mock_query):
                with patch("fairgraph.kgobject.warn") as mock_warn:
                    result = obj.exists(mock_client)
                    mock_warn.assert_called_once()

        assert result is False

    def test_exists_duplicate_raises(self):
        """exists() raises when >1 result and ignore_duplicates=False."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = [
            {"@id": f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001"},
            {"@id": f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000002"},
        ]
        mock_client.query.return_value = mock_response
        mock_query = MagicMock()

        with patch.object(obj, "_build_existence_query", return_value={"a": 1}):
            with patch.object(MockKGObject2, "generate_minimal_query", return_value=mock_query):
                with pytest.raises(Exception, match="Existence query is not specific enough"):
                    obj.exists(mock_client, ignore_duplicates=False)

    def test_exists_instance_not_found_returns_false(self):
        """exists() returns False when instance_from_full_uri returns None."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = [{"@id": f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001"}]
        mock_client.query.return_value = mock_response
        mock_client.instance_from_full_uri.return_value = None
        mock_query = MagicMock()

        with patch.object(obj, "_build_existence_query", return_value={"a": 1}):
            with patch.object(MockKGObject2, "generate_minimal_query", return_value=mock_query):
                result = obj.exists(mock_client, ignore_duplicates=True)

        assert result is False


class TestKGObjectSaveMore:

    def test_save_replace_raises_auth_error(self):
        """With ignore_auth_errors=False, AuthorizationError on replace propagates."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.replace_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=True):
            with pytest.raises(AuthorizationError):
                obj.save(mock_client, space="mock", recursive=False, replace=True, ignore_auth_errors=False)

    def test_save_update_raises_auth_error(self):
        """With ignore_auth_errors=False, AuthorizationError on update propagates."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        mock_client.update_instance.side_effect = AuthorizationError("denied")

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={
                "https://openminds.ebrains.eu/vocab/aRequiredString": "changed"
            }):
                with pytest.raises(AuthorizationError):
                    obj.save(mock_client, space="mock", recursive=False, ignore_auth_errors=False)

    def test_save_storagesize_only_change_is_noop(self):
        """When only storageSize changed, save() is a no-op (storageSize is locked)."""
        obj = _make_full_obj()
        mock_client = MagicMock()
        activity_log = MagicMock()

        with patch.object(obj, "exists", return_value=True):
            with patch.object(obj, "modified_data", return_value={
                "storageSize": 12345
            }):
                obj.save(mock_client, space="mock", recursive=False, activity_log=activity_log)

        mock_client.update_instance.assert_not_called()
        activity_log.update.assert_called()

    def test_save_create_auth_error_with_activity_log(self):
        """Activity log records create-error entry when auth error is ignored on create."""
        MockKGObject2.set_error_handling("none")
        obj = MockKGObject2(a=1)
        MockKGObject2.set_error_handling("error")
        mock_client = MagicMock()
        mock_client.create_new_instance.side_effect = AuthorizationError("denied")
        activity_log = MagicMock()

        with patch.object(obj, "exists", return_value=False):
            obj.save(mock_client, space="mock", recursive=False,
                     ignore_auth_errors=True, activity_log=activity_log)

        activity_log.update.assert_called()
        call_kwargs = activity_log.update.call_args[1]
        assert call_kwargs.get("entry_type") == "create-error"


class TestKGObjectMisc:

    def test_dump(self, tmp_path):
        """dump() saves to file without error."""
        obj = _make_full_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001")
        file_path = str(tmp_path / "test.jsonld")
        with patch("openminds.base.LinkedMetadata.save") as mock_save:
            obj.dump(file_path)
            mock_save.assert_called_once()

    def test_show_long_values_truncated(self, capsys):
        """show() truncates long values to fit max_width."""
        obj = _make_simple_obj(id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000001234")
        with patch("fairgraph.kgobject.have_tabulate", True):
            # max_width=30 is small enough to trigger truncation for the id value
            obj.show(max_width=30)
        captured = capsys.readouterr()
        assert "..." in captured.out

    def test_export_raises(self):
        """export() raises NotImplementedError."""
        obj = _make_simple_obj()
        with pytest.raises(NotImplementedError):
            obj.export("/some/path")

    def test_generate_minimal_query_no_filters(self):
        """generate_minimal_query() with no filters returns a serialized query."""
        mock_client = MagicMock()
        result = MockKGObject2.generate_minimal_query(client=mock_client, filters=None)
        assert result is not None

    def test_children_with_follow_links(self):
        """children() with follow_links calls resolve() first."""
        obj = MockKGObject2(a=1, id=f"{ID_NAMESPACE}00000000-0000-0000-0000-000000000001")
        mock_client = MagicMock()
        with patch.object(obj, "resolve") as mock_resolve:
            children = obj.children(mock_client, follow_links={"some": {}})
        mock_resolve.assert_called_once()
