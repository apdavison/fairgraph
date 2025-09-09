"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import StockNumber as OMStockNumber
from fairgraph import EmbeddedMetadata


class StockNumber(EmbeddedMetadata, OMStockNumber):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/StockNumber"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, identifier=None, vendor=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, identifier=identifier, vendor=vendor)


# cast openMINDS instances to their fairgraph subclass
StockNumber.set_error_handling(None)
for key, value in OMStockNumber.__dict__.items():
    if isinstance(value, OMStockNumber):
        fg_instance = StockNumber.from_jsonld(value.to_jsonld())
        fg_instance._space = StockNumber.default_space
        setattr(StockNumber, key, fg_instance)
StockNumber.set_error_handling("log")
