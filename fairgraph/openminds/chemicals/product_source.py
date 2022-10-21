"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ProductSource(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/chemicals/ProductSource"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("digital_identifier", "openminds.core.RRID", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("identifier", str, "vocab:identifier", multiple=False, required=False,
              doc="Term or code used to identify the product source."),
        Field("product_name", str, "vocab:productName", multiple=False, required=True,
              doc="no description available"),
        Field("provider", ["openminds.core.Organization", "openminds.core.Person"], "vocab:provider", multiple=False, required=True,
              doc="no description available"),
        Field("purity", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:purity", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('product_name', 'provider')
