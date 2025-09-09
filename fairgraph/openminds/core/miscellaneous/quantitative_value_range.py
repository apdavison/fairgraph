"""
A representation of a range of quantitative values.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import QuantitativeValueRange as OMQuantitativeValueRange
from fairgraph import EmbeddedMetadata


from numbers import Real


class QuantitativeValueRange(EmbeddedMetadata, OMQuantitativeValueRange):
    """
    A representation of a range of quantitative values.
    """

    type_ = "https://openminds.om-i.org/types/QuantitativeValueRange"
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


# cast openMINDS instances to their fairgraph subclass
QuantitativeValueRange.set_error_handling(None)
for key, value in OMQuantitativeValueRange.__dict__.items():
    if isinstance(value, OMQuantitativeValueRange):
        fg_instance = QuantitativeValueRange.from_jsonld(value.to_jsonld())
        fg_instance._space = QuantitativeValueRange.default_space
        setattr(QuantitativeValueRange, key, fg_instance)
QuantitativeValueRange.set_error_handling("log")
