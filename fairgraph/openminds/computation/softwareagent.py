"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class SoftwareAgent(KGObjectV3):
    """

    """
    default_space = "model"
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
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("software", "openminds.core.SoftwareVersion", "vocab:software", multiple=False, required=True,
              doc="no description available"),
        Field("environment", "openminds.computation.Environment", "vocab:environment", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = None