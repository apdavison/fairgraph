"""
Tests of fairgraph.brainsimulation module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

from datetime import datetime
from fairgraph.analysis import AnalysisResult, Analysis, AnalysisConfiguration, AnalysisScript
from .utils import (kg_client, MockKGObject, test_data_lookup, generate_random_object,
                    BaseTestKG, random_uuid)


test_data_lookup.update({
    "/v0/data/modelvalidation/simulation/analysisresult/v1.0.0/": "test/test_data/nexus/analysis/analysisresult_list_0_10.json",
    "/v0/data/modelvalidation/simulation/analysisactivity/v0.1.0/": "test/test_data/nexus/analysis/analysis_list_0_10.json",
    "/v0/data/modelvalidation/simulation/analysisconfiguration/v0.1.0/": "test/test_data/nexus/analysis/analysisconfiguration_list_0_10.json",
    "/v0/data/modelvalidation/simulation/analysisscript/v0.1.0/": "test/test_data/nexus/analysis/analysisscript_list_0_10.json",
})



class TestAnalysisResult(BaseTestKG):
    class_under_test = AnalysisResult

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_existence_query(self, kg_client):
        obj = AnalysisResult("foo", timestamp=datetime(2000, 1, 1))
        expected = {
            "op": "and",
            "value": [
                {
                    "path": "schema:name",
                    "op": "eq",
                    "value": "foo"
                },
                {
                    "path": "prov:generatedAtTime",
                    "op": "eq",
                    "value": "2000-01-01T00:00:00"
                }
            ]
        }
        generated = obj._build_existence_query(api="nexus")
        assert expected == generated


class TestAnalysis(BaseTestKG):
    class_under_test = Analysis

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestAnalysisConfiguration(BaseTestKG):
    class_under_test = AnalysisConfiguration

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


class TestAnalysisScript(BaseTestKG):
    class_under_test = AnalysisScript

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)
