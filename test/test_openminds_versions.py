"""
Tests for v4/v5 openMINDS version support and backwards compatibility.
"""

from unittest.mock import MagicMock, patch

import pytest

import fairgraph
import fairgraph.openminds
import fairgraph.openminds.v4
import fairgraph.openminds.v5
from fairgraph.kgobject import KGObject

from .utils import MockKGClient


def test_v4_imports():
    """v4 modules can be imported explicitly."""
    import fairgraph.openminds.v4.core as omcore4

    assert hasattr(omcore4, "Person")
    assert hasattr(omcore4, "Dataset")
    assert omcore4.Person.__module__.startswith("fairgraph.openminds.v4")


def test_v5_imports():
    """v5 modules can be imported explicitly."""
    import fairgraph.openminds.v5.core as omcore5

    assert hasattr(omcore5, "Person")
    assert hasattr(omcore5, "Dataset")
    assert omcore5.Person.__module__.startswith("fairgraph.openminds.v5")


def test_v5_neuroimaging():
    """v5-only neuroimaging module exists."""
    import fairgraph.openminds.v5.neuroimaging as omneuroimaging

    assert hasattr(omneuroimaging, "MRIScanner")
    assert hasattr(omneuroimaging, "StaticMRIAcquisition")
    assert hasattr(omneuroimaging, "DynamicMRIAcquisition")


def test_v5_new_classes():
    """v5 has new classes not present in v4."""
    import fairgraph.openminds.v5.core as omcore5
    import fairgraph.openminds.v5.sands as omsands5

    # New v5 core classes
    assert hasattr(omcore5, "Interface")
    assert hasattr(omcore5, "InterfaceVersion")
    assert hasattr(omcore5, "GridImage")
    assert hasattr(omcore5, "LocalFile")
    assert hasattr(omcore5, "ISNI")
    assert hasattr(omcore5, "LEI")

    # Renamed atlas classes in v5
    assert hasattr(omsands5, "AnatomicalAtlas")
    assert hasattr(omsands5, "CommonCoordinateFramework")


def test_backwards_compat_core_import():
    """import fairgraph.openminds.core works and returns v4."""
    import fairgraph.openminds.core as omcore

    assert omcore is fairgraph.openminds.v4.core


def test_backwards_compat_all_modules():
    """All v4 modules accessible via backwards-compat path."""
    om = fairgraph.openminds
    assert om.chemicals is om.v4.chemicals
    assert om.computation is om.v4.computation
    assert om.controlled_terms is om.v4.controlled_terms
    assert om.core is om.v4.core
    assert om.ephys is om.v4.ephys
    assert om.publications is om.v4.publications
    assert om.sands is om.v4.sands
    assert om.specimen_prep is om.v4.specimen_prep
    assert om.stimulation is om.v4.stimulation


def test_backwards_compat_submodules_are_aliased():
    """Importing a nested v4 submodule via the legacy path returns the same
    module object as the explicit v4 path.

    Without this, ``unittest.mock.patch`` (and any other code that walks a
    dotted attribute path) would silently see two distinct copies of the
    module: the v4 one used by the actual classes, and a fresh duplicate
    loaded via the legacy path. Patches set on the duplicate would have no
    effect on the code under test.
    """
    import importlib

    legacy_to_v4 = [
        ("fairgraph.openminds.core.products.dataset_version",
         "fairgraph.openminds.v4.core.products.dataset_version"),
        ("fairgraph.openminds.sands.atlas.brain_atlas_version",
         "fairgraph.openminds.v4.sands.atlas.brain_atlas_version"),
        ("fairgraph.openminds.controlled_terms.species",
         "fairgraph.openminds.v4.controlled_terms.species"),
    ]
    for legacy_name, v4_name in legacy_to_v4:
        legacy_mod = importlib.import_module(legacy_name)
        v4_mod = importlib.import_module(v4_name)
        assert legacy_mod is v4_mod, f"{legacy_name} is not the same object as {v4_name}"


def test_v4_and_v5_classes_are_distinct():
    """v4 and v5 classes with the same name are different objects."""
    v4_person = fairgraph.openminds.v4.core.Person
    v5_person = fairgraph.openminds.v5.core.Person
    assert v4_person is not v5_person
    assert v4_person.__module__ != v5_person.__module__


def test_registry_versioned_lookup():
    """Registry returns correct version-specific classes."""
    from openminds.registry import lookup_type

    cls4 = lookup_type("https://openminds.om-i.org/types/Person", "v4")
    cls5 = lookup_type("https://openminds.om-i.org/types/Person", "v5")
    assert cls4 is not cls5
    assert cls4.__module__.startswith("fairgraph.openminds.v4")
    assert cls5.__module__.startswith("fairgraph.openminds.v5")


def test_v4_class_name_attribute():
    """v4 classes have correct class_name for registry."""
    person = fairgraph.openminds.v4.core.Person
    assert person.class_name == "openminds.v4.core.Person"


def test_v5_class_name_attribute():
    """v5 classes have correct class_name for registry."""
    person = fairgraph.openminds.v5.core.Person
    assert person.class_name == "openminds.v5.core.Person"


def test_v4_list_kg_classes():
    """list_kg_classes works for v4 modules."""
    import fairgraph.openminds.v4.core as omcore4

    classes = omcore4.list_kg_classes()
    class_names = [cls.__name__ for cls in classes]
    assert "Person" in class_names
    assert "Dataset" in class_names


def test_v5_list_kg_classes():
    """list_kg_classes works for v5 modules."""
    import fairgraph.openminds.v5.core as omcore5

    classes = omcore5.list_kg_classes()
    class_names = [cls.__name__ for cls in classes]
    assert "Person" in class_names
    assert "Dataset" in class_names


def test_client_default_version_is_v4():
    """MockKGClient constructed with no kwargs defaults to v4."""
    client = MockKGClient()
    assert client.openminds_version == "v4"


def test_client_v5_version_attribute():
    """MockKGClient round-trips an explicit v5 version."""
    client = MockKGClient(openminds_version="v5")
    assert client.openminds_version == "v5"


def test_invalid_openminds_version_rejected():
    """Constructing a KGClient with an unsupported openminds_version raises ValueError."""
    from fairgraph.client import KGClient

    with pytest.raises(ValueError, match="openminds_version"):
        KGClient(
            host="core.kg-ppd.ebrains.eu",
            token="dummy",
            allow_interactive=False,
            openminds_version="v3",
        )


def test_from_id_uses_client_version():
    """KGObject.from_id passes the client's openminds_version to lookup_type."""
    mock_uri = "http://example.org/00000000-0000-0000-0000-000000000000"

    for version, expected_module_prefix in (("v4", "fairgraph.openminds.v4"),
                                            ("v5", "fairgraph.openminds.v5")):
        client = MockKGClient(openminds_version=version)
        sentinel = object()
        captured = {}

        def fake_lookup(type_iri, requested_version):
            captured["type_iri"] = type_iri
            captured["version"] = requested_version
            cls = MagicMock()
            cls.from_jsonld.return_value = sentinel
            cls.__module__ = f"{expected_module_prefix}.core"
            return cls

        with patch("fairgraph.kgobject.lookup_type", side_effect=fake_lookup):
            result = KGObject.from_id(mock_uri, client)

        assert captured["version"] == version
        assert captured["type_iri"] == "https://openminds.om-i.org/types/Model"
        assert result is sentinel
