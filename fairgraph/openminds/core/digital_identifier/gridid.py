"""
A GRID (Global Research Identifier Database) identifier.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import GRIDID as OMGRIDID
from fairgraph import KGObject


class GRIDID(KGObject, OMGRIDID):
    """
    A GRID (Global Research Identifier Database) identifier.
    """

    type_ = "https://openminds.om-i.org/types/GRIDID"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            "openminds.latest.core.Organization",
            "digitalIdentifier",
            reverse="digital_identifiers",
            multiple=True,
            description="reverse of 'digital_identifiers'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(self, identifier=None, identifies=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self, id=id, space=space, scope=scope, data=data, identifier=identifier, identifies=identifies
        )
