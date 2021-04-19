"""
Structured information on an image.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class Image(KGObject):
    """
    Structured information on an image.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/Image"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("coordinate_space", "openminds.sands.CoordinateSpace", "vocab:coordinateSpace", multiple=False, required=True,
              doc="Two or three dimensional geometric setting."),
        Field("defined_in", "openminds.core.File", "vocab:definedIn", multiple=False, required=True,
              doc="Reference to a file instance in which something is stored."),
        Field("voxel_sizes", "openminds.core.QuantitativeValue", "vocab:voxelSize", multiple=True, required=True,
              doc="Extent of the discrete elements comprising a three-dimensional entity."),
        
    ]
    existence_query_fields = ('name',)