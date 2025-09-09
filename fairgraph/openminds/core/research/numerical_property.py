"""
Structured information about a property of some entity or process whose value is a number.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import NumericalProperty as OMNumericalProperty
from fairgraph import EmbeddedMetadata


class NumericalProperty(EmbeddedMetadata, OMNumericalProperty):
    """
    Structured information about a property of some entity or process whose value is a number.
    """

    type_ = "https://openminds.om-i.org/types/NumericalProperty"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, name=None, values=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, name=name, values=values)


# cast openMINDS instances to their fairgraph subclass
NumericalProperty.set_error_handling(None)
for key, value in OMNumericalProperty.__dict__.items():
    if isinstance(value, OMNumericalProperty):
        fg_instance = NumericalProperty.from_jsonld(value.to_jsonld())
        fg_instance._space = NumericalProperty.default_space
        setattr(NumericalProperty, key, fg_instance)
NumericalProperty.set_error_handling("log")
