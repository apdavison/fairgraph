"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import IdentifiersDotOrgID
from fairgraph import KGObject


class IdentifiersDotOrgID(KGObject, IdentifiersDotOrgID):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/IdentifiersDotOrgID"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            ["openminds.latest.core.Dataset", "openminds.latest.core.DatasetVersion"],
            "digitalIdentifier",
            reverse="digital_identifier",
            multiple=True,
            description="reverse of 'digital_identifier'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(self, identifier=None, identifies=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self, id=id, space=space, scope=scope, data=data, identifier=identifier, identifies=identifies
        )
