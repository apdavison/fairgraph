"""
An identifiable list of property-value pairs.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class PropertyValueList(KGObject):
    """
    An identifiable list of property-value pairs.
    """

    default_space = "dataset"
    type_ = ["https://openminds.ebrains.eu/core/PropertyValueList"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Field(
            "property_value_pairs",
            ["openminds.core.NumericalProperty", "openminds.core.StringProperty"],
            "vocab:propertyValuePair",
            multiple=True,
            required=True,
            doc="no description available",
        ),
    ]
    existence_query_fields = ("lookup_label",)

    def __init__(self, lookup_label=None, property_value_pairs=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            property_value_pairs=property_value_pairs,
        )
