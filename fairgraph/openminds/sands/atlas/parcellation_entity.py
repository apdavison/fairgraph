"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class ParcellationEntity(KGObjectV3):
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
        Field("has_parents", "openminds.sands.ParcellationEntity", "vocab:hasParent", multiple=True, required=False,
              doc="Reference to a parent object or legal person."),
        Field("versions", "openminds.sands.ParcellationEntityVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the parcellation entity."),
        Field("ontology_identifier", IRI, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the parcellation entity registered within a particular ontology."),
        Field("related_uberon_term", "openminds.controlledterms.UBERONParcellation", "vocab:relatedUBERONTerm", multiple=False, required=False,
              doc="no description available"),
        
    ]
    existence_query_fields = ('name',)

