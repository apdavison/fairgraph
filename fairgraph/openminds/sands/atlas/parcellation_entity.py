"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ParcellationEntity as OMParcellationEntity
from fairgraph import KGObject


class ParcellationEntity(KGObject, OMParcellationEntity):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationEntity"
    default_space = "atlas"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_children",
            ["openminds.latest.sands.ParcellationEntity", "openminds.latest.sands.ParcellationEntityVersion"],
            "hasParent",
            reverse="has_parents",
            multiple=True,
            description="reverse of 'has_parents'",
        ),
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
    aliases = {"versions": "has_versions"}
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        lookup_label=None,
        abbreviation=None,
        alternate_names=None,
        definition=None,
        has_children=None,
        has_parents=None,
        has_versions=None,
        is_location_of=None,
        is_target_of=None,
        is_used_to_group=None,
        ontology_identifiers=None,
        related_uberon_term=None,
        studied_in=None,
        versions=None,
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
            alternate_names=alternate_names,
            definition=definition,
            has_children=has_children,
            has_parents=has_parents,
            has_versions=has_versions,
            is_location_of=is_location_of,
            is_target_of=is_target_of,
            is_used_to_group=is_used_to_group,
            ontology_identifiers=ontology_identifiers,
            related_uberon_term=related_uberon_term,
            studied_in=studied_in,
            versions=versions,
        )


# cast openMINDS instances to their fairgraph subclass
ParcellationEntity.set_error_handling(None)
for key, value in OMParcellationEntity.__dict__.items():
    if isinstance(value, OMParcellationEntity):
        fg_instance = ParcellationEntity.from_jsonld(value.to_jsonld())
        fg_instance._space = ParcellationEntity.default_space
        setattr(ParcellationEntity, key, fg_instance)
ParcellationEntity.set_error_handling("log")
