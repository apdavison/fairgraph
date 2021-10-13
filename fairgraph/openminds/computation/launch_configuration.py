"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class LaunchConfiguration(KGObjectV3):
    """
    
    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/LaunchConfiguration"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the launch configuration."),
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the launch configuration."),
        Field("executable", str, "vocab:executable", multiple=False, required=True,
              doc="no description available"),
        Field("arguments", str, "vocab:arguments", multiple=True, required=False,
              doc="no description available"),
        Field("environment_variables", "openminds.core.ParameterSet", "vocab:environmentVariables", multiple=False, required=False,
              doc="no description available"),
        
    ]
    existence_query_fields = ('executable', 'name')

