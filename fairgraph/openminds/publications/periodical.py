"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Periodical(KGObject):
    """

    """
    default_space = "livepapers"
    type = ["https://openminds.ebrains.eu/publications/Periodical"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=False,
              doc="Whole, non-abbreviated name of the periodical."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the periodical."),
        Field("digital_identifier", "openminds.core.ISSN", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),

    ]
    existence_query_fields = ('alias',)
