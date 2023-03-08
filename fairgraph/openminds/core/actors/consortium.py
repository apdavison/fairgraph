"""
Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class Consortium(KGObject):
    """
    Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Consortium"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the consortium."),
        Field("alias", str, "vocab:shortName", multiple=False, required=False,
              doc="Shortened or fully abbreviated name of the consortium."),
        Field("contact_information", "openminds.core.ContactInformation", "vocab:contactInformation", multiple=False, required=False,
              doc="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.)."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the consortium."),

    ]
    existence_query_fields = ('name',)
