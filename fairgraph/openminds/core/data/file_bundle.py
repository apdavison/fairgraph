"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FileBundle as OMFileBundle
from fairgraph import KGObject


class FileBundle(KGObject, OMFileBundle):
    """
    Structured information on a bundle of file instances.
    """

    type_ = "https://openminds.om-i.org/types/FileBundle"
    default_space = "files"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            [
                "openminds.latest.ephys.ElectrodeArrayUsage",
                "openminds.latest.ephys.ElectrodeUsage",
                "openminds.latest.ephys.PipetteUsage",
                "openminds.latest.specimen_prep.SlicingDeviceUsage",
            ],
            "metadataLocation",
            reverse="metadata_locations",
            multiple=True,
            description="reverse of 'metadata_locations'",
        ),
        Property(
            "has_parts",
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
        Property(
            "is_also_part_of",
            "openminds.latest.computation.WorkflowRecipeVersion",
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "is_input_to",
            "openminds.latest.core.DatasetVersion",
            "inputData",
            reverse="input_data",
            multiple=True,
            description="reverse of 'input_data'",
        ),
        Property(
            "is_location_of",
            ["openminds.latest.core.ServiceLink", "openminds.latest.ephys.Recording"],
            "dataLocation",
            reverse="data_location",
            multiple=True,
            description="reverse of 'data_location'",
        ),
        Property(
            "is_output_of",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            ["output", "outputData"],
            reverse=["output_data", "outputs"],
            multiple=True,
            description="reverse of output_data, outputs",
        ),
        Property(
            "is_reference_for",
            "openminds.latest.computation.ValidationTestVersion",
            "referenceData",
            reverse="reference_data",
            multiple=True,
            description="reverse of 'reference_data'",
        ),
        Property(
            "specifies",
            "openminds.latest.stimulation.EphysStimulus",
            "specification",
            reverse="specifications",
            multiple=True,
            description="reverse of 'specifications'",
        ),
    ]
    existence_query_properties = ("is_part_of", "name")

    def __init__(
        self,
        name=None,
        content_description=None,
        describes=None,
        format=None,
        grouped_by=None,
        grouping_types=None,
        has_parts=None,
        hash=None,
        is_also_part_of=None,
        is_input_to=None,
        is_location_of=None,
        is_output_of=None,
        is_part_of=None,
        is_reference_for=None,
        specifies=None,
        storage_size=None,
        id=None,
        data=None,
        space=None,
        release_status=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            release_status=release_status,
            data=data,
            name=name,
            content_description=content_description,
            describes=describes,
            format=format,
            grouped_by=grouped_by,
            grouping_types=grouping_types,
            has_parts=has_parts,
            hash=hash,
            is_also_part_of=is_also_part_of,
            is_input_to=is_input_to,
            is_location_of=is_location_of,
            is_output_of=is_output_of,
            is_part_of=is_part_of,
            is_reference_for=is_reference_for,
            specifies=specifies,
            storage_size=storage_size,
        )
