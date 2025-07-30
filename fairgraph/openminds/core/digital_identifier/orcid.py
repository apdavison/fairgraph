"""
A persistent identifier for a researcher provided by Open Researcher and Contributor ID, Inc.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ORCID
from fairgraph import KGObject


class ORCID(KGObject, ORCID):
    """
    A persistent identifier for a researcher provided by Open Researcher and Contributor ID, Inc.
    """

    type_ = "https://openminds.ebrains.eu/core/ORCID"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            "openminds.latest.core.Person",
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
