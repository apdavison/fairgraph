"""
Structured information on a quanitative value.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class QuantitativeValue(KGObject):
    """
    Structured information on a quanitative value.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/QuantitativeValue"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("value", float, "vocab:value", multiple=False, required=True,
              doc="Entry for a property."),
        Field("uncertaintys", float, "vocab:uncertainty", multiple=True, required=False,
              doc="Quanitative value range defining the uncertainty of a measurement."),
        Field("type_of_uncertainty", "openminds.controlledTerms.TypeOfUncertainty", "vocab:typeOfUncertainty", multiple=False, required=False,
              doc="Distinct technique used to quanitify the uncertainty of a measurement."),
        Field("unit", "openminds.controlledTerms.UnitOfMeasurement", "vocab:unit", multiple=False, required=False,
              doc="Determinate quantity adopted as a standard of measurement."),
        
    ]
    existence_query_fields = ('name',)