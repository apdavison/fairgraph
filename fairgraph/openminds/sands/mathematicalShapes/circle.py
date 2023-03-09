"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Circle(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/Circle"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("radius", "openminds.core.QuantitativeValue", "vocab:radius", multiple=False, required=True,
              doc="no description available"),

    ]
