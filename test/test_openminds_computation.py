from fairgraph.openminds.computation import Environment

from test.utils_v3 import mock_client


class TestEnvironment:
    def test_generate_query(self, mock_client):
        generated = Environment.generate_query(
            "simple", "myspace", mock_client,
            filter_keys=["name", "hardware", "configuration", "software", "description"])
        expected = {
            "@context": {
                "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
                "merge": {"@id": "merge", "@type": "@id"},
                "path": {"@id": "path", "@type": "@id"},
                "propertyName": {"@id": "propertyName", "@type": "@id"},
                "query": "https://schema.hbp.eu/myQuery/",
            },
            "meta": {
                "description": "Automatically generated by fairgraph",
                "name": "fg-Environment-simple-myspace-filters-configuration-description-hardware-name-software",
                "type": "https://openminds.ebrains.eu/computation/Environment",
            },
            "structure": [
                {"filter": {"op": "EQUALS", "parameter": "id"}, "path": "@id"},
                {
                    "filter": {"op": "EQUALS", "value": "myspace_1234"},
                    "path": "https://core.kg.ebrains.eu/vocab/meta/space",
                    "propertyName": "query:space",
                },
                {"path": "@type"},
                {
                    "filter": {"op": "CONTAINS", "parameter": "name"},
                    "path": "https://openminds.ebrains.eu/vocab/name",
                    "propertyName": "vocab:name",
                    "required": True,
                    "sort": True,
                },
                {
                    "path": "https://openminds.ebrains.eu/vocab/configuration",
                    "propertyName": "vocab:configuration",
                    "required": True,
                    "structure": [
                        {"filter": {"op": "CONTAINS", "parameter": "configuration"},
                         "path": "@id"},
                        {"path": "@type"}
                    ],
                },
                {
                    "filter": {"op": "CONTAINS", "parameter": "description"},
                    "path": "https://openminds.ebrains.eu/vocab/description",
                    "propertyName": "vocab:description",
                    "required": True
                },
                {
                    "path": "https://openminds.ebrains.eu/vocab/hardware",
                    "propertyName": "vocab:hardware",
                    "required": True,
                    "structure": [
                        {
                            "filter": {"op": "CONTAINS", "parameter": "hardware"},
                            "path": "@id",
                        },
                        {"path": "@type"},
                    ],
                },
                {
                    "ensureOrder": True,
                    "path": "https://openminds.ebrains.eu/vocab/software",
                    "propertyName": "Qsoftware",
                    "required": True,
                    "structure": [
                        {
                            "filter": {"op": "CONTAINS", "parameter": "software"},
                            "path": "@id",
                        },
                        {"path": "@type"},
                    ],
                },
                {
                    "ensureOrder": True,
                    "path": "https://openminds.ebrains.eu/vocab/software",
                    "propertyName": "vocab:software",
                    "structure": [
                        {"path": "@id"},
                        {"path": "@type"},
                    ],
                },
            ],
        }
        assert generated == expected
