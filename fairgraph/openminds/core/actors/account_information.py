"""
Structured information about a user account for a web service.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class AccountInformation(KGObject):
    """
    Structured information about a user account for a web service.
    """

    default_space = "common"
    type_ = "https://openminds.ebrains.eu/core/AccountInformation"
    properties = [
        Property(
            "service", "openminds.core.WebService", "vocab:service", required=True, doc="no description available"
        ),
        Property("user_name", str, "vocab:userName", required=True, doc="no description available"),
    ]
    reverse_properties = [
        Property(
            "belongs_to",
            "openminds.core.Person",
            "^vocab:associatedAccount",
            reverse="associated_accounts",
            multiple=True,
            doc="reverse of 'associated_accounts'",
        ),
    ]
    existence_query_properties = ("service", "user_name")

    def __init__(self, belongs_to=None, service=None, user_name=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id, space=space, scope=scope, data=data, belongs_to=belongs_to, service=service, user_name=user_name
        )
