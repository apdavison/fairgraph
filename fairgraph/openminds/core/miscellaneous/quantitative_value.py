"""
Structured information on a quantitative value.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import QuantitativeValue
from fairgraph import EmbeddedMetadata


from numbers import Real


class QuantitativeValue(EmbeddedMetadata, QuantitativeValue):
    """
    Structured information on a quantitative value.
    """

    type_ = "https://openminds.om-i.org/types/QuantitativeValue"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        type_of_uncertainty=None,
        uncertainties=None,
        unit=None,
        value=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            type_of_uncertainty=type_of_uncertainty,
            uncertainties=uncertainties,
            unit=unit,
            value=value,
        )
