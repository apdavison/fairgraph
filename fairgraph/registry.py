"""
Classes and functions for looking up schema classes
based on names and type identifiers.

"""

from __future__ import annotations
from itertools import chain
from typing import TYPE_CHECKING, Union, List, Dict
from warnings import warn

from openminds.properties import Property
from openminds.registry import Registry

from .base import OPENMINDS_VERSION

if TYPE_CHECKING:
    from .node import ContainsMetadata


docstring_template = """
{base}

Args
----
{args}

"""


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
        #   -->  'openminds.v4.sands.AnatomicalTargetPosition'
        class_dict["class_name"] = ".".join(
            class_dict["__module__"].replace("fairgraph.openminds", f"openminds.{OPENMINDS_VERSION}").split(".")[:3]
            + [name]
        )
        class_dict["preferred_import_path"] = class_dict["class_name"]
        cls = Registry.__new__(meta, name, bases, class_dict)
        cls._property_lookup = {prop.name: prop for prop in (cls.properties + cls.reverse_properties)}
        return cls

    def _get_doc(cls) -> str:
        """Dynamically generate docstrings"""
        # todo: consider generating the docstring in the build pipeline,
        #       avoiding all this run-time messing about
        field_docs = []
        if hasattr(cls, "properties"):

            def gen_path(type_):
                if type_.__module__ == "builtins":
                    return type_.__name__
                else:
                    return "~{}.{}".format(type_.__module__, type_.__name__)

            for property in cls.all_properties:
                doc = "{} : {}\n    {}".format(
                    property.name, ", ".join(gen_path(t) for t in property.types), property.description
                )
                # todo: add property.instructions if present
                field_docs.append(doc)
        # todo: also document id, data, space, release_status
        return docstring_template.format(base=cls._base_docstring, args="\n".join(field_docs))

    __doc__ = property(_get_doc)  # type: ignore[assignment]

    @property
    def all_properties(cls):
        return chain(cls.properties, cls.reverse_properties)

    @property
    def all_property_names(cls):
        return [p.name for p in cls.all_properties]

    @property
    def reverse_property_names(cls):
        return [p.name for p in cls.reverse_properties]

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
