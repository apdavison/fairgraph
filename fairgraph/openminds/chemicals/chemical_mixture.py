"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ChemicalMixture(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/chemicals/ChemicalMixture"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the chemical mixture."),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("components", "openminds.chemicals.AmountOfChemical", "vocab:components", multiple=True, required=True,
              doc="no description available"),
        Field("product_source", "openminds.chemicals.ProductSource", "vocab:productSource", multiple=False, required=False,
              doc="no description available"),
        Field("type", "openminds.controlledterms.ChemicalMixtureType", "vocab:type", multiple=False, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]
    existence_query_fields = ('components', 'type')
