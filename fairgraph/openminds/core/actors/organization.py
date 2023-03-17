"""
Structured information on an organization.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class Organization(KGObject):
    """
    Structured information on an organization.
    """
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Organization"]
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
        Field("affiliations", "openminds.core.Affiliation", "vocab:affiliation", multiple=True, required=False,
              doc="Declaration of a person being closely associated to an organization."),
        Field("digital_identifiers", ["openminds.core.GRIDID", "openminds.core.RORID", "openminds.core.RRID"], "vocab:digitalIdentifier", multiple=True, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("has_parents", "openminds.core.Organization", "vocab:hasParent", multiple=True, required=False,
              doc="Reference to a parent object or legal person."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the organization."),

    ]
    existence_query_fields = ('name',)

    def __init__(self, name=None, alias=None, affiliations=None, digital_identifiers=None, has_parents=None, homepage=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, alias=alias, affiliations=affiliations, digital_identifiers=digital_identifiers, has_parents=has_parents, homepage=homepage)