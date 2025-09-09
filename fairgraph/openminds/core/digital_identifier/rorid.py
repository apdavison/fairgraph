"""
A persistent identifier for a research organization, provided by the Research Organization Registry.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import RORID as OMRORID
from fairgraph import KGObject


class RORID(KGObject, OMRORID):
    """
    A persistent identifier for a research organization, provided by the Research Organization Registry.
    """

    type_ = "https://openminds.om-i.org/types/RORID"
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


# cast openMINDS instances to their fairgraph subclass
RORID.set_error_handling(None)
for key, value in OMRORID.__dict__.items():
    if isinstance(value, OMRORID):
        fg_instance = RORID.from_jsonld(value.to_jsonld())
        fg_instance._space = RORID.default_space
        setattr(RORID, key, fg_instance)
RORID.set_error_handling("log")
