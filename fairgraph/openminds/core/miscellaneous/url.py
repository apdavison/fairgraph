"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class URL(KGObject):
    """
    
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/URL"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("url", str, "vocab:URL", multiple=False, required=False,
              doc="no description available"),
        
    ]
    existence_query_fields = None