from copy import deepcopy
import os
import subprocess
import sys
import tempfile
import pytest
from fairgraph.utility import (
    expand_filter,
    compact_uri,
    in_notebook,
    accepted_terms_of_use,
    sha1sum,
    normalize_data,
    adapt_namespaces_3to4,
    adapt_namespaces_4to3,
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


def test_initialise_instances_resolves_cross_references():
    # Regression for the fairgraph side of openMINDS issue #94
    # (https://github.com/openMetadataInitiative/openMINDS_Python/issues/94).
    #
    # Importing fairgraph recasts the openMINDS library instances to their fairgraph
    # subclasses. Cross-references between those instances (e.g. ParcellationEntityVersion
    # -> ParcellationEntity via `has_parents`) must be resolved to the actual recast
    # fairgraph objects, not left as raw {"@id": ...} dicts or unresolved KGProxy objects.
    #
    # Previously the recast serialised each instance with embed_linked_nodes=ALWAYS, which
    # recursed without bound over the cyclic ParcellationEntity <-> ParcellationEntityVersion
    # instance graph (RecursionError, and then out-of-memory once a cycle guard was added).
    # initialise_instances now does a shallow recast (links become KGProxy) followed by a
    # resolution pass against an id -> object lookup.
    import fairgraph
    from fairgraph.openminds.sands import ParcellationEntity, ParcellationEntityVersion
    from fairgraph.kgproxy import KGProxy

    # The library instances were recast to typed fairgraph objects.
    pe_by_id = {
        obj.id: obj
        for obj in vars(ParcellationEntity).values()
        if isinstance(obj, ParcellationEntity)
    }
    assert pe_by_id, "no ParcellationEntity library instances were recast"
    assert all(isinstance(pe, fairgraph.KGObject) for pe in pe_by_id.values())

    # Find a version that references a parent entity and check the reference is resolved.
    parent = None
    for version in vars(ParcellationEntityVersion).values():
        if not isinstance(version, ParcellationEntityVersion) or not version.has_parents:
            continue
        parents = version.has_parents
        parents = parents if isinstance(parents, (list, tuple)) else [parents]
        parent = next((p for p in parents if isinstance(p, ParcellationEntity)), None)
        if parent is not None:
            break
    assert parent is not None, "no ParcellationEntityVersion with a ParcellationEntity parent found"

    # The cross-reference is a typed fairgraph object, not a raw dict (issue #94) and not
    # an unresolved proxy; it is the very same recast object held as a class attribute.
    assert not isinstance(parent, dict)
    assert not isinstance(parent, KGProxy)
    assert isinstance(parent, ParcellationEntity)
    assert parent is pe_by_id[parent.id]


def test_import_fairgraph_is_silent_and_does_not_crash():
    # Regression: importing fairgraph recasts the openMINDS library instances. This used to
    # recurse without bound over the cyclic ParcellationEntity <-> ...Version instance graph
    # (RecursionError, then out-of-memory), and once that was fixed it emitted validation
    # warnings for the intentionally-incomplete library instances. A bare `import fairgraph`
    # must now complete cleanly and produce no output on stdout or stderr.
    #
    # This runs in a subprocess because fairgraph is already imported in the test session
    # (the recast runs only once, at import time), so the behaviour can only be observed
    # from a fresh interpreter.
    result = subprocess.run(
        [sys.executable, "-c", "import fairgraph"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == "", f"unexpected stdout:\n{result.stdout}"
    assert result.stderr == "", f"unexpected stderr:\n{result.stderr}"


def test_error_handling_restored_to_default_after_import():
    # initialise_instances suppresses validation handling globally while recasting the
    # library instances, then restores the default ("log") in a finally block. Guard against
    # that restore being dropped, which would silently leave validation disabled (error
    # handling set to None) for the whole session, for both linked and embedded classes.
    import fairgraph  # noqa: F401
    from fairgraph.base import ErrorHandling
    from fairgraph.openminds.sands import ParcellationEntity, AtlasAnnotation

    assert ParcellationEntity.error_handling == ErrorHandling.log  # a KGObject class
    assert AtlasAnnotation.error_handling == ErrorHandling.log  # an embedded (KGEmbedded) class
