"""
Structured information on the category of the software application.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class SoftwareApplicationCategory(KGObject):
    """
    Structured information on the category of the software application.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/controlledTerms/SoftwareApplicationCategory"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the software application category."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        
    ]
    existence_query_fields = ('name',)