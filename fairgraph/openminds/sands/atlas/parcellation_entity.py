"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ParcellationEntity(KGObject):
    """

    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/ParcellationEntity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the parcellation entity."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("alternative_names", str, "vocab:alternativeName", multiple=True, required=False,
              doc="no description available"),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("has_parents", "openminds.sands.ParcellationEntity", "vocab:hasParent", multiple=True, required=False,
              doc="Reference to a parent object or legal person."),
        Field("versions", "openminds.sands.ParcellationEntityVersion", "vocab:hasVersion", multiple=True, required=False,
              doc="Reference to variants of an original."),
        Field("ontology_identifiers", str, "vocab:ontologyIdentifier", multiple=True, required=False,
              doc="Term or code used to identify the parcellation entity registered within a particular ontology."),
        Field("related_uberon_term", "openminds.controlledterms.UBERONParcellation", "vocab:relatedUBERONTerm", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('name',)
