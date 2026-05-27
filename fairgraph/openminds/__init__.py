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


from . import v4, v5

# Backwards compatibility: expose v4 modules at top level so that
# `import fairgraph.openminds.core` continues to work
from .v4 import chemicals, computation, controlled_terms, core, ephys, publications, sands, specimen_prep, stimulation


def _install_v4_compat_aliases():
    """Alias every v4 module and submodule under the legacy ``fairgraph.openminds.<top>...`` path.

    Without recursive aliasing, walking a dotted path like
    ``fairgraph.openminds.core.products.dataset_version`` would force Python to
    import a *fresh* module object distinct from the v4 module it shadows.
    Anything that resolved a class via the legacy path (e.g. ``mocker.patch``,
    ``isinstance`` checks) would then operate on a duplicate copy and silently
    diverge from code that uses the v4 path.
    """
    import importlib
    import pkgutil

    top_modules = [
        "chemicals", "computation", "controlled_terms", "core",
        "ephys", "publications", "sands", "specimen_prep", "stimulation",
    ]
    for top_name in top_modules:
        top_mod = getattr(v4, top_name)
        sys.modules[f"{__name__}.{top_name}"] = top_mod
        v4_prefix = top_mod.__name__
        legacy_prefix = f"{__name__}.{top_name}"
        for info in pkgutil.walk_packages(top_mod.__path__, prefix=v4_prefix + "."):
            submod = importlib.import_module(info.name)
            legacy_name = legacy_prefix + submod.__name__[len(v4_prefix):]
            sys.modules[legacy_name] = submod


_install_v4_compat_aliases()
del _install_v4_compat_aliases
