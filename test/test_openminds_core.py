import os
import json
from random import randint
from uuid import UUID
from copy import deepcopy
from datetime import datetime
import shutil
import tempfile
import urllib.request

import pytest

from openminds import IRI

from fairgraph.utility import as_list
from fairgraph.kgproxy import KGProxy
from fairgraph.kgquery import KGQuery
from fairgraph.kgobject import KGObject
import fairgraph.openminds.core as omcore
import fairgraph.openminds.controlled_terms as omterms
from fairgraph.utility import ActivityLog, sha1sum

from test.utils import mock_client, kg_client, skip_if_no_connection, skip_if_using_production_server


def test_query_generation(mock_client):
    for cls in omcore.list_kg_classes():
        generated = cls.generate_query(space="collab-foobar", client=mock_client, with_reverse_properties=True)
        filename = f"test/test_data/queries/openminds/core/{cls.__name__.lower()}_simple_query.json"
        with open(filename, "r") as fp:
            expected = json.load(fp)
        assert generated == expected


@skip_if_no_connection
def test_retrieve_released_models_no_filter_api_core(kg_client):
    models = omcore.Model.list(
        kg_client, release_status="released", space="model", api="core", size=20, from_index=randint(0, 80)
    )
    assert len(models) == 20
    for m in models:
        assert m.space == "model"


@skip_if_no_connection
def test_retrieve_released_models_no_filter_api_query(kg_client):
    models = omcore.Model.list(
        kg_client, release_status="released", space="model", api="query", size=20, from_index=randint(0, 80)
    )
    assert len(models) == 20


@skip_if_no_connection
def test_retrieve_released_models_with_filter_api_core(kg_client):
    with pytest.raises(ValueError):
        models = omcore.Model.list(kg_client, release_status="released", api="core", name="foo")


@skip_if_no_connection
def test_retrieve_released_models_filter_species_by_obj(kg_client):
    rat = omterms.Species.by_name("Rattus norvegicus", kg_client)
    assert rat.name == "Rattus norvegicus"
    models = omcore.Model.list(kg_client, release_status="released", space="model", api="query", study_targets=rat)
    assert len(models) > 0
    for model in models:
        study_targets = [st.resolve(kg_client, release_status="released") for st in as_list(model.study_targets)]
        if study_targets:
            assert rat in study_targets


@skip_if_no_connection
def test_retrieve_released_datasets_filter_species_by_openminds_obj(kg_client):
    rat = omterms.Species.by_name("Rattus norvegicus", kg_client)
    rat_om = omterms.Species.rattus_norvegicus
    assert rat.name == rat_om.name == "Rattus norvegicus"
    follow_links = {"study_targets": {}}
    datasets = omcore.DatasetVersion.list(kg_client, space="dataset", study_targets=rat, follow_links=follow_links)
    datasets_om = omcore.DatasetVersion.list(kg_client, space="dataset", study_targets=rat_om, follow_links=follow_links)
    assert len(datasets) > 0
    assert len(datasets) == len(datasets_om)
    assert [ds.id for ds in datasets] == [ds.id for ds in datasets_om]
    for dataset in datasets_om:
        assert rat in dataset.study_targets


@skip_if_no_connection
def test_retrieve_released_models_filter_species_by_uuid(kg_client):
    human = omterms.Species.by_name("Homo sapiens", kg_client)
    models = omcore.Model.list(
        kg_client, release_status="released", space="model", api="query", study_targets=UUID(human.uuid)
    )
    assert len(models) > 0
    for model in models:
        if model.study_targets:
            assert human.id in [st.id for st in as_list(model.study_targets)]


@skip_if_no_connection
def test_retrieve_released_models_filter_species_by_id(kg_client):
    mouse = omterms.Species.by_name("Mus musculus", kg_client)
    models = omcore.Model.list(
        kg_client, release_status="released", space="model", api="query", study_targets=IRI(mouse.id)
    )
    # todo: fix so that don't need to wrap the id in an IRI
    assert len(models) > 0
    for model in models:
        if model.study_targets:
            assert mouse.id in [st.id for st in as_list(model.study_targets)]


@skip_if_no_connection
def test_retrieve_released_models_filter_custodian(kg_client):
    alain = omcore.Person.list(kg_client, family_name="Destexhe", given_name="Alain")[0]
    assert alain.given_name == "Alain"
    models = omcore.Model.list(kg_client, release_status="released", space="model", api="query", custodians=alain)
    assert len(models) > 0
    for model in models:
        assert alain.id in [c.id for c in as_list(model.custodians)]


@skip_if_no_connection
def test_retrieve_models_filter_by_space(kg_client):
    all_models = omcore.Model.list(kg_client, release_status="in progress", space=None, size=10000)
    n_models_in_model_space_core = omcore.Model.count(
        kg_client, release_status="in progress", space="model", api="core"
    )
    n_models_in_model_space_query = omcore.Model.count(
        kg_client, release_status="in progress", space="model", api="query"
    )
    assert n_models_in_model_space_core == n_models_in_model_space_query
    assert len(all_models) > n_models_in_model_space_core
    assert len([m for m in all_models if m.space == "model"]) == n_models_in_model_space_query


@skip_if_no_connection
def test_retrieve_single_model_with_followed_links(kg_client):
    model = omcore.Model.from_uri(
        "https://kg.ebrains.eu/api/instances/708024f7-9dd7-4c92-ae95-936db23c6d99",
        kg_client,
        follow_links={"abstraction_level": {}},
    )
    assert isinstance(model.abstraction_level, omterms.ModelAbstractionLevel)  # followed
    assert isinstance(model.scope, KGProxy)  # not followed


@skip_if_no_connection
def test_retrieve_single_model_from_alias(kg_client):
    model = omcore.Model.from_alias("AdEx Models", kg_client)
    assert model.uuid == "3ca9ae35-c9df-451f-ac76-4925bd2c7dc6"


@skip_if_no_connection
def test_retrieve_single_model_from_ambiguous_alias(kg_client):
    model = omcore.Model.from_alias("hippo", kg_client)
    # check that warning is emitted


@skip_if_no_connection
def test_retrieve_unknown_type(kg_client):
    obj = KGObject.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert isinstance(obj, omcore.Model)


@skip_if_no_connection
def test_resolve_model(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.name == "Scaffold Model of Cerebellum microcircuit version 2.0"
    assert isinstance(model.versions, KGProxy)
    resolved_model2 = deepcopy(model).resolve(
        kg_client, release_status="released", follow_links={"versions": {}, "custodians": {"affiliations": {}}}
    )
    assert isinstance(resolved_model2.versions, omcore.ModelVersion)
    assert isinstance(resolved_model2.custodians[0].affiliations[0].member_of, KGProxy)

    resolved_model4 = deepcopy(model).resolve(
        kg_client, release_status="released", follow_links={"custodians": {"affiliations": {"member_of": {}}}}
    )
    assert isinstance(resolved_model4.custodians[0].affiliations[0].member_of, omcore.Organization)


@skip_if_no_connection
def test_retrieve_released_models_follow_links(kg_client):
    models = omcore.Model.list(
        kg_client,
        release_status="released",
        space="model",
        api="query",
        size=5,
        from_index=randint(0, 80),
        follow_links={"versions": {}, "developers": {"affiliations": {"member_of": {}}}, "abstraction_level": {}},
        with_reverse_properties=True,
    )
    assert len(models) == 5
    for model in models:
        # check first level links have been resolved
        for version in as_list(model.versions):
            assert isinstance(version, omcore.ModelVersion)
        if model.abstraction_level:
            assert isinstance(model.abstraction_level, omterms.ModelAbstractionLevel)
        for developer in as_list(model.developers):
            assert isinstance(developer, (omcore.Person, omcore.Organization, omcore.Consortium))
        # check second level links have _not_ been resolved
        for version in as_list(model.versions):
            if version.accessibility:
                assert isinstance(version.accessibility, KGProxy)
            if version.repository:
                assert isinstance(version.repository, KGProxy)


@skip_if_no_connection
def test_retrieve_released_model_versions_no_follow(kg_client):
    for api in ("query", "core"):
        versions = omcore.ModelVersion.list(
            kg_client,
            release_status="released",
            space="model",
            api=api,
            size=5,
            from_index=randint(0, 80),
            with_reverse_properties=True,
        )
        for ver in versions:
            if ver.formats:
                for ct_proxy in as_list(ver.formats):
                    assert isinstance(ct_proxy, KGProxy)
                    assert ct_proxy.classes == [omcore.ContentType]
            if api == "query":
                assert isinstance(ver.is_version_of[0], KGProxy)
                assert ver.is_version_of[0].classes == [omcore.Model]
            else:
                assert isinstance(ver.is_version_of, KGQuery)
                assert ver.is_version_of.classes == [omcore.Model]


@skip_if_no_connection
def test_retrieve_released_model_versions_follow_reverse_links(kg_client):
    versions = omcore.ModelVersion.list(
        kg_client,
        release_status="released",
        space="model",
        api="query",
        size=5,
        from_index=randint(0, 80),
        follow_links={
            "accessibility": {},
            "formats": {},
            "is_version_of": {
                "abstraction_level": {},
                "versions": {},
                "developers": {"affiliation": {"member_of": {}}},
            },
        },
        with_reverse_properties=True,
    )
    for ver in versions:
        # check first level forward links have been resolved
        if ver.accessibility:
            assert isinstance(ver.accessibility, omterms.ProductAccessibility)
        if ver.formats:
            for fmt in as_list(ver.formats):
                assert isinstance(fmt, omcore.ContentType)
        # check first level reverse links have been resolved
        model = ver.is_version_of[0]
        assert isinstance(model, omcore.Model)
        # check forward links from first level reverse links
        assert ver.id in [ver2.id for ver2 in as_list(model.versions)]
        if model.abstraction_level:
            assert isinstance(model.abstraction_level, omterms.ModelAbstractionLevel)
        if model.scope:
            assert isinstance(model.scope, KGProxy)
        for developer in as_list(model.developers):
            assert isinstance(developer, (omcore.Person, omcore.Organization, omcore.Consortium))


# @skip_if_no_connection
# def test_retrieve_released_people_resolve_two_steps(kg_client):
#     people = omcore.Person.list(
#         kg_client,
#         release_status="released",
#         space="common",
#         api="query",
#         size=5,
#         from_index=randint(0, 100),
#         follow_links=2,
#     )
#     assert len(people) == 5


# @skip_if_no_connection
# def test_retrieve_released_models_resolve_two_steps(kg_client):
#     models = omcore.Model.list(kg_client, release_status="released", space="model",
#                                api="query", size=10, from_index=randint(0, 80),
#                                follow_links=2)
#     assert len(models) == 10
#     for model in models:
#         # check first level links have been resolved
#         for version in as_list(model.versions):
#             assert isinstance(version, omcore.ModelVersion)
#         if model.abstraction_level:
#             assert isinstance(model.abstraction_level, omterms.ModelAbstractionLevel)
#         for developer in as_list(model.developers):
#             assert isinstance(developer, (omcore.Person, omcore.Organization, omcore.Consortium))
#         # check second level links have been resolved
#         for version in as_list(model.versions):
#             if version.accessibility:
#                 assert isinstance(version.accessibility, omterms.ProductAccessibility)
#             if version.repository:
#                 assert isinstance(version.repository, omcore.FileRepository)
#         # check third level links have _not_ been resolved
#         for version in as_list(model.versions):
#             if version.repository:
#                 assert isinstance(version.repository.type, KGProxy)
#             if version.hosted_by:
#                 assert isinstance(version.repository.hosted_by, KGProxy)


@skip_if_no_connection
def test_query_across_links(kg_client):
    models = omcore.Model.list(
        kg_client,
        release_status="released",
        space="model",
        api="query",
        follow_links={"developers": {"affiliations": {"member_of": {}}}},
        developers__affiliations__member_of="7bdf4340-c718-45ea-9912-41079799dfd3",
    )
    assert len(models) > 0
    assert len(models) < 100
    for model in models:
        orgs = []
        for dev in as_list(model.developers):
            for affil in as_list(dev.affiliations):
                if affil.member_of:
                    orgs.append(affil.member_of.uuid)
        assert "7bdf4340-c718-45ea-9912-41079799dfd3" in orgs

    # check that "follow_links" is not needed for the cross-link filter to work
    models2 = omcore.Model.list(
        kg_client,
        release_status="released",
        space="model",
        api="query",
        follow_links=None,
        developers__affiliations__member_of="7bdf4340-c718-45ea-9912-41079799dfd3",
    )
    assert set(model.id for model in models) == set(model.id for model in models2)
    assert isinstance(models[0].developers[0], omcore.Person)
    assert isinstance(models2[0].developers[0], KGProxy)


@skip_if_no_connection
def test_query_across_reverse_links(kg_client):
    versions = omcore.ModelVersion.list(
        kg_client,
        release_status="released",
        space="model",
        api="query",
        follow_links={"is_version_of": {"developers": {"affiliations": {"member_of": {}}}}},
        is_version_of__developers__affiliations__member_of="7bdf4340-c718-45ea-9912-41079799dfd3",
    )
    assert len(versions) > 0
    assert len(versions) < 100
    for version in versions:
        orgs = []
        model = version.is_version_of[0]
        for dev in as_list(model.developers):
            for affil in as_list(dev.affiliations):
                if affil.member_of:
                    orgs.append(affil.member_of.uuid)
        assert "7bdf4340-c718-45ea-9912-41079799dfd3" in orgs


@skip_if_no_connection
def test_resolve_reverse_link(kg_client):
    repo = omcore.FileRepository.from_id("c569b826-9d2e-4ba0-9363-561906c67cd6", kg_client)
    files = repo.files.resolve(kg_client)
    assert len(files) == 37


@skip_if_no_connection
def test_count_released_models(kg_client):
    models = omcore.Model.list(kg_client, release_status="released", space="model", api="core", size=1000)
    n_models = omcore.Model.count(kg_client, release_status="released", space="model", api="core")
    assert len(models) == n_models
    assert n_models > 100


@skip_if_no_connection
def test_count_models_with_filters(kg_client):
    # rat = omterms.Species.by_name("Rattus norvegicus", kg_client)
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)

    models = omcore.Model.list(
        kg_client,
        release_status="released",
        space="model",
        api="auto",
        study_targets=ca1,
        model_scope=single_cell,  # note that 'model_scope' is an alias for 'scope'
    )
    n_models = omcore.Model.count(
        kg_client,
        release_status="released",
        space="model",
        api="auto",
        study_targets=ca1,
        model_scope=single_cell,
    )
    assert len(models) == n_models
    assert n_models > 1


@skip_if_no_connection
def test_exists_method_with_known_id(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.existence_query_properties == ("full_name",)

    new_model = omcore.Model(id=model.id)
    assert new_model != model
    assert new_model.exists(kg_client)
    assert new_model == model


@skip_if_no_connection
def test_exists_method_without_id(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.existence_query_properties == ("full_name",)

    new_model = omcore.Model(name=model.name)
    assert new_model != model
    assert new_model.exists(kg_client)
    assert new_model == model


def test__update():
    example_data = {
        "@id": "https://kg.ebrains.eu/api/instances/e90fc25a-fc35-4066-9ff2-ca3583a2d008",
        "@type": "https://openminds.om-i.org/types/Person",
        "http://schema.org/identifier": [
            "ba78ffe138e3a79a7514f26441fba6ff",
            "https://nexus.humanbrainproject.org/v0/data/uniminds/core/person/v1.0.0/e90fc25a-fc35-4066-9ff2-ca3583a2d008",
            "https://kg.ebrains.eu/api/instances/e90fc25a-fc35-4066-9ff2-ca3583a2d008",
        ],
        "https://core.kg.ebrains.eu/vocab/meta/revision": "_fCLxIMC---",
        "https://core.kg.ebrains.eu/vocab/meta/space": "common",
        "https://openminds.om-i.org/props/affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "https://openminds.om-i.org/props/memberOf": {
                    "@id": "https://kg.ebrains.eu/api/instances/05c23d56-b27e-4cf2-8c47-ed12c1a441e7"
                },
            }
        ],
        "https://openminds.om-i.org/props/contactInformation": [
            {"@id": "https://kg.ebrains.eu/api/instances/4b88cd1e-e222-47e9-9b4a-32b648bddbca"},
            {"@id": "https://kg.ebrains.eu/api/instances/bc036c71-084b-4ffa-8430-4543095660f2"},
        ],
        "https://openminds.om-i.org/props/familyName": "Bianchi",
        "https://openminds.om-i.org/props/givenName": "Daniela",
    }
    person = omcore.Person.from_jsonld(example_data, release_status="in progress")
    for key in (
        "http://schema.org/identifier",
        "https://core.kg.ebrains.eu/vocab/meta/revision",
        "https://core.kg.ebrains.eu/vocab/meta/space",
    ):
        example_data.pop(key)
    assert person.remote_data == example_data
    # this follows the sequence in person.save()
    updated_data = person.modified_data()
    assert len(updated_data) == 0


@skip_if_no_connection
def test_KGQuery_resolve(kg_client):
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)
    filters = {"study_targets": ca1, "model_scope": single_cell}
    q = KGQuery(omcore.Model, filters)
    models_q = q.resolve(kg_client, release_status="released")
    models_direct = omcore.Model.list(kg_client, release_status="released", space="model", api="query", **filters)
    assert models_q == models_direct


@skip_if_no_connection
def test_KGQuery_count(kg_client):
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)
    filters = {"study_targets": ca1, "scope": single_cell}
    q = KGQuery(omcore.Model, filters)
    n_models_q = q.count(kg_client, space="model", release_status="released")
    n_models_direct = omcore.Model.count(kg_client, release_status="released", space="model", api="query", **filters)
    assert n_models_q == n_models_direct
    assert n_models_q > 1


def test_to_jsonld():
    person1 = omcore.Person(
        id="0000",
        given_name="Thorin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(name="The Lonely Mountain")),
    )
    expected1 = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "0000",
        "@type": "https://openminds.om-i.org/types/Person",
        "affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "memberOf": {
                    "@type": "https://openminds.om-i.org/types/Organization",
                    "fullName": "The Lonely Mountain",
                },
            }
        ],
        "familyName": "Oakenshield",
        "givenName": "Thorin",
    }
    assert person1.to_jsonld(embed_linked_nodes=True, include_empty_properties=False) == expected1
    with pytest.raises(ValueError) as err:
        person1.to_jsonld(embed_linked_nodes=False, include_empty_properties=False)
        assert "Exporting as a stand-alone JSON-LD document requires @id to be defined" in err

    person2 = omcore.Person(
        id="0000",
        given_name="Thorin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(id="1111", name="The Lonely Mountain")),
    )
    expected2a = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "0000",
        "@type": "https://openminds.om-i.org/types/Person",
        "affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "memberOf": {
                    "@id": "1111",
                    "@type": "https://openminds.om-i.org/types/Organization",
                    "fullName": "The Lonely Mountain",
                },
            }
        ],
        "familyName": "Oakenshield",
        "givenName": "Thorin",
    }
    expected2b = {
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
        "@id": "0000",
        "@type": "https://openminds.om-i.org/types/Person",
        "affiliation": [
            {
                "@type": "https://openminds.om-i.org/types/Affiliation",
                "memberOf": {"@id": "1111"},
            }
        ],
        "familyName": "Oakenshield",
        "givenName": "Thorin",
    }
    assert person2.to_jsonld(embed_linked_nodes=True, include_empty_properties=False) == expected2a
    assert person2.to_jsonld(embed_linked_nodes=False, include_empty_properties=False) == expected2b


@skip_if_using_production_server
def test_save_new_mock(mock_client):
    timestamp = datetime.now()
    new_model = omcore.Model(
        name=f"Dummy new model created for testing at {timestamp}",
        alias=f"DummyModel-{timestamp.isoformat()}",
        abstraction_level=omterms.ModelAbstractionLevel.by_name("protein structure", mock_client),
        custodians=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        description="This model should never actually appear in the KG. If it does, please remove it.",
        developers=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        digital_identifier=None,
        versions=None,
        homepage=IRI("http://example.com"),
        how_to_cite=None,
        scope=omterms.ModelScope.by_name("subcellular", mock_client),
        study_targets=[
            omterms.Species.by_name("Mus musculus", mock_client),
            omterms.CellType.by_name("astrocyte", mock_client),
            omterms.UBERONParcellation.by_name("amygdala", mock_client),
        ],
    )
    log = ActivityLog()
    new_model.save(mock_client, space="myspace", recursive=False, activity_log=log)
    assert len(log.entries) == 1
    assert log.entries[0].cls == "Model"
    assert log.entries[0].space == "myspace"
    assert log.entries[0].type == "create"


@skip_if_using_production_server
def test_save_existing_mock(mock_client):
    timestamp = datetime.now()
    new_model = omcore.Model(
        id="http://example.org/00000000-0000-0000-0000-000000000000",
        name=f"Dummy new model created for testing at {timestamp}",
        alias=f"DummyModel-{timestamp.isoformat()}",
        abstraction_level=omterms.ModelAbstractionLevel.by_name("protein structure", mock_client),
        custodians=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        description="This model should never actually appear in the KG. If it does, please remove it.",
        developers=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        digital_identifier=None,
        versions=None,
        homepage=IRI("http://example.com"),
        how_to_cite=None,
        scope=omterms.ModelScope.by_name("subcellular", mock_client),
        study_targets=[
            omterms.Species.by_name("Mus musculus", mock_client),
            omterms.CellType.by_name("astrocyte", mock_client),
            omterms.UBERONParcellation.by_name("amygdala", mock_client),
        ],
    )
    new_model._space = "model"
    log = ActivityLog()
    new_model.save(mock_client, recursive=False, activity_log=log)
    assert len(log.entries) == 1
    assert log.entries[0].cls == "Model"
    assert log.entries[0].space == "model"
    assert log.entries[0].type == "update"


@skip_if_using_production_server
def test_save_existing_mock_no_updates_allowed(mock_client):
    timestamp = datetime.now()
    new_model = omcore.Model(
        id="http://example.org/00000000-0000-0000-0000-000000000000",
        name=f"Dummy new model created for testing at {timestamp}",
        alias=f"DummyModel-{timestamp.isoformat()}",
        abstraction_level=omterms.ModelAbstractionLevel.by_name("protein structure", mock_client),
        custodians=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        description="This model should never actually appear in the KG. If it does, please remove it.",
        developers=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        digital_identifier=None,
        versions=None,
        homepage=IRI("http://example.com"),
        how_to_cite=None,
        scope=omterms.ModelScope.by_name("subcellular", mock_client),
        study_targets=[
            omterms.Species.by_name("Mus musculus", mock_client),
            omterms.CellType.by_name("astrocyte", mock_client),
            omterms.UBERONParcellation.by_name("amygdala", mock_client),
        ],
    )
    new_model._space = "model"

    new_model.allow_update = False

    log = ActivityLog()
    new_model.save(mock_client, recursive=False, activity_log=log)
    assert len(log.entries) == 1
    assert log.entries[0].type == "no-op"


@skip_if_using_production_server
def test_save_replace_existing_mock(mock_client):
    timestamp = datetime.now()
    new_model = omcore.Model(
        id="http://example.org/00000000-0000-0000-0000-000000000000",
        name=f"Dummy new model created for testing at {timestamp}",
        alias=f"DummyModel-{timestamp.isoformat()}",
        abstraction_level=omterms.ModelAbstractionLevel.by_name("protein structure", mock_client),
        custodians=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        description="This model should never actually appear in the KG. If it does, please remove it.",
        developers=omcore.Person(given_name="Bilbo", family_name="Baggins", id="fake_uuid", space="common"),
        digital_identifier=None,
        versions=None,
        homepage=IRI("http://example.com"),
        how_to_cite=None,
        scope=omterms.ModelScope.by_name("subcellular", mock_client),
        study_targets=[
            omterms.Species.by_name("Mus musculus", mock_client),
            omterms.CellType.by_name("astrocyte", mock_client),
            omterms.UBERONParcellation.by_name("amygdala", mock_client),
        ],
    )
    new_model._space = "model"
    log = ActivityLog()
    new_model.save(mock_client, recursive=False, replace=True, activity_log=log)
    assert len(log.entries) == 1
    assert log.entries[0].cls == "Model"
    assert log.entries[0].space == "model"
    assert log.entries[0].type == "replacement"


@skip_if_using_production_server
def test_save_new_recursive_mock(mock_client):
    new_person = omcore.Person(
        given_name="Thorin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(name="The Lonely Mountain")),
    )
    log = ActivityLog()
    new_person.save(mock_client, space="myspace", recursive=True, activity_log=log)
    assert len(log.entries) == 2
    assert log.entries[0].cls == "Organization"
    assert log.entries[0].space == "myspace"
    assert log.entries[0].type == "create"
    assert log.entries[1].cls == "Person"
    assert log.entries[1].space == "myspace"
    assert log.entries[1].type == "create"
    assert UUID(new_person.uuid)
    assert UUID(new_person.affiliations.member_of.uuid)


# def test_save_existing_with_id_mock(mock_client):
#    existing_model = mock_client.instances[]


def test_normalize_filter():
    result = omcore.Model.normalize_filter(
        {
            "developers": {"affiliations": {"member_of": omcore.Organization(id="some_id")}},
            "digital_identifier": {"identifier": "https://doi.org/some-doi"},
        }
    )
    expected = {
        "developers": {"affiliations": {"member_of": "some_id"}},
        "digital_identifier": {"identifier": "https://doi.org/some-doi"},
    }
    assert result == expected


def test_normalize_filter_with_invalid_keys():
    with pytest.raises(ValueError) as excinfo:
        omcore.ModelVersion.normalize_filter(
            {"authors": {"given_name": "Zaphod"}, "documentation": {"iri": "http://example.org"}}
        )  # should be "developers", "full_documentation"
    assert str(excinfo.value) == "Invalid filters: authors, documentation"
    with pytest.raises(ValueError) as excinfo:
        omcore.ModelVersion.normalize_filter(
            {"developers": {"digital_identifiers": {"id": "https://orcid.org/some-id"}}}
        )  # should be "identifier", not "id"
    assert str(excinfo.value) == "Invalid filter: id"


def test_class_docstring():
    assert "email address" in omcore.Person.__doc__


def test_property_names():
    assert omcore.Person.property_names == [
        "affiliations",
        "alternate_names",
        "associated_accounts",
        "contact_information",
        "digital_identifiers",
        "family_name",
        "given_name",
    ]
    assert omcore.Person.reverse_property_names == [
        "activities",
        "comments",
        "coordinated_projects",
        "developed",
        "funded",
        "is_custodian_of",
        "is_owner_of",
        "is_provider_of",
        "manufactured",
        "published",
        "started",
    ]
    assert omcore.Person.required_property_names == ["given_name"]


def test_diff():
    person1 = omcore.Person(
        id="0000",
        given_name="Thorin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(id="1000", name="The Lonely Mountain")),
    )
    person2 = omcore.Person(
        given_name="Thorin son of Thráin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(id="1001", name="Erebor")),
    )
    expected = {
        "id": ("0000", None),
        "properties": {
            "given_name": ("Thorin", "Thorin son of Thráin"),
            "affiliations": (
                omcore.Affiliation(member_of=omcore.Organization(id="1000", name="The Lonely Mountain")),
                omcore.Affiliation(member_of=omcore.Organization(id="1001", name="Erebor")),
            ),
        },
    }
    assert person1.diff(person2) == expected

    assert person1.affiliations.member_of.diff(person2) == {"type": (omcore.Organization, omcore.Person)}


def test_show():
    # todo: capture stdout
    person1 = omcore.Person(
        id="0000",
        given_name="Thorin",
        family_name="Oakenshield",
        affiliations=omcore.Affiliation(member_of=omcore.Organization(name="The Lonely Mountain")),
    )
    person1.show()
    person1.show(max_width=120)


def test_file_download():
    file_obj = omcore.File(
        name="installation.rst",
        iri=IRI("https://raw.githubusercontent.com/HumanBrainProject/fairgraph/master/doc/installation.rst"),
        hashes=omcore.Hash(algorithm="SHA1", digest="7c97abf3c007bfa58d58e09c0e497ceffd93bd11"),
    )
    local_dir = tempfile.mkdtemp()

    # test download to a directory
    local_filename = file_obj.download(local_dir, client=None, accept_terms_of_use=True)
    assert str(local_filename) == os.path.join(local_dir, file_obj.name)
    assert sha1sum(local_filename) == file_obj.hashes.digest

    # test download to a specific filename
    local_filename_expected = os.path.join(local_dir, "installation1.rst")
    local_filename = file_obj.download(local_filename_expected, client=None, accept_terms_of_use=True)
    assert str(local_filename) == local_filename_expected
    assert sha1sum(local_filename) == file_obj.hashes.digest

    shutil.rmtree(local_dir)


def test_file_from_local_file():
    file_obj = omcore.File.from_local_file("test/utils.py")
    assert file_obj.name == "test/utils.py"
    assert file_obj.storage_size.value == float(os.stat("test/utils.py").st_size)
    assert file_obj.format.name == "text/x-python"
    assert file_obj.hashes.digest == sha1sum("test/utils.py")


@skip_if_no_connection
def test_dataset_version_download(mocker):
    mock_urlretrieve = mocker.patch(
        "fairgraph.openminds.core.products.dataset_version.urlretrieve",
        lambda url, local_filename: (local_filename, None),
    )
    fake_dsv = omcore.DatasetVersion(
        repository=omcore.FileRepository(iri=IRI("https://data-proxy.ebrains.eu/api/v1/public/foo/bar"))
    )
    local_dir = tempfile.mkdtemp()
    local_filename, repository_url = fake_dsv.download(local_dir, client=None, accept_terms_of_use=True)
    os.rmdir(local_dir)
    assert repository_url == "https://data-proxy.ebrains.eu/api/v1/public/foo/bar"
    assert str(local_filename) == os.path.join(local_dir, "bar.zip")


@skip_if_no_connection
def test_person_me(kg_client):
    person = omcore.Person.me(kg_client, allow_multiple=False)
    # the following assumes that anyone running these tests is represented in the KG
    assert isinstance(person, omcore.Person)


# def test_children():


def test_with_new_namespace_from_core():
    data = {
        "https://openminds.om-i.org/props/hasVersion": {
            "@id": "https://kg.ebrains.eu/api/instances/7035d53f-1597-4a45-9f72-23c2c933ec66"
        },
        "@type": "https://openminds.om-i.org/types/Model",
        "https://openminds.om-i.org/props/description": "The scaffolding procedure has been enhanced compared to version 1.0. It's able to generate a scalable cerebellar structure, embedding specific 3D positions for each neuron and specific pair connections. Customized placement strategies allow to match layered density and encumbrance for each neuron type. Customized connection strategies allow to match anisotropic geometrical fields of intersection, and statistical convergence and divergence ratios.\nThe scaffold can host different neuron models. Several input stimulation patterns can be used to investigate network complex dynamics, revealing the relationships between structural constraints and underlying neuron mechanisms with the cerebellar circuit functioning, over space and time.\n\nMain link to Sonata conversion can be found here:\nhttps://github.com/SelezioneCasuale/scaffold/tree/sonata-version/scaffold",
        "https://openminds.om-i.org/props/studyTarget": [
            {"@id": "https://kg.ebrains.eu/api/instances/ab532423-1fd7-4255-8c6f-f99dc6df814f"},
            {"@id": "https://kg.ebrains.eu/api/instances/a70b0307-22fc-4730-a61f-fd279f43a3cf"},
        ],
        "https://core.kg.ebrains.eu/vocab/meta/revision": "_hEUXXvy--q",
        "https://openminds.om-i.org/props/custodian": [
            {"@id": "https://kg.ebrains.eu/api/instances/2905ce6c-bc89-4c99-b8b0-0fa9a17d1897"},
            {"@id": "https://kg.ebrains.eu/api/instances/3477f916-5494-42ae-8b07-d2cb48231657"},
            {"@id": "https://kg.ebrains.eu/api/instances/a594cfe2-f53a-470f-b52e-697b8d5a8958"},
            {"@id": "https://kg.ebrains.eu/api/instances/5dcb9bd9-f93f-48c4-88e0-ff0ed4221ac8"},
            {"@id": "https://kg.ebrains.eu/api/instances/5ad4749a-6e5a-4512-86ff-b89834c1b87c"},
        ],
        "https://openminds.om-i.org/props/developer": [
            {"@id": "https://kg.ebrains.eu/api/instances/2905ce6c-bc89-4c99-b8b0-0fa9a17d1897"},
            {"@id": "https://kg.ebrains.eu/api/instances/3477f916-5494-42ae-8b07-d2cb48231657"},
            {"@id": "https://kg.ebrains.eu/api/instances/a594cfe2-f53a-470f-b52e-697b8d5a8958"},
            {"@id": "https://kg.ebrains.eu/api/instances/5dcb9bd9-f93f-48c4-88e0-ff0ed4221ac8"},
            {"@id": "https://kg.ebrains.eu/api/instances/5ad4749a-6e5a-4512-86ff-b89834c1b87c"},
        ],
        "https://openminds.om-i.org/props/fullName": "Scaffold Model of Cerebellum microcircuit version 2.0",
        "https://core.kg.ebrains.eu/vocab/meta/space": "model",
        "https://openminds.om-i.org/props/abstractionLevel": {
            "@id": "https://kg.ebrains.eu/api/instances/57becc19-f0a1-4d23-99bb-eb3b7d3cdb9a"
        },
        "@id": "https://kg.ebrains.eu/api/instances/708024f7-9dd7-4c92-ae95-936db23c6d99",
        "https://openminds.om-i.org/props/scope": {
            "@id": "https://kg.ebrains.eu/api/instances/6c678004-b8e0-4339-90c5-824e66503eb9"
        },
        "http://schema.org/identifier": ["https://kg.ebrains.eu/api/instances/708024f7-9dd7-4c92-ae95-936db23c6d99"],
        "https://core.kg.ebrains.eu/vocab/meta/firstReleasedAt": "2022-02-04T15:11:40.157Z",
        "https://core.kg.ebrains.eu/vocab/meta/lastReleasedAt": "2023-03-23T10:09:30.130Z",
    }
    orig_type = omcore.Model.type_
    obj = omcore.Model.from_jsonld(data, release_status="released")
    assert obj.abstraction_level
    assert len(obj.developers) == 5
    omcore.Model.type_ = orig_type


def test_with_new_namespace_from_query():
    data = {
        "@id": "https://kg.ebrains.eu/api/instances/708024f7-9dd7-4c92-ae95-936db23c6d99",
        "https://schema.hbp.eu/myQuery/space": "model",
        "@type": "https://openminds.om-i.org/types/Model",
        "abstractionLevel": {"@id": "https://kg.ebrains.eu/api/instances/57becc19-f0a1-4d23-99bb-eb3b7d3cdb9a"},
        "custodian": [
            {
                "@id": "https://kg.ebrains.eu/api/instances/2905ce6c-bc89-4c99-b8b0-0fa9a17d1897",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/3477f916-5494-42ae-8b07-d2cb48231657",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/a594cfe2-f53a-470f-b52e-697b8d5a8958",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/5dcb9bd9-f93f-48c4-88e0-ff0ed4221ac8",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/5ad4749a-6e5a-4512-86ff-b89834c1b87c",
                "@type": "https://openminds.om-i.org/types/Person",
            },
        ],
        "description": "The scaffolding procedure has been enhanced compared to version 1.0. It's able to generate a scalable cerebellar structure, embedding specific 3D positions for each neuron and specific pair connections. Customized placement strategies allow to match layered density and encumbrance for each neuron type. Customized connection strategies allow to match anisotropic geometrical fields of intersection, and statistical convergence and divergence ratios.\nThe scaffold can host different neuron models. Several input stimulation patterns can be used to investigate network complex dynamics, revealing the relationships between structural constraints and underlying neuron mechanisms with the cerebellar circuit functioning, over space and time.\n\nMain link to Sonata conversion can be found here:\nhttps://github.com/SelezioneCasuale/scaffold/tree/sonata-version/scaffold",
        "developer": [
            {
                "@id": "https://kg.ebrains.eu/api/instances/2905ce6c-bc89-4c99-b8b0-0fa9a17d1897",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/3477f916-5494-42ae-8b07-d2cb48231657",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/a594cfe2-f53a-470f-b52e-697b8d5a8958",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/5dcb9bd9-f93f-48c4-88e0-ff0ed4221ac8",
                "@type": "https://openminds.om-i.org/types/Person",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/5ad4749a-6e5a-4512-86ff-b89834c1b87c",
                "@type": "https://openminds.om-i.org/types/Person",
            },
        ],
        "digitalIdentifier": [],
        "fullName": "Scaffold Model of Cerebellum microcircuit version 2.0",
        "hasVersion": [
            {
                "@id": "https://kg.ebrains.eu/api/instances/7035d53f-1597-4a45-9f72-23c2c933ec66",
                "@type": "https://openminds.om-i.org/types/ModelVersion",
            }
        ],
        "homepage": None,
        "howToCite": None,
        "scope": [
            {
                "@id": "https://kg.ebrains.eu/api/instances/6c678004-b8e0-4339-90c5-824e66503eb9",
                "@type": "https://openminds.om-i.org/types/ModelScope",
            }
        ],
        "shortName": None,
        "studyTarget": [
            {
                "@id": "https://kg.ebrains.eu/api/instances/ab532423-1fd7-4255-8c6f-f99dc6df814f",
                "@type": "https://openminds.om-i.org/types/Species",
            },
            {
                "@id": "https://kg.ebrains.eu/api/instances/a70b0307-22fc-4730-a61f-fd279f43a3cf",
                "@type": "https://openminds.om-i.org/types/UBERONParcellation",
            },
        ],
        "about": [],
        "hasPart": [],
        "@context": {"@vocab": "https://openminds.om-i.org/props/"},
    }
    # omcore.set_error_handling("error")
    orig_types = (omcore.Model.type_, omcore.Person.type_)
    obj = omcore.Model.from_jsonld(data, release_status="released")
    assert obj.abstraction_level
    assert len(obj.developers) == 5
    omcore.Model.type_, omcore.Person.type_ = orig_types
