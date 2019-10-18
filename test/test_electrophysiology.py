# encoding: utf-8
"""
Tests of fairgraph.electrophysiology module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

from fairgraph.base import KGQuery, KGProxy, as_list, Distribution
from fairgraph.commons import BrainRegion, CellType, QuantitativeValue
from fairgraph.core import use_namespace as use_core_namespace
from fairgraph.electrophysiology import (
    Trace, MultiChannelMultiTrialRecording, PatchedCell, Slice, BrainSlicingActivity,
    PatchedSlice, PatchedCellCollection, PatchClampActivity, PatchClampExperiment,
    QualifiedTraceGeneration, QualifiedMultiTraceGeneration,
    IntraCellularSharpElectrodeExperiment, IntraCellularSharpElectrodeRecordedCell,
    IntraCellularSharpElectrodeRecordedCellCollection,
    IntraCellularSharpElectrodeRecordedSlice, IntraCellularSharpElectrodeRecording,
    list_kg_classes, use_namespace as use_electrophysiology_namespace)
from fairgraph.minds import Dataset

from .utils import kg_client, MockKGObject, test_data_lookup, BaseTestKG
from pyxus.resources.entity import Instance

import pytest


test_data_lookup.update({
    "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/": "test/test_data/nexus/electrophysiology/patchedcell_list_0_50.json",
    "/v0/data/neuralactivity/electrophysiology/trace/v0.1.0/": "test/test_data/nexus/electrophysiology/trace_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/multitrace/v0.1.0/": "test/test_data/nexus/electrophysiology/multitrace_list_0_10.json",
    "/v0/data/neuralactivity/core/slice/v0.1.0/": "test/test_data/nexus/electrophysiology/slice_list_0_10.json",
    "/v0/data/neuralactivity/experiment/brainslicing/v0.1.0/": "test/test_data/nexus/electrophysiology/brainslicing_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedslice/v0.1.0/": "test/test_data/nexus/electrophysiology/patchedslice_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedcellcollection/v0.1.0/": "test/test_data/nexus/electrophysiology/patchedcellcollection_list_0_10.json",
    "/v0/data/neuralactivity/experiment/wholecellpatchclamp/v0.1.0/": "test/test_data/nexus/electrophysiology/wholecellpatchclamp_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/stimulusexperiment/v0.1.0/": "test/test_data/nexus/electrophysiology/stimulusexperiment_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/tracegeneration/v0.1.0/": "test/test_data/nexus/electrophysiology/tracegeneration_list_0_10.json",
    "/v0/data/neuralactivity/electrophysiology/multitracegeneration/v0.1.0/": "test/test_data/nexus/electrophysiology/multitracegeneration_list_0_10.json",
    "/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/5ab24291-8dca-4a45-a484-8a8c28d396e2": "test/test_data/nexus/electrophysiology/patchedcell_example.json",
})

use_core_namespace("neuralactivity")
use_electrophysiology_namespace("neuralactivity")




class TestPatchedCell(BaseTestKG):
    class_under_test = PatchedCell

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

    def test_round_trip(self, kg_client):
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
        instance.data["@id"] = "http://fake_uuid_93f9cd9a9b"
        instance.data["@type"] = PatchedCell.type
        cell2 = PatchedCell.from_kg_instance(instance, kg_client)
        for field in ("name", "brain_location", "cell_type",
                      "pipette_id", "seal_resistance", "pipette_resistance",
                      "liquid_junction_potential", "labeling_compound",
                      "reversal_potential_cl"):
            assert getattr(cell1, field) == getattr(cell2, field)


    def test_repr(self):
        try:
            unicode
        except NameError:
            cell = PatchedCell("example001",
                            brain_location=BrainRegion("primary auditory cortex"),
                            collection=None,
                            cell_type=CellType("pyramidal cell"),
                            experiments=None,
                            pipette_id=31,
                            seal_resistance=QuantitativeValue(1.2, "GΩ"),
                            pipette_resistance=QuantitativeValue(1.5, "MΩ"),
                            liquid_junction_potential=None,
                            labeling_compound="0.1% biocytin ",
                            reversal_potential_cl=None)
            expected_repr = ("PatchedCell(name='example001', "
                            "brain_location=BrainRegion('primary auditory cortex', 'http://purl.obolibrary.org/obo/UBERON_0034751'), "
                            "cell_type=CellType('pyramidal cell', 'http://purl.obolibrary.org/obo/CL_0000598'), "
                            "pipette_id=31, seal_resistance=QuantitativeValue(1.2 'GΩ'), "
                            "pipette_resistance=QuantitativeValue(1.5 'MΩ'), "
                            "labeling_compound='0.1% biocytin ', id=None)")
            assert repr(cell) == expected_repr
        else:
            pytest.skip("The remaining lifespan of Python 2 is too short to fix unicode representation errors")


class TestTrace(BaseTestKG):
    class_under_test = Trace

    def test_list(self, kg_client):
        traces = Trace.list(kg_client, size=10)
        assert len(traces) == 10

    def test_round_trip(self, kg_client):
        trace1 = Trace("example001",
                       data_location=Distribution("http://example.com/example.csv",
                                                  content_type="text/tab-separated-values"),
                       generated_by=MockKGObject(id="http://fake_uuid_abc123", type=PatchClampExperiment.type),
                       generation_metadata=MockKGObject(id="http://fake_uuid_def456", type=QualifiedTraceGeneration.type),
                       channel=42,
                       data_unit="mV",
                       time_step=QuantitativeValue(0.1, "ms"),
                       part_of=MockKGObject(id="http://fake_uuid_ghi789", type=Dataset.type))
        instance = Instance(Trace.path, trace1._build_data(kg_client), Instance.path)
        instance.data["@id"] = "http://fake_uuid_6a5d6ecf87"
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


class TestMultiChannelMultiTrialRecording(BaseTestKG):
    class_under_test = MultiChannelMultiTrialRecording

    def test_list(self, kg_client):
        traces = MultiChannelMultiTrialRecording.list(kg_client, size=10)
        assert len(traces) == 4


class TestSlice(BaseTestKG):
    class_under_test = Slice

    def test_list(self, kg_client):
        slices = Slice.list(kg_client, size=10)
        assert len(slices) == 10


class TestBrainSlicingActivity(BaseTestKG):
    class_under_test = BrainSlicingActivity

    def test_list(self, kg_client):
        activities = BrainSlicingActivity.list(kg_client, size=10)
        assert len(activities) == 10


class TestPatchedSlice(BaseTestKG):
    class_under_test = PatchedSlice

    def test_list(self, kg_client):
        slices = PatchedSlice.list(kg_client, size=10)
        assert len(slices) == 10


class TestPatchedCellCollection(BaseTestKG):
    class_under_test = PatchedCellCollection

    def test_list(self, kg_client):
        collections = PatchedCellCollection.list(kg_client, size=10)
        assert len(collections) == 10


class TestPatchClampActivity(BaseTestKG):
    class_under_test = PatchClampActivity

    def test_list(self, kg_client):
        activities = PatchClampActivity.list(kg_client, size=10)
        assert len(activities) == 10


class TestPatchClampExperiment(BaseTestKG):
    class_under_test = PatchClampExperiment

    def test_list(self, kg_client):
        experiments = PatchClampExperiment.list(kg_client, size=10)
        assert len(experiments) == 10


class TestQualifiedTraceGeneration(BaseTestKG):
    class_under_test = QualifiedTraceGeneration

    def test_list(self, kg_client):
        tracegens = QualifiedTraceGeneration.list(kg_client, size=10)
        assert len(tracegens) == 10


class TestQualifiedMultiTraceGeneration(BaseTestKG):
    class_under_test = QualifiedMultiTraceGeneration

    def test_list(self, kg_client):
        tracegens = QualifiedMultiTraceGeneration.list(kg_client, size=10)
        assert len(tracegens) == 4


class TestIntraCellularSharpElectrodeRecordedCell(BaseTestKG):
    class_under_test = IntraCellularSharpElectrodeRecordedCell


class TestIntraCellularSharpElectrodeRecording(BaseTestKG):
    class_under_test = IntraCellularSharpElectrodeRecording


class TestIntraCellularSharpElectrodeRecordedCellCollection(BaseTestKG):
    class_under_test = IntraCellularSharpElectrodeRecordedCellCollection


class TestIntraCellularSharpElectrodeRecordedSlice(BaseTestKG):
    class_under_test = IntraCellularSharpElectrodeRecordedSlice


class TestIntraCellularSharpElectrodeExperiment(BaseTestKG):
    class_under_test = IntraCellularSharpElectrodeExperiment


class TestModuleFunctions(object):

    def test_list_kg_classes(self):
        expected_classes = set((
            Trace, MultiChannelMultiTrialRecording, PatchedCell, Slice, BrainSlicingActivity,
            PatchedSlice, PatchedCellCollection, PatchClampActivity, PatchClampExperiment,
            QualifiedTraceGeneration, QualifiedMultiTraceGeneration,
            IntraCellularSharpElectrodeExperiment, IntraCellularSharpElectrodeRecordedCell,
            IntraCellularSharpElectrodeRecordedCellCollection,
            IntraCellularSharpElectrodeRecordedSlice, IntraCellularSharpElectrodeRecording
        ))
        assert set(list_kg_classes()) == expected_classes
