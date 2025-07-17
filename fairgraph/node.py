from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Dict, List, Union, Any
from copy import copy
import logging
from warnings import warn

from openminds.base import value_to_jsonld
from openminds.properties import Property

from .registry import Node
from .base import Resolvable, ErrorHandling, RepresentsSingleObject
from .kgquery import KGQuery
from .queries import (
    QueryProperty,
    get_query_properties,
    get_query_filter_property,
    get_filter_value
)
from .errors import ResolutionFailure, CannotBuildExistenceQuery
from .utility import (
    as_list,  # temporary for backwards compatibility (a lot of code imports it from here)
    expand_uri,
    invert_dict
)

if TYPE_CHECKING:
    from .client import KGClient
    from .utility import ActivityLog

logger = logging.getLogger("fairgraph")

JSONdict = Dict[str, Any]  # see https://github.com/python/typing/issues/182 for some possible improvements

default_context = {
    "v3": {
        "vocab": "https://openminds.ebrains.eu/vocab/",
    },
    "v4": {
        "vocab": "https://openminds.om-i.org/props/"
    }
}


class ContainsMetadata(Resolvable, metaclass=Node):  # KGObject and EmbeddedMetadata
    properties: List[Property] = []
    reverse_properties: List[Property] = []
    context: Dict[str, str] = default_context["v3"]
    type_: str
    scope: Optional[str]
    space: Union[str, None]
    default_space: Union[str, None]
    remote_data: Optional[JSONdict]
    aliases: Dict[str, str] = {}
    error_handling: ErrorHandling = ErrorHandling.log

    def __init__(self, data: Optional[Dict] = None, **properties):
        properties_copy = copy(properties)
        for prop in self.__class__.all_properties:
            try:
                val = properties[prop.name]
            except KeyError:
                if prop.required:
                    msg = "Property '{}' is required.".format(prop.name)
                    ErrorHandling.handle_violation(self.error_handling, msg)
                val = None
            else:
                properties_copy.pop(prop.name)
            if isinstance(val, (list, tuple)) and len(val) == 0:  # empty list
                val = None
            setattr(self, prop.name, val)
        for name_, alias_ in self.aliases.items():
            # the trailing underscores are because 'name' and 'alias' can be keys in 'properties'
            if name_ in properties_copy:
                val = properties_copy.pop(name_)
                if val is not None:
                    if properties.get(alias_, None):
                        raise ValueError(f"'{name_}' is an alias for '{alias_}', you cannot specify both")
                    setattr(self, alias_, val)
        if len(properties_copy) > 0:
            if len(properties_copy) == 1:
                raise NameError(f'{self.__class__.__name__} does not have a property named "{list(properties_copy)[0]}".')
            else:
                raise NameError(
                    f"""{self.__class__.__name__} does not have properties named "{'", "'.join(properties_copy)}"."""
                )

        # we store the original remote data in `_raw_remote_data`
        # and a normalized version in `remote_data`
        self._raw_remote_data = data  # for debugging
        self.remote_data = {}
        if data:
            self.remote_data = self.to_jsonld(include_empty_properties=True, embed_linked_nodes=False)

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            if name in self.aliases:
                return object.__getattribute__(self, self.aliases[name])
            else:
                raise

    def __setattr__(self, name, value):
        try:
            prop = self._property_lookup[name]
        except KeyError:
            if name in self.aliases:
                setattr(self, self.aliases[name], value)
            else:
                super().__setattr__(name, value)
        else:
            failures = prop.validate(value)
            if failures:
                errmsg = str(failures)  # todo: create a nicer error message
                ErrorHandling.handle_violation(self.error_handling, errmsg)
            super().__setattr__(name, value)

    @classmethod
    def get_property(cls, name):
        return cls._property_lookup[name]

    @classmethod
    def from_jsonld(cls, data: JSONdict, scope: Optional[str] = None) -> ContainsMetadata:
        """
        Create an instance of the class from a JSON-LD document.
        """
        pass

    def save(
        self,
        client: KGClient,
        space: Optional[str] = None,
        recursive: bool = True,
        activity_log: Optional[ActivityLog] = None,
        replace: bool = False,
        ignore_auth_errors: bool = False,
        ignore_duplicates: bool = False
    ):
        pass

    @classmethod
    def set_error_handling(
        cls, value: Union[ErrorHandling, None]
    ):
        """
        Control validation for this class.

        Args:
            value (str): action to follow when there is a validation failure.
                (e.g. if a required property is not provided).
                Possible values: "error", "warning", "log", None
            property_names (str or list of str, optional): If not provided, the error handling
                mode will be applied to all properties. If a property name or list of names is given,
                the mode will be applied only to those properties.
        """
        if value is None:
            cls.error_handling = ErrorHandling.none
        else:
            cls.error_handling = ErrorHandling(value)

    @classmethod
    def normalize_filter(cls, filter_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize a dict containing filter key:value pairs so that it can be used
        in a call to the KG query API.

        Example:
            >>> import fairgraph.openminds.core as omcore
            >>> person = omcore.Person.from_uuid("045f846f-f010-4db8-97b9-b95b20970bf2", kg_client)
            >>> filter_dict = {"custodians": person, "name": "Virtual"}
            >>> omcore.Dataset.normalize_filter(filter_dict)
            {'name': 'Virtual',
             'custodians': 'https://kg.ebrains.eu/api/instances/045f846f-f010-4db8-97b9-b95b20970bf2'}
        """
        normalized = {}
        filter_dict_copy = filter_dict.copy()

        # handle aliases
        for name_, alias_ in cls.aliases.items():
            if name_ in filter_dict_copy:
                filter_dict_copy[alias_] = filter_dict_copy.pop(name_)

        for prop in cls.all_properties:
            if prop.name in filter_dict_copy:
                value = filter_dict_copy[prop.name]
                if isinstance(value, dict):
                    normalized[prop.name] = {}
                    for child_cls in prop.types:
                        normalized[prop.name].update(child_cls.normalize_filter(value))
                else:
                    normalized[prop.name] = get_filter_value(prop, value)
        return normalized

    @classmethod
    def generate_query_properties(cls, follow_links: Optional[Dict[str, Any]] = None):
        """
        Generate a list of QueryProperty instances for this class
        for use in constructing a KG query definition.

        Args:
            follow_links (dict): The links in the graph to follow when constructing the query. Defaults to None.
        """
        if issubclass(cls, RepresentsSingleObject):  # KGObject
            properties = [
                QueryProperty("https://core.kg.ebrains.eu/vocab/meta/space", name="query:space"),
                QueryProperty("@type"),
            ]
        else:  # EmbeddedMetadata
            properties = [QueryProperty("@type")]
        reverse_aliases = invert_dict(cls.aliases)
        for prop in cls.all_properties:
            if prop.is_link and follow_links:
                if prop.name in follow_links:
                    properties.extend(get_query_properties(prop, follow_links[prop.name]))
                elif reverse_aliases.get(prop.name, None) in follow_links:
                    properties.extend(get_query_properties(prop, follow_links[reverse_aliases[prop.name]]))
                else:
                    properties.extend(get_query_properties(prop))
            else:
                properties.extend(get_query_properties(prop))
        return properties

    @classmethod
    def generate_query_filter_properties(
        cls,
        filters: Optional[Dict[str, Any]] = None,
    ):
        """

        Args:
            filters (dict, optional): A dict containing search parameters for the query.
        """
        if filters is None:
            filters = {}
        properties = []
        for prop in cls.all_properties:
            if prop.name in filters:
                properties.append(get_query_filter_property(prop, filters[prop.name]))
        return properties

    @classmethod
    def _deserialize_data(cls, data: JSONdict, include_id: bool = False):
        # check types match
        if cls.type_ not in data["@type"]:
            if types_match(cls.type_, data["@type"][0]):
                cls.type_ = data["@type"][0]
            else:
                raise TypeError("type mismatch {} - {}".format(cls.type_, data["@type"]))
        # normalize data by expanding keys
        context = copy(cls.context)
        if "om-i.org" in cls.type_:
            context = default_context["v4"]
        else:
            context = default_context["v3"]

        D = {"@type": data["@type"]}
        if include_id:
            D["@id"] = data["@id"]
        for key, value in data.items():
            if "__" in key:
                key, type_filter = key.split("__")
                normalised_key = expand_uri(key, context)
                value = [item for item in as_list(value) if item["@type"][0].endswith(type_filter)]
                if normalised_key in D:
                    D[normalised_key].extend(value)
                else:
                    D[normalised_key] = value
            elif key.startswith("Q"):  # for 'Q' properties in data from queries
                D[key] = value
            elif key[0] != "@":
                normalised_key = expand_uri(key, context)
                D[normalised_key] = value

        def _get_type_from_data(data_item):
            type_ = data_item.get("@type", None)
            if type_:
                return type_[0]
            else:
                return None

        deserialized_data = {}
        for prop in cls.all_properties:
            expanded_path = expand_uri(prop.path, context)
            data_item = D.get(expanded_path)
            if data_item is not None and prop.reverse:
                # for reverse properties, more than one property can have the same path
                # so we extract only those sub-items whose types match
                try:
                    data_item = [
                        part for part in as_list(data_item)
                        if _get_type_from_data(part) in [t.type_ for t in prop.types]
                    ]
                except AttributeError:
                    # problem when a forward and reverse path both given the same expanded path
                    # e.g. for Configuration
                    data_item = None
            # sometimes queries put single items in a list, this removes the enclosing list
            if (not prop.multiple) and isinstance(data_item, (list, tuple)) and len(data_item) == 1:
                data_item = data_item[0]
            if data_item is None:
                if prop.reverse and "@id" in data:
                    if isinstance(prop.reverse, list):
                        # todo: handle all possible reverses
                        #       for now, we just take the first
                        deserialized_data[prop.name] = KGQuery(prop.types, {prop.reverse[0]: data["@id"]})
                    else:
                        deserialized_data[prop.name] = KGQuery(prop.types, {prop.reverse: data["@id"]})
                else:
                    deserialized_data[prop.name] = None
            else:
                deserialized_data[prop.name] = prop.deserialize(data_item)
        return deserialized_data

    def resolve(
        self,
        client: KGClient,
        scope: Optional[str] = None,
        use_cache: bool = True,
        follow_links: Optional[Dict[str, Any]] = None,
    ):
        """
        Resolve properties that are represented by KGProxy objects.

        Args:
            client: KGClient object that handles the communication with the KG.
            scope (str): The scope of instances to include in the response.
                   Valid values are 'released', 'in progress', 'any'.
            use_cache (bool): whether to use cached data if they exist. Defaults to True.
            follow_links (dict): The links in the graph to follow. Defaults to None.

        Note: a real (non-proxy) object resolves to itself.
        """
        use_scope = scope or self.scope or "released"
        if follow_links:
            reverse_aliases = invert_dict(self.__class__.aliases)
            for prop in self.__class__.all_properties:
                if prop.is_link:
                    follow_name = None
                    if prop.name in follow_links:
                        follow_name = prop.name
                    elif reverse_aliases.get(prop.name, None) in follow_links:
                        follow_name = reverse_aliases[prop.name]

                    if follow_name:
                        if issubclass(prop.types[0], ContainsMetadata):
                            values = getattr(self, prop.name)
                            resolved_values: List[Any] = []
                            for value in as_list(values):
                                if isinstance(value, Resolvable):
                                    if isinstance(value, ContainsMetadata) and isinstance(value, RepresentsSingleObject):
                                        # i.e. isinstance(value, KGObject) - already resolved
                                        resolved_values.append(value)
                                    else:
                                        try:
                                            resolved_value = value.resolve(
                                                client,
                                                scope=use_scope,
                                                use_cache=use_cache,
                                                follow_links=follow_links[follow_name],
                                            )
                                        except ResolutionFailure as err:
                                            warn(str(err))
                                            resolved_values.append(value)
                                        else:
                                            resolved_values.append(resolved_value)
                            if isinstance(values, RepresentsSingleObject):
                                assert len(resolved_values) == 1
                                setattr(self, prop.name, resolved_values[0])
                            elif values is None:
                                assert len(resolved_values) == 0
                                setattr(self, prop.name, None)
                            else:
                                setattr(self, prop.name, resolved_values)
        return self

    def _build_existence_query(self) -> Union[None, Dict[str, Any]]:
        """
        Generate a KG query definition (as a JSON-LD document) that can be used to
        check whether a locally-defined object (with no ID) already exists in the KG.
        """
        if self.existence_query_properties is None:
            return None

        query_properties = []
        for property_name in self.existence_query_properties:
            for property in self.__class__.all_properties:
                if property.name == property_name:
                    query_properties.append(property)
                    break
        if len(query_properties) < 1:
            raise CannotBuildExistenceQuery("Empty existence query for class {}".format(self.__class__.__name__))
        query = {}
        for property in query_properties:
            query_property_name = property.name
            value = getattr(self, property.name)
            if isinstance(value, ContainsMetadata):
                if hasattr(value, "id") and value.id:
                    query[query_property_name] = value.id
                else:
                    sub_query = value._build_existence_query()
                    query.update({f"{query_property_name}__{key}": val for key, val in sub_query.items()})
            elif isinstance(value, (list, tuple)):
                raise CannotBuildExistenceQuery("not implemented yet")
            elif value is None:
                raise CannotBuildExistenceQuery(f"Required value for '{query_property_name}' is missing")
            else:
                query_val = value_to_jsonld(value, include_empty_properties=False, embed_linked_nodes=False)
                if query_val is None:
                    raise CannotBuildExistenceQuery(f"Required value for '{query_property_name}' is missing")
                query[query_property_name] = query_val
        return query
