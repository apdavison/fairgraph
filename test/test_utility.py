from copy import deepcopy
import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from fairgraph.utility import (
    expand_filter,
    expand_uri,
    compact_uri,
    in_notebook,
    accepted_terms_of_use,
    sha1sum,
    normalize_data,
    adapt_namespaces_3to4,
    adapt_namespaces_4to3,
    adapt_type_4to3,
    adapt_namespaces_for_query,
    types_match,
    LogEntry,
    ActivityLog,
    handle_scope_keyword,
)
from .utils import kg_client, skip_if_no_connection


def test_expand_filter():
    filter = {
        "developers__affiliations__member_of__alias": "CNRS",
        "digital_identifier__identifier": "https://doi.org/some-doi",
    }
    result = expand_filter(filter)
    expected = {
        "developers": {"affiliations": {"member_of": {"alias": "CNRS"}}},
        "digital_identifier": {"identifier": "https://doi.org/some-doi"},
    }
    assert result == expected


def test_compact_uri():
    context = {"foaf": "http://xmlns.com/foaf/0.1/"}
    uri_list = "http://xmlns.com/foaf/0.1/Person"
    result = compact_uri(uri_list, context)
    assert result == "foaf:Person"

    uri_list = ["http://xmlns.com/foaf/0.1/Person", "foaf:homepage"]
    result = compact_uri(uri_list, context)
    assert result == ("foaf:Person", "foaf:homepage")

    uri_list = "http://purl.org/dc/elements/1.1/creator"
    with pytest.raises(ValueError):
        result = compact_uri(uri_list, context, strict=True)
    result = compact_uri(uri_list, context)
    assert result == uri_list


def test_in_notebook():
    assert not in_notebook()


@skip_if_no_connection
def test_accepted_terms_of_use(kg_client, mocker):
    result = accepted_terms_of_use(kg_client, accept_terms_of_use=True)
    assert result is True
    mocker.patch("builtins.input")
    result = accepted_terms_of_use(kg_client, accept_terms_of_use=False)
    assert result is False
    mocker.patch("builtins.input", lambda prompt: "yes")
    result = accepted_terms_of_use(kg_client, accept_terms_of_use=False)
    assert result is True


def test_sha1sum():
    fp = tempfile.NamedTemporaryFile(mode="w+b", delete=False)
    fp.write(b"0" * 256)
    fp.close()
    assert sha1sum(fp.name) == "80a963e503e9ed478c2cc528fd344d58122929c2"
    os.remove(fp.name)


def test_normalize_data():
    data = {
        "@id": "http://example.org/00000000-0000-0000-0000-000000000000",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "affiliation": {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "memberOf": {
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "fullName": "The Lonely Mountain",
            },
        },
        "familyName": "Oakenshield",
        "givenName": "Thorin",
        "alternateName": None
    }
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    expected = {
        "@id": "http://example.org/00000000-0000-0000-0000-000000000000",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/affiliation": {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "https://openminds.ebrains.eu/vocab/memberOf": {
                "@type": "https://openminds.ebrains.eu/core/Organization",
                "https://openminds.ebrains.eu/vocab/fullName": "The Lonely Mountain",
            },
        },
        "https://openminds.ebrains.eu/vocab/familyName": "Oakenshield",
        "https://openminds.ebrains.eu/vocab/givenName": "Thorin",
        "https://openminds.ebrains.eu/vocab/alternateName": None
    }
    assert normalize_data(data, context) == expected


def test_expand_uri_prefix_not_in_context():
    context = {"foaf": "http://xmlns.com/foaf/0.1/"}
    with pytest.raises(ValueError, match="prefix dc not found in context"):
        expand_uri("dc:title", context)


def test_expand_uri_base_url_without_trailing_slash():
    context = {"foaf": "http://xmlns.com/foaf/0.1"}  # no trailing slash
    result = expand_uri("foaf:Person", context)
    assert result == "http://xmlns.com/foaf/0.1/Person"


def test_compact_uri_vocab_prefix():
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    result = compact_uri("https://openminds.ebrains.eu/vocab/fullName", context)
    assert result == "fullName"


def test_expand_filter_nested_dict_raises():
    with pytest.raises(TypeError, match="single-level dict"):
        expand_filter({"key": {"nested": "value"}})


def test_log_entry_repr():
    entry = LogEntry("MyClass", "some-id", None, "myspace", "create")
    assert repr(entry) == "create: MyClass(some-id) in 'myspace'"


def test_log_entry_as_dict():
    entry = LogEntry("MyClass", "some-id", {"field": "value"}, "myspace", "update")
    d = entry.as_dict()
    assert d == {
        "cls": "MyClass",
        "id": "some-id",
        "delta": {"field": "value"},
        "space": "myspace",
        "type_": "update",
    }


def test_activity_log_repr():
    log = ActivityLog()
    log.entries.append(LogEntry("Foo", "id-1", None, "space1", "create"))
    log.entries.append(LogEntry("Bar", "id-2", None, "space2", "update"))
    r = repr(log)
    assert "create: Foo(id-1)" in r
    assert "update: Bar(id-2)" in r


def test_handle_scope_keyword_deprecated():
    with pytest.warns(DeprecationWarning, match="scope.*deprecated"):
        result = handle_scope_keyword("released", "any")
    assert result == "released"


def test_handle_scope_keyword_not_deprecated():
    result = handle_scope_keyword(None, "in progress")
    assert result == "in progress"


def test_normalize_data_none():
    assert normalize_data(None, {}) is None


def test_normalize_data_q_prefix_key():
    context = {"@vocab": "https://example.com/vocab/"}
    data = {"Q:someQuery": "value"}
    result = normalize_data(data, context)
    # Key starting with Q is kept as-is
    assert "Q:someQuery" in result


def test_types_match_same():
    assert types_match("https://example.com/A", "https://example.com/A") is True


def test_types_match_same_last_segment():
    assert types_match("https://openminds.ebrains.eu/core/Person", "https://openminds.om-i.org/types/Person") is True


def test_types_match_different():
    assert types_match("https://example.com/A", "https://example.com/B") is False


def test_in_notebook_zmq(monkeypatch):
    mock_shell = MagicMock()
    mock_shell.__class__.__name__ = "ZMQInteractiveShell"
    with patch("fairgraph.utility.get_ipython", return_value=mock_shell, create=True):
        import fairgraph.utility as util_module
        original = getattr(util_module, "get_ipython", None)
        import builtins
        original_builtins = builtins.__dict__.get("get_ipython")
        builtins.__dict__["get_ipython"] = lambda: mock_shell
        try:
            result = in_notebook()
        finally:
            if original_builtins is None:
                builtins.__dict__.pop("get_ipython", None)
            else:
                builtins.__dict__["get_ipython"] = original_builtins
    assert result is True


def test_in_notebook_terminal(monkeypatch):
    mock_shell = MagicMock()
    mock_shell.__class__.__name__ = "TerminalInteractiveShell"
    import builtins
    original_builtins = builtins.__dict__.get("get_ipython")
    builtins.__dict__["get_ipython"] = lambda: mock_shell
    try:
        result = in_notebook()
    finally:
        if original_builtins is None:
            builtins.__dict__.pop("get_ipython", None)
        else:
            builtins.__dict__["get_ipython"] = original_builtins
    assert result is False


def test_in_notebook_other_shell(monkeypatch):
    mock_shell = MagicMock()
    mock_shell.__class__.__name__ = "SomeOtherShell"
    import builtins
    original_builtins = builtins.__dict__.get("get_ipython")
    builtins.__dict__["get_ipython"] = lambda: mock_shell
    try:
        result = in_notebook()
    finally:
        if original_builtins is None:
            builtins.__dict__.pop("get_ipython", None)
        else:
            builtins.__dict__["get_ipython"] = original_builtins
    assert result is False


def test_adapt_namespaces_3to4_with_list_type():
    """adapt_type_3to4 handles list @type."""
    data = [{"@type": ["https://openminds.ebrains.eu/core/Person"], "@id": "0000"}]
    adapt_namespaces_3to4(data)
    assert data[0]["@type"] == "https://openminds.om-i.org/types/Person"


def test_adapt_namespaces_3to4_with_openminds_instance_uri():
    """adapt_instance_uri_3to4 replaces ebrains.eu with om-i.org for openminds URIs."""
    data = [{"@id": "https://openminds.ebrains.eu/instances/someInstance", "@type": "https://openminds.ebrains.eu/core/Person"}]
    adapt_namespaces_3to4(data)
    assert data[0]["@id"] == "https://openminds.om-i.org/instances/someInstance"


def test_adapt_namespaces_4to3_with_list_type():
    """adapt_type_4to3 handles list @type."""
    import fairgraph.openminds.core  # populate registry
    data = [{"@type": ["https://openminds.om-i.org/types/Person"], "@id": "0000"}]
    adapt_namespaces_4to3(data)
    # type should be converted to v3 format
    assert "openminds.ebrains.eu" in data[0]["@type"]


def test_adapt_namespaces_4to3_with_openminds_instance_uri():
    """adapt_instance_uri_4to3 replaces om-i.org with ebrains.eu for openminds URIs."""
    import fairgraph.openminds.core  # populate registry
    data = [{"@id": "https://openminds.om-i.org/instances/someInstance", "@type": "https://openminds.om-i.org/types/Person"}]
    adapt_namespaces_4to3(data)
    assert data[0]["@id"] == "https://openminds.ebrains.eu/instances/someInstance"


def test_adapt_namespaces_for_query():
    """adapt_namespaces_for_query converts a v4 query structure to v3."""
    import fairgraph.openminds.core  # populate registry
    query = {
        "meta": {
            "type": "https://openminds.om-i.org/types/Person",
        },
        "structure": [
            {
                "path": "https://openminds.om-i.org/props/familyName",
                "filter": {"value": "Smith"},
            }
        ],
    }
    result = adapt_namespaces_for_query(query)
    assert "openminds.ebrains.eu" in result["meta"]["type"]
    assert "openminds.ebrains.eu/vocab" in result["structure"][0]["path"]


def test_adapt_namespaces():
    import fairgraph.openminds.core  # needed to populate the registry for lookup

    data_v3 = [
        {
            "@id": "0000",
            "@type": "https://openminds.ebrains.eu/core/Person",
            "https://openminds.ebrains.eu/vocab/affiliation": {
                "@type": "https://openminds.ebrains.eu/core/Affiliation",
                "https://openminds.ebrains.eu/vocab/memberOf": {
                    "@type": "https://openminds.ebrains.eu/core/Organization",
                    "https://openminds.ebrains.eu/vocab/fullName": "The Lonely Mountain",
                },
            },
            "https://openminds.ebrains.eu/vocab/familyName": "Oakenshield",
            "https://openminds.ebrains.eu/vocab/givenName": "Thorin",
        }
    ]
    data_v4 = [
        {
            "@id": "0000",
            "@type": "https://openminds.om-i.org/types/Person",
            "https://openminds.om-i.org/props/affiliation": {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "https://openminds.om-i.org/props/memberOf": {
                    "@type": "https://openminds.om-i.org/types/Organization",
                    "https://openminds.om-i.org/props/fullName": "The Lonely Mountain",
                },
            },
            "https://openminds.om-i.org/props/familyName": "Oakenshield",
            "https://openminds.om-i.org/props/givenName": "Thorin",
        }
    ]

    data = deepcopy(data_v3)
    adapt_namespaces_3to4(data)
    assert data == data_v4

    data = deepcopy(data_v4)
    adapt_namespaces_4to3(data)
    assert data == data_v3

    assert data_v3 != data_v4
