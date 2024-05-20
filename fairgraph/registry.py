"""
Classes and functions for looking up schema classes
based on names and type identifiers.

"""

from __future__ import annotations
from itertools import chain
import logging
from typing import TYPE_CHECKING, Union, List, Dict
from warnings import warn

from openminds.properties import Property
from openminds.registry import Registry

if TYPE_CHECKING:
    from .node import ContainsMetadata


class Node(Registry):
    """Metaclass for registering Knowledge Graph classes."""

    properties: List[Property] = []
    type_: Union[str, List[str]]
    context: Dict[str, str]
    _base_docstring: str

    def __new__(meta, name, bases, class_dict):
        # set class_name so that the fairgraph class replaces the equivalent openminds class
        # in the registry
        # e.g.   'fairgraph.openminds.sands.miscellaneous.anatomical_target_position'
        #   -->  'openminds.latest.sands.AnatomicalTargetPosition'
        class_dict["class_name"] = ".".join(
            class_dict["__module__"].replace("fairgraph.openminds", "openminds.latest").split(".")[:3] + [name]
        )
        cls = Registry.__new__(meta, name, bases, class_dict)
        cls._property_lookup = {prop.name: prop for prop in (cls.properties + cls.reverse_properties)}
        return cls

    @property
    def all_properties(cls):
        return chain(cls.properties, cls.reverse_properties)

    @property
    def fields(cls):
        warn(
            "Use of the 'fields' attribute is deprecated, it will be removed in a future release. "
            "Use 'properties' instead",
            DeprecationWarning,
        )
        return cls.properties + cls.reverse_properties

    @property
    def field_names(cls):
        warn(
            "Use of the 'field_names' attribute is deprecated, it will be removed in a future release. "
            "Use 'property_names' instead",
            DeprecationWarning,
        )
        return cls.property_names

    @property
    def required_field_names(cls):
        warn(
            "Use of the 'required_field_names' attribute is deprecated, it will be removed in a future release. "
            "Use 'required_property_names' instead",
            DeprecationWarning,
        )
        return cls.property_names

    @property
    def existence_query_fields(cls):
        warn(
            "Use of the 'existence_query_fields' attribute is deprecated, it will be removed in a future release. "
            "Use 'existence_query_properties' instead",
            DeprecationWarning,
        )
        return cls.existence_query_properties
