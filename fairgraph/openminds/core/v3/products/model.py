"""
Structured information on a computational model (concept level).
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class Model(KGObject):
    """
    Structured information on a computational model (concept level).
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/Model"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("abstraction_level", "openminds.controlledTerms.ModelAbstractionLevel", "vocab:abstractionLevel", multiple=False, required=True,
              doc="Extent of simplification of physical, spatial, or temporal details or attributes in the study of objects or systems."),
        Field("developers", ["openminds.core.Organization", "openminds.core.Person"], "vocab:developer", multiple=True, required=True,
              doc="Legal person that creates or improves products or services (e.g., software, applications, etc.)."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.SWHID"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("versions", "openminds.core.ModelVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("model_scope", "openminds.controlledTerms.ModelScope", "vocab:scope", multiple=False, required=True,
              doc="Extent of something."),
        Field("study_targets", ["openminds.sands.AnatomicalEntity", "openminds.controlledTerms.CellType", "openminds.controlledTerms.Organ", "openminds.controlledTerms.Strain", "openminds.controlledTerms.Species", "openminds.controlledTerms.BiologicalSex", "openminds.controlledTerms.TermSuggestion", "openminds.controlledTerms.Disease", "openminds.controlledTerms.Handedness", "openminds.controlledTerms.DiseaseModel", "openminds.controlledTerms.Phenotype"], "vocab:studyTarget", multiple=True, required=True,
              doc="Structure or function that was targeted within a study."),
        Field("custodians", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="Legal person entrusted with guarding and maintaining property or records."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the model."),
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the model."),
        Field("homepage", str, "vocab:homepage", multiple=False, required=False,
              doc="Main website of something or someone."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the model."),
        
    ]
    existence_query_fields = ('name',)