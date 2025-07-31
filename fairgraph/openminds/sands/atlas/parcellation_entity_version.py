"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ParcellationEntityVersion
from fairgraph import KGObject


class ParcellationEntityVersion(KGObject, ParcellationEntityVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationEntityVersion"
    default_space = "atlas"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_children",
            "openminds.latest.sands.ParcellationEntityVersion",
            "hasParent",
            reverse="has_parents",
            multiple=True,
            description="reverse of 'has_parents'",
        ),
        Property(
            "is_location_of",
            [
                "openminds.latest.core.ServiceLink",
                "openminds.latest.core.TissueSample",
                "openminds.latest.core.TissueSampleCollection",
                "openminds.latest.ephys.ElectrodeArrayUsage",
                "openminds.latest.ephys.ElectrodeUsage",
                "openminds.latest.ephys.PipetteUsage",
            ],
            ["anatomicalLocation", "anatomicalLocationOfElectrodes", "dataLocation"],
            reverse=[
                "anatomical_location",
                "anatomical_locations",
                "anatomical_locations_of_electrodes",
                "data_location",
            ],
            multiple=True,
            description="reverse of anatomical_location, anatomical_locations, anatomical_locations_of_electrodes, data_location",
        ),
        Property(
            "is_part_of",
            "openminds.latest.sands.ParcellationTerminologyVersion",
            "hasEntity",
            reverse="has_entities",
            multiple=True,
            description="reverse of 'has_entities'",
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
            "is_version_of",
            "openminds.latest.sands.ParcellationEntity",
            "hasVersion",
            reverse="has_versions",
            multiple=True,
            description="reverse of 'has_versions'",
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
    existence_query_properties = ("name", "version_identifier")

    def __init__(
        self,
        name=None,
        lookup_label=None,
        abbreviation=None,
        additional_remarks=None,
        alternate_names=None,
        corrected_name=None,
        has_annotations=None,
        has_children=None,
        has_parents=None,
        is_location_of=None,
        is_part_of=None,
        is_target_of=None,
        is_used_to_group=None,
        is_version_of=None,
        ontology_identifiers=None,
        relation_assessments=None,
        studied_in=None,
        version_identifier=None,
        version_innovation=None,
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
            lookup_label=lookup_label,
            abbreviation=abbreviation,
            additional_remarks=additional_remarks,
            alternate_names=alternate_names,
            corrected_name=corrected_name,
            has_annotations=has_annotations,
            has_children=has_children,
            has_parents=has_parents,
            is_location_of=is_location_of,
            is_part_of=is_part_of,
            is_target_of=is_target_of,
            is_used_to_group=is_used_to_group,
            is_version_of=is_version_of,
            ontology_identifiers=ontology_identifiers,
            relation_assessments=relation_assessments,
            studied_in=studied_in,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
