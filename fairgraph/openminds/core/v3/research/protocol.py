"""
Structured information on a research project.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class Protocol(KGObject):
    """
    Structured information on a research project.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/Protocol"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the protocol."),
        Field("behavioral_tasks", "openminds.controlledTerms.BehavioralTask", "vocab:behavioralTask", multiple=True, required=False,
              doc="Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("study_targets", ["openminds.sands.AnatomicalEntity", "openminds.controlledTerms.CellType", "openminds.controlledTerms.Organ", "openminds.controlledTerms.Strain", "openminds.controlledTerms.Species", "openminds.controlledTerms.BiologicalSex", "openminds.controlledTerms.TermSuggestion", "openminds.controlledTerms.Disease", "openminds.controlledTerms.Handedness", "openminds.controlledTerms.DiseaseModel", "openminds.controlledTerms.Phenotype"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),
        Field("techniques", "openminds.controlledTerms.Technique", "vocab:technique", multiple=True, required=True,
              doc="Method of accomplishing a desired aim."),
        
    ]
    existence_query_fields = ('name',)