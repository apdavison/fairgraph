# encoding: utf-8
"""
Tests of fairgraph.electrophysiology module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

import json
import os
from urllib.parse import parse_qs, urlparse

import pytest
from openid_http_client.http_client import HttpClient

import fairgraph.client
from fairgraph.base import KGQuery, KGProxy, as_list, Distribution
from fairgraph.commons import BrainRegion, CellType, QuantitativeValue
from fairgraph.electrophysiology import (BrainSlicingActivity,
                                         MultiChannelMultiTrialRecording,
                                         PatchClampActivity,
                                         PatchClampExperiment, PatchedCell,
                                         PatchedCellCollection, PatchedSlice,
                                         QualifiedMultiTraceGeneration,
                                         QualifiedTraceGeneration, Slice,
                                         Trace)
from fairgraph.minds import Dataset
from pyxus.client import NexusClient, NexusConfig
from pyxus.resources.repository import (ContextRepository, DomainRepository,
                                        InstanceRepository,
                                        OrganizationRepository,
                                        SchemaRepository)
from pyxus.resources.entity import Instance


test_data_lookup = {
    "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/": "test/test_data/electrophysiology/patchedcell_list_0_50.json",
    "/v0/data/neuralactivity/electrophysiology/trace/v0.1.0/": "test/test_data/electrophysiology/trace_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/multitrace/v0.1.0/": "test/test_data/electrophysiology/multitrace_list_0_10.json",
    "/v0/data/neuralactivity/core/slice/v0.1.0/": "test/test_data/electrophysiology/slice_list_0_10.json",
    "/v0/data/neuralactivity/experiment/brainslicing/v0.1.0/": "test/test_data/electrophysiology/brainslicing_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedslice/v0.1.0/": "test/test_data/electrophysiology/patchedslice_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedcellcollection/v0.1.0/": "test/test_data/electrophysiology/patchedcellcollection_list_0_10.json",
    "/v0/data/neuralactivity/experiment/wholecellpatchclamp/v0.1.0/": "test/test_data/electrophysiology/wholecellpatchclamp_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/stimulusexperiment/v0.1.0/": "test/test_data/electrophysiology/stimulusexperiment_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/tracegeneration/v0.1.0/": "test/test_data/electrophysiology/tracegeneration_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/multitracegeneration/v0.1.0/": "test/test_data/electrophysiology/multitracegeneration_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2": "test/test_data/electrophysiology/patchedcell_example.json",
}


class MockHttpClient(HttpClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
                if filtr["path"] == "nsg:brainLocation / nsg:brainRegion":
                    results = [item for item in data["results"]
                               if as_list(item["source"]["brainLocation"]["brainRegion"])[0]["@id"] == filtr["value"]]
                    data["results"] = results
                else:
                    raise NotImplementedError("todo")
            return data
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


class TestPatchedCell(object):

    def test_list(self, kg_client):
        cells = PatchedCell.list(kg_client, size=50)
        assert len(cells) == 30
        assert cells[0].brain_location == BrainRegion("hippocampus CA1")
        assert isinstance(cells[0].collection, KGQuery)
        assert cells[0].cell_type == CellType("hippocampus CA1 pyramidal cell")
        assert isinstance(cells[0].experiments, KGQuery)
        assert cells[0].pipette_id is None
        assert cells[0].seal_resistance is None
        assert cells[0].pipette_resistance is None
        assert cells[0].liquid_junction_potential is None
        assert cells[0].labeling_compound is None
        assert cells[0].reversal_potential_cl == QuantitativeValue(-16.0, unit_text="mV")

    def test_list_with_filter(self, kg_client):
        cells = PatchedCell.list(kg_client, brain_region=BrainRegion("hippocampus CA1"), size=50)
        assert len(cells) == 26

    def test_get_from_uri(self, kg_client):
        uri = "https://nexus.humanbrainproject.org/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2"
        cell = PatchedCell.from_uri(uri, kg_client)
        assert isinstance(cell, PatchedCell)
        assert cell.brain_location == [BrainRegion('lobule 5 of the cerebellar vermis'),
                                       BrainRegion('lobule 6 of the cerebellar vermis'),
                                       BrainRegion('lobule 7 of the cerebellar vermis'),
                                       BrainRegion('lobule 8 of the cerebellar vermis')]
        assert isinstance(cell.collection, KGQuery)
        assert isinstance(cell.experiments, KGQuery)

    def test_get_from_uuid(self, kg_client):
        uri = "https://nexus.humanbrainproject.org/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2"
        a = PatchedCell.from_uri(uri, kg_client)
        b = PatchedCell.from_uuid("5ab24291-8dca-4a45-a484-8a8c28d396e2", kg_client)
        assert a == b

    def test_get_from_uri_with_cache(self, kg_client):
        assert len(kg_client.cache) == 0
        assert kg_client._nexus_client._http_client.request_count == 0
        uri = "https://nexus.humanbrainproject.org/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2"
        # 1st call
        cell1 = PatchedCell.from_uri(uri, kg_client)
        assert len(kg_client.cache) == 1
        assert kg_client._nexus_client._http_client.request_count == 1
        assert uri in kg_client.cache
        # 2nd call
        cell2 = PatchedCell.from_uri(uri, kg_client)
        assert kg_client._nexus_client._http_client.request_count == 1  # should be unchanged if cache was used
        # 3rd call, without cache
        cell3 = PatchedCell.from_uri(uri, kg_client, use_cache=False)
        assert kg_client._nexus_client._http_client.request_count == 2
        assert cell1.id == cell2.id == cell3.id == uri

    def test_round_trip(self):
        cell1 = PatchedCell("example001",
                            brain_location=BrainRegion("primary auditory cortex"),
                            collection=None,
                            cell_type=CellType("pyramidal cell"),
                            experiments=None,
                            pipette_id=31,
                            seal_resistance=QuantitativeValue(1.2, "GΩ"),
                            pipette_resistance=QuantitativeValue(1.5, "MΩ"),
                            liquid_junction_potential=QuantitativeValue(5.0, "mV"),
                            labeling_compound="0.1% biocytin ",
                            reversal_potential_cl=QuantitativeValue(-65, "mV"))
        instance = Instance(PatchedCell.path, cell1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "fake_uuid_93f9cd9a9b"
        instance.data["@type"] = PatchedCell.type
        cell2 = PatchedCell.from_kg_instance(instance, kg_client)
        for field in ("name", "brain_location", "cell_type",
                      "pipette_id", "seal_resistance", "pipette_resistance",
                      "liquid_junction_potential", "labeling_compound",
                      "reversal_potential_cl"):
            assert getattr(cell1, field) == getattr(cell2, field)

class TestTrace(object):

    def test_list(self, kg_client):
        traces = Trace.list(kg_client, size=10)
        assert len(traces) == 10

    def test_round_trip(self):
        trace1 = Trace("example001",
                       data_location=Distribution("http://example.com/example.csv",
                                                  content_type="text/tab-separated-values"),
                       generated_by=MockKGObject(id="abc123", type=PatchClampExperiment.type),
                       generation_metadata=MockKGObject(id="def456", type=QualifiedTraceGeneration.type),
                       channel=42,
                       data_unit="mV",
                       time_step=QuantitativeValue(0.1, "ms"),
                       part_of=MockKGObject(id="ghi789", type=Dataset.type))
        instance = Instance(Trace.path, trace1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "fake_uuid_6a5d6ecf87"
        instance.data["@type"] = Trace.type
        trace2 = Trace.from_kg_instance(instance, kg_client)
        for field in ("name", "data_location", "channel", "data_unit", "time_step"):
            assert getattr(trace1, field) == getattr(trace2, field)
        for field in ("generated_by", "generation_metadata", "part_of"):
            obj1 = getattr(trace1, field)
            obj2 = getattr(trace2, field)
            assert isinstance(obj2, KGProxy)
            assert obj1.id == obj2.id
            assert obj1.type == obj2.type


def test_MultiChannelMultiTrialRecording(kg_client):
    traces = MultiChannelMultiTrialRecording.list(kg_client, size=10)
    assert len(traces) == 4

def test__Slice(kg_client):
    slices = Slice.list(kg_client, size=10)
    assert len(slices) == 10


class TestBrainSlicingActivity(object):

    def test_list(self, kg_client):
        activities = BrainSlicingActivity.list(kg_client, size=10)
        assert len(activities) == 10

    def test_round_trip(self):
        pass  # todo


def test__PatchedSlice(kg_client):
    slices = PatchedSlice.list(kg_client, size=10)
    assert len(slices) == 10

def test__PatchedCellCollection(kg_client):
    collections = PatchedCellCollection.list(kg_client, size=10)
    assert len(collections) == 10

def test__PatchClampActivity(kg_client):
    activities = PatchClampActivity.list(kg_client, size=10)
    assert len(activities) == 10

def test__PatchClampExperiment(kg_client):
    experiments = PatchClampExperiment.list(kg_client, size=10)
    assert len(experiments) == 10

def test__QualifiedTraceGeneration(kg_client):
    tracegens = QualifiedTraceGeneration.list(kg_client, size=10)
    assert len(tracegens) == 10

def test__QualifiedMultiTraceGeneration(kg_client):
    tracegens = QualifiedMultiTraceGeneration.list(kg_client, size=10)
    assert len(tracegens) == 4
