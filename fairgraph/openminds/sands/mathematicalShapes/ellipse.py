"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Ellipse(KGObject):
    """

    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/Ellipse"]
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
    existence_query_fields = ('semi_major_axis', 'semi_minor_axis')
