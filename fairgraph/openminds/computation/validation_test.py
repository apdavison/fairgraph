"""
Structured information about the definition of a process for validating a computational model.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class ValidationTest(KGObject):
    """
    Structured information about the definition of a process for validating a computational model.
    """
    default_space = "computation"
    type_ = ["https://openminds.ebrains.eu/computation/ValidationTest"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the validation test."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the validation test."),
        Field("custodians", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the validation test."),
        Field("developers", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:developer", multiple=True, required=True,
              doc="Legal person that creates or improves products or services (e.g., software, applications, etc.)."),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("versions", "openminds.computation.ValidationTestVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the validation test."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("reference_data_acquisitions", "openminds.controlledterms.Technique", "vocab:referenceDataAcquisition", multiple=True, required=False,
              doc="no description available"),
        Field("model_scope", "openminds.controlledterms.ModelScope", "vocab:scope", multiple=False, required=False,
              doc="Extent of something."),
        Field("score_type", "openminds.controlledterms.DifferenceMeasure", "vocab:scoreType", multiple=False, required=False,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.Species", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.VisualStimulusType", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),

    ]
    existence_query_fields = ('name', 'alias')

    def __init__(self, name=None, alias=None, custodians=None, description=None, developers=None, digital_identifier=None, versions=None, homepage=None, how_to_cite=None, reference_data_acquisitions=None, model_scope=None, score_type=None, study_targets=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, alias=alias, custodians=custodians, description=description, developers=developers, digital_identifier=digital_identifier, versions=versions, homepage=homepage, how_to_cite=how_to_cite, reference_data_acquisitions=reference_data_acquisitions, model_scope=model_scope, score_type=score_type, study_targets=study_targets)