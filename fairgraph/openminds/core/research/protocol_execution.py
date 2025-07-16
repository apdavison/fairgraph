"""
Structured information on a protocol execution.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from datetime import datetime, time


class ProtocolExecution(KGObject):
    """
    Structured information on a protocol execution.
    """

    default_space = "dataset"
    type_ = "https://openminds.ebrains.eu/core/ProtocolExecution"
    properties = [
        Property(
            "behavioral_protocols",
            "openminds.core.BehavioralProtocol",
            "vocab:behavioralProtocol",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "custom_property_sets",
            "openminds.core.CustomPropertySet",
            "vocab:customPropertySet",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the protocol execution.",
        ),
        Property("end_time", [datetime, time], "vocab:endTime", doc="no description available"),
        Property(
            "inputs",
            [
                "openminds.core.File",
                "openminds.core.FileBundle",
                "openminds.core.SubjectGroupState",
                "openminds.core.SubjectState",
                "openminds.core.TissueSampleCollectionState",
                "openminds.core.TissueSampleState",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "vocab:input",
            multiple=True,
            required=True,
            doc="Something or someone that is put into or participates in a process or machine.",
        ),
        Property(
            "is_part_of",
            "openminds.core.DatasetVersion",
            "vocab:isPartOf",
            required=True,
            doc="Reference to the ensemble of multiple things or beings.",
        ),
        Property("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Property(
            "outputs",
            [
                "openminds.core.File",
                "openminds.core.FileBundle",
                "openminds.core.SubjectGroupState",
                "openminds.core.SubjectState",
                "openminds.core.TissueSampleCollectionState",
                "openminds.core.TissueSampleState",
            ],
            "vocab:output",
            multiple=True,
            required=True,
            doc="Something or someone that comes out of, is delivered or produced by a process or machine.",
        ),
        Property(
            "performed_by",
            ["openminds.computation.SoftwareAgent", "openminds.core.Person"],
            "vocab:performedBy",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "preparation_design",
            "openminds.controlled_terms.PreparationType",
            "vocab:preparationDesign",
            doc="no description available",
        ),
        Property(
            "protocols",
            "openminds.core.Protocol",
            "vocab:protocol",
            multiple=True,
            required=True,
            doc="Plan that describes the process of a scientific or medical experiment, treatment, or procedure.",
        ),
        Property("start_time", [datetime, time], "vocab:startTime", doc="no description available"),
        Property(
            "study_targets",
            [
                "openminds.controlled_terms.AuditoryStimulusType",
                "openminds.controlled_terms.BiologicalOrder",
                "openminds.controlled_terms.BiologicalSex",
                "openminds.controlled_terms.BreedingType",
                "openminds.controlled_terms.CellCultureType",
                "openminds.controlled_terms.CellType",
                "openminds.controlled_terms.Disease",
                "openminds.controlled_terms.DiseaseModel",
                "openminds.controlled_terms.ElectricalStimulusType",
                "openminds.controlled_terms.GeneticStrainType",
                "openminds.controlled_terms.GustatoryStimulusType",
                "openminds.controlled_terms.Handedness",
                "openminds.controlled_terms.MolecularEntity",
                "openminds.controlled_terms.OlfactoryStimulusType",
                "openminds.controlled_terms.OpticalStimulusType",
                "openminds.controlled_terms.Organ",
                "openminds.controlled_terms.OrganismSubstance",
                "openminds.controlled_terms.OrganismSystem",
                "openminds.controlled_terms.Species",
                "openminds.controlled_terms.SubcellularEntity",
                "openminds.controlled_terms.TactileStimulusType",
                "openminds.controlled_terms.TermSuggestion",
                "openminds.controlled_terms.TissueSampleType",
                "openminds.controlled_terms.UBERONParcellation",
                "openminds.controlled_terms.VisualStimulusType",
                "openminds.sands.CustomAnatomicalEntity",
                "openminds.sands.ParcellationEntity",
                "openminds.sands.ParcellationEntityVersion",
            ],
            "vocab:studyTarget",
            multiple=True,
            doc="Structure or function that was targeted within a study.",
        ),
    ]
    reverse_properties = [
        Property(
            "based_on_protocol_execution",
            ["openminds.sands.AtlasAnnotation", "openminds.sands.CustomAnnotation"],
            "^vocab:criteria",
            reverse="criteria",
            multiple=True,
            doc="reverse of 'criteria'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        based_on_protocol_execution=None,
        behavioral_protocols=None,
        custom_property_sets=None,
        description=None,
        end_time=None,
        inputs=None,
        is_part_of=None,
        outputs=None,
        performed_by=None,
        preparation_design=None,
        protocols=None,
        start_time=None,
        study_targets=None,
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
            based_on_protocol_execution=based_on_protocol_execution,
            behavioral_protocols=behavioral_protocols,
            custom_property_sets=custom_property_sets,
            description=description,
            end_time=end_time,
            inputs=inputs,
            is_part_of=is_part_of,
            outputs=outputs,
            performed_by=performed_by,
            preparation_design=preparation_design,
            protocols=protocols,
            start_time=start_time,
            study_targets=study_targets,
        )
