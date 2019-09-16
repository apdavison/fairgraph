# encoding: utf-8
"""
Utility classes and functions for testing fairgraph, in particular various mock objects
including a mock Http client which returns data loaded from the files in the test_data directory.
"""

import json
import os
from copy import deepcopy
try:
    from urllib.parse import parse_qs, urlparse
except ImportError:
    from urlparse import parse_qs, urlparse  # py2

import uuid

import pytest
from openid_http_client.http_client import HttpClient

from pyxus.client import NexusClient, NexusConfig
from pyxus.resources.repository import (ContextRepository, DomainRepository,
                                        InstanceRepository,
                                        OrganizationRepository,
                                        SchemaRepository)
import fairgraph.client
from fairgraph.base import as_list


# test_data_lookup = {
#     "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/": "test/test_data/electrophysiology/patchedcell_list_0_50.json",
#     "/v0/data/neuralactivity/electrophysiology/trace/v0.1.0/": "test/test_data/electrophysiology/trace_list_0_10.json",
#     "/v0/data/neuralactivity/electrophysiology/multitrace/v0.1.0/": "test/test_data/electrophysiology/multitrace_list_0_10.json",
#     "/v0/data/neuralactivity/core/slice/v0.1.0/": "test/test_data/electrophysiology/slice_list_0_10.json",
#     "/v0/data/neuralactivity/experiment/brainslicing/v0.1.0/": "test/test_data/electrophysiology/brainslicing_list_0_10.json",
#     "/v0/data/neuralactivity/experiment/patchedslice/v0.1.0/": "test/test_data/electrophysiology/patchedslice_list_0_10.json",
#     "/v0/data/neuralactivity/experiment/patchedcellcollection/v0.1.0/": "test/test_data/electrophysiology/patchedcellcollection_list_0_10.json",
#     "/v0/data/neuralactivity/experiment/wholecellpatchclamp/v0.1.0/": "test/test_data/electrophysiology/wholecellpatchclamp_list_0_10.json",
#     "/v0/data/neuralactivity/electrophysiology/stimulusexperiment/v0.1.0/": "test/test_data/electrophysiology/stimulusexperiment_list_0_10.json",
#     "/v0/data/neuralactivity/electrophysiology/tracegeneration/v0.1.0/": "test/test_data/electrophysiology/tracegeneration_list_0_10.json",
#     "/v0/data/neuralactivity/electrophysiology/multitracegeneration/v0.1.0/": "test/test_data/electrophysiology/multitracegeneration_list_0_10.json",
#     "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2": "test/test_data/electrophysiology/patchedcell_example.json",
# }
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
            if "filter" in parts.query:
                query = parse_qs(parts.query)
                filtr = eval(query['filter'][0])
                if filtr.get("path") == "nsg:brainLocation / nsg:brainRegion":
                    results = [item for item in data["results"]
                               if as_list(item["source"]["brainLocation"]["brainRegion"])[0]["@id"] == filtr["value"]]
                elif filtr.get("path") in ("schema:givenName", "schema:familyName"):
                    results = [item for item in data["results"]
                               if item["source"][filtr["path"].split(":")[1]] == filtr["value"]]
                elif "op" in filtr:
                    # James Bond does not exist
                    if filtr["value"][0]["value"] in ("James", "Bond"):
                        results = []
                    elif filtr["value"][0]["value"] in ("Katherine", "Johnson"):
                        results = [item for item in data["results"]
                                   if item["source"]["familyName"] == "Johnson"]
                else:
                    raise NotImplementedError("todo")
                data = deepcopy(data)  # don't want to mess with the cache
                data["results"] = results
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

    def __init__(self, scheme=None, host=None, prefix=None, alternative_namespace=None, auth_client=None):
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


class MockKGObject(object):

    def __init__(self, id, type):
        self.id = id
        self.type = type


@pytest.fixture
def kg_client():
    fairgraph.client.NexusClient = MockNexusClient
    client = fairgraph.client.KGClient("thisismytoken")
    #token = os.environ["HBP_token"]
    #client = fairgraph.client.KGClient(token)
    return client
