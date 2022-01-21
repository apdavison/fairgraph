"""
Structured information on used funding.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Funding(KGObject):
    """
    Structured information on used funding.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Funding"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("acknowledgement", str, "vocab:acknowledgement", multiple=False, required=False,
              doc="Offical declaration or avowal of appreciation of an act or achievement."),
        Field("award_number", str, "vocab:awardNumber", multiple=False, required=False,
              doc="Machine-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need."),
        Field("award_title", str, "vocab:awardTitle", multiple=False, required=False,
              doc="Human-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need."),
        Field("funder", ["openminds.core.Organization", "openminds.core.Person"], "vocab:funder", multiple=False, required=True,
              doc="Legal person that provides money for a particular purpose."),

    ]
    existence_query_fields = ('funder',)
