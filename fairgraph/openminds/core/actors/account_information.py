"""
Structured information about a user account for a web service.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class AccountInformation(KGObject):
    """
    Structured information about a user account for a web service.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/AccountInformation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("service", "openminds.core.WebService", "vocab:service", multiple=False, required=True,
              doc="no description available"),
        Field("user_name", str, "vocab:userName", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('service', 'user_name')
