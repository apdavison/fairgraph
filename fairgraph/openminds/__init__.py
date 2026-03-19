import sys
import inspect
from fairgraph.kgobject import KGObject
from fairgraph.embedded import KGEmbedded


def list_kg_classes(module=None):
    """List all KG classes defined in the given module (defaults to this module)"""
    if module is None:
        module = sys.modules[__name__]
    return [obj for name, obj in inspect.getmembers(module)
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(module.__name__)]


def list_embedded_metadata_classes(module=None):
    """List all embedded metadata classes defined in the given module (defaults to this module)"""
    if module is None:
        module = sys.modules[__name__]
    return [obj for name, obj in inspect.getmembers(module)
            if inspect.isclass(obj) and issubclass(obj, KGEmbedded) and obj.__module__.startswith(module.__name__)]


def set_error_handling(value, module=None):
    """
    Control validation for all classes in the given module (defaults to this module).

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
        module: the module whose classes should be updated. Defaults to this module.
    """
    for cls in list_kg_classes(module) + list_embedded_metadata_classes(module):
        cls.set_error_handling(value)


from . import chemicals, computation, controlled_terms, core, ephys, publications, sands, specimen_prep, stimulation
