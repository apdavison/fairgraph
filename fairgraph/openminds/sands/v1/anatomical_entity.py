"""
Structured information on an anatomical entity.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class AnatomicalEntity(KGObject):
    """
    Structured information on an anatomical entity.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/AnatomicalEntity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("has_parent", "openminds.sands.AnatomicalEntity", "vocab:hasParent", multiple=False, required=False,
              doc="Reference to a parent object or legal person."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        Field("other_anatomical_relations", "openminds.sands.AnatomicalEntityRelation", "vocab:otherAnatomicalRelation", multiple=True, required=False,
              doc="Reference to a related anatomical structure."),
        
    ]
    existence_query_fields = ('name',)