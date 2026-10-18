from warnings import warn
from .specimen_prep import *

warn(
    "The `specimenprep` module has been renamed to `specimen_prep`, this alias will be removed in version 1.0",
    DeprecationWarning,
)
