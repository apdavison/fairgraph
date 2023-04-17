"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class TissueSampleCollectionState(KGObject):
    """ """

    default_space = "dataset"
    type_ = ["https://openminds.ebrains.eu/core/TissueSampleCollectionState"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Field(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            doc="Mention of what deserves additional attention or notice.",
        ),
        Field(
            "age",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:age",
            doc="Time of life or existence at which some particular qualification, capacity or event arises.",
        ),
        Field(
            "attributes",
            "openminds.controlledterms.TissueSampleAttribute",
            "vocab:attribute",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "descended_from",
            [
                "openminds.core.SubjectGroupState",
                "openminds.core.SubjectState",
                "openminds.core.TissueSampleCollectionState",
                "openminds.core.TissueSampleState",
            ],
            "vocab:descendedFrom",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            doc="Term or code that identifies the tissue sample collection state within a particular product.",
        ),
        Field(
            "pathologies",
            ["openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel"],
            "vocab:pathology",
            multiple=True,
            doc="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
        ),
        Field(
            "relative_time_indication",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:relativeTimeIndication",
            doc="no description available",
        ),
        Field(
            "weight",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:weight",
            doc="Amount that a thing or being weighs.",
        ),
    ]
    existence_query_fields = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        additional_remarks=None,
        age=None,
        attributes=None,
        descended_from=None,
        internal_identifier=None,
        pathologies=None,
        relative_time_indication=None,
        weight=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            additional_remarks=additional_remarks,
            age=age,
            attributes=attributes,
            descended_from=descended_from,
            internal_identifier=internal_identifier,
            pathologies=pathologies,
            relative_time_indication=relative_time_indication,
            weight=weight,
        )
