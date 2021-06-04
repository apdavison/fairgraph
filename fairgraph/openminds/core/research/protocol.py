"""
Structured information on a research project.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class Protocol(KGObjectV3):
    """
    Structured information on a research project.
    """
    default_space = "model"
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
        Field("behavioral_tasks", "openminds.controlledterms.BehavioralTask", "vocab:behavioralTask", multiple=True, required=False,
              doc="Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("study_options", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ", "openminds.controlledterms.Strain", "openminds.controlledterms.Species", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.Disease", "openminds.controlledterms.Handedness", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.Phenotype", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity"], "vocab:studyOption", multiple=True, required=False,
              doc="no description available"),
        Field("techniques", "openminds.controlledterms.Technique", "vocab:technique", multiple=True, required=True,
              doc="Method of accomplishing a desired aim."),

    ]
    existence_query_fields = None