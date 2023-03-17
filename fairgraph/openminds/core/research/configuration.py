"""
Structured information about the properties or parameters of an entity or process.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class Configuration(KGObject):
    """
    Structured information about the properties or parameters of an entity or process.
    """
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Configuration"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("configuration", str, "vocab:configuration", multiple=False, required=True,
              doc="no description available"),
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=True,
              doc="Method of digitally organizing and structuring data or information."),

    ]
    existence_query_fields = ('configuration',)

    def __init__(self, lookup_label=None, configuration=None, format=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, lookup_label=lookup_label, configuration=configuration, format=format)