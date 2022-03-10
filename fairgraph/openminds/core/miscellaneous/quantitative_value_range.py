"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class QuantitativeValueRange(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/core/QuantitativeValueRange"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("max_value", float, "vocab:maxValue", multiple=False, required=True,
              doc="Greatest quantity attained or allowed."),
        Field("max_value_unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:maxValueUnit", multiple=False, required=False,
              doc="no description available"),
        Field("min_value", float, "vocab:minValue", multiple=False, required=True,
              doc="Smallest quantity attained or allowed."),
        Field("min_value_unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:minValueUnit", multiple=False, required=False,
              doc="no description available"),

    ]
