"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class SoftwareAgent(KGObject):
    """

    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/SoftwareAgent"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the software agent."),
        Field("environment", "openminds.computation.Environment", "vocab:environment", multiple=False, required=False,
              doc="no description available"),
        Field("software", "openminds.core.SoftwareVersion", "vocab:software", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'software')
