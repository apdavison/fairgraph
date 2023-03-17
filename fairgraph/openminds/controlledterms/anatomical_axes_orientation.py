"""
Structured information on the anatomical directions of the X, Y, and Z axis.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - RSA
         - X, Y, Z axes are oriented towards right, superior and anterior, respectively.
       * - SAL
         - X, Y, Z axes are oriented towards superior, anterior and left, respectively.
       * - RIP
         - X, Y, Z axes are oriented towards right, inferior and posterior, respectively.
       * - SRA
         - X, Y, Z axes are oriented towards superior, right and anterior, respectively.
       * - ALI
         - X, Y, Z axes are oriented towards anterior, left and inferior, respectively.
       * - ILA
         - X, Y, Z axes are oriented towards inferior, left and anterior, respectively.
       * - SAR
         - X, Y, Z axes are oriented towards superior, anterior and right, respectively.
       * - ILP
         - X, Y, Z axes are oriented towards inferior, left and posterior, respectively.
       * - RSP
         - X, Y, Z axes are oriented towards right, superior and posterior, respectively.
       * - ASR
         - X, Y, Z axes are oriented towards anterior, superior and right, respectively.
       * - IPR
         - X, Y, Z axes are oriented towards inferior, posterior and right, respectively.
       * - IPL
         - X, Y, Z axes are oriented towards inferior, posterior and left, respectively.
       * - RPS
         - X, Y, Z axes are oriented towards right, posterior and superior, respectively.
       * - SPL
         - X, Y, Z axes are oriented towards superior, posterior and left, respectively.
       * - SPR
         - X, Y, Z axes are oriented towards superior, posterior and right, respectively.
       * - AIL
         - X, Y, Z axes are oriented towards anterior, inferior and left, respectively.
       * - LIA
         - X, Y, Z axes are oriented towards left, inferior and anterior, respectively.
       * - RAS
         - X, Y, Z axes are oriented towards right, anterior and superior, respectively.
       * - IAR
         - X, Y, Z axes are oriented towards inferior, anterior and right, respectively.
       * - PSL
         - X, Y, Z axes are oriented towards posterior, superior and left, respectively.

Here we show the first 20 values, an additional 28 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class AnatomicalAxesOrientation(KGObject):
    """
    Structured information on the anatomical directions of the X, Y, and Z axis.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - RSA
         - X, Y, Z axes are oriented towards right, superior and anterior, respectively.
       * - SAL
         - X, Y, Z axes are oriented towards superior, anterior and left, respectively.
       * - RIP
         - X, Y, Z axes are oriented towards right, inferior and posterior, respectively.
       * - SRA
         - X, Y, Z axes are oriented towards superior, right and anterior, respectively.
       * - ALI
         - X, Y, Z axes are oriented towards anterior, left and inferior, respectively.
       * - ILA
         - X, Y, Z axes are oriented towards inferior, left and anterior, respectively.
       * - SAR
         - X, Y, Z axes are oriented towards superior, anterior and right, respectively.
       * - ILP
         - X, Y, Z axes are oriented towards inferior, left and posterior, respectively.
       * - RSP
         - X, Y, Z axes are oriented towards right, superior and posterior, respectively.
       * - ASR
         - X, Y, Z axes are oriented towards anterior, superior and right, respectively.
       * - IPR
         - X, Y, Z axes are oriented towards inferior, posterior and right, respectively.
       * - IPL
         - X, Y, Z axes are oriented towards inferior, posterior and left, respectively.
       * - RPS
         - X, Y, Z axes are oriented towards right, posterior and superior, respectively.
       * - SPL
         - X, Y, Z axes are oriented towards superior, posterior and left, respectively.
       * - SPR
         - X, Y, Z axes are oriented towards superior, posterior and right, respectively.
       * - AIL
         - X, Y, Z axes are oriented towards anterior, inferior and left, respectively.
       * - LIA
         - X, Y, Z axes are oriented towards left, inferior and anterior, respectively.
       * - RAS
         - X, Y, Z axes are oriented towards right, anterior and superior, respectively.
       * - IAR
         - X, Y, Z axes are oriented towards inferior, anterior and right, respectively.
       * - PSL
         - X, Y, Z axes are oriented towards posterior, superior and left, respectively.

Here we show the first 20 values, an additional 28 values are not shown.

    """
    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/AnatomicalAxesOrientation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the anatomical axes orientation."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the anatomical axes orientation."),
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

    def __init__(self, name=None, definition=None, description=None, interlex_identifier=None, knowledge_space_link=None, preferred_ontology_identifier=None, synonyms=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, definition=definition, description=description, interlex_identifier=interlex_identifier, knowledge_space_link=knowledge_space_link, preferred_ontology_identifier=preferred_ontology_identifier, synonyms=synonyms)