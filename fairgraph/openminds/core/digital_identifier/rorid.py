"""
A persistent identifier for a research organization, provided by the Research Organization Registry.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class RORID(KGObject):
    """
    A persistent identifier for a research organization, provided by the Research Organization Registry.
    """

    default_space = "common"
    type_ = "https://openminds.ebrains.eu/core/RORID"
    properties = [
        Property("identifier", str, "vocab:identifier", required=True, doc="Term or code used to identify the RORID."),
    ]
    reverse_properties = [
        Property(
            "identifies",
            "openminds.core.Organization",
            "^vocab:digitalIdentifier",
            reverse="digital_identifiers",
            multiple=True,
            doc="reverse of 'digital_identifiers'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(self, identifier=None, identifies=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id, space=space, scope=scope, data=data, identifier=identifier, identifies=identifies
        )
