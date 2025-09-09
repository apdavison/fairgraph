"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.specimen_prep import SlicingDeviceUsage as OMSlicingDeviceUsage
from fairgraph import KGObject


class SlicingDeviceUsage(KGObject, OMSlicingDeviceUsage):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SlicingDeviceUsage"
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
            "used_for",
            "openminds.latest.specimen_prep.TissueSampleSlicing",
            "device",
            reverse="device",
            multiple=True,
            description="reverse of 'device'",
        ),
        Property(
            "used_in",
            "openminds.latest.ephys.CellPatching",
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
        device=None,
        generation_device=None,
        metadata_locations=None,
        oscillation_amplitude=None,
        placed_by=None,
        slice_thickness=None,
        slicing_angles=None,
        slicing_plane=None,
        slicing_speed=None,
        used_for=None,
        used_in=None,
        used_specimen=None,
        used_to_measure=None,
        used_to_record=None,
        vibration_frequency=None,
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
            device=device,
            generation_device=generation_device,
            metadata_locations=metadata_locations,
            oscillation_amplitude=oscillation_amplitude,
            placed_by=placed_by,
            slice_thickness=slice_thickness,
            slicing_angles=slicing_angles,
            slicing_plane=slicing_plane,
            slicing_speed=slicing_speed,
            used_for=used_for,
            used_in=used_in,
            used_specimen=used_specimen,
            used_to_measure=used_to_measure,
            used_to_record=used_to_record,
            vibration_frequency=vibration_frequency,
        )


# cast openMINDS instances to their fairgraph subclass
SlicingDeviceUsage.set_error_handling(None)
for key, value in OMSlicingDeviceUsage.__dict__.items():
    if isinstance(value, OMSlicingDeviceUsage):
        fg_instance = SlicingDeviceUsage.from_jsonld(value.to_jsonld())
        fg_instance._space = SlicingDeviceUsage.default_space
        setattr(SlicingDeviceUsage, key, fg_instance)
SlicingDeviceUsage.set_error_handling("log")
