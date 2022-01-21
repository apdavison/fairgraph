# encoding: utf-8
"""
Tests of fairgraph.brainsimulation module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

from datetime import datetime
try:
    from pyxus.resources.entity import Instance
    have_pyxus = True
except ImportError:
    have_pyxus = False
import pytest

from fairgraph.base_v2 import KGQuery, KGProxy, as_list, Distribution, KGObject
from fairgraph.commons import BrainRegion, CellType, QuantitativeValue
from fairgraph.brainsimulation import (
    ModelScript, ModelProject, ModelInstance, MEModel, Morphology, EModel,
    ValidationTestDefinition, ValidationScript, ValidationResult, ValidationActivity,
    Simulation,  SimulationOutput, SimulationConfiguration
)
from fairgraph.core import Person, use_namespace as use_core_namespace

from .utils import (kg_client, MockKGObject, test_data_lookup, generate_random_object,
                    BaseTestKG, random_uuid)

use_core_namespace("modelvalidation")


test_data_lookup.update({
    "/v0/data/modelvalidation/simulation/emodel/v0.1.1/": "test/test_data/nexus/brainsimulation/emodel_list_0_10.json",
    "/v0/data/modelvalidation/simulation/memodel/v0.1.2/": "test/test_data/nexus/brainsimulation/memodel_list_0_10.json",
    "/v0/data/modelvalidation/simulation/modelinstance/v0.1.1/": "test/test_data/nexus/brainsimulation/modelinstance_list_0_10.json",
    "/v0/data/modelvalidation/simulation/modelproject/v0.1.1/": "test/test_data/nexus/brainsimulation/modelproject_list_0_10.json",
    "/v0/data/modelvalidation/simulation/emodelscript/v0.1.0/": "test/test_data/nexus/brainsimulation/modelscript_list_0_10.json",
    "/v0/data/modelvalidation/simulation/morphology/v0.1.1/": "test/test_data/nexus/brainsimulation/morphology_list_0_10.json",
    "/v0/data/modelvalidation/simulation/modelvalidation/v0.2.0/": "test/test_data/nexus/brainsimulation/validationactivity_list_0_10.json",
    "/v0/data/modelvalidation/simulation/validationresult/v0.1.0/": "test/test_data/nexus/brainsimulation/validationresult_list_0_10.json",
    "/v0/data/modelvalidation/simulation/validationscript/v0.1.0/": "test/test_data/nexus/brainsimulation/validationscript_list_0_10.json",
    "/v0/data/modelvalidation/simulation/validationtestdefinition/v0.1.0/": "test/test_data/nexus/brainsimulation/validationtestdefinition_list_0_10.json",
    "/v0/data/modelvalidation/simulation/simulationactivity/v0.1.0/": "test/test_data/nexus/brainsimulation/simulation_list_0_10.json",
    "/v0/data/modelvalidation/simulation/simulationactivity/v0.3.2/": "test/test_data/nexus/brainsimulation/simulation_list_0_10.json",
    "/v0/data/modelvalidation/simulation/simulationresult/v0.1.0/": "test/test_data/nexus/brainsimulation/simulationoutput_list_0_10.json",
    "/v0/data/modelvalidation/simulation/simulationconfiguration/v0.1.0/": "test/test_data/nexus/brainsimulation/simulationconfiguration_list_0_10.json",
    "/query/modelvalidation/simulation/modelproject/v0.1.1/fgResolved/instances": "test/test_data/kgquery/brainsimulation/modelproject_list_resolved_0_10.json",
    "/query/modelvalidation/simulation/modelproject/v0.1.1/fgSimple/instances": "test/test_data/kgquery/brainsimulation/modelproject_list_simple_0_10.json",
    "/query/modelvalidation/simulation/memodel/v0.1.2/fgSimple/instances": "test/test_data/kgquery/brainsimulation/memodel_list_simple_0_10.json",

    "/query/neuralactivity/core/person/v0.1.0/fgSimple/instances": "test/test_data/kgquery/core/person_list_simple_0_10.json",

})

@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestModelScript(BaseTestKG):
    class_under_test = ModelScript

    def test_get_context(self, kg_client):
        obj = ModelScript("test_code",
                          code_location="https://github.com/SomeOrg/ProjName",
                          code_format="Python", license="BSD",
                          id="http://fake_uuid_381aa74bc9")
        context = sorted(obj.get_context(kg_client),
                         key=lambda obj: str(obj))
        expected_context = sorted([
            'https://nexus.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0',
            'https://nexus.humanbrainproject.org/v0/contexts/neurosciencegraph/core/data/v0.3.1',
            {'license': 'schema:license'}
        ], key=lambda obj: str(obj))
        assert context == expected_context


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestModelProject(BaseTestKG):
    class_under_test = ModelProject

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_list_kgquery(self, kg_client):
        models = ModelProject.list(kg_client, api="query", scope="latest", size=10, resolved=True)
        assert len(models) == 10

    def test_list_nexus_with_filter(self, kg_client):
        models = ModelProject.list(kg_client, api="nexus", size=10, species="Rattus norvegicus")
        assert len(models) == 6

    def test_list_kgquery_with_filter(self, kg_client):
        models = ModelProject.list(kg_client, api="query", scope="latest", size=10, resolved=True, species="Rattus norvegicus")
        assert len(models) == 2

    def test_count_nexus(self, kg_client):
        count = ModelProject.count(kg_client, api='nexus')
        assert count == 351

    def test_count_kgquery(self, kg_client):
        count = ModelProject.count(kg_client, api='query')
        assert count == 351

    def test_existence_query(self, kg_client):
        obj = ModelProject(name="foo",
                           owners=Person("Holmes", "Sherlock"),
                           authors=Person("Holmes", "Sherlock"),
                           description="",
                           private=True,
                           date_created=datetime(2000, 1, 1))
        expected = {
            "op": "and",
            "value": [
                {
                    "path": "schema:name",
                    "op": "eq",
                    "value": "foo"
                },
                {
                    "path": "schema:dateCreated",
                    "op": "eq",
                    "value": "2000-01-01T00:00:00"
                }
            ]
        }
        generated = obj._build_existence_query(api="nexus")
        assert expected == generated


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestModelInstance(BaseTestKG):
    class_under_test = ModelInstance

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestMEModel(BaseTestKG):
    class_under_test = MEModel

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestMorphology(BaseTestKG):
    class_under_test = Morphology

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)

    def test_round_trip_with_morphology_file(self, kg_client):
        cls = self.class_under_test
        obj1 = cls("test_morph", morphology_file="http://example.com/test.asc")
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
                    assert val1.type == val2.cls.type
                else:
                    assert val1 == val2
        assert obj1.morphology_file == obj2.morphology_file


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestEModel(BaseTestKG):
    class_under_test = EModel

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestValidationTestDefinition(BaseTestKG):
    class_under_test = ValidationTestDefinition

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestValidationScript(BaseTestKG):
    class_under_test = ValidationScript

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestValidationResult(BaseTestKG):
    class_under_test = ValidationResult

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestValidationActivity(BaseTestKG):
    class_under_test = ValidationActivity

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestSimulation(BaseTestKG):
    class_under_test = Simulation

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestSimulationOutput(BaseTestKG):
    class_under_test = SimulationOutput

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)


@pytest.mark.skipif(not have_pyxus, reason="pyxus not available")
class TestSimulationConfiguration(BaseTestKG):
    class_under_test = SimulationConfiguration

    def test_list_nexus(self, kg_client):
        cls = self.class_under_test
        objects = cls.list(kg_client, api="nexus", size=10)
        assert len(objects) == 10, len(objects)
