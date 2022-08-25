"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class NumericalProperty(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/core/NumericalProperty"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the numerical property."),
        Field("values", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:value", multiple=True, required=True,
              doc="Entry for a property."),

    ]
