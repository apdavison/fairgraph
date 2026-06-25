"""
Helpers for introspecting a module to discover and configure its KG classes.

These are used by the per-domain ``fairgraph.openminds`` submodules to expose
module-scoped ``list_kg_classes()``, ``list_embedded_metadata_classes()`` and
``set_error_handling()`` functions.
"""

import inspect

from .kgobject import KGObject
from .embedded import KGEmbedded


def list_kg_classes(module):
    """List all KG classes defined in the given module."""
    return [obj for name, obj in inspect.getmembers(module)
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(module.__name__)]


def list_embedded_metadata_classes(module):
    """List all embedded metadata classes defined in the given module."""
    return [obj for name, obj in inspect.getmembers(module)
            if inspect.isclass(obj) and issubclass(obj, KGEmbedded) and obj.__module__.startswith(module.__name__)]


def set_error_handling(value, module):
    """
    Control validation for all classes in the given module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
        module: the module whose classes should be updated.
    """
    for cls in list_kg_classes(module) + list_embedded_metadata_classes(module):
        cls.set_error_handling(value)
