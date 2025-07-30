"""
Structured information about the source of a chemical substance or mixture.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.chemicals import ProductSource
from fairgraph import KGObject


class ProductSource(KGObject, ProductSource):
    """
    Structured information about the source of a chemical substance or mixture.
    """

    type_ = "https://openminds.ebrains.eu/chemicals/ProductSource"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_source_of",
            ["openminds.latest.chemicals.ChemicalMixture", "openminds.latest.chemicals.ChemicalSubstance"],
            "productSource",
            reverse="product_source",
            multiple=True,
            description="reverse of 'product_source'",
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
        return KGObject.__init__(
            self,
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
