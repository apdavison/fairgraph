"""
A representation of a range of quantitative values.
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


from numbers import Real


class QuantitativeValueRange(EmbeddedMetadata):
    """
    A representation of a range of quantitative values.
    """

    type_ = "https://openminds.ebrains.eu/core/QuantitativeValueRange"
    properties = [
        Property("max_value", Real, "vocab:maxValue", required=True, doc="Greatest quantity attained or allowed."),
        Property(
            "max_value_unit",
            "openminds.controlled_terms.UnitOfMeasurement",
            "vocab:maxValueUnit",
            doc="no description available",
        ),
        Property("min_value", Real, "vocab:minValue", required=True, doc="Smallest quantity attained or allowed."),
        Property(
            "min_value_unit",
            "openminds.controlled_terms.UnitOfMeasurement",
            "vocab:minValueUnit",
            doc="no description available",
        ),
    ]
    reverse_properties = []

    def __init__(
        self,
        max_value=None,
        max_value_unit=None,
        min_value=None,
        min_value_unit=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            data=data,
            max_value=max_value,
            max_value_unit=max_value_unit,
            min_value=min_value,
            min_value_unit=min_value_unit,
        )
