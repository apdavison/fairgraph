"""
Structured information about a user account for a web service.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import AccountInformation as OMAccountInformation
from fairgraph import KGObject


class AccountInformation(KGObject, OMAccountInformation):
    """
    Structured information about a user account for a web service.
    """

    type_ = "https://openminds.om-i.org/types/AccountInformation"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "belongs_to",
            "openminds.latest.core.Person",
            "associatedAccount",
            reverse="associated_accounts",
            multiple=True,
            description="reverse of 'associated_accounts'",
        ),
    ]
    existence_query_properties = ("service", "user_name")

    def __init__(self, belongs_to=None, service=None, user_name=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            belongs_to=belongs_to,
            service=service,
            user_name=user_name,
        )


# cast openMINDS instances to their fairgraph subclass
AccountInformation.set_error_handling(None)
for key, value in OMAccountInformation.__dict__.items():
    if isinstance(value, OMAccountInformation):
        fg_instance = AccountInformation.from_jsonld(value.to_jsonld())
        fg_instance._space = AccountInformation.default_space
        setattr(AccountInformation, key, fg_instance)
AccountInformation.set_error_handling("log")
