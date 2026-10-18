from warnings import warn
from .controlled_terms import *

warn(
    "The `controlledterms` module has been renamed to `controlled_terms`, this alias will be removed in version 1.0",
    DeprecationWarning,
)
