"""
Structured information about a computation whose type is unknown or unspecified.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class GenericComputation(KGObject):
    """
    Structured information about a computation whose type is unknown or unspecified.
    """
    default_space = "computation"
    type_ = ["https://openminds.ebrains.eu/computation/GenericComputation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("custom_property_sets", "openminds.core.CustomPropertySet", "vocab:customPropertySet", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the generic computation."),
        Field("end_time", datetime, "vocab:endTime", multiple=False, required=False,
              doc="no description available"),
        Field("environment", ["openminds.computation.Environment", "openminds.core.WebServiceVersion"], "vocab:environment", multiple=False, required=True,
              doc="no description available"),
        Field("inputs", ["openminds.computation.LocalFile", "openminds.core.File", "openminds.core.FileBundle", "openminds.core.SoftwareVersion"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("launch_configuration", "openminds.computation.LaunchConfiguration", "vocab:launchConfiguration", multiple=False, required=False,
              doc="no description available"),
        Field("outputs", ["openminds.computation.LocalFile", "openminds.core.File", "openminds.core.FileArchive", "openminds.core.FileBundle"], "vocab:output", multiple=True, required=True,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("performed_by", ["openminds.computation.SoftwareAgent", "openminds.core.Person"], "vocab:performedBy", multiple=True, required=False,
              doc="no description available"),
        Field("recipe", "openminds.computation.WorkflowRecipeVersion", "vocab:recipe", multiple=False, required=False,
              doc="no description available"),
        Field("resource_usages", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:resourceUsage", multiple=True, required=False,
              doc="no description available"),
        Field("start_time", datetime, "vocab:startTime", multiple=False, required=True,
              doc="no description available"),
        Field("started_by", ["openminds.computation.SoftwareAgent", "openminds.core.Person"], "vocab:startedBy", multiple=False, required=False,
              doc="no description available"),
        Field("status", "openminds.controlledterms.ActionStatusType", "vocab:status", multiple=False, required=False,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.Species", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.VisualStimulusType", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),
        Field("tags", str, "vocab:tag", multiple=True, required=False,
              doc="no description available"),
        Field("techniques", "openminds.controlledterms.AnalysisTechnique", "vocab:technique", multiple=True, required=False,
              doc="Method of accomplishing a desired aim."),
        Field("was_informed_by", ["openminds.computation.DataAnalysis", "openminds.computation.DataCopy", "openminds.computation.GenericComputation", "openminds.computation.ModelValidation", "openminds.computation.Optimization", "openminds.computation.Simulation", "openminds.computation.Visualization"], "vocab:wasInformedBy", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
