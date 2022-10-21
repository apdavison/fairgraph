"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Channel(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/ephys/Channel"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the channel within a particular product."),
        Field("unit_of_measurement", "openminds.controlledterms.UnitOfMeasurement", "vocab:unitOfMeasurement", multiple=False, required=True,
              doc="no description available"),

    ]
