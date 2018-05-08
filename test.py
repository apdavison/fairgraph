"""

"""

from pyxus.client import NexusClient, NexusConfig
from pyxus.resources.repository import (DomainRepository, ContextRepository, 
                                        OrganizationRepository,
                                        InstanceRepository, SchemaRepository)
import nar.client
from nar.electrophysiology import PatchClampExperiment


#class MockQueryResult(object):
#    results = {"results": []}


class MockHttpClient(object):

    def __init__(self, endpoint, prefix, auth_client=None, raw=False, alternative_endpoint_writing=None):
        pass

    def get(self, *args, **kwargs):
        return {
            "total": 42,
            "results": [],
            "links": []
        }


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


def test_PatchClampExperiment():
    nar.client.NexusClient = MockNexusClient
    client = nar.client.NARClient("thisismytoken")
    experiments = PatchClampExperiment.list(client)
