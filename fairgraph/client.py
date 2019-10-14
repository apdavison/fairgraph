"""
define client
"""

import os
import json
import logging
try:
    from urllib.parse import urlparse, quote_plus
except ImportError:  # Python 2
    from urlparse import urlparse
    from urllib import quote_plus
from openid_http_client.auth_client.access_token_client import AccessTokenClient
from openid_http_client.http_client import HttpClient
from pyxus.client import NexusClient
from pyxus.resources.entity import Instance

from .errors import AuthenticationError


CURL_LOGGER = logging.getLogger("curl")
CURL_LOGGER.setLevel(logging.WARNING)
logger = logging.getLogger("fairgraph")


class KGClient(object):
    """docstring"""

    def __init__(self, token=None,
                 nexus_endpoint="https://nexus.humanbrainproject.org/v0",
                 kg_query_endpoint="https://kg.humanbrainproject.org/query"):
        if token is None:
            try:
                token = os.environ["HBP_AUTH_TOKEN"]
            except KeyError:
                raise AuthenticationError("No token provided.")
        ep = urlparse(nexus_endpoint)
        self.nexus_endpoint = nexus_endpoint
        auth_client = AccessTokenClient(token)
        self._nexus_client = NexusClient(scheme=ep.scheme, host=ep.netloc, prefix=ep.path[1:],
                                         alternative_namespace=nexus_endpoint,
                                         auth_client=auth_client)
        self._kg_query_client = HttpClient(kg_query_endpoint, "", auth_client=auth_client)
        self._instance_repo = self._nexus_client.instances
        self.cache = {}  # todo: use combined uri and rev as cache keys


    def list(self, cls, from_index=0, size=100, deprecated=False, api="nexus", scope="released",
             resolved=False, filter=None, context=None):
        """docstring"""
        if api == "nexus":
            instances = []
            organization, domain, schema, version = cls.path.split("/")
            subpath = "/{}/{}/{}/{}".format(organization, domain, schema, version)
            if filter:
                filter = quote_plus(json.dumps(filter))
            if context:
                context=quote_plus(json.dumps(context))
            query = self._nexus_client.instances.list(subpath=subpath,
                                                      filter_query=filter,
                                                      context=context,
                                                      from_index=from_index,
                                                      size=size,
                                                      deprecated=deprecated,
                                                      resolved=True)

            # todo: add support for "sort" field
            instances.extend(query.results)
            next = query.get_next_link()
            while len(instances) < size and next:
                query = self._nexus_client.instances.list_by_full_path(next)
                instances.extend(query.results)
                next = query.get_next_link()

            for instance in instances:
                self.cache[instance.data["@id"]] = instance
            return [cls.from_kg_instance(instance, self, resolved=resolved) # todo: lazy resolution
                    for instance in instances]
        elif api == "query":
            if hasattr(cls, "query_id"):
                if scope not in ("released", "inferred"):  # todo - use a more user-friendly term for 'inferred' and map appropriately
                    raise ValueError("'scope' must be either 'released' or 'inferred'")
                start = from_index
                response = self._kg_query_client.get(
                    "{}/{}/instances?start={}&size={}&databaseScope={}".format(cls.path,
                                                                               cls.query_id,
                                                                               start,
                                                                               size,
                                                                               scope.upper()))
                instances = [
                    Instance(cls.path, data, Instance.path)
                    for data in response["results"]
                ]
                start += response["size"]
                while start < min(response["total"], size):
                    response = self._kg_query_client.get(
                        "{}/{}/instances?start={}&size={}&databaseScope={}".format(cls.path,
                                                                                   cls.query_id,
                                                                                   start,
                                                                                   size,
                                                                                   scope.upper()))
                    instances.extend([
                        Instance(cls.path, data, Instance.path)
                        for data in response["results"]
                    ])
                    start += response["size"]
                # todo: caching
                return [cls.from_kg_instance(instance, self, resolved=resolved)
                        for instance in instances]
            else:
                raise NotImplementedError("Coming soon. For now, please use api='nexus'")
        else:
            raise ValueError("'api' must be either 'nexus' or 'query'")

    def filter_query(self, path, filter, context, from_index=0, size=100, deprecated=False):
        instances = []
        query = self._nexus_client.instances.list(
            subpath=path,
            filter_query=quote_plus(json.dumps(filter)),
            context=quote_plus(json.dumps(context)),
            from_index=from_index,
            size=size,
            deprecated=deprecated,
            resolved=True)
        # todo: add support for "sort" field
        instances.extend(query.results)
        next = query.get_next_link()
        while len(instances) < size and next:
            query = self._nexus_client.instances.list_by_full_path(next)
            instances.extend(query.results)
            next = query.get_next_link()

        for instance in instances:
            self.cache[instance.data["@id"]] = instance
        return instances

    def instance_from_full_uri(self, uri, cls=None, use_cache=True, deprecated=False, api="nexus"):
        # 'deprecated=True' means 'returns an instance even if that instance is deprecated'
        # should perhaps be called 'show_deprecated' or 'include_deprecated'
        if use_cache and uri in self.cache:
            logger.debug("Retrieving instance from cache")
            instance = self.cache[uri]
        elif api == "nexus":
            instance = Instance(Instance.extract_id_from_url(uri, self._instance_repo.path),
                                data=self._instance_repo._http_client.get(uri),
                                root_path=Instance.path)
            self.cache[instance.data["@id"]] = instance
            logger.debug("Retrieved instance from KG " + str(instance.data))
            if instance and deprecated is False and instance.data["nxv:deprecated"]:
                instance = None
        elif api == "query":
            if cls and hasattr(cls, "query_id"):
                response = self._kg_query_client.get(
                    "{}/{}/instances?databaseScope=INFERRED&id={}".format(cls.path,
                                                                          cls.query_id,
                                                                          uri))
                instance = Instance(cls.path, response["results"][0], Instance.path)
            else:
                raise NotImplementedError("Coming soon. For now, please use api='nexus'")
        else:
            raise ValueError("'api' must be either 'nexus' or 'query'")
        return instance

    def instance_from_uuid(self, path, uuid, deprecated=False):
        # todo: caching
        instance = self._instance_repo.read_by_full_id(path + "/" + uuid)
        if instance and deprecated is False and instance.data["nxv:deprecated"]:
            return None
        else:
            return instance

    def create_new_instance(self, path, data):
        instance = Instance(path, data, Instance.path)
        entity = self._nexus_client.instances.create(instance)
        entity.data.update(data)
        return entity

    def update_instance(self, instance):
        instance.data.pop("links", None)
        instance.data.pop("nxv:rev", None)
        instance.data.pop("nxv:deprecated", None)
        instance = self._nexus_client.instances.update(instance)
        return instance

    def delete_instance(self, instance):
        self._nexus_client.instances.delete(instance)
        if instance.id in self.cache:
            self.cache.pop(instance.id)

    def by_name(self, cls, name, match="equals", all=False, api="nexus"):
        """Retrieve an object based on the value of schema:name"""
        # todo: allow non-exact searches
        if api not in ("query", "nexus"):
            raise ValueError("'api' must be either 'nexus' or 'query'")
        valid_match_methods = {
            #"query": ("starts_with", "ends_with", "contains", "equals", "regex"),
            "query": ("contains", "equals"),
            "nexus": ("equals")
        }
        if match not in valid_match_methods[api]:
            raise ValueError("'match' must be one of {}".format(valid_match_methods[api]))

        if api == "nexus":
            op = {"equals": "eq", "contains": "in"}[match]
            context = {"schema": "http://schema.org/"}
            query_filter = {
                "path": "schema:name",
                "op": op,
                "value": name
            }
            instances = self.filter_query(cls.path, query_filter, context)
        else:
            assert api == "query"
            if hasattr(cls, "query_id"):
                response = self._kg_query_client.get(
                    "{}/{}{}/instances?databaseScope=INFERRED&name={}".format(cls.path,
                                                                              cls.query_id,
                                                                              match == "contains" and "_name_contains" or "",  # workaround
                                                                              name))
                instances = [Instance(cls.path, result, Instance.path)
                             for result in response["results"]]
            else:
                raise NotImplementedError("Coming soon. For now, please use api='nexus'")
        if instances:
            if all:
                return [cls.from_kg_instance(inst, self)
                        for inst in instances]
            else:  # return only the first result
                return cls.from_kg_instance(instances[0], self)
        else:
            return None
