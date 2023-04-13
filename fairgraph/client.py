"""
define client
"""

# Copyright 2018-2023 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import os
import logging
from typing import Any, Dict, Iterable, List, Optional, Union, TYPE_CHECKING
from uuid import uuid4, UUID

try:
    from kg_core.kg import kg
    from kg_core.request import Stage, Pagination, ExtendedResponseConfiguration, ReleaseTreeScope
    from kg_core.response import ResultPage, JsonLdDocument, SpaceInformation

    have_kg_core = True
except ImportError:
    have_kg_core = False

from .errors import AuthenticationError, AuthorizationError, ResourceExistsError

if TYPE_CHECKING:
    from .kgobject import KGObject

try:
    import clb_nb_utils.oauth as clb_oauth  # type: ignore
except ImportError:
    clb_oauth = None


logger = logging.getLogger("fairgraph")


if have_kg_core:
    STAGE_MAP = {
        "released": Stage.RELEASED,
        "latest": Stage.IN_PROGRESS,
        "in progress": Stage.IN_PROGRESS,
    }
    default_response_configuration = ExtendedResponseConfiguration(return_embedded=True)


AVAILABLE_PERMISSIONS = [
    "CREATE",
    "READ",
    "DELETE",
    "RELEASE",
    "INVITE_FOR_REVIEW",
    "INVITE_FOR_SUGGESTION",
    "SUGGEST",
    "UNRELEASE",
    "READ_RELEASED",
    "RELEASE_STATUS",
    "WRITE",
]


class KGClient(object):
    def __init__(
        self,
        token: Optional[str] = None,
        host: str = "core.kg-ppd.ebrains.eu",
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        if not have_kg_core:
            raise ImportError(
                "Please install the kg_core package from https://github.com/HumanBrainProject/kg-core-python/"
            )
        if client_id and client_secret:
            self._kg_client_builder = kg(host).with_credentials(client_id, client_secret)
        elif token:
            self._kg_client_builder = kg(host).with_token(token)
        elif clb_oauth:
            self._kg_client_builder = kg(host).with_token(clb_oauth.get_token())  # running in EBRAINS Jupyter Lab
        else:
            try:
                self._kg_client_builder = kg(host).with_token(os.environ["KG_AUTH_TOKEN"])
            except KeyError:
                raise AuthenticationError("Need to provide either token or client id/secret.")
        self._kg_client = self._kg_client_builder.build()
        self.__kg_admin_client = None
        self.host = host
        self._user_info = None
        self.cache: Dict[str, JsonLdDocument] = {}
        self._query_cache: Dict[str, str] = {}
        self.accepted_terms_of_use = False

    @property
    def _kg_admin_client(self):
        if self.__kg_admin_client is None:
            self.__kg_admin_client = self._kg_client_builder.build_admin()
        return self.__kg_admin_client

    @property
    def token(self) -> Optional[str]:
        return self._kg_client.instances._kg_config.token_handler._fetch_token()

    def _check_response(
        self,
        response: ResultPage[JsonLdDocument],
        ignore_not_found: bool = False,
        error_context: str = "",
    ) -> ResultPage[JsonLdDocument]:
        if response.error:
            # todo: handle "ignore_not_found"
            if response.error.code == 403:
                raise AuthorizationError(f"{response} {error_context}")
            elif response.error.code == 401:
                raise AuthenticationError(f"{response} {error_context}")
            elif response.error.code == 404 and ignore_not_found:
                return response
            elif response.error.code == 409:
                raise ResourceExistsError(f"{response} {error_context}")
            else:
                raise Exception(f"Error: {response.error} {error_context}")
        else:
            return response

    def query(
        self,
        filter: Dict[str, str],
        query: Dict[str, Any],
        space: Optional[str] = None,
        instance_id: Optional[str] = None,
        from_index: int = 0,
        size: int = 100,
        scope: str = "released",
        id_key: str = "@id",
        use_stored_query: bool = False,
    ) -> ResultPage[JsonLdDocument]:

        query_id = query.get("@id", None)
        if use_stored_query:

            def _query(scope, from_index, size):
                response = self._kg_client.queries.execute_query_by_id(
                    query_id=self.uuid_from_uri(query_id),
                    additional_request_params=filter or {},
                    stage=STAGE_MAP[scope],
                    pagination=Pagination(start=from_index, size=size),
                    instance_id=instance_id,
                    # restrict_to_spaces=[space] if space else None,
                )
                error_context = f"_query(scope={scope} space={space} query_id={query_id} filter={filter} instance_id={instance_id} size={size} from_index={from_index})"
                return self._check_response(response, error_context=error_context)

        else:

            def _query(scope, from_index, size):
                response = self._kg_client.queries.test_query(
                    query,
                    additional_request_params=filter or {},
                    stage=STAGE_MAP[scope],
                    pagination=Pagination(start=from_index, size=size),
                    instance_id=instance_id,
                    # restrict_to_spaces=[space] if space else None,
                )
                error_context = f"_query(scope={scope} space={space} query_id={query_id} filter={filter} instance_id={instance_id} size={size} from_index={from_index})"
                return self._check_response(response, error_context=error_context)

        if scope == "any":
            # the following implementation is simple but very inefficient
            # because we retrieve _all_ instances and then apply the limits
            # from_index and size.
            # todo: make this more efficient, but be sure to clearly
            #       explain the algorithm
            instances = {}
            # first we get the released instances
            response = _query("released", 0, 100000)
            for instance in response.data:
                instances[instance[id_key]] = instance
            # now we get the "in progress" instances, and overwrite
            # any existing released instances which have the same id
            response = _query("in progress", 0, 100000)
            for instance in response.data:
                instances[instance[id_key]] = instance
            response.data = list(instances.values())[from_index : from_index + size]
            response.size = len(response.data)
            response.total = len(instances)
            return response
        else:
            return _query(scope, from_index, size)

    def list(
        self,
        target_type: str,
        space: Optional[str] = None,
        from_index: int = 0,
        size: int = 100,
        scope: str = "released",
    ) -> ResultPage[JsonLdDocument]:
        """docstring"""

        def _list(scope, from_index, size):
            response = self._kg_client.instances.list(
                stage=STAGE_MAP[scope],
                target_type=target_type,
                space=space,
                response_configuration=default_response_configuration,
                pagination=Pagination(start=from_index, size=size),
            )
            error_context = (
                f"_list(scope={scope} space={space} target_type={target_type} size={size} from_index={from_index})"
            )
            return self._check_response(response, error_context=error_context)

        if scope == "any":
            # see comments in query() about this implementation
            instances = {}
            # first we get the released instances
            response = _list("released", 0, 100000)
            for instance in response.data:
                instances[instance["@id"]] = instance
            # now we get the "in progress" instances, and overwrite
            # any existing released instances which have the same id
            response = _list("in progress", 0, 100000)
            for instance in response.data:
                instances[instance["@id"]] = instance
            response.data = list(instances.values())[from_index : from_index + size]
            response.size = len(response.data)
            response.total = len(instances)
            return response
        else:
            return _list(scope, from_index, size)

    def instance_from_full_uri(
        self,
        uri: str,
        use_cache: bool = True,
        scope: str = "released",
        require_full_data: bool = True,
    ) -> JsonLdDocument:
        logger.debug("Retrieving instance from {}, api='core' use_cache={}".format(uri, use_cache))
        data: JsonLdDocument
        if use_cache and uri in self.cache:
            logger.debug("Retrieving instance {} from cache".format(uri))
            data = self.cache[uri]
        else:

            def _get_instance(scope):
                try:
                    response = self._kg_client.instances.get_by_id(
                        stage=STAGE_MAP[scope],
                        instance_id=self.uuid_from_uri(uri),
                        extended_response_configuration=default_response_configuration,
                    )
                except Exception as err:
                    if "404" in str(err):
                        data = None
                    else:
                        raise
                else:
                    data = response.data
                # in some circumstances, the KG returns "minimal" metadata,
                # e.g. with just the id and fullName fields
                # this means the user does not have full access, so we count this as no data
                if require_full_data and data and "http://schema.org/identifier" not in data:
                    data = None
                return data

            if scope == "any":
                data_ip = _get_instance("in progress")
                data_rel = _get_instance("released")
                data = data_rel or data_ip
                if data_ip is not None:
                    data.update(data_ip)
            else:
                data = _get_instance(scope)
        return data

    def create_new_instance(
        self, data: JsonLdDocument, space: str, instance_id: Optional[str] = None
    ) -> JsonLdDocument:
        if "'@id': None" in str(data):
            raise Exception("payload contains undefined ids")
        if instance_id:
            response = self._kg_client.instances.create_new_with_id(
                space=space,
                payload=data,
                instance_id=instance_id,
                extended_response_configuration=default_response_configuration,
            )
        else:
            response = self._kg_client.instances.create_new(
                space=space,
                payload=data,
                extended_response_configuration=default_response_configuration,
            )
        error_context = f"create_new_instance(data={data}, space={space}, instance_id={instance_id})"
        return self._check_response(response, error_context=error_context).data

    def update_instance(self, instance_id: str, data: JsonLdDocument) -> JsonLdDocument:
        response = self._kg_client.instances.contribute_to_partial_replacement(
            instance_id=instance_id,
            payload=data,
            extended_response_configuration=default_response_configuration,
        )
        error_context = f"update_instance(data={data}, instance_id={instance_id})"
        return self._check_response(response, error_context=error_context).data

    def replace_instance(self, instance_id: str, data: JsonLdDocument) -> JsonLdDocument:
        response = self._kg_client.instances.contribute_to_full_replacement(
            instance_id=instance_id,
            payload=data,
            extended_response_configuration=default_response_configuration,
        )
        error_context = f"replace_instance(data={data}, instance_id={instance_id})"
        return self._check_response(response, error_context=error_context).data

    def delete_instance(self, instance_id: str, ignore_not_found: bool = True):
        response = self._kg_client.instances.delete(instance_id)
        # response is None if no errors
        return response

    def uri_from_uuid(self, uuid: str) -> str:
        namespace = self._kg_client.instances._kg_config.id_namespace
        return f"{namespace}{uuid}"

    def uuid_from_uri(self, uri: str) -> UUID:
        namespace = self._kg_client.instances._kg_config.id_namespace
        assert uri.startswith(namespace)
        return UUID(uri[len(namespace) :])

    def store_query(self, query_label: str, query_definition: Dict[str, Any], space: str):
        existing_query = self.retrieve_query(query_label)
        if existing_query:
            query_id = self.uuid_from_uri(existing_query["@id"])
        else:
            query_id = uuid4()

        try:
            response = self._check_response(
                self._kg_client.queries.save_query(
                    query_id=query_id, payload=query_definition, space=space or "myspace"
                )
            )
        except AuthorizationError:
            response = self._check_response(
                self._kg_client.queries.save_query(query_id=query_id, payload=query_definition, space="myspace")
            )

        query_definition["@id"] = self.uri_from_uuid(query_id)

    def retrieve_query(self, query_label: str) -> Dict[str, Any]:
        if query_label not in self._query_cache:
            response = self._check_response(self._kg_client.queries.list_per_root_type(search=query_label))
            if response.total == 0:
                return None
            elif response.total > 1:
                # check for exact match to query_label
                found_match = False
                kgvq = "https://core.kg.ebrains.eu/vocab/query"
                for result in response.data:
                    if result[f"{kgvq}/meta"][f"{kgvq}/name"] == query_label:
                        query_definition = result
                        found_match = True
                        break
                if not found_match:
                    return None
            else:
                query_definition = response.data[0]
            self._query_cache[query_label] = query_definition
        return self._query_cache[query_label]

    def user_info(self) -> Dict[str, Any]:
        if self._user_info is None:
            try:
                self._user_info = self._kg_client.users.my_info().data
            except KeyError:
                self._user_info is None
        return self._user_info

    def spaces(
        self, permissions: Optional[Iterable[str]] = None, names_only: bool = False
    ) -> Union[List[str], List[SpaceInformation]]:
        if permissions and isinstance(permissions, Iterable):
            for permission in permissions:
                if permission.upper() not in AVAILABLE_PERMISSIONS:
                    raise ValueError(f"Invalid permission '{permission}'")
        response = self._kg_client.spaces.list(permissions=bool(permissions), pagination=Pagination(start=0, size=100))
        accessible_spaces = self._check_response(response).data
        if permissions and isinstance(permissions, Iterable):
            filtered_spaces = []
            for space in accessible_spaces:
                for permission in permissions:
                    if permission.upper() in space.permissions:
                        if names_only:
                            filtered_spaces.append(space.name)
                        else:
                            filtered_spaces.append(space)
            return filtered_spaces
        else:
            if names_only:
                return [space.name for space in accessible_spaces]
            else:
                return accessible_spaces

    @property
    def _private_space(self) -> str:
        # temporary workaround
        return f"private-{self.user_info().identifiers[0]}"

    def configure_space(self, space_name: Optional[str] = None, types: Optional[List[KGObject]] = None) -> str:
        """
        Creates and configures a Knowledge Graph (KG) space with the specified name and types.

        Args:
            space_name (str, required (optional only if you run inside a collab)): The name of the KG space to create and configure.
                If not provided, the method will try to obtain the collab ID from the environment
                variables and use it to generate a default space name in the format "collab-collab_id".
                If you are not launching this from inside an EBRAINS collab, you should provide a space name.
            types (list of Type, required): An array containing the Type classes that should be included
                in this space.

        Returns:
            str: The name of the configured KG space.

        Example usage:
            types = [Dataset, DatasetVersion, Software, SoftwareVersion]
            space_name = "collab-MyCollab"
            kg_client = KGClient()
            kg_client.configure_space(space_name, types)
        """
        if space_name is None:
            collab_id = os.environ.get("LAB_COLLAB_ID")
            if collab_id is None:
                raise ValueError(
                    "If you are not launching this from inside an EBRAINS collab, you should provide a space name with the following format: collab-collab_id."
                )
            else:
                space_name = f"collab-{collab_id}"
        result = self._kg_admin_client.create_space_definition(space=space_name)
        if result:  # error
            raise Exception(f"Unable to configure KG space for space '{space_name}': {result}")
        for cls in types:
            result = self._kg_admin_client.assign_type_to_space(space=space_name, target_type=cls.type_[0])
            if result:  # error
                raise Exception(f"Unable to assign {cls.__name__} to space {space_name}: {result}")
        return space_name

    def move_to_space(self, uri: str, destination_space: str):
        response = self._kg_client.instances.move(instance_id=self.uuid_from_uri(uri), space=destination_space)
        if response.error:
            raise Exception(response.error)

    def is_released(self, uri: str, with_children: bool = False) -> bool:
        """Release status of the node"""
        if with_children:
            release_tree_scope = ReleaseTreeScope.CHILDREN_ONLY
        else:
            release_tree_scope = ReleaseTreeScope.TOP_INSTANCE_ONLY
        response = self._kg_client.instances.get_release_status(
            instance_id=self.uuid_from_uri(uri), release_tree_scope=release_tree_scope
        )
        if response.data in ("RELEASED", "HAS_CHANGED"):
            return True
        elif response.data == "UNRELEASED":
            return False
        else:
            raise AuthorizationError("You are not able to access the release status")

    def release(self, uri: str):
        """Release the node with the given uri"""
        response = self._kg_client.instances.release(self.uuid_from_uri(uri))
        if response:
            raise Exception(f"Can't release node with id {uri}. Error message: {response}")

    def unrelease(self, uri: str):
        """Unrelease the node with the given uri"""
        response = self._kg_client.instances.unrelease(self.uuid_from_uri(uri))
        if response:
            raise Exception(f"Can't unrelease node with id {uri}. Error message: {response}")
