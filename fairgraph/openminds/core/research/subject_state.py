"""
Structured information on a temporary state of a subject.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class SubjectState(KGObject):
    """
    Structured information on a temporary state of a subject.
    """
    default_space = "dataset"
    type_ = ["https://openminds.ebrains.eu/core/SubjectState"]
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
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("age", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:age", multiple=False, required=False,
              doc="Time of life or existence at which some particular qualification, capacity or event arises."),
        Field("age_category", "openminds.controlledterms.AgeCategory", "vocab:ageCategory", multiple=False, required=True,
              doc="Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings."),
        Field("attributes", "openminds.controlledterms.SubjectAttribute", "vocab:attribute", multiple=True, required=False,
              doc="no description available"),
        Field("descended_from", "openminds.core.SubjectState", "vocab:descendedFrom", multiple=False, required=False,
              doc="no description available"),
        Field("handedness", "openminds.controlledterms.Handedness", "vocab:handedness", multiple=False, required=False,
              doc="Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the subject state within a particular product."),
        Field("pathologies", ["openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel"], "vocab:pathology", multiple=True, required=False,
              doc="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease."),
        Field("relative_time_indication", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:relativeTimeIndication", multiple=False, required=False,
              doc="no description available"),
        Field("weight", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:weight", multiple=False, required=False,
              doc="Amount that a thing or being weighs."),

    ]
    existence_query_fields = ('lookup_label',)

    def __init__(self, lookup_label=None, additional_remarks=None, age=None, age_category=None, attributes=None, descended_from=None, handedness=None, internal_identifier=None, pathologies=None, relative_time_indication=None, weight=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, lookup_label=lookup_label, additional_remarks=additional_remarks, age=age, age_category=age_category, attributes=attributes, descended_from=descended_from, handedness=handedness, internal_identifier=internal_identifier, pathologies=pathologies, relative_time_indication=relative_time_indication, weight=weight)