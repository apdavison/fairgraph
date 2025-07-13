"""
Structured information about how to contact a given person or consortium.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ContactInformation(KGObject):
    """
    Structured information about how to contact a given person or consortium.
    """

    default_space = "restricted"
    type_ = "https://openminds.ebrains.eu/core/ContactInformation"
    properties = [
        Property(
            "email",
            str,
            "vocab:email",
            required=True,
            doc="Address to which or from which an electronic mail can be sent.",
        ),
    ]
    reverse_properties = [
        Property(
            "is_contact_information_of",
            ["openminds.core.Consortium", "openminds.core.Person"],
            "^vocab:contactInformation",
            reverse="contact_information",
            multiple=True,
            doc="reverse of 'contact_information'",
        ),
    ]
    existence_query_properties = ("email",)

    def __init__(self, email=None, is_contact_information_of=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            email=email,
            is_contact_information_of=is_contact_information_of,
        )
