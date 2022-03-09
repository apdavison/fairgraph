"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class StimulationExperiment(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/StimulationExperiment"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the stimulation experiment within a particular product."),
        Field("stimulation_devices", ["openminds.ephys.Device", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"], "vocab:stimulationDevice", multiple=True, required=True,
              doc="no description available"),
        Field("aquisition_devices", ["openminds.ephys.Device", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"], "vocab:aquisitionDevice", multiple=True, required=True,
              doc="no description available"),
        Field("target_holding_potential", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:targetHoldingPotential", multiple=False, required=False,
              doc="no description available"),
        Field("inputs", ["openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState", "openminds.ephys.PatchedCell"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("outputs", "openminds.ephys.Recording", "vocab:output", multiple=True, required=True,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("compensation_current", "openminds.ephys.Measurement", "vocab:compensationCurrent", multiple=False, required=False,
              doc="no description available"),
        Field("measured_holding_potential", "openminds.ephys.Measurement", "vocab:measuredHoldingPotential", multiple=False, required=False,
              doc="no description available"),
        Field("series_resistance", "openminds.ephys.Measurement", "vocab:seriesResistance", multiple=False, required=False,
              doc="no description available"),
        Field("input_resistance", "openminds.ephys.Measurement", "vocab:inputResistance", multiple=False, required=False,
              doc="no description available"),
        Field("stimulus", "openminds.core.Stimulation", "vocab:stimulus", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('stimulation_devices', 'aquisition_devices', 'inputs', 'outputs', 'stimulus')
