
import json
from random import randint
from uuid import UUID
from copy import deepcopy
from fairgraph.base_v3 import as_list, IRI, KGProxy, KGQuery
import fairgraph.openminds.core as omcore
import fairgraph.openminds.controlledterms as omterms

from test.utils_v3 import mock_client, kg_client


def test_query_generation(mock_client):
    for cls in omcore.list_kg_classes():
        generated = cls.generate_query("simple", "collab-foobar", mock_client)
        filename = f"test/test_data/queries/openminds/core/{cls.__name__.lower()}_simple_query.json"
        with open(filename, "r") as fp:
            expected = json.load(fp)
        assert generated == expected


def test_retrieve_released_models_no_filter_api_core(kg_client):
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="core", size=20, from_index=randint(0, 80))
    assert len(models) == 20
    for m in models:
        assert m.space == "model"


def test_retrieve_released_models_no_filter_api_query(kg_client):
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="query", size=20, from_index=randint(0, 80))
    assert len(models) == 20


def test_retrieve_released_models_filter_species_by_obj(kg_client):
    rat = omterms.Species.by_name("Rattus norvegicus", kg_client)
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="query", study_targets=rat)
    assert len(models) > 0
    for model in models:
        study_targets = model.study_targets.resolve(kg_client, scope="released")
        if study_targets:
            assert rat in as_list(study_targets)


def test_retrieve_released_models_filter_species_by_uuid(kg_client):
    human = omterms.Species.by_name("Homo sapiens", kg_client)
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="query", study_targets=UUID(human.uuid))
    assert len(models) > 0
    for model in models:
        if model.study_targets:
            assert human.id in [st.id for st in as_list(model.study_targets)]


def test_retrieve_released_models_filter_species_by_id(kg_client):
    mouse = omterms.Species.by_name("Mus musculus", kg_client)
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="query", study_targets=IRI(mouse.id))
    # todo: fix so that don't need to wrap the id in an IRI
    assert len(models) > 0
    for model in models:
        if model.study_targets:
            assert mouse.id in [st.id for st in as_list(model.study_targets)]


def test_retrieve_released_models_filter_custodian(kg_client):
    alain = omcore.Person.list(kg_client, family_name="Destexhe", given_name="Alain")[0]
    assert alain.given_name == "Alain"
    models = omcore.Model.list(kg_client, scope="released", space="model", 
                               api="query", custodians=alain)
    assert len(models) > 0
    for model in models:
        assert alain.id in [c.id for c in as_list(model.custodians)]


def test_resolve_model(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.name == "Scaffold Model of Cerebellum microcircuit version 2.0"
    assert isinstance(model.versions, KGProxy)
    resolved_model2 = deepcopy(model).resolve(kg_client, scope="in progress", follow_links=2)
    assert isinstance(resolved_model2.versions, omcore.ModelVersion)
    assert isinstance(resolved_model2.custodians[0].affiliations[0].organization, KGProxy)

    resolved_model4 = deepcopy(model).resolve(kg_client, scope="in progress", follow_links=3)
    assert isinstance(resolved_model4.custodians[0].affiliations[0].organization, omcore.Organization)


def test_count_released_models(kg_client):
    models = omcore.Model.list(kg_client, scope="released", space="model", api="core", size=1000)
    n_models = omcore.Model.count(kg_client, scope="released", space="model", api="core")
    assert len(models) == n_models
    assert n_models > 100


def test_count_models_with_filters(kg_client):
    #rat = omterms.Species.by_name("Rattus norvegicus", kg_client)
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)

    models = omcore.Model.list(kg_client, scope="released", space="model", api="query", study_targets=ca1, model_scope=single_cell)
    n_models = omcore.Model.count(kg_client, scope="released", space="model", api="query", study_targets=ca1, model_scope=single_cell)
    assert len(models) == n_models
    assert n_models > 1


def test_exists_method_with_known_id(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.existence_query_fields == ("name",)

    new_model = omcore.Model(id=model.id)
    assert new_model != model
    assert new_model.exists(kg_client)
    assert new_model == model


def test_exists_method_without_id(kg_client):
    model = omcore.Model.from_id("708024f7-9dd7-4c92-ae95-936db23c6d99", kg_client)
    assert model.existence_query_fields == ("name",)

    new_model = omcore.Model(name=model.name)
    assert new_model != model
    assert new_model.exists(kg_client)
    assert new_model == model



def test_KGQuery_resolve(kg_client):
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)
    filters = {"study_targets": ca1, "model_scope": single_cell}
    q = KGQuery(omcore.Model, filters)
    models_q = q.resolve(kg_client, scope="released")
    models_direct = omcore.Model.list(kg_client, scope="released", space="model", api="query", **filters)
    assert models_q == models_direct


def test_KGQuery_count(kg_client):
    ca1 = omterms.UBERONParcellation.by_name("CA1 field of hippocampus", kg_client)
    single_cell = omterms.ModelScope.by_name("single cell", kg_client)
    filters = {"study_targets": ca1, "model_scope": single_cell}
    q = KGQuery(omcore.Model, filters)
    n_models_q = q.count(kg_client, space="model", scope="released")
    n_models_direct = omcore.Model.count(kg_client, scope="released", space="model", api="query", **filters)
    assert n_models_q == n_models_direct
    assert n_models_q > 1
