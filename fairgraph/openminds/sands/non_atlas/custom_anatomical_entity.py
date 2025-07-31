"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CustomAnatomicalEntity
from fairgraph import KGObject


class CustomAnatomicalEntity(KGObject, CustomAnatomicalEntity):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CustomAnatomicalEntity"
    default_space = "spatial"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_location_of",
            [
                "openminds.latest.core.TissueSample",
                "openminds.latest.core.TissueSampleCollection",
                "openminds.latest.ephys.ElectrodeArrayUsage",
                "openminds.latest.ephys.ElectrodeUsage",
                "openminds.latest.ephys.PipetteUsage",
            ],
            ["anatomicalLocation", "anatomicalLocationOfElectrodes"],
            reverse=["anatomical_location", "anatomical_locations", "anatomical_locations_of_electrodes"],
            multiple=True,
            description="reverse of anatomical_location, anatomical_locations, anatomical_locations_of_electrodes",
        ),
        Property(
            "is_target_of",
            "openminds.latest.sands.AnatomicalTargetPosition",
            "anatomicalTarget",
            reverse="anatomical_targets",
            multiple=True,
            description="reverse of 'anatomical_targets'",
        ),
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "studied_in",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.ValidationTest",
                "openminds.latest.computation.Visualization",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "studyTarget",
            reverse="study_targets",
            multiple=True,
            description="reverse of 'study_targets'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        has_annotations=None,
        is_location_of=None,
        is_target_of=None,
        is_used_to_group=None,
        related_uberon_term=None,
        relation_assessments=None,
        studied_in=None,
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
            name=name,
            has_annotations=has_annotations,
            is_location_of=is_location_of,
            is_target_of=is_target_of,
            is_used_to_group=is_used_to_group,
            related_uberon_term=related_uberon_term,
            relation_assessments=relation_assessments,
            studied_in=studied_in,
        )
