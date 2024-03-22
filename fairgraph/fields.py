from warnings import warn

from .properties import Property as Field

warn(
    "The 'Field' class has been renamed to 'Property' "
    "for consistency with openMINDS. "
    "Use of 'Field' will still work until the next release, "
    "when this alias will be removed.",
    DeprecationWarning,
)
