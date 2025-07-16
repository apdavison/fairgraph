"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class SubjectGroupState(KGObject):
    """
    <description not available>
    """

    default_space = "dataset"
    type_ = "https://openminds.ebrains.eu/core/SubjectGroupState"
    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            doc="Mention of what deserves additional attention or notice.",
        ),
        Property(
            "age",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:age",
            doc="Time of life or existence at which some particular qualification, capacity or event arises.",
        ),
        Property(
            "age_categories",
            "openminds.controlled_terms.AgeCategory",
            "vocab:ageCategory",
            multiple=True,
            required=True,
            doc="Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings.",
        ),
        Property(
            "attributes",
            "openminds.controlled_terms.SubjectAttribute",
            "vocab:attribute",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "descended_from", "openminds.core.SubjectGroupState", "vocab:descendedFrom", doc="no description available"
        ),
        Property(
            "handedness",
            "openminds.controlled_terms.Handedness",
            "vocab:handedness",
            multiple=True,
            doc="Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            doc="Term or code that identifies the subject group state within a particular product.",
        ),
        Property("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Property(
            "pathologies",
            ["openminds.controlled_terms.Disease", "openminds.controlled_terms.DiseaseModel"],
            "vocab:pathology",
            multiple=True,
            doc="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
        ),
        Property(
            "relative_time_indication",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:relativeTimeIndication",
            doc="no description available",
        ),
        Property(
            "weight",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:weight",
            doc="Amount that a thing or being weighs.",
        ),
    ]
    reverse_properties = [
        Property(
            "has_children",
            [
                "openminds.core.SubjectGroupState",
                "openminds.core.TissueSampleCollectionState",
                "openminds.core.TissueSampleState",
            ],
            "^vocab:descendedFrom",
            reverse="descended_from",
            multiple=True,
            doc="reverse of 'descended_from'",
        ),
        Property(
            "is_input_to",
            ["openminds.ephys.RecordingActivity", "openminds.specimen_prep.TissueCulturePreparation"],
            "^vocab:input",
            reverse="inputs",
            multiple=True,
            doc="reverse of 'inputs'",
        ),
        Property(
            "is_output_of",
            ["openminds.core.ProtocolExecution", "openminds.stimulation.StimulationActivity"],
            "^vocab:output",
            reverse="outputs",
            multiple=True,
            doc="reverse of 'outputs'",
        ),
        Property(
            "is_state_of",
            "openminds.core.SubjectGroup",
            "^vocab:studiedState",
            reverse="studied_states",
            multiple=True,
            doc="reverse of 'studied_states'",
        ),
        Property(
            "is_used_to_group",
            "openminds.core.FileBundle",
            "^vocab:groupedBy",
            reverse="grouped_by",
            multiple=True,
            doc="reverse of 'grouped_by'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        additional_remarks=None,
        age=None,
        age_categories=None,
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
        weight=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            additional_remarks=additional_remarks,
            age=age,
            age_categories=age_categories,
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
            weight=weight,
        )
