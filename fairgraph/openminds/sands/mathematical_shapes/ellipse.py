"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class Ellipse(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Ellipse"
    properties = [
        Property(
            "semi_major_axis",
            "openminds.core.QuantitativeValue",
            "vocab:semiMajorAxis",
            required=True,
            doc="no description available",
        ),
        Property(
            "semi_minor_axis",
            "openminds.core.QuantitativeValue",
            "vocab:semiMinorAxis",
            required=True,
            doc="no description available",
        ),
    ]
    reverse_properties = []

    def __init__(self, semi_major_axis=None, semi_minor_axis=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, semi_major_axis=semi_major_axis, semi_minor_axis=semi_minor_axis)
