"""
Structured information on an organization.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Organization(KGObject):
    """
    Structured information on an organization.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Organization"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the organization."),
        Field("alias", str, "vocab:shortName", multiple=False, required=False,
              doc="Shortened or fully abbreviated name of the organization."),
        Field("digital_identifiers", ["openminds.core.GRIDID", "openminds.core.RORID", "openminds.core.RRID"], "vocab:digitalIdentifier", multiple=True, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("has_parent", "openminds.core.Organization", "vocab:hasParent", multiple=False, required=False,
              doc="Reference to a parent object or legal person."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the organization."),

    ]
    existence_query_fields = ('name',)
