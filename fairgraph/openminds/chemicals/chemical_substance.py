"""
Structured information about a chemical substance.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ChemicalSubstance(KGObject):
    """
    Structured information about a chemical substance.
    """

    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/chemicals/ChemicalSubstance"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            multiple=False,
            required=False,
            doc="no description available",
        ),
        Field(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            multiple=False,
            required=False,
            doc="Mention of what deserves additional attention or notice.",
        ),
        Field(
            "molecular_entity",
            "openminds.controlledterms.MolecularEntity",
            "vocab:molecularEntity",
            multiple=False,
            required=True,
            doc="no description available",
        ),
        Field(
            "product_source",
            "openminds.chemicals.ProductSource",
            "vocab:productSource",
            multiple=False,
            required=False,
            doc="no description available",
        ),
        Field(
            "purity",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:purity",
            multiple=False,
            required=False,
            doc="no description available",
        ),
    ]
    existence_query_fields = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        additional_remarks=None,
        molecular_entity=None,
        product_source=None,
        purity=None,
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
            molecular_entity=molecular_entity,
            product_source=product_source,
            purity=purity,
        )
