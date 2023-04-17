"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class WebResource(KGObject):
    """ """

    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/WebResource"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "iri",
            IRI,
            "vocab:IRI",
            required=True,
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
        Field("content_description", str, "vocab:contentDescription", doc="no description available"),
        Field(
            "format",
            "openminds.core.ContentType",
            "vocab:format",
            doc="Method of digitally organizing and structuring data or information.",
        ),
    ]
    existence_query_fields = ("iri",)

    def __init__(self, iri=None, content_description=None, format=None, id=None, data=None, space=None, scope=None):
        return super().__init__(
            id=id, space=space, scope=scope, data=data, iri=iri, content_description=content_description, format=format
        )
