"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ContactInformation(KGObject):
    """

    """
    default_space = "restricted"
    type = ["https://openminds.ebrains.eu/core/ContactInformation"]
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
