"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class ServiceLink(KGObjectV3):
    """
    
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/ServiceLink"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("data_location", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:dataLocation", multiple=False, required=True,
              doc="no description available"),
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the service link."),
        Field("open_data_in", "openminds.core.URL", "vocab:openDataIn", multiple=False, required=True,
              doc="no description available"),
        Field("service", "openminds.controlledterms.Service", "vocab:service", multiple=False, required=True,
              doc="no description available"),
        
    ]
    existence_query_fields = ('data_location', 'open_data_in', 'service')

