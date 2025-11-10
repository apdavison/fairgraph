"""
Structured information on a quantitative value.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.v4.core import QuantitativeValue as OMQuantitativeValue
from fairgraph import EmbeddedMetadata


from numbers import Real


class QuantitativeValue(EmbeddedMetadata, OMQuantitativeValue):
    """
    Structured information on a quantitative value.
    """

    type_ = "https://openminds.om-i.org/types/QuantitativeValue"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("value", "unit", "uncertainties")

    def __init__(
        self,
        type_of_uncertainty=None,
        uncertainties=None,
        unit=None,
        value=None,
        id=None,
        data=None,
        space=None,
        release_status=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            type_of_uncertainty=type_of_uncertainty,
            uncertainties=uncertainties,
            unit=unit,
            value=value,
        )
