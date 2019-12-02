# encoding: utf-8
"""
Tests of fairgraph.base module.
"""

from fairgraph.base import KGQuery, KGProxy, as_list, Distribution, build_kg_object
from fairgraph.commons import QuantitativeValue
from fairgraph.core import Person

from .utils import kg_client, MockKGObject
from pyxus.resources.entity import Instance

import pytest


class TestDistribution(object):

    def test_to_jsonld(self, kg_client):
        obj = Distribution(location="http://example.com/data.dat",
                           size=123,  # bytes
                           digest="abcdef",
                           digest_method="sha1",
                           content_type="application/foo",
                           original_file_name="data.dat")
        data = obj.to_jsonld(kg_client)
        expected_data = {
            '@context': 'https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0',
            'contentSize': {'unit': 'byte', 'value': 123},
            'digest': {'algorithm': 'sha1', 'value': 'abcdef'},
            'downloadURL': 'http://example.com/data.dat',
            'mediaType': 'application/foo',
            'originalFileName': 'data.dat'}
        assert data == expected_data

    def test_from_jsonld(self, kg_client):
        data = {
            '@context': 'https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0',
            'contentSize': {'unit': 'byte', 'value': 456},
            'digest': {'algorithm': 'sha1', 'value': 'a1b2c3'},
            'downloadURL': 'http://example.com/data2.dat',
            'mediaType': 'application/bar',
            'originalFileName': 'data2.dat'
        }
        obj = Distribution.from_jsonld(data)
        assert obj.size == 456
        assert obj.content_type == "application/bar"
        assert obj.digest == 'a1b2c3'
        assert obj.digest_method == "sha1"
        assert obj.location == 'http://example.com/data2.dat'

    def test_from_jsonld_minimal(self, kg_client):
        data = {
            '@context': 'https://nexus.humanbrainproject.org/v0/contexts/nexus/core/distribution/v0.1.0',
            'downloadURL': 'http://example.com/data2.dat',
        }
        obj = Distribution.from_jsonld(data)
        assert obj.size is None
        assert obj.content_type is None
        assert obj.digest is None
        assert obj.digest_method is None
        assert obj.location == 'http://example.com/data2.dat'


class TestModuleFunctions(object):

    def test_build_kg_object(self, kg_client):
        obj = build_kg_object(Person, {"@id": "http://fake_uuid_a8575fdd19"})
        assert isinstance(obj, KGProxy)

        obj = build_kg_object(Person, {"@list": [{"@id": "http://fake_uuid_a8575fdd19"}]})
        assert isinstance(obj, KGProxy)

        obj = build_kg_object(Person,
                              [{"@id": "http://fake_uuid_a8575fdd19"},
                               {"@id": "http://fake_uuid_91ddf5758a"}])
        assert isinstance(obj, list)
        assert isinstance(obj[1], KGProxy)

        obj = build_kg_object(Distribution, {"downloadURL": "http://example.com/data.dat"})
        assert isinstance(obj, Distribution)

        with pytest.raises(ValueError):
            build_kg_object(tuple, {"@id": "http://fake_uuid_a8575fdd19"})

        with pytest.raises(ValueError):
            build_kg_object(Person, "abcde")

        obj = build_kg_object(None, {"@id": "http://fake_uuid_a8575fdd19", "@type": Person.type})
        assert isinstance(obj, KGProxy)
        assert obj.type == Person.type
