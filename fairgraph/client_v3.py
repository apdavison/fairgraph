"""
define client
"""

# Copyright 2018-2021 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import logging
from uuid import uuid4

try:
    from kg_core.oauth import SimpleToken, ClientCredentials
    from kg_core.kg import KGv3
    from kg_core.models import Stage, Pagination
    have_v3 = True
except ImportError:
    have_v3 = False

from .errors import AuthenticationError


logger = logging.getLogger("fairgraph")


STAGE_MAP = {
    "released": Stage.RELEASED,
    "latest": Stage.IN_PROGRESS,
    "in progress": Stage.IN_PROGRESS
}


class KGv3Client(object):

    def __init__(
        self,
        token: str = None,
        host: str = "core.kg-ppd.ebrains.eu",
        client_id: str = None,
        client_secret: str = None
    ):
        if client_id and client_secret:
            token_handler = ClientCredentials(client_id, client_secret)
        elif token:
            token_handler = SimpleToken(token)
        else:
            try:
                token_handler = SimpleToken(os.environ["KG_AUTH_TOKEN"])
            except KeyError:
                raise AuthenticationError("Need to provide either token or client id/secret.")
        self._kg_client = KGv3(host=host, token_handler=token_handler)
        self.cache = {}

    def query(self, query_label, filter, from_index=0, size=100, scope="released", context=None):
        query = self.retrieve_query(query_label)
        uuid = self.uuid_from_uri(query["@id"])
        response = self._kg_client.get(
            path=f"/queries/{uuid}/instances",
            params={
                "from": from_index,
                "size": size,
                "stage": STAGE_MAP[scope],
                "allRequestParams": filter
            }
        )
        if response.is_successful():
            data = response.data()
            if context:
                for item in data:
                    item["@context"] = context
            return data
        else:
            raise Exception(response.error())

    def list(self, cls, space=None, from_index=0, size=100, api="core", scope="released",
             resolved=False, filter=None):
        """docstring"""

        if api == "core":
            # todo: handle filters, context, resolved, deprecated
            response = self._kg_client.get_instances(
                stage=STAGE_MAP[scope],
                target_type=cls.type,
                space=space or cls.space,
                # we use the default ResponseConfiguration
                pagination=Pagination(start_from=from_index, size=size)
            )
            return [cls.from_kg_instance(instance, self, resolved=resolved)
                    for instance in response.data()]
        elif api == "query":
            if resolved:
                query_type = "resolved"
            else:
                query_type = "simple"
            query_label = cls.get_query_label(query_type, space)
            instances = self.query(query_label, filter=filter, from_index=from_index,
                                   size=size, scope=scope, context=cls.context)
            return [cls.from_kg_instance(instance, self, resolved=resolved)
                    for instance in instances]
        else:
            raise ValueError("api must be either 'core' or 'query'")

    def count(self, cls, space=None, filter=None, scope="released"):
        raise NotImplementedError()

    def instance_from_full_uri(self, uri, use_cache=True, scope="released", resolved=False):
        logger.debug("Retrieving instance from {}, api='core' use_cache={}".format(uri, use_cache))
        if resolved:
            raise NotImplementedError
        if use_cache and uri in self.cache:
            logger.debug("Retrieving instance {} from cache".format(uri))
            data = self.cache[uri]
        else:
            try:
                response = self._kg_client.get_instance(
                    stage=STAGE_MAP[scope],
                    instance_id=self._kg_client.uuid_from_absolute_id(uri)
                )
            except Exception as err:
                if "404" in str(err):
                    data = None
                else:
                    raise
            else:
                data = response.data()
        return data

    def by_name(self, cls, name, match="equals", all=False,
                space=None, scope="released", resolved=False):
        """Retrieve an object based on the value of schema:name"""
        raise NotImplementedError()

    def create_new_instance(self, data=None, space=None, instance_id=None):
        response = self._kg_client.create_instance(
            space=space,
            payload=data,
            normalize_payload=True,
            instance_id=instance_id  # if already have id
        )
        if response.is_successful():
            return response.data()
        else:
            raise Exception(response.error())

    def update_instance(self, data):
        raise NotImplementedError()

    def delete_instance(self, instance_id):
        raise NotImplementedError()

    def uri_from_uuid(self, uuid):
        return self._kg_client.absolute_id(uuid)

    def uuid_from_uri(self, uri):
        return self._kg_client.uuid_from_absolute_id(uri)

    def store_query(self, query_label, query_definition, space):
        existing_query = self.retrieve_query(query_label)
        if existing_query:
            uuid = self.uuid_from_uri(existing_query["@id"])
        else:
            uuid = uuid4()

        response = self._kg_client.put(
            path=f"/queries/{uuid}",
            payload=query_definition,
            params={
                "space": space
            })
        # todo: handle errors

    def retrieve_query(self, query_label):
        response = self._kg_client.get(
            path=f"/queries/",
            params={
                "search": query_label
            }
        )
        if response.total() == 0:
            return None
        elif response.total() > 1:
            raise Exception("Retrieved multiple queries, this shouldn't happen")
        else:
            return response.data()[0]
