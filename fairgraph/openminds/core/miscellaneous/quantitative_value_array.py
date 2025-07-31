"""
A representation of an array of quantitative values, optionally with uncertainties.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import QuantitativeValueArray
from fairgraph import KGObject


from numbers import Real


class QuantitativeValueArray(KGObject, QuantitativeValueArray):
    """
    A representation of an array of quantitative values, optionally with uncertainties.
    """

    type_ = "https://openminds.om-i.org/types/QuantitativeValueArray"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("values",)

    def __init__(
        self,
        negative_uncertainties=None,
        positive_uncertainties=None,
        type_of_uncertainty=None,
        unit=None,
        values=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            negative_uncertainties=negative_uncertainties,
            positive_uncertainties=positive_uncertainties,
            type_of_uncertainty=type_of_uncertainty,
            unit=unit,
            values=values,
        )
