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


def test_expand_filter_keeps_siblings():
    filter = {
        "developers__given_name": "Bilbo",
        "developers__family_name": "Baggins",
    }
    assert expand_filter(filter) == {"developers": {"given_name": "Bilbo", "family_name": "Baggins"}}


def test_expand_filter_expands_dicts_in_lists():
    filter = {"coordinates": [{"value": 1.0, "unit__name": "mm"}, {"value": 2.0, "unit__name": "mm"}]}
    assert expand_filter(filter) == {
        "coordinates": [{"value": 1.0, "unit": {"name": "mm"}}, {"value": 2.0, "unit": {"name": "mm"}}]
    }


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
        "alternateName": None,
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
        "https://openminds.ebrains.eu/vocab/alternateName": None,
    }
    assert normalize_data(data, context) == expected


def test_initialise_instances_resolves_cross_references():
    # Regression for the fairgraph side of openMINDS issue #94
    # (https://github.com/openMetadataInitiative/openMINDS_Python/issues/94).
    #
    # fairgraph recasts the openMINDS library instances to their fairgraph
    # subclasses. Cross-references between those instances (e.g. ParcellationEntityVersion
    # -> ParcellationEntity via `has_parents`) must be resolved to the actual recast
    # fairgraph objects, not left as raw {"@id": ...} dicts or unresolved KGProxy objects.
    #
    # Previously the recast serialised each instance with embed_linked_nodes=ALWAYS, which
    # recursed without bound over the cyclic ParcellationEntity <-> ParcellationEntityVersion
    # instance graph (RecursionError, and then out-of-memory once a cycle guard was added).
    # Recasting is now a shallow recast (links become KGProxy) followed by a
    # resolution pass against an id -> object lookup.
    import fairgraph
    from fairgraph.openminds.sands import ParcellationEntity, ParcellationEntityVersion
    from fairgraph.kgproxy import KGProxy

    # The library instances were recast to typed fairgraph objects.
    pe_by_id = {obj.id: obj for obj in ParcellationEntity.instances()}
    assert pe_by_id, "no ParcellationEntity library instances were recast"
    assert all(isinstance(pe, fairgraph.KGObject) for pe in pe_by_id.values())

    # Find a version that references a parent entity and check the reference is resolved.
    parent = None
    for version in ParcellationEntityVersion.instances():
        if not version.has_parents:
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
    # Regression: recasting the openMINDS library instances, which used to happen when
    # importing fairgraph, used to recurse without bound over the cyclic
    # ParcellationEntity <-> ...Version instance graph (RecursionError, then out-of-memory),
    # and once that was fixed it emitted validation warnings for the intentionally-incomplete
    # library instances. Importing fairgraph and recasting these instances must now complete
    # cleanly and produce no output on stdout or stderr.
    #
    # This runs in a subprocess because the library instances are recast at most once
    # per session, so the behaviour can only be observed from a fresh interpreter.
    code = "import fairgraph; fairgraph.openminds.sands.ParcellationEntityVersion.instances()"
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == "", f"unexpected stdout:\n{result.stdout}"
    assert result.stderr == "", f"unexpected stderr:\n{result.stderr}"


def test_validation_restored_after_recasting():
    # Recasting the library instances suppresses validation. Guard against that suppression
    # outlasting the recast, which would silently leave validation disabled for the whole
    # session, for both linked and embedded classes.
    from fairgraph.base import ErrorHandling, is_validation_suppressed
    from fairgraph.openminds.sands import ParcellationEntity, AtlasAnnotation

    ParcellationEntity.instances()
    assert not is_validation_suppressed()

    assert ParcellationEntity.error_handling == ErrorHandling.log  # a KGObject class
    assert AtlasAnnotation.error_handling == ErrorHandling.log  # an embedded (KGEmbedded) class


def _run_in_fresh_interpreter(code):
    # library instances are recast at most once per session, so their recasting
    # can only be observed from a fresh interpreter
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stderr
    assert result.stderr == "", f"unexpected stderr:\n{result.stderr}"


def test_library_instances_are_recast_on_first_use():
    _run_in_fresh_interpreter("""
import fairgraph
from fairgraph.openminds.controlled_terms import BiologicalSex, Species
from fairgraph.openminds.v5.controlled_terms import Species as SpeciesV5

assert not isinstance(Species.__dict__["mus_musculus"], Species)  # not recast at import
mouse = Species.mus_musculus
assert isinstance(mouse, Species) and isinstance(mouse, fairgraph.KGObject)
assert Species.__dict__["mus_musculus"] is mouse
assert mouse in Species.instances()
assert Species.by_name("Mus musculus") is mouse
# other classes are left alone
assert not isinstance(BiologicalSex.__dict__["male"], BiologicalSex)
assert not isinstance(SpeciesV5.__dict__["mus_musculus"], SpeciesV5)
""")


def test_library_instances_recast_through_by_name():
    _run_in_fresh_interpreter("""
import fairgraph
from fairgraph.openminds.controlled_terms import Species

assert isinstance(Species.by_name("Mus musculus"), Species)
""")


def test_library_instances_recast_after_openminds_by_name():
    # by_name() caches a lookup table on the class; the fairgraph class must not
    # use one built by its openMINDS parent, which holds openMINDS objects
    _run_in_fresh_interpreter("""
import fairgraph
import openminds.v4.controlled_terms
from fairgraph.openminds.controlled_terms import Species

assert not isinstance(openminds.v4.controlled_terms.Species.by_name("Mus musculus"), fairgraph.KGObject)
assert isinstance(Species.by_name("Mus musculus"), Species)
""")


def test_library_instances_recast_with_links_to_other_classes():
    # recasting a class recasts the classes whose library instances it links to
    _run_in_fresh_interpreter("""
from fairgraph.openminds.sands import ParcellationEntity, ParcellationEntityVersion

from fairgraph.utility import as_list

assert not any(isinstance(value, ParcellationEntity) for value in vars(ParcellationEntity).values())
parents = [
    parent
    for version in ParcellationEntityVersion.instances()
    for parent in as_list(version.has_parents)
    if isinstance(parent, ParcellationEntity)
]
assert parents
assert all(any(parent is value for value in vars(ParcellationEntity).values()) for parent in parents[:10])
""")


def test_recasting_library_instances_keeps_error_handling():
    _run_in_fresh_interpreter("""
from fairgraph.base import ErrorHandling
from fairgraph.openminds.controlled_terms import Species
from fairgraph.openminds.core import Person
from fairgraph.openminds.sands import AtlasAnnotation, ParcellationEntityVersion

Species.set_error_handling("error")
Person.set_error_handling("warning")
Species.mus_musculus
ParcellationEntityVersion.instances()
assert Species.error_handling == ErrorHandling.error
assert Person.error_handling == ErrorHandling.warning
assert ParcellationEntityVersion.error_handling == ErrorHandling.log
assert AtlasAnnotation.error_handling == ErrorHandling.log
""")


def test_validation_suppressed_only_in_current_thread():
    import threading
    import warnings
    from fairgraph.base import ErrorHandling, validation_suppressed

    def violate():
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            ErrorHandling.handle_violation(ErrorHandling.warning, "a violation")
        return len(caught)

    # The other thread is started before validation is suppressed, as since Python 3.14 a thread can
    # start with a copy of the context of the code that starts it (the default on free-threaded builds).
    # It reports a violation while this thread is inside the block; the two never warn at the same time,
    # as catch_warnings() is not thread-safe.
    go, done = threading.Event(), threading.Event()
    results = []

    def other_thread():
        go.wait()
        results.append(violate())
        done.set()

    thread = threading.Thread(target=other_thread)
    thread.start()
    with validation_suppressed():
        assert violate() == 0
        go.set()
        assert done.wait(timeout=10)
    thread.join()
    assert results == [1]
    assert violate() == 1
