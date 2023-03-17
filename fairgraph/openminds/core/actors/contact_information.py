"""
Structured information about how to contact a given person or consortium.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class ContactInformation(KGObject):
    """
    Structured information about how to contact a given person or consortium.
    """
    default_space = "restricted"
    type_ = ["https://openminds.ebrains.eu/core/ContactInformation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("email", str, "vocab:email", multiple=False, required=True,
              doc="Address to which or from which an electronic mail can be sent."),

    ]
    existence_query_fields = ('email',)

    def __init__(self, email=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, email=email)