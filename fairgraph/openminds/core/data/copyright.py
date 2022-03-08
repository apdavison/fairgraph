"""
Structured information on the copyright.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Copyright(EmbeddedMetadata):
    """
    Structured information on the copyright.
    """
    type = ["https://openminds.ebrains.eu/core/Copyright"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("holders", ["openminds.core.Organization", "openminds.core.Person"], "vocab:holder", multiple=True, required=True,
              doc="Legal person in possession of something."),
        Field("year", str, "vocab:year", multiple=False, required=True,
              doc="Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December."),

    ]
