"""
Structured information on a quantitative value.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import QuantitativeValue as OMQuantitativeValue
from fairgraph import EmbeddedMetadata


from numbers import Real


class QuantitativeValue(EmbeddedMetadata, OMQuantitativeValue):
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


# cast openMINDS instances to their fairgraph subclass
QuantitativeValue.set_error_handling(None)
for key, value in OMQuantitativeValue.__dict__.items():
    if isinstance(value, OMQuantitativeValue):
        fg_instance = QuantitativeValue.from_jsonld(value.to_jsonld())
        fg_instance._space = QuantitativeValue.default_space
        setattr(QuantitativeValue, key, fg_instance)
QuantitativeValue.set_error_handling("log")
