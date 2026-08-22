import sys

from . import v4, v5

# Backwards compatibility: expose v4 modules at top level so that
# `import fairgraph.openminds.core` continues to work
from .v4 import chemicals, computation, controlled_terms, core, ephys, publications, sands, specimen_prep, stimulation


def set_error_handling(value):
    """Set error handling for all openMINDS classes, in both v4 and v5."""
    for version_module in (v4, v5):
        version_module.set_error_handling(value)


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
        "chemicals",
        "computation",
        "controlled_terms",
        "core",
        "ephys",
        "publications",
        "sands",
        "specimen_prep",
        "stimulation",
    ]
    for top_name in top_modules:
        top_mod = getattr(v4, top_name)
        sys.modules[f"{__name__}.{top_name}"] = top_mod
        v4_prefix = top_mod.__name__
        legacy_prefix = f"{__name__}.{top_name}"
        for info in pkgutil.walk_packages(top_mod.__path__, prefix=v4_prefix + "."):
            submod = importlib.import_module(info.name)
            legacy_name = legacy_prefix + submod.__name__[len(v4_prefix) :]
            sys.modules[legacy_name] = submod


_install_v4_compat_aliases()
del _install_v4_compat_aliases
