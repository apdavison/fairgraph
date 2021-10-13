"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class SubjectGroupState(KGObjectV3):
    """
    
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/SubjectGroupState"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("age_categories", "openminds.controlledterms.AgeCategory", "vocab:ageCategory", multiple=True, required=True,
              doc="Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings."),
        Field("handedness", "openminds.controlledterms.Handedness", "vocab:handedness", multiple=True, required=False,
              doc="Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task."),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("age", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:age", multiple=False, required=False,
              doc="Time of life or existence at which some particular qualification, capacity or event arises."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("pathologys", ["openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel"], "vocab:pathology", multiple=True, required=False,
              doc="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease."),
        Field("weight", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:weight", multiple=False, required=False,
              doc="Amount that a thing or being weighs."),
        
    ]
    existence_query_fields = ('lookup_label',)

