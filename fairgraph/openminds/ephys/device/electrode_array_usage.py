"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import ElectrodeArrayUsage
from fairgraph import KGObject


class ElectrodeArrayUsage(KGObject, ElectrodeArrayUsage):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ElectrodeArrayUsage"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "generation_device",
            "openminds.latest.stimulation.EphysStimulus",
            "generatedBy",
            reverse="generated_by",
            multiple=True,
            description="reverse of 'generated_by'",
        ),
        Property(
            "placed_by",
            "openminds.latest.ephys.ElectrodePlacement",
            "device",
            reverse="devices",
            multiple=True,
            description="reverse of 'devices'",
        ),
        Property(
            "used_in",
            ["openminds.latest.ephys.CellPatching", "openminds.latest.ephys.RecordingActivity"],
            "device",
            reverse="devices",
            multiple=True,
            description="reverse of 'devices'",
        ),
        Property(
            "used_to_measure",
            "openminds.latest.core.Measurement",
            "measuredWith",
            reverse="measured_with",
            multiple=True,
            description="reverse of 'measured_with'",
        ),
        Property(
            "used_to_record",
            "openminds.latest.ephys.Recording",
            "recordedWith",
            reverse="recorded_with",
            multiple=True,
            description="reverse of 'recorded_with'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        anatomical_locations_of_arrays=None,
        anatomical_locations_of_electrodes=None,
        contact_resistances=None,
        device=None,
        generation_device=None,
        metadata_locations=None,
        placed_by=None,
        spatial_locations_of_electrodes=None,
        used_electrodes=None,
        used_in=None,
        used_specimen=None,
        used_to_measure=None,
        used_to_record=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            anatomical_locations_of_arrays=anatomical_locations_of_arrays,
            anatomical_locations_of_electrodes=anatomical_locations_of_electrodes,
            contact_resistances=contact_resistances,
            device=device,
            generation_device=generation_device,
            metadata_locations=metadata_locations,
            placed_by=placed_by,
            spatial_locations_of_electrodes=spatial_locations_of_electrodes,
            used_electrodes=used_electrodes,
            used_in=used_in,
            used_specimen=used_specimen,
            used_to_measure=used_to_measure,
            used_to_record=used_to_record,
        )
