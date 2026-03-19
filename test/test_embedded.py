# encoding: utf-8
"""
Tests for fairgraph.embedded module.
"""

import pytest
from unittest.mock import MagicMock, patch
from openminds.base import LinkedMetadata, EmbeddedMetadata as OMEmbeddedMetadata
from openminds.properties import Property
from fairgraph.embedded import KGEmbedded
from fairgraph.kgobject import KGObject
from fairgraph.node import KGNode

from test.test_base import MockEmbeddedObject, MockKGObject2


class TestKGEmbeddedFromJsonld:

    def test_from_jsonld_basic(self):
        data = {
            "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
            "https://openminds.ebrains.eu/vocab/aNumber": 42.0,
        }
        obj = MockEmbeddedObject.from_jsonld(data)
        assert obj is not None
        assert obj.a_number == 42.0

    def test_from_jsonld_with_id_warns_and_returns_none(self):
        data = {
            "@id": "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000001234",
            "@type": "https://openminds.ebrains.eu/mock/MockEmbeddedObject",
            "https://openminds.ebrains.eu/vocab/aNumber": 5.0,
        }
        with pytest.warns(UserWarning, match="Expected embedded metadata"):
            result = MockEmbeddedObject.from_jsonld(data)
        assert result is None


class TestKGEmbeddedEquality:

    def test_eq_same_data(self):
        obj1 = MockEmbeddedObject(a_number=5.0)
        obj2 = MockEmbeddedObject(a_number=5.0)
        assert obj1 == obj2

    def test_eq_different_data(self):
        obj1 = MockEmbeddedObject(a_number=5.0)
        obj2 = MockEmbeddedObject(a_number=6.0)
        assert obj1 != obj2

    def test_eq_different_types(self):
        obj1 = MockEmbeddedObject(a_number=5.0)
        assert obj1 != "not an embedded object"


class TestKGEmbeddedSpaceProperties:

    def test_space_returns_none(self):
        obj = MockEmbeddedObject(a_number=1.0)
        assert obj.space is None

    def test_default_space_returns_none(self):
        obj = MockEmbeddedObject(a_number=1.0)
        assert obj.default_space is None


class TestKGEmbeddedSave:

    def test_save_with_linked_kgnode(self):
        """save() should recursively call save() on linked KGNode sub-components."""
        # Create a mock KGObject2 child (KGNode subclass)
        child = MockKGObject2(a=42)
        child._space = "mock"

        # We need an embedded that has a KGNode property; use MockEmbeddedObject
        # by setting a property value to a KGNode directly - but MockEmbeddedObject
        # only has a_string, a_date, a_number, none of which are KGNodes.
        # So we'll use a custom embedded class for this test.
        class EmbeddedWithLink(KGEmbedded, OMEmbeddedMetadata):
            type_ = "https://openminds.ebrains.eu/mock/EmbeddedWithLink"
            schema_version = "latest"
            preferred_import_path = "test.test_embedded.EmbeddedWithLink"
            context = {
                "vocab": "https://openminds.ebrains.eu/vocab/",
            }
            properties = [
                Property(
                    "linked_obj",
                    MockKGObject2,
                    "https://openminds.ebrains.eu/vocab/linkedObj",
                    multiple=False,
                    required=False,
                )
            ]
            reverse_properties = []

        embedded = EmbeddedWithLink(linked_obj=child)
        mock_client = MagicMock()

        with patch.object(child, "save") as mock_child_save:
            embedded.save(mock_client, space="mock")
            mock_child_save.assert_called_once()

    def test_save_raises_for_unwritable_controlled_space(self):
        """save() raises if a value targets controlled space but doesn't exist there."""
        class ControlledNode(KGObject, LinkedMetadata):
            default_space = "controlled"
            type_ = "https://openminds.ebrains.eu/mock/ControlledNode"
            schema_version = "latest"
            preferred_import_path = "test.test_embedded.ControlledNode"
            context = {"vocab": "https://openminds.ebrains.eu/vocab/"}
            properties = []
            reverse_properties = []

        class EmbeddedWithControlled(KGEmbedded, OMEmbeddedMetadata):
            type_ = "https://openminds.ebrains.eu/mock/EmbeddedWithControlled"
            schema_version = "latest"
            preferred_import_path = "test.test_embedded.EmbeddedWithControlled"
            context = {"vocab": "https://openminds.ebrains.eu/vocab/"}
            properties = [
                Property(
                    "ctrl",
                    ControlledNode,
                    "https://openminds.ebrains.eu/vocab/ctrl",
                    multiple=False,
                    required=False,
                )
            ]
            reverse_properties = []

        child = ControlledNode()
        child._space = None
        embedded = EmbeddedWithControlled(ctrl=child)
        mock_client = MagicMock()

        # exists returns False → should raise because can't write to controlled space
        with patch.object(child, "exists", return_value=False):
            with pytest.raises(Exception, match="Cannot write to controlled space"):
                embedded.save(mock_client, space="controlled")
