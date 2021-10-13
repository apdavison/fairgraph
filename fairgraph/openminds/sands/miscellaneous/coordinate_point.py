"""
Structured information on a coordinate point.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class CoordinatePoint(EmbeddedMetadata):
    """
    Structured information on a coordinate point.
    """
    type = ["https://openminds.ebrains.eu/sands/CoordinatePoint"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("coordinates", "openminds.core.QuantitativeValue", "vocab:coordinates", multiple=True, required=True,
              doc="Pair or triplet of numbers defining a location in a given coordinate space."),
        Field("coordinate_space", ["openminds.sands.CommonCoordinateSpace", "openminds.sands.CustomCoordinateSpace"], "vocab:coordinateSpace", multiple=False, required=True,
              doc="Two or three dimensional geometric setting."),
        
    ]

