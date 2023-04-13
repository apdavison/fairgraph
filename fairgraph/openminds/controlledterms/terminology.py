"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - modality
         -
       * - analysis technique
         -
       * - atlas type
         -
       * - operating system
         -
       * - biological order
         -
       * - `anatomical plane <http://purl.obolibrary.org/obo/UBERON_0035085>`_
         - A flat anatomical 2D surface that bisects an anatomical structure or an anatomical space.
       * - dataset type
         -
       * - criteria quality type
         -
       * - learning resource type
         - A 'learning resource type' groups persistent resources that explicitly entail learning activities or learning experiences in a certain format (e.g., in a physical or digital presentation).
       * - technique
         -
       * - colormap
         - A colormap is a lookup table specifying the colors to be used in rendering a palettized image, [adapted from [Wiktionary](https://en.wiktionary.org/wiki/colormap)].
       * - patch clamp variation
         - A variation of the patch clamp technique
       * - `age category <http://purl.obolibrary.org/obo/UBERON_0000105>`_
         - The age category describes a specific spatiotemporal part of the life cycle of an organism.
       * - contribution type
         -
       * - (meta)data model type
         -
       * - species
         -
       * - tissue sample attribute
         -
       * - handedness
         -
       * - operating device
         -
       * - type of uncertainty
         -

Here we show the first 20 values, an additional 62 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class Terminology(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - modality
         -
       * - analysis technique
         -
       * - atlas type
         -
       * - operating system
         -
       * - biological order
         -
       * - `anatomical plane <http://purl.obolibrary.org/obo/UBERON_0035085>`_
         - A flat anatomical 2D surface that bisects an anatomical structure or an anatomical space.
       * - dataset type
         -
       * - criteria quality type
         -
       * - learning resource type
         - A 'learning resource type' groups persistent resources that explicitly entail learning activities or learning experiences in a certain format (e.g., in a physical or digital presentation).
       * - technique
         -
       * - colormap
         - A colormap is a lookup table specifying the colors to be used in rendering a palettized image, [adapted from [Wiktionary](https://en.wiktionary.org/wiki/colormap)].
       * - patch clamp variation
         - A variation of the patch clamp technique
       * - `age category <http://purl.obolibrary.org/obo/UBERON_0000105>`_
         - The age category describes a specific spatiotemporal part of the life cycle of an organism.
       * - contribution type
         -
       * - (meta)data model type
         -
       * - species
         -
       * - tissue sample attribute
         -
       * - handedness
         -
       * - operating device
         -
       * - type of uncertainty
         -

Here we show the first 20 values, an additional 62 values are not shown.

    """
    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Terminology"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the terminology."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the terminology."),
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
        return super().__init__(id=id, space=space, scope=scope, data=data, name=name, definition=definition, description=description, interlex_identifier=interlex_identifier, knowledge_space_link=knowledge_space_link, preferred_ontology_identifier=preferred_ontology_identifier, synonyms=synonyms)