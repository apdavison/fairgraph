"""
Structured information on a temporary state of a subject.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import SubjectState
from fairgraph import KGObject


class SubjectState(KGObject, SubjectState):
    """
    Structured information on a temporary state of a subject.
    """

    type_ = "https://openminds.om-i.org/types/SubjectState"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_children",
            [
                "openminds.latest.core.SubjectState",
                "openminds.latest.core.TissueSampleCollectionState",
                "openminds.latest.core.TissueSampleState",
            ],
            "descendedFrom",
            reverse="descended_from",
            multiple=True,
            description="reverse of 'descended_from'",
        ),
        Property(
            "is_input_to",
            [
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
            ],
            "input",
            reverse="inputs",
            multiple=True,
            description="reverse of 'inputs'",
        ),
        Property(
            "is_output_of",
            [
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "output",
            reverse="outputs",
            multiple=True,
            description="reverse of 'outputs'",
        ),
        Property(
            "is_state_of",
            "openminds.latest.core.Subject",
            "studiedState",
            reverse="studied_states",
            multiple=True,
            description="reverse of 'studied_states'",
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
            "used_in",
            [
                "openminds.latest.ephys.ElectrodeArrayUsage",
                "openminds.latest.ephys.ElectrodeUsage",
                "openminds.latest.ephys.PipetteUsage",
                "openminds.latest.specimen_prep.SlicingDeviceUsage",
            ],
            "usedSpecimen",
            reverse="used_specimen",
            multiple=True,
            description="reverse of 'used_specimen'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        additional_remarks=None,
        age=None,
        age_category=None,
        attributes=None,
        descended_from=None,
        handedness=None,
        has_children=None,
        internal_identifier=None,
        is_input_to=None,
        is_output_of=None,
        is_state_of=None,
        is_used_to_group=None,
        pathologies=None,
        relative_time_indication=None,
        used_in=None,
        weight=None,
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
            additional_remarks=additional_remarks,
            age=age,
            age_category=age_category,
            attributes=attributes,
            descended_from=descended_from,
            handedness=handedness,
            has_children=has_children,
            internal_identifier=internal_identifier,
            is_input_to=is_input_to,
            is_output_of=is_output_of,
            is_state_of=is_state_of,
            is_used_to_group=is_used_to_group,
            pathologies=pathologies,
            relative_time_indication=relative_time_indication,
            used_in=used_in,
            weight=weight,
        )
