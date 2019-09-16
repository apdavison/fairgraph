# encoding: utf-8
"""
Tests of fairgraph.brainsimulation module, using a mock Http client
which returns data loaded from the files in the test_data directory.
"""

from fairgraph.base import KGQuery, KGProxy, as_list, Distribution
from fairgraph.commons import BrainRegion, CellType, QuantitativeValue
from fairgraph.brainsimulation import ModelScript

from .utils import kg_client, MockKGObject, test_data_lookup
from pyxus.resources.entity import Instance


class TestModelScript(object):

    def test_get_context(self, kg_client):
        obj = ModelScript("test_code",
                          code_location="https://github.com/SomeOrg/ProjName",
                          code_format="Python", license="BSD",
                          id="fake_uuid_381aa74bc9")
        context = sorted(obj.get_context(kg_client),
                         key=lambda obj: str(obj))
        expected_context = sorted([
            'https://nexus.humanbrainproject.org/v0/contexts/nexus/core/resource/v0.3.0',
            'https://nexus.humanbrainproject.org/v0/contexts/neurosciencegraph/core/data/v0.3.1',
            {'license': 'schema:license'}
        ], key=lambda obj: str(obj))
        assert context == expected_context
