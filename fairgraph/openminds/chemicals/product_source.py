"""
Structured information about the source of a chemical substance or mixture.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.chemicals import ProductSource as OMProductSource
from fairgraph import KGObject


class ProductSource(KGObject, OMProductSource):
    """
    Structured information about the source of a chemical substance or mixture.
    """

    type_ = "https://openminds.om-i.org/types/ProductSource"
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


# cast openMINDS instances to their fairgraph subclass
ProductSource.set_error_handling(None)
for key, value in OMProductSource.__dict__.items():
    if isinstance(value, OMProductSource):
        fg_instance = ProductSource.from_jsonld(value.to_jsonld())
        fg_instance._space = ProductSource.default_space
        setattr(ProductSource, key, fg_instance)
ProductSource.set_error_handling("log")
