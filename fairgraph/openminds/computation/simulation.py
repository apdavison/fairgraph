"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class Simulation(KGObjectV3):
    """

    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/Simulation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("inputs", ["openminds.core.File", "openminds.core.FileBundle", "openminds.core.ModelVersion", "openminds.core.SoftwareVersion"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("outputs", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:output", multiple=True, required=True,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("environment", "openminds.computation.Environment", "vocab:environment", multiple=False, required=True,
              doc="no description available"),
        Field("launch_configuration", "openminds.computation.LaunchConfiguration", "vocab:launchConfiguration", multiple=False, required=True,
              doc="no description available"),
        Field("started_by", ["openminds.computation.SoftwareAgent", "openminds.core.Person"], "vocab:startedBy", multiple=False, required=False,
              doc="no description available"),
        Field("was_informed_by", ["openminds.computation.DataAnalysis", "openminds.computation.Simulation", "openminds.computation.Optimization", "openminds.computation.Visualization"], "vocab:wasInformedBy", multiple=False, required=False,
              doc="no description available"),
        Field("status", "openminds.controlledterms.ActionStatusType", "vocab:status", multiple=False, required=False,
              doc="no description available"),
        Field("resource_usages", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:resourceUsage", multiple=True, required=False,
              doc="no description available"),
        Field("tags", str, "vocab:tags", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the simulation."),
        Field("ended_at_time", datetime, "vocab:endedAtTime", multiple=False, required=False,
              doc="no description available"),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("parameter_sets", "openminds.core.ParameterSet", "vocab:parameterSet", multiple=True, required=False,
              doc="Manner, position, or direction in which digital or physical properties are set to determine a particular function, characteristics or behavior of something."),
        Field("started_at_time", datetime, "vocab:startedAtTime", multiple=False, required=True,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.Handedness", "openminds.controlledterms.Organ", "openminds.controlledterms.Phenotype", "openminds.controlledterms.Species", "openminds.controlledterms.Strain", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),

    ]
    existence_query_fields = ('lookup_label',)
