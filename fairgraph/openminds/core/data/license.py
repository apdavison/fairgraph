"""
Structured information on a used license.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class License(KGObject):
    """
    Structured information on a used license.
    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/core/License"]
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
            "vocab:fullName",
            multiple=False,
            required=True,
            doc="Whole, non-abbreviated name of the license.",
        ),
        Field(
            "alias",
            str,
            "vocab:shortName",
            multiple=False,
            required=True,
            doc="Shortened or fully abbreviated name of the license.",
        ),
        Field(
            "legal_code",
            IRI,
            "vocab:legalCode",
            multiple=False,
            required=True,
            doc="Type of legislation that claims to cover the law system (complete or parts) as it existed at the time the code was enacted.",
        ),
        Field(
            "webpages",
            str,
            "vocab:webpage",
            multiple=True,
            required=False,
            doc="Hypertext document (block of information) found on the World Wide Web.",
        ),
    ]
    existence_query_fields = ("alias",)

    def __init__(
        self,
        name=None,
        alias=None,
        legal_code=None,
        webpages=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            alias=alias,
            legal_code=legal_code,
            webpages=webpages,
        )
