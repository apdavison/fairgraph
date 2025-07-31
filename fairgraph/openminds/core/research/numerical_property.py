"""
Structured information about a property of some entity or process whose value is a number.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import NumericalProperty
from fairgraph import EmbeddedMetadata


class NumericalProperty(EmbeddedMetadata, NumericalProperty):
    """
    Structured information about a property of some entity or process whose value is a number.
    """

    type_ = "https://openminds.om-i.org/types/NumericalProperty"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, name=None, values=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, name=name, values=values)
