"""
Structured information on a person.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class Person(KGObject):
    """
    Structured information on a person.
    """
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Person"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("affiliations", "openminds.core.Affiliation", "vocab:affiliation", multiple=True, required=False,
              doc="Declaration of a person being closely associated to an organization."),
        Field("alternate_names", str, "vocab:alternateName", multiple=True, required=False,
              doc="no description available"),
        Field("associated_accounts", "openminds.core.AccountInformation", "vocab:associatedAccount", multiple=True, required=False,
              doc="no description available"),
        Field("contact_information", "openminds.core.ContactInformation", "vocab:contactInformation", multiple=False, required=False,
              doc="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.)."),
        Field("digital_identifiers", "openminds.core.ORCID", "vocab:digitalIdentifier", multiple=True, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("family_name", str, "vocab:familyName", multiple=False, required=False,
              doc="Name borne in common by members of a family."),
        Field("given_name", str, "vocab:givenName", multiple=False, required=True,
              doc="Name given to a person, including all potential middle names, but excluding the family name."),

    ]
    existence_query_fields = ('given_name', 'family_name')

    def __init__(self, affiliations=None, alternate_names=None, associated_accounts=None, contact_information=None, digital_identifiers=None, family_name=None, given_name=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, affiliations=affiliations, alternate_names=alternate_names, associated_accounts=associated_accounts, contact_information=contact_information, digital_identifiers=digital_identifiers, family_name=family_name, given_name=given_name)

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def me(cls, client, allow_multiple=False, follow_links=0):
        user_info = client.user_info()
        possible_matches = cls.list(
            client, scope="in progress", space="common",
            follow_links=follow_links,
            family_name=user_info.family_name,
            given_name=user_info.given_name
        )
        if len(possible_matches) == 0:
            person = Person(family_name=user_info.family_name,
                            given_name=user_info.given_name)
        elif len(possible_matches) == 1:
            person = possible_matches[0]
        elif allow_multiple:
            person = possible_matches
        else:
            raise Exception("Found multiple matches")
        return person
