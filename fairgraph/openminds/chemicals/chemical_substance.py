"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ChemicalSubstance(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/chemicals/ChemicalSubstance"]
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
        Field("molecular_entity", "openminds.controlledterms.MolecularEntity", "vocab:molecularEntity", multiple=False, required=True,
              doc="no description available"),
        Field("product_source", "openminds.chemicals.ProductSource", "vocab:productSource", multiple=False, required=False,
              doc="no description available"),
        Field("purity", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:purity", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
