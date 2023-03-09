"""
Structured information about the amount of a given chemical that was used.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class AmountOfChemical(KGObject):
    """
    Structured information about the amount of a given chemical that was used.
    """
    default_space = "in-depth"
    type = ["https://openminds.ebrains.eu/chemicals/AmountOfChemical"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("amount", "openminds.core.QuantitativeValue", "vocab:amount", multiple=False, required=False,
              doc="no description available"),
        Field("chemical_product", ["openminds.chemicals.ChemicalMixture", "openminds.chemicals.ChemicalSubstance", "openminds.controlledterms.MolecularEntity"], "vocab:chemicalProduct", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('chemical_product',)
