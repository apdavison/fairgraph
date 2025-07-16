"""
A GRID (Global Research Identifier Database) identifier.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class GRIDID(KGObject):
    """
    A GRID (Global Research Identifier Database) identifier.
    """

    default_space = "common"
    type_ = "https://openminds.ebrains.eu/core/GRIDID"
    properties = [
        Property(
            "identifier", str, "vocab:identifier", required=True, doc="Term or code used to identify the GRIDID."
        ),
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
