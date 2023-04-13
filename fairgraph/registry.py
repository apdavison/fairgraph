"""
Classes and functions for looking up schema classes
based on names, types, IRIs

"""

from __future__ import annotations
from typing import TYPE_CHECKING, Union, List, Optional

if TYPE_CHECKING:
    from .base import ContainsMetadata

registry: dict = {"names": {}, "types": {}}


def register_class(target_class: ContainsMetadata):
    if "openminds" in target_class.__module__:
        parts = target_class.__module__.split(".")
        name = ".".join(parts[1:3] + [target_class.__name__])  # e.g. openminds.core.Dataset
    else:
        name = target_class.__module__.split(".")[-1] + "." + target_class.__name__

    registry["names"][name] = target_class
    if hasattr(target_class, "type_"):
        if isinstance(target_class.type_, str):
            type_ = target_class.type_
        else:
            type_ = tuple(sorted(target_class.type_))
        if type_ in registry["types"]:
            if isinstance(registry["types"][type_], list):
                registry["types"][type_].append(target_class)
            else:
                registry["types"][type_] = [registry["types"][type_], target_class]
        else:
            registry["types"][type_] = target_class


def lookup(class_name: str) -> ContainsMetadata:
    return registry["names"][class_name]


def lookup_type(class_type: Union[str, List[str]]) -> ContainsMetadata:
    if isinstance(class_type, str):
        if class_type in registry["types"]:
            return registry["types"][class_type]
        else:
            return registry["types"][(class_type,)]
    else:
        return registry["types"][tuple(sorted(class_type))]


docstring_template = """
{base}

Args
----
{args}

"""


class Registry(type):
    """Metaclass for registering Knowledge Graph classes"""

    fields = []

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        cls._base_docstring = class_dict.get("__doc__", "").strip()
        register_class(cls)
        return cls

    def _get_doc(self) -> str:
        """Dynamically generate docstrings"""
        field_docs = []
        if hasattr(self, "fields"):

            def gen_path(type_):
                if type_.__module__ == "builtins":
                    return type_.__name__
                else:
                    return "~{}.{}".format(type_.__module__, type_.__name__)

            for field in self.fields:
                doc = "{} : {}\n    {}".format(field.name, ", ".join(gen_path(t) for t in field.types), field.doc)
                field_docs.append(doc)
        return docstring_template.format(base=self._base_docstring, args="\n".join(field_docs))

    __doc__ = property(_get_doc)

    @property
    def field_names(cls) -> List[str]:
        return [f.name for f in cls.fields]

    @property
    def required_field_names(cls) -> List[str]:
        return [f.name for f in cls.fields if f.required]
