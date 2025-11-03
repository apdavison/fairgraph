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

    def __init__(self, identifier=None, vendor=None, id=None, data=None, space=None, release_status=None):
        return EmbeddedMetadata.__init__(self, data=data, identifier=identifier, vendor=vendor)
