"""
define client
"""

import json
import logging
from urllib.parse import urlparse, quote_plus
from pyxus.client import NexusClient
from pyxus.resources.entity import Instance
from .core import Organization
from .electrophysiology import PatchClampExperiment


CURL_LOGGER = logging.getLogger("curl")
CURL_LOGGER.setLevel(logging.WARNING)


class NARClient(object):
    """docstring"""

    def __init__(self, token, nexus_endpoint="https://nexus.humanbrainproject.org/v0"):
        ep = urlparse(nexus_endpoint)
        self._nexus_client = NexusClient(scheme=ep.scheme, host=ep.netloc, prefix=ep.path[1:],
                                         alternative_namespace=nexus_endpoint,
                                         token=token)
        self._instance_repo = self._nexus_client.instances
        self.cache = {}  # todo: use combined uri and rev as cache keys

    def list(self, cls, from_index=0, size=100):
        """docstring"""
        instances = self._nexus_client.instances.list_by_schema(*cls.path.split("/"),
                                                                from_index=from_index,
                                                                size=size,
                                                                resolved=True).results
        for instance in instances:
            self.cache[instance.data["@id"]] = instance
        return [cls.from_kg_instance(instance, self) # todo: lazy resolution
                for instance in instances]

    def filter_query(self, path, filter, context, from_index=0, size=100):
        # todo: add size and from_index arguments
        response = self._nexus_client.instances.list(
            subpath=path, 
            filter_query=quote_plus(json.dumps(filter)), 
            context=quote_plus(json.dumps(context)),
            from_index=from_index,
            size=size,
            resolved=True)
        for instance in response.results:
            self.cache[instance.data["@id"]] = instance
        return response.results

    def instance_from_full_uri(self, uri):
        if uri in self.cache:
            return self.cache[uri]
        else:
            instance = Instance(Instance.extract_id_from_url(uri, self._instance_repo.path), 
                                data=self._instance_repo._http_client.get(uri),
                                root_path=Instance.path)
            self.cache[instance.data["@id"]] = instance
            return instance

    def create_new_instance(self, path, data):
        instance = Instance(path, data, Instance.path)
        entity = self._nexus_client.instances.create(instance)
        return entity