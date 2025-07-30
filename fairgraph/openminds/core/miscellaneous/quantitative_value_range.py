"""
A representation of a range of quantitative values.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import QuantitativeValueRange
from fairgraph import EmbeddedMetadata


from numbers import Real


class QuantitativeValueRange(EmbeddedMetadata, QuantitativeValueRange):
    """
    A representation of a range of quantitative values.
    """

    type_ = "https://openminds.ebrains.eu/core/QuantitativeValueRange"
    # forward properties are defined in the parent class (in openMINDS-Python)
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
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            max_value=max_value,
            max_value_unit=max_value_unit,
            min_value=min_value,
            min_value_unit=min_value_unit,
        )
