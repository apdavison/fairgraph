# encoding: utf-8
"""
Utility classes and functions for testing fairgraph, in particular various mock objects
including a mock Http client which returns data loaded from the files in the test_data directory.
"""

import json
import os
import sys
import random
from datetime import datetime, date
from copy import deepcopy
try:
    from urllib.parse import parse_qs, urlparse
except ImportError:
    from urlparse import parse_qs, urlparse  # py2

import uuid

import pytest
from jsondiff import diff as jsondiff

try:
    from openid_http_client.http_client import HttpClient
    from pyxus.client import NexusClient, NexusConfig
    from pyxus.resources.entity import Instance
    from pyxus.resources.repository import (ContextRepository, DomainRepository,
                                            InstanceRepository,
                                            OrganizationRepository,
                                            SchemaRepository)
    have_pyxus = True
except ImportError:
    have_pyxus = False
    HttpClient = object
    NexusClient = object


import fairgraph.client_v2
from fairgraph.base_v2 import as_list, KGObject, MockKGObject, KGProxy, Distribution, IRI
from fairgraph.commons import (QuantitativeValue, QuantitativeValueRange,
                               OntologyTerm, Age, Address, Species)


test_data_lookup = {}


class MockHttpClient(HttpClient):

    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)  # for when we drop Python 2 support
        super(MockHttpClient, self).__init__(*args, **kwargs)
        self.cache = {}
        self.request_count = 0

    def _request(self, method_name, endpoint_url, data=None, headers=None, can_retry=True):
        self.request_count += 1
        full_url = self._create_full_url(endpoint_url)
        print(full_url)
        parts = urlparse(full_url)
        query = parse_qs(parts.query)
        # to do: handle the query part
        if method_name == 'get':
            test_data_path = test_data_lookup[parts.path]
            if test_data_path in self.cache:
                data = self.cache[test_data_path]
            else:
                with open(test_data_path, "r") as fp:
                    data = json.load(fp)
                self.cache[test_data_path] = data
            #if "query" in parts.path:
            #        raise Exception()  # for debugging
            if parts.netloc == "nexus.humanbrainproject.org":
                if "filter" in parts.query:  # api="nexus"
                    query = parse_qs(parts.query)
                    filtr = eval(query['filter'][0])
                    if filtr.get("path") == "nsg:brainLocation / nsg:brainRegion":
                        results = [item for item in data["results"]
                                if as_list(item["source"]["brainLocation"]["brainRegion"])[0]["@id"] == filtr["value"]]
                    elif filtr.get("path") in ("schema:givenName", "schema:familyName"):
                        results = [item for item in data["results"]
                                if item["source"][filtr["path"].split(":")[1]] == filtr["value"]]
                    elif filtr.get("path") == "prov:used / rdf:type":
                        results = [item for item in data["results"]
                                if filtr["value"] in data["results"][0]["source"]["prov:used"]["@type"]]
                    elif filtr.get("path") == "nsg:species":
                        results = [item for item in data["results"]
                                if item["source"].get("species", {"@id": None})["@id"] == filtr["value"]]
                    elif "op" in filtr:
                        if filtr["op"] == "eq" and filtr["path"] == "schema:name":
                            results = [item for item in data["results"]
                                    if item["source"]["name"] == filtr["value"]]
                        # James Bond does not exist
                        elif filtr["value"][0]["value"] in ("James", "Bond"):
                            results = []
                        elif filtr["value"][0]["value"] in ("Katherine", "Johnson"):
                            results = [item for item in data["results"]
                                    if item["source"]["familyName"] == "Johnson"]
                    else:
                        raise NotImplementedError("todo")
                    data = deepcopy(data)  # don't want to mess with the cache
                    data["results"] = results
            elif parts.netloc == "kg.humanbrainproject.eu":
                if "species" in parts.query:   # api="query"
                    query = parse_qs(parts.query)
                    if "species" in query:
                        value = query["species"][0]
                        results = [item for item in data["results"]
                                if item.get("species", [{"@id": None}])[0]["@id"] == value]
                        data = deepcopy(data)
                        data["results"] = results
                elif "id" in parts.query:
                    query = parse_qs(parts.query)
                    value = query["id"][0]
                    results = [item for item in data["results"]
                            if item["@id"] == value]
                    data = deepcopy(data)
                    data["results"] = results
            else:
                raise NotImplementedError
            return data
        elif method_name == 'post':
            # assume success, generate random uuid
            response = {
                "@context": "https://nexus-int.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0",
                "@id": "https://nexus-int.humanbrainproject.org/v0{}/{}".format(endpoint_url, uuid.uuid4()),
                "nxv:rev": 1
            }
            return response
        else:
            raise NotImplementedError("to do")


class MockNexusClient(NexusClient):

    def __init__(self, scheme=None, host=None, prefix=None,
                 alternative_namespace=None, auth_client=None):
        if not have_pyxus:
            return
        self.version = None
        self.namespace = alternative_namespace if alternative_namespace is not None else "{}://{}".format(scheme, host)
        self.env = None
        self.config = NexusConfig(scheme, host, prefix, alternative_namespace)
        self._http_client = MockHttpClient(self.config.NEXUS_ENDPOINT, self.config.NEXUS_PREFIX, auth_client=auth_client,
                                           alternative_endpoint_writing=self.config.NEXUS_NAMESPACE)
        self.domains = DomainRepository(self._http_client)
        self.contexts = ContextRepository(self._http_client)
        self.organizations = OrganizationRepository(self._http_client)
        self.instances = InstanceRepository(self._http_client)
        self.schemas = SchemaRepository(self._http_client)


@pytest.fixture
def kg_client():
    fairgraph.client_v2.NexusClient = MockNexusClient
    fairgraph.client_v2.HttpClient = MockHttpClient
    client = fairgraph.client_v2.KGClient("thisismytoken")
    #token = os.environ["HBP_token"]
    #client = fairgraph.client.KGClient(token)
    return client


lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

lli = len(lorem_ipsum)


def _random_text():
    start = random.randint(0, lli // 2)
    end = random.randint(lli // 2, lli)
    return lorem_ipsum[start:end]


def random_uuid():
    return "http://stuff/{}".format(uuid.uuid4())


def generate_random_object(cls, all_fields=True):
    attrs = {}
    for field in cls.fields:
        if all_fields or field.required:
            obj_type = field.types[0]  # todo: pick randomly if len(field.types) > 1
            if not field.intrinsic:
                value = None
            elif obj_type == str:
                value = _random_text()
            elif obj_type == int:
                value = random.randint(1, 10)
            elif obj_type == float:
                value = random.uniform(0, 1000)
            elif issubclass(obj_type, KGObject):
                if obj_type == KGObject:
                    # specific type is not determined
                    # arbitrarily, let's choose minds.Dataset
                    value = MockKGObject(id=random_uuid(), type=["minds:Dataset"])
                else:
                    value = MockKGObject(id=random_uuid(), type=getattr(obj_type, "type", None))
            elif obj_type == QuantitativeValue:
                # todo: subclass QV so we can specify the required dimensionality in `fields`
                value = QuantitativeValue(random.uniform(-10, 10),
                                          random.choice(list(QuantitativeValue.unit_codes)))
            elif obj_type == QuantitativeValueRange:
                # todo: subclass QVR so we can specify the required dimensionality in `fields`
                min = random.uniform(-10, 10)
                value = QuantitativeValueRange(min, min + random.uniform(1, 10),
                                               random.choice(list(QuantitativeValue.unit_codes)))
            elif issubclass(obj_type, OntologyTerm):
                value = obj_type(random.choice(list(obj_type.iri_map)))
            elif obj_type == datetime:
                value = datetime.now()
            elif obj_type == date:
                value = date.today()
            elif obj_type == bool:
                value = random.choice([True, False])
            elif obj_type == Distribution:
                value = Distribution("http://example.com/myfile.txt")
            elif obj_type == Age:
                value = Age(QuantitativeValue(random.randint(7, 150), "days"), "Post-natal")
            elif obj_type == IRI:
                value = "http://example.com/åêïøù"
            elif obj_type == Address:
                value = Address("Paris", "France")
            elif obj_type == dict:
                value = {
                    "a": 1, "b": 2
                }
            else:
                raise NotImplementedError(str(obj_type))
            attrs[field.name] = value
    return cls(**attrs)


def dates_equal(d1, d2):
    """Allow comparing dates with datetimes"""
    if isinstance(d1, date):
        d1 = datetime(d1.year, d1.month, d1.day)
    if isinstance(d2, date):
        d2 = datetime(d2.year, d2.month, d2.day)
    return d1 == d2


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class BaseTestKG(object):

    def test_round_trip_random(self, kg_client):
        cls = self.class_under_test
        if cls.fields:
            obj1 = generate_random_object(cls)
            instance = Instance(cls.path, obj1._build_data(kg_client), Instance.path)
            instance.data["@id"] = random_uuid()
            instance.data["@type"] = cls.type
            obj2 = cls.from_kg_instance(instance, kg_client)
            for field in cls.fields:
                if field.intrinsic:
                    val1 = getattr(obj1, field.name)
                    val2 = getattr(obj2, field.name)
                    if issubclass(field.types[0], KGObject):
                        assert isinstance(val1, MockKGObject)
                        assert isinstance(val2, KGProxy)
                        if isinstance(val2.cls, list):
                            assert val1.type in (possible_class.type for possible_class in val2.cls)
                        else:
                            assert val1.type == val2.cls.type
                    elif date in field.types:
                        assert dates_equal(val1, val2)
                    else:
                        assert val1 == val2
                # todo: test non-intrinsic fields

    def test_round_trip_minimal_random(self, kg_client):
        cls = self.class_under_test
        if cls.fields:
            obj1 = generate_random_object(cls, all_fields=False)
            instance = Instance(cls.path, obj1._build_data(kg_client), Instance.path)
            instance.data["@id"] = random_uuid()
            instance.data["@type"] = cls.type
            obj2 = cls.from_kg_instance(instance, kg_client)
            for field in cls.fields:
                if field.intrinsic and field.required:
                    val1 = getattr(obj1, field.name)
                    val2 = getattr(obj2, field.name)
                    if issubclass(field.types[0], KGObject):
                        assert isinstance(val1, MockKGObject)
                        assert isinstance(val2, KGProxy)
                        if isinstance(val2.cls, list):
                            assert val1.type in (possible_class.type for possible_class in val2.cls)
                        else:
                            assert val1.type == val2.cls.type
                    elif date in field.types:
                        assert dates_equal(val1, val2)
                    else:
                        assert val1 == val2
                # todo: test non-intrinsic fields

    @pytest.mark.skipif(sys.version_info < (3, 6), reason="requires Python 3.6 or higher")
    # because earlier versions don't preserve dict insert order
    def test_generate_query(self, kg_client):
        cls = self.class_under_test
        generated = cls.generate_query("fgResolved", kg_client, resolved=True)
        #key = "{}_{}_resolved_query".format(cls.__module__.split(".")[1], cls.__name__.lower())
        test_data = "test/test_data/kgquery/{}/{}_resolved_query.json".format(
            cls.__module__.split(".")[1], cls.__name__.lower())
        with open(test_data) as fp:
            expected = json.load(fp)
        assert not jsondiff(generated, expected), jsondiff(generated, expected)

        generated = cls.generate_query("fgSimple", kg_client, resolved=False)
        #key = "{}_{}_simple_query".format(cls.__module__.split(".")[1], cls.__name__.lower())
        test_data = test_data.replace("resolved", "simple")
        with open(test_data) as fp:
            expected = json.load(fp)
        assert not jsondiff(generated, expected), jsondiff(generated, expected)
