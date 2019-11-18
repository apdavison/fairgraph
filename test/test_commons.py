# encoding: utf-8
"""

"""

from fairgraph.commons import QuantitativeValue, QuantitativeValueRange


class TestQuantitativeValueRange(object):

    def test_create(self):
        obj = QuantitativeValueRange(5, 7, "weeks")
        assert obj.min == 5
        assert obj.max == 7
        assert obj.unit_code == "http://purl.obolibrary.org/obo/UO_0000034"

    def test_to_jsonld(self):
        obj = QuantitativeValueRange(5, 7, "weeks")
        expected = {
            "@type": "nsg:QuantitativeValue",
            "minValue": 5,
            "maxValue": 7,
            "label": "weeks",
            "unitCode": {"@id": "http://purl.obolibrary.org/obo/UO_0000034"}
        }
        assert obj.to_jsonld() == expected

    def test_from_jsonld(self):
        data = {
            "@type": "nsg:QuantitativeValue",
            "minValue": 0.5,
            "maxValue": 1.5,
            "label": "µm",
            "unitCode": {"@id": "http://purl.obolibrary.org/obo/UO_0000017"}
        }
        obj = QuantitativeValueRange.from_jsonld(data)
        assert obj.min == 0.5
        assert obj.max == 1.5
        assert obj.unit_text == "µm"

        data = None
        assert QuantitativeValueRange.from_jsonld(data) is None

        data = obj.to_jsonld_alt()
        obj2 = QuantitativeValueRange.from_jsonld(data)
        assert obj.unit_code == "http://purl.obolibrary.org/obo/UO_0000017"
        assert obj.max == 1.5

    def test_from_jsonld_alt(self):
        data = {
            "http://schema.org/value": 0.05,
            "http://schema.org/unitText": "ms"
        }
        obj = QuantitativeValue.from_jsonld(data)
        assert obj.value == 0.05
        assert obj.unit_text == "ms"