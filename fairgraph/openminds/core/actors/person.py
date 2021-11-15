"""
Structured information on a person.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class Person(KGObjectV3):
    """
    Structured information on a person.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Person"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("digital_identifiers", "openminds.core.ORCID", "vocab:digitalIdentifier", multiple=True, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("contact_information", "openminds.core.ContactInformation", "vocab:contactInformation", multiple=False, required=False,
              doc="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.)."),
        Field("family_name", str, "vocab:familyName", multiple=False, required=False,
              doc="Name borne in common by members of a family."),
        Field("given_name", str, "vocab:givenName", multiple=False, required=True,
              doc="Name given to a person, including all potential middle names, but excluding the family name."),
        Field("affiliations", "openminds.core.Affiliation", "vocab:affiliation", multiple=True, required=False,
              doc="Declaration of a person being closely associated to an organization."),

    ]
    existence_query_fields = ('given_name', 'family_name')


    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def me(cls, client, allow_multiple=False, resolved=False):
        user_info = client.user_info()
        if user_info is None:
            raise Exception("User information could not be retrieved. You may need to refresh your token.")
        family_name = user_info["http://schema.org/familyName"]
        given_name = user_info["http://schema.org/givenName"]
        possible_matches = cls.list(
            client, scope="in progress", space="common",
            resolved=resolved,
            family_name=family_name,
            given_name=given_name
        )
        if len(possible_matches) == 0:
            person = Person(family_name=family_name, given_name=given_name)
        elif len(possible_matches) == 1:
            person = possible_matches[0]
        elif allow_multiple:
            person = possible_matches
        else:
            raise Exception("Found multiple matches")
        return person
