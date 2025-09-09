"""
Structured information about how to contact a given person or consortium.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ContactInformation as OMContactInformation
from fairgraph import KGObject


class ContactInformation(KGObject, OMContactInformation):
    """
    Structured information about how to contact a given person or consortium.
    """

    type_ = "https://openminds.om-i.org/types/ContactInformation"
    default_space = "restricted"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_contact_information_of",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Person"],
            "contactInformation",
            reverse="contact_information",
            multiple=True,
            description="reverse of 'contact_information'",
        ),
    ]
    existence_query_properties = ("email",)

    def __init__(self, email=None, is_contact_information_of=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            email=email,
            is_contact_information_of=is_contact_information_of,
        )


# cast openMINDS instances to their fairgraph subclass
ContactInformation.set_error_handling(None)
for key, value in OMContactInformation.__dict__.items():
    if isinstance(value, OMContactInformation):
        fg_instance = ContactInformation.from_jsonld(value.to_jsonld())
        fg_instance._space = ContactInformation.default_space
        setattr(ContactInformation, key, fg_instance)
ContactInformation.set_error_handling("log")
