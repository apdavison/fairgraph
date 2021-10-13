"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class Environment(KGObjectV3):
    """
    
    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/Environment"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the environment."),
        Field("hardware", "openminds.computation.HardwareSystem", "vocab:hardware", multiple=False, required=True,
              doc="no description available"),
        Field("configuration", "openminds.core.ParameterSet", "vocab:configuration", multiple=True, required=False,
              doc="no description available"),
        Field("software", "openminds.core.SoftwareVersion", "vocab:software", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the environment."),
        
    ]
    existence_query_fields = ('name', 'hardware')

