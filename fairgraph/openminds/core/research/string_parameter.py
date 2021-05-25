"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class StringParameter(KGObject):
    """
    
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/StringParameter"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("value", str, "vocab:value", multiple=False, required=True,
              doc="Entry for a property."),
        
    ]
    existence_query_fields = ('name',)