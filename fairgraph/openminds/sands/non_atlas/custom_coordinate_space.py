"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class CustomCoordinateSpace(KGObject):
    """

    """
    default_space = "spatial"
    type = ["https://openminds.ebrains.eu/sands/CustomCoordinateSpace"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the custom coordinate space."),
        Field("anatomical_axes_orientation", "openminds.controlledterms.AnatomicalAxesOrientation", "vocab:anatomicalAxesOrientation", multiple=False, required=True,
              doc="Relation between reference planes used in anatomy and mathematics."),
        Field("axes_origins", "openminds.core.QuantitativeValue", "vocab:axesOrigin", multiple=True, required=True,
              doc="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space."),
        Field("default_images", "openminds.core.File", "vocab:defaultImage", multiple=True, required=False,
              doc="Two or three dimensional image that particluarly represents a specific coordinate space."),
        Field("native_unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:nativeUnit", multiple=False, required=True,
              doc="Determinate quantity used in the original measurement."),

    ]
    existence_query_fields = ('name',)
