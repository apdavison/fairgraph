"""
Structured information on the computer system or set of systems in which a computation is deployed and executed.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Environment(KGObject):
    """
    Structured information on the computer system or set of systems in which a computation is deployed and executed.
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
        Field("configuration", "openminds.core.Configuration", "vocab:configuration", multiple=False, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the environment."),
        Field("hardware", "openminds.computation.HardwareSystem", "vocab:hardware", multiple=False, required=True,
              doc="no description available"),
        Field("software", "openminds.core.SoftwareVersion", "vocab:software", multiple=True, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'hardware')
