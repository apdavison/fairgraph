"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class Affiliation(KGObject):
    """
    
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/Affiliation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("start_date", str, "vocab:startDate", multiple=False, required=False,
              doc="Date in the Gregorian calendar at which something begins in time"),
        Field("end_date", str, "vocab:endDate", multiple=False, required=False,
              doc="Date in the Gregorian calendar at which something terminates in time."),
        Field("organization", "openminds.core.Organization", "vocab:organization", multiple=False, required=True,
              doc="Legally accountable, administrative and functional structure."),
        
    ]
    existence_query_fields = ('name',)