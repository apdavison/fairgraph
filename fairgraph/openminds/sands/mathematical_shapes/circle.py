"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class Circle(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Circle"
    properties = [
        Property(
            "radius", "openminds.core.QuantitativeValue", "vocab:radius", required=True, doc="no description available"
        ),
    ]
    reverse_properties = []

    def __init__(self, radius=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, radius=radius)
