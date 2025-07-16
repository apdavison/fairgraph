"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class StockNumber(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/StockNumber"
    properties = [
        Property(
            "identifier", str, "vocab:identifier", required=True, doc="Term or code used to identify the stock number."
        ),
        Property(
            "vendor", "openminds.core.Organization", "vocab:vendor", required=True, doc="no description available"
        ),
    ]
    reverse_properties = []

    def __init__(self, identifier=None, vendor=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, identifier=identifier, vendor=vendor)
