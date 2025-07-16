"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class CoordinatePoint(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CoordinatePoint"
    properties = [
        Property(
            "coordinate_space",
            ["openminds.sands.CommonCoordinateSpaceVersion", "openminds.sands.CustomCoordinateSpace"],
            "vocab:coordinateSpace",
            required=True,
            doc="Two or three dimensional geometric setting.",
        ),
        Property(
            "coordinates",
            "openminds.core.QuantitativeValue",
            "vocab:coordinates",
            multiple=True,
            required=True,
            doc="Pair or triplet of numbers defining a location in a given coordinate space.",
        ),
    ]
    reverse_properties = []

    def __init__(self, coordinate_space=None, coordinates=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, coordinate_space=coordinate_space, coordinates=coordinates)
