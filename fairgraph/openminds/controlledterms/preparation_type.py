"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `in utero <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90>`_
         - Something happening in, within, or while inside the uterus.
       * - `in vivo <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89>`_
         - Something happening or existing inside a living body.
       * - `ex vivo <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88>`_
         - Something happening or existing outside a living body.
       * - `in vitro <http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro>`_
         - Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).
       * - `in silico <http://id.nlm.nih.gov/mesh/2018/M0572590>`_
         - Conducted or produced by means of computer modelling or simulation.
       * - `in situ <http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu>`_
         - Something happening or being examined in the original place instead of being moved to another place

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class PreparationType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `in utero <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/90>`_
         - Something happening in, within, or while inside the uterus.
       * - `in vivo <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/89>`_
         - Something happening or existing inside a living body.
       * - `ex vivo <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/88>`_
         - Something happening or existing outside a living body.
       * - `in vitro <http://uri.interlex.org/tgbugs/uris/readable/technique/inVitro>`_
         - Something happening outside the body in artificial conditions (e.g., in a test tube or culture dish).
       * - `in silico <http://id.nlm.nih.gov/mesh/2018/M0572590>`_
         - Conducted or produced by means of computer modelling or simulation.
       * - `in situ <http://uri.interlex.org/tgbugs/uris/readable/technique/inSitu>`_
         - Something happening or being examined in the original place instead of being moved to another place

    """
    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/PreparationType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the preparation type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the preparation type."),
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