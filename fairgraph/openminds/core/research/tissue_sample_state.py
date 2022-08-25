"""
Structured information on a temporary state of a tissue sample.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class TissueSampleState(KGObject):
    """
    Structured information on a temporary state of a tissue sample.
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/TissueSampleState"]
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
        Field("attributes", "openminds.controlledterms.TissueSampleAttribute", "vocab:attribute", multiple=True, required=False,
              doc="no description available"),
        Field("descended_from", ["openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"], "vocab:descendedFrom", multiple=True, required=False,
              doc="no description available"),
        Field("pathologies", ["openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel"], "vocab:pathology", multiple=True, required=False,
              doc="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease."),
        Field("relative_time_indication", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:relativeTimeIndication", multiple=False, required=False,
              doc="no description available"),
        Field("weight", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:weight", multiple=False, required=False,
              doc="Amount that a thing or being weighs."),

    ]
    existence_query_fields = ('lookup_label',)
