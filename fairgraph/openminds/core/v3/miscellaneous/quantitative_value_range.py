"""

"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class QuantitativeValueRange(KGObject):
    """
    
    """
    space = "model"
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
        Field("min_value", float, "vocab:minValue", multiple=False, required=True,
              doc="Smallest quantity attained or allowed."),
        Field("unit", "openminds.controlledTerms.UnitOfMeasurement", "vocab:unit", multiple=False, required=False,
              doc="Determinate quantity adopted as a standard of measurement."),
        
    ]
    existence_query_fields = ('name',)