"""
A GRID (Global Research Identifier Database) identifier.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class GRIDID(KGObject):
    """
    A GRID (Global Research Identifier Database) identifier.
    """
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/GRIDID"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("identifier", str, "vocab:identifier", multiple=False, required=True,
              doc="Term or code used to identify the GRIDID."),

    ]
    existence_query_fields = ('identifier',)

    def __init__(self, identifier=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, identifier=identifier)