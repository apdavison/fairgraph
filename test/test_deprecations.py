"""
Tests that deprecated names still work and emit a DeprecationWarning (see doc/deprecations.rst).
"""

import importlib
import sys

import pytest

import fairgraph
from fairgraph.base import Releasable
from fairgraph.embedded import KGEmbedded
from fairgraph.node import KGNode
from fairgraph.registry import NodeMeta
from fairgraph.utility import handle_scope_keyword


@pytest.mark.parametrize(
    "module_name,alias,replacement",
    [
        ("fairgraph", "EmbeddedMetadata", KGEmbedded),
        ("fairgraph.embedded", "EmbeddedMetadata", KGEmbedded),
        ("fairgraph.node", "ContainsMetadata", KGNode),
        ("fairgraph.base", "RepresentsSingleObject", Releasable),
        ("fairgraph.registry", "Node", NodeMeta),
    ],
)
def test_deprecated_alias(module_name, alias, replacement):
    module = importlib.import_module(module_name)
    with pytest.warns(DeprecationWarning, match=f"'{alias}' is deprecated.*version 1.0.*'{replacement.__name__}'"):
        obj = getattr(module, alias)
    assert obj is replacement


def test_deprecated_alias_from_import():
    with pytest.warns(DeprecationWarning, match="'Node' is deprecated"):
        from fairgraph.registry import Node
    assert Node is NodeMeta


def test_unknown_attribute_still_raises():
    with pytest.raises(AttributeError, match="has no attribute 'NoSuchThing'"):
        fairgraph.registry.NoSuchThing


@pytest.mark.parametrize(
    "old_name,new_name", [("controlledterms", "controlled_terms"), ("specimenprep", "specimen_prep")]
)
def test_deprecated_module(old_name, new_name):
    module_path = f"fairgraph.openminds.{old_name}"
    sys.modules.pop(module_path, None)  # the warning is only emitted when the module is first imported
    with pytest.warns(
        DeprecationWarning, match=f"`{old_name}` module has been renamed to `{new_name}`.*removed in version 1.0"
    ):
        old_module = importlib.import_module(module_path)
    new_module = importlib.import_module(f"fairgraph.openminds.{new_name}")
    assert old_module.list_kg_classes() == new_module.list_kg_classes()


def test_deprecated_scope_keyword():
    with pytest.warns(DeprecationWarning, match="'scope' is deprecated.*version 1.0"):
        assert handle_scope_keyword("any", "released") == "any"
