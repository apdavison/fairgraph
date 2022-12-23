"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - cleared skull cranial window
         - A cranial window that is constructed by clearing a small region of the skull.
       * - transcranial window
         - A cranial window that is constructed by removal of a small region of the skull.
       * - thinned skull cranial window
         - A cranial window that is constructed by thinning a small region of the skull.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class CranialWindowConstructionType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - cleared skull cranial window
         - A cranial window that is constructed by clearing a small region of the skull.
       * - transcranial window
         - A cranial window that is constructed by removal of a small region of the skull.
       * - thinned skull cranial window
         - A cranial window that is constructed by thinning a small region of the skull.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/CranialWindowConstructionType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the cranial window construction type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the cranial window construction type."),
        Field("interlex_identifier", IRI, "vocab:interlexIdentifier", multiple=False, required=False,
              doc="Persistent identifier for a term registered in the InterLex project."),
        Field("knowledge_space_link", IRI, "vocab:knowledgeSpaceLink", multiple=False, required=False,
              doc="Persistent link to an encyclopedia entry in the Knowledge Space project."),
        Field("preferred_ontology_identifier", IRI, "vocab:preferredOntologyIdentifier", multiple=False, required=False,
              doc="Persistent identifier of a preferred ontological term."),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name',)
