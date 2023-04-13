"""
Structured information about a mixture of chemical substances.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ChemicalMixture(KGObject):
    """
    Structured information about a mixture of chemical substances.
    """

    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/chemicals/ChemicalMixture"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            multiple=False,
            required=False,
            doc="Word or phrase that constitutes the distinctive designation of the chemical mixture.",
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
            "has_parts",
            "openminds.chemicals.AmountOfChemical",
            "vocab:hasPart",
            multiple=True,
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
            "type",
            "openminds.controlledterms.ChemicalMixtureType",
            "vocab:type",
            multiple=False,
            required=True,
            doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
        ),
    ]
    existence_query_fields = ("has_parts", "type")

    def __init__(
        self,
        name=None,
        additional_remarks=None,
        has_parts=None,
        product_source=None,
        type=None,
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
            name=name,
            additional_remarks=additional_remarks,
            has_parts=has_parts,
            product_source=product_source,
            type=type,
        )
