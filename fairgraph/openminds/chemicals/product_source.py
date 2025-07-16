"""
Structured information about the source of a chemical substance or mixture.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ProductSource(KGObject):
    """
    Structured information about the source of a chemical substance or mixture.
    """

    default_space = "in-depth"
    type_ = "https://openminds.ebrains.eu/chemicals/ProductSource"
    properties = [
        Property(
            "digital_identifier",
            "openminds.core.RRID",
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property("identifier", str, "vocab:identifier", doc="Term or code used to identify the product source."),
        Property("product_name", str, "vocab:productName", required=True, doc="no description available"),
        Property(
            "provider",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:provider",
            required=True,
            doc="no description available",
        ),
        Property(
            "purity",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:purity",
            doc="no description available",
        ),
    ]
    reverse_properties = [
        Property(
            "is_source_of",
            ["openminds.chemicals.ChemicalMixture", "openminds.chemicals.ChemicalSubstance"],
            "^vocab:productSource",
            reverse="product_source",
            multiple=True,
            doc="reverse of 'product_source'",
        ),
    ]
    existence_query_properties = ("product_name", "provider")

    def __init__(
        self,
        digital_identifier=None,
        identifier=None,
        is_source_of=None,
        product_name=None,
        provider=None,
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
            digital_identifier=digital_identifier,
            identifier=identifier,
            is_source_of=is_source_of,
            product_name=product_name,
            provider=provider,
            purity=purity,
        )
