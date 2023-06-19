import os
import json
import pytest
from kg_core.request import Stage, Pagination
from fairgraph.queries import Query, QueryProperty, Filter
import fairgraph.openminds.core as omcore
from .utils import kg_client, mock_client, skip_if_no_connection


@pytest.fixture()
def example_query_model_version():
    return Query(
        node_type="https://openminds.ebrains.eu/core/ModelVersion",
        label="fg-testing-modelversion",
        space="model",
        properties=[
            QueryProperty("@type"),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/fullName",
                name="vocab:fullName",
                filter=Filter("CONTAINS", parameter="name"),
                sorted=True,
                required=True,
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/versionIdentifier",
                name="vocab:versionIdentifier",
                filter=Filter("EQUALS", parameter="version"),
                required=True,
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/format",
                name="vocab:format",
                ensure_order=True,
                properties=[
                    QueryProperty("@id", filter=Filter("EQUALS", parameter="format")),
                    QueryProperty("@type"),
                ],
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/custodian",
                name="vocab:custodian",
                ensure_order=True,
                type_filter="https://openminds.ebrains.eu/core/Person",
                properties=[
                    QueryProperty("@id", filter=Filter("EQUALS", parameter="custodian")),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/affiliation",
                        name="vocab:affiliation",
                        properties=[
                            QueryProperty("@type"),
                            QueryProperty(
                                "https://openminds.ebrains.eu/vocab/memberOf",
                                name="vocab:memberOf",
                                properties=[QueryProperty("@id")],
                            ),
                            QueryProperty(
                                "https://openminds.ebrains.eu/vocab/startDate",
                                name="vocab:startDate",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


@pytest.fixture()
def example_query_model():
    return Query(
        node_type="https://openminds.ebrains.eu/core/Model",
        label="fg-testing-model",
        space="model",
        properties=[
            QueryProperty("@type"),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/fullName",
                name="vocab:fullName",
                filter=Filter("CONTAINS", parameter="name"),
                sorted=True,
                required=True,
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/custodian",
                name="vocab:custodian",
                type_filter="https://openminds.ebrains.eu/core/Person",
                properties=[
                    # QueryProperty("@type"),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/familyName",
                        name="vocab:familyName",
                    ),
                ],
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/custodian",
                name="vocab:organization",
                type_filter="https://openminds.ebrains.eu/core/Organization",
                properties=[
                    # QueryProperty("@type"),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/shortName",
                        name="vocab:shortName",
                    ),
                ],
            ),
        ],
    )


@pytest.fixture()
def example_query_repository_with_reverse():
    return Query(
        node_type="https://openminds.ebrains.eu/core/FileRepository",
        properties=[
            QueryProperty("https://openminds.ebrains.eu/vocab/IRI", name="location"),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/fileRepository",
                reverse=True,
                name="files",
                properties=[
                    QueryProperty("https://openminds.ebrains.eu/vocab/name", name="filename"),
                    QueryProperty(
                        [
                            "https://openminds.ebrains.eu/vocab/format",
                            "https://openminds.ebrains.eu/vocab/name",
                        ],
                        name="format",
                    ),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/hash",
                        name="hash",
                        properties=[
                            QueryProperty(
                                "https://openminds.ebrains.eu/vocab/digest",
                                name="digest",
                            ),
                            QueryProperty(
                                "https://openminds.ebrains.eu/vocab/algorithm",
                                name="algorithm",
                            ),
                        ],
                    ),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/storageSize",
                        name="size",
                        expect_single=True,
                        properties=[
                            QueryProperty("https://openminds.ebrains.eu/vocab/value", name="value"),
                            QueryProperty(
                                [
                                    "https://openminds.ebrains.eu/vocab/unit",
                                    "https://openminds.ebrains.eu/vocab/name",
                                ],
                                name="units",
                                expect_single=True,
                            ),
                        ],
                    ),
                ],
            ),
            QueryProperty(
                "https://openminds.ebrains.eu/vocab/repository",
                reverse=True,
                required=True,
                name="contains_dataset_version",
                properties=[
                    QueryProperty("@id"),
                    QueryProperty(
                        "https://openminds.ebrains.eu/vocab/shortName",
                        name="alias",
                        filter=Filter("EQUALS", parameter="dataset_alias"),
                    ),
                ],
            ),
        ],
    )


def test_query_builder(example_query_model_version):
    generated = example_query_model_version.serialize()
    expected = {
        "@context": {
            "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
            "path": {"@id": "path", "@type": "@id"},
            "merge": {"@id": "merge", "@type": "@id"},
            "propertyName": {"@id": "propertyName", "@type": "@id"},
            "query": "https://schema.hbp.eu/myQuery/",
        },
        "meta": {
            "description": "Automatically generated by fairgraph",
            "name": "fg-testing-modelversion",
            "type": "https://openminds.ebrains.eu/core/ModelVersion",
        },
        "structure": [
            {
                "filter": {"op": "EQUALS", "parameter": "id"},
                "path": "@id",
            },
            {
                "filter": {"op": "EQUALS", "value": "model"},
                "path": "https://core.kg.ebrains.eu/vocab/meta/space",
                "propertyName": "query:space",
            },
            {"path": "@type"},
            {
                "filter": {"op": "CONTAINS", "parameter": "name"},
                "path": "https://openminds.ebrains.eu/vocab/fullName",
                "propertyName": "vocab:fullName",
                "required": True,
                "sort": True,
            },
            {
                "filter": {"op": "EQUALS", "parameter": "version"},
                "path": "https://openminds.ebrains.eu/vocab/versionIdentifier",
                "propertyName": "vocab:versionIdentifier",
                "required": True,
            },
            {
                "ensureOrder": True,
                "path": "https://openminds.ebrains.eu/vocab/format",
                "propertyName": "vocab:format",
                "structure": [
                    {"filter": {"op": "EQUALS", "parameter": "format"}, "path": "@id"},
                    {"path": "@type"},
                ],
            },
            {
                "ensureOrder": True,
                "path": {
                    "@id": "https://openminds.ebrains.eu/vocab/custodian",
                    "typeFilter": {"@id": "https://openminds.ebrains.eu/core/Person"},
                },
                "propertyName": "vocab:custodian",
                "structure": [
                    {
                        "filter": {"op": "EQUALS", "parameter": "custodian"},
                        "path": "@id",
                    },
                    {
                        "path": "https://openminds.ebrains.eu/vocab/affiliation",
                        "propertyName": "vocab:affiliation",
                        "structure": [
                            {"path": "@type"},
                            {
                                "path": "https://openminds.ebrains.eu/vocab/memberOf",
                                "propertyName": "vocab:memberOf",
                                "structure": [{"path": "@id"}],
                            },
                            {
                                "path": "https://openminds.ebrains.eu/vocab/startDate",
                                "propertyName": "vocab:startDate",
                            },
                        ],
                    },
                ],
            },
        ],
    }
    assert generated == expected


def test_query_with_reverse_fields(example_query_repository_with_reverse):
    generated = example_query_repository_with_reverse.serialize()
    expected = {
        "@context": {
            "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
            "query": "https://schema.hbp.eu/myQuery/",
            "merge": {"@id": "merge", "@type": "@id"},
            "propertyName": {"@id": "propertyName", "@type": "@id"},
            "path": {"@id": "path", "@type": "@id"},
        },
        "meta": {
            "type": "https://openminds.ebrains.eu/core/FileRepository",
            "description": "Automatically generated by fairgraph",
        },
        "structure": [
            {"filter": {"op": "EQUALS", "parameter": "id"}, "path": "@id"},
            {
                "path": "https://core.kg.ebrains.eu/vocab/meta/space",
                "propertyName": "query:space",
            },
            {
                "propertyName": "location",
                "path": "https://openminds.ebrains.eu/vocab/IRI",
            },
            {
                "propertyName": "files",
                "path": {
                    "@id": "https://openminds.ebrains.eu/vocab/fileRepository",
                    "reverse": True,
                },
                "structure": [
                    {
                        "propertyName": "filename",
                        "path": "https://openminds.ebrains.eu/vocab/name",
                    },
                    {
                        "propertyName": "format",
                        "path": [
                            "https://openminds.ebrains.eu/vocab/format",
                            "https://openminds.ebrains.eu/vocab/name",
                        ],
                    },
                    {
                        "propertyName": "hash",
                        "path": "https://openminds.ebrains.eu/vocab/hash",
                        "structure": [
                            {
                                "propertyName": "digest",
                                "path": "https://openminds.ebrains.eu/vocab/digest",
                            },
                            {
                                "propertyName": "algorithm",
                                "path": "https://openminds.ebrains.eu/vocab/algorithm",
                            },
                        ],
                    },
                    {
                        "propertyName": "size",
                        "path": "https://openminds.ebrains.eu/vocab/storageSize",
                        "singleValue": "FIRST",
                        "structure": [
                            {
                                "propertyName": "value",
                                "path": "https://openminds.ebrains.eu/vocab/value",
                            },
                            {
                                "propertyName": "units",
                                "singleValue": "FIRST",
                                "path": [
                                    "https://openminds.ebrains.eu/vocab/unit",
                                    "https://openminds.ebrains.eu/vocab/name",
                                ],
                            },
                        ],
                    },
                ],
            },
            {
                "path": {"@id": "https://openminds.ebrains.eu/vocab/repository", "reverse": True},
                "propertyName": "contains_dataset_version",
                "required": True,
                "structure": [
                    {"path": "@id"},
                    {
                        "filter": {"op": "EQUALS", "parameter": "dataset_alias"},
                        "path": "https://openminds.ebrains.eu/vocab/shortName",
                        "propertyName": "alias",
                    },
                ],
            },
        ],
    }
    assert generated == expected


@skip_if_no_connection
def test_execute_query(kg_client, example_query_model_version):
    response = kg_client._kg_client.queries.test_query(
        payload=example_query_model_version.serialize(),
        stage=Stage.IN_PROGRESS,
        pagination=Pagination(start=0, size=3),
    )
    data = response.data
    assert len(data) == 3
    expected_keys = set(
        [
            "@id",
            "@type",
            "https://schema.hbp.eu/myQuery/space",
            "vocab:custodian",
            "vocab:format",
            "vocab:versionIdentifier",
            "vocab:fullName",
        ]
    )
    data0 = data[0]
    assert set(data0.keys()) == expected_keys

    if data0["vocab:custodian"]:
        custodian0 = data0["vocab:custodian"][0]
        assert set(custodian0.keys()) == set(["@id", "vocab:affiliation"])
        if custodian0["vocab:affiliation"]:
            affil0 = custodian0["vocab:affiliation"][0]
            assert set(affil0.keys()) == set(["@type", "vocab:memberOf", "vocab:startDate"])


@skip_if_no_connection
def test_execute_query_with_id_filter(kg_client, example_query_model):
    target_id = "https://kg.ebrains.eu/api/instances/3ca9ae35-c9df-451f-ac76-4925bd2c7dc6"
    response = kg_client._kg_client.queries.test_query(
        payload=example_query_model.serialize(),
        instance_id=kg_client.uuid_from_uri(target_id),
        stage=Stage.IN_PROGRESS,
        pagination=Pagination(start=0, size=10),
    )
    data = response.data
    assert len(data) == 1
    assert data[0]["vocab:fullName"] == "AdEx Neuron Models with PyNN"
    assert data[0]["vocab:custodian"][0]["vocab:familyName"] == "Destexhe"
    # assert data[0]["vocab:organization"][0]["vocab:shortName"] == "Destexhe Lab"


@skip_if_no_connection
def test_execute_query_with_reverse_fields_and_instance_id(kg_client, example_query_repository_with_reverse):
    target_id = "https://kg.ebrains.eu/api/instances/2f8d64f3-d848-49bd-baa6-a2c7080c98da"
    response = kg_client._kg_client.queries.test_query(
        payload=example_query_repository_with_reverse.serialize(),
        instance_id=kg_client.uuid_from_uri(target_id),
        stage=Stage.IN_PROGRESS,
        pagination=Pagination(start=0, size=10),
    )
    data = response.data
    assert len(data) == 1
    assert (
        data[0]["location"]
        == "https://object.cscs.ch/v1/AUTH_7e4157014a3d4c1f8ffe270b57008fd4/brette-etal-2007?prefix=Benchmark2"
    )
    assert "VAbenchmarks" in data[0]["files"][0]["filename"]
    assert data[0]["files"][5]["hash"][0]["algorithm"] == "MD5"


@skip_if_no_connection
def test_execute_query_with_reverse_fields_and_filter(kg_client, example_query_repository_with_reverse):
    response = kg_client._kg_client.queries.test_query(
        payload=example_query_repository_with_reverse.serialize(),
        additional_request_params={"dataset_alias": "data-brette-etal-2007-benchmark2-v1"},
        stage=Stage.IN_PROGRESS,
        pagination=Pagination(start=0, size=10),
    )
    data = response.data
    assert len(data) == 1
    assert (
        data[0]["location"]
        == "https://object.cscs.ch/v1/AUTH_7e4157014a3d4c1f8ffe270b57008fd4/brette-etal-2007?prefix=Benchmark2"
    )
    assert "VAbenchmarks" in data[0]["files"][0]["filename"]
    assert data[0]["files"][5]["hash"][0]["algorithm"] == "MD5"
    assert data[0]["contains_dataset_version"][0]["alias"] == "data-brette-etal-2007-benchmark2-v1"


def test_openminds_core_queries(mock_client):
    for cls in omcore.list_kg_classes():
        path_expected = os.path.join(
            os.path.dirname(__file__),
            "test_data",
            "queries",
            "openminds",
            "core",
            f"{cls.__name__.lower()}_simple_query.json",
        )
        with open(path_expected) as fp:
            generated = cls.generate_query(
                space="collab-foobar",
                client=mock_client,
                follow_links=None,
            )
            expected = json.load(fp)
            assert generated == expected


def test_generate_query_with_follow_one_link(mock_client):
    for cls in (omcore.Person,):
        path_expected = os.path.join(
            os.path.dirname(__file__),
            "test_data",
            "queries",
            "openminds",
            "core",
            f"{cls.__name__.lower()}_resolved-1_query.json",
        )
        with open(path_expected) as fp:
            generated = cls.generate_query(
                space=None,
                client=mock_client,
                filters=None,
                follow_links={
                    "affiliations": {"member_of": {}},
                    "associated_accounts": {},
                    "contact_information": {},
                    "digital_identifiers": {},
                },
            )
            expected = json.load(fp)
            assert generated == expected


def test_generate_query_with_follow_named_links(mock_client):
    cls = omcore.Person
    path_expected = os.path.join(
        os.path.dirname(__file__),
        "test_data",
        "queries",
        "openminds",
        "core",
        f"{cls.__name__.lower()}_newstyle_query.json",
    )
    with open(path_expected) as fp:
        generated = cls.generate_query(
            space=None,
            client=mock_client,
            filters={"affiliations__member_of__has_parents__alias": "FZJ"},
            follow_links={"affiliations": {"member_of": {"has_parents": {}}}, "contact_information": {}},
        )
        expected = json.load(fp)
        assert generated == expected
