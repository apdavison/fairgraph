"""
Structured information on a protocol execution.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class ProtocolExecution(KGObjectV3):
    """
    Structured information on a protocol execution.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/ProtocolExecution"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the protocol execution."),
        Field("inputs", ["openminds.core.FileBundle", "openminds.core.File", "openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("outputs", ["openminds.core.FileBundle", "openminds.core.File", "openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"], "vocab:output", multiple=True, required=True,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("parameter_sets", "openminds.core.ParameterSet", "vocab:parameterSet", multiple=True, required=False,
              doc="Manner, position, or direction in which digital or physical properties are set to determine a particular function, characteristics or behavior of something."),
        Field("preparation_type", "openminds.controlledterms.PreparationType", "vocab:preparationType", multiple=False, required=False,
              doc="Distinct class of actions or processes that make something ready for use or service."),
        Field("protocols", "openminds.core.Protocol", "vocab:protocol", multiple=True, required=True,
              doc="Plan that describes the process of a scientific or medical experiment, treatment, or procedure."),
        Field("semantically_anchored_tos", "openminds.sands.CustomAnatomicalEntity", "vocab:semanticallyAnchoredTo", multiple=True, required=False,
              doc="Reference to a related anatomical structure without providing a quantitative proof of the claimed relation."),
        Field("study_targets", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ", "openminds.controlledterms.Strain", "openminds.controlledterms.Species", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.Disease", "openminds.controlledterms.Handedness", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.Phenotype", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),

    ]
    existence_query_fields = None