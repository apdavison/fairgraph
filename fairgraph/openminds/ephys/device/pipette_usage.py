"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class PipetteUsage(KGObject):
    """

    """
    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/ephys/PipetteUsage"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("anatomical_location", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalLocation", multiple=False, required=False,
              doc="no description available"),
        Field("chloride_reversal_potentials", "openminds.core.Measurement", "vocab:chlorideReversalPotential", multiple=True, required=False,
              doc="no description available"),
        Field("compensation_current", "openminds.core.Measurement", "vocab:compensationCurrent", multiple=False, required=False,
              doc="no description available"),
        Field("device", "openminds.ephys.Pipette", "vocab:device", multiple=False, required=True,
              doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function."),
        Field("end_membrane_potential", "openminds.core.Measurement", "vocab:endMembranePotential", multiple=False, required=False,
              doc="no description available"),
        Field("holding_potential", "openminds.core.Measurement", "vocab:holdingPotential", multiple=False, required=False,
              doc="no description available"),
        Field("input_resistance", "openminds.core.Measurement", "vocab:inputResistance", multiple=False, required=False,
              doc="no description available"),
        Field("labeling_compound", ["openminds.chemicals.ChemicalMixture", "openminds.chemicals.ChemicalSubstance", "openminds.controlledterms.MolecularEntity"], "vocab:labelingCompound", multiple=False, required=False,
              doc="no description available"),
        Field("liquid_junction_potential", "openminds.core.Measurement", "vocab:liquidJunctionPotential", multiple=False, required=False,
              doc="no description available"),
        Field("metadata_locations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:metadataLocation", multiple=True, required=False,
              doc="no description available"),
        Field("pipette_resistance", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:pipetteResistance", multiple=False, required=False,
              doc="no description available"),
        Field("pipette_solution", "openminds.chemicals.ChemicalMixture", "vocab:pipetteSolution", multiple=False, required=True,
              doc="no description available"),
        Field("seal_resistance", "openminds.core.Measurement", "vocab:sealResistance", multiple=False, required=False,
              doc="no description available"),
        Field("series_resistance", "openminds.core.Measurement", "vocab:seriesResistance", multiple=False, required=False,
              doc="no description available"),
        Field("spatial_location", "openminds.sands.CoordinatePoint", "vocab:spatialLocation", multiple=False, required=False,
              doc="no description available"),
        Field("start_membrane_potential", "openminds.core.Measurement", "vocab:startMembranePotential", multiple=False, required=False,
              doc="no description available"),
        Field("used_specimen", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:usedSpecimen", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
