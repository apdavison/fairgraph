"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import EmbeddedMetadata, IRI
from fairgraph.fields import Field


class StringProperty(EmbeddedMetadata):
    """ """

    type_ = ["https://openminds.ebrains.eu/core/StringProperty"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the string property.",
        ),
        Field("value", str, "vocab:value", required=True, doc="Entry for a property."),
    ]

    def __init__(self, name=None, value=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, name=name, value=value)
