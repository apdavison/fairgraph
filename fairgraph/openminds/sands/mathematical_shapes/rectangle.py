"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class Rectangle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Rectangle"
    properties = [
        Property(
            "length", "openminds.core.QuantitativeValue", "vocab:length", required=True, doc="no description available"
        ),
        Property(
            "width", "openminds.core.QuantitativeValue", "vocab:width", required=True, doc="no description available"
        ),
    ]
    reverse_properties = []

    def __init__(self, length=None, width=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, length=length, width=width)
