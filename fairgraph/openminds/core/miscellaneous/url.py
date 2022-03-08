"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class URL(KGObject):
    """

    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/URL"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("url", IRI, "vocab:URL", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('url',)
