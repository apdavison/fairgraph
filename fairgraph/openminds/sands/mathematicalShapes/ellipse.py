"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Ellipse(EmbeddedMetadata):
    """

    """
    type_ = ["https://openminds.ebrains.eu/sands/Ellipse"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("semi_major_axis", "openminds.core.QuantitativeValue", "vocab:semiMajorAxis", multiple=False, required=True,
              doc="no description available"),
        Field("semi_minor_axis", "openminds.core.QuantitativeValue", "vocab:semiMinorAxis", multiple=False, required=True,
              doc="no description available"),

    ]
