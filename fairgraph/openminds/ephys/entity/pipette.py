"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Pipette(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Pipette"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("external_diameter", "openminds.core.QuantitativeValue", "vocab:externalDiameter", multiple=False, required=False,
              doc="no description available"),
        Field("internal_diameter", "openminds.core.QuantitativeValue", "vocab:internalDiameter", multiple=False, required=False,
              doc="no description available"),
        Field("pipette_resistance", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:pipetteResistance", multiple=False, required=True,
              doc="no description available"),
        Field("pipette_solution", str, "vocab:pipetteSolution", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('pipette_resistance', 'pipette_solution')
