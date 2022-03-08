"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class PatchedCell(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/PatchedCell"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("pipettes", "openminds.ephys.Pipette", "vocab:pipettes", multiple=True, required=False,
              doc="no description available"),
        Field("start_membrane_potential", "openminds.ephys.Measurement", "vocab:startMembranePotential", multiple=False, required=False,
              doc="no description available"),
        Field("end_membrane_potential", "openminds.ephys.Measurement", "vocab:endMembranePotential", multiple=False, required=False,
              doc="no description available"),
        Field("seal_resistances", "openminds.ephys.Measurement", "vocab:sealResistance", multiple=True, required=False,
              doc="no description available"),
        Field("liquid_junction_potentials", "openminds.ephys.Measurement", "vocab:liquidJunctionPotential", multiple=True, required=False,
              doc="no description available"),
        Field("chloride_reversal_potentials", "openminds.ephys.Measurement", "vocab:chlorideReversalPotential", multiple=True, required=False,
              doc="no description available"),
        Field("labeling_compound", str, "vocab:labelingCompound", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ()
