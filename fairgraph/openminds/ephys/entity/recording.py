"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Recording(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Recording"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("channels", "openminds.ephys.Channel", "vocab:channels", multiple=True, required=False,
              doc="no description available"),
        Field("data_locations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:dataLocation", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the recording."),
        Field("devices", ["openminds.ephys.Device", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"], "vocab:devices", multiple=True, required=False,
              doc="no description available"),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the recording within a particular product."),
        Field("orders", int, "vocab:order", multiple=True, required=False,
              doc="no description available"),
        Field("time_step", "openminds.core.QuantitativeValue", "vocab:timeStep", multiple=False, required=True,
              doc="no description available"),
        Field("unit_of_measurement", "openminds.controlledterms.UnitOfMeasurement", "vocab:unitOfMeasurement", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('time_step',)
