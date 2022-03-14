"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ContentTypePattern(KGObject):
    """

    """
    default_space = "files"
    type = ["https://openminds.ebrains.eu/core/ContentTypePattern"]
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
        Field("content_type", "openminds.core.ContentType", "vocab:contentType", multiple=False, required=True,
              doc="no description available"),
        Field("regex", str, "vocab:regex", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
