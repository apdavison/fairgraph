"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class SingleColor(KGObject):
    """ """

    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/SingleColor"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("value", str, "vocab:value", required=True, doc="Entry for a property."),
        Field(
            "preferred_by",
            "openminds.sands.ViewerSpecification",
            "^vocab:preferredDisplayColor",
            reverse="preferred_display_colors",
            multiple=True,
            doc="reverse of 'preferredDisplayColor'",
        ),
    ]
    existence_query_fields = ("value",)

    def __init__(self, value=None, preferred_by=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, space=space, scope=scope, data=data, value=value, preferred_by=preferred_by)
