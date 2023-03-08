"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `cardiovascular system <http://purl.obolibrary.org/obo/UBERON_0004535>`_
         - 'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.
       * - `central nervous system <http://purl.obolibrary.org/obo/UBERON_0001017>`_
         - The 'central nervous system' is the main processing center in most organisms. Its function is to take in sensory information, process information, and send out motor signals.
       * - `musculoskeletal system <http://purl.obolibrary.org/obo/UBERON_0002204>`_
         - The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.
       * - `digestive system <http://purl.obolibrary.org/obo/UBERON_0001007>`_
         - The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.
       * - `vascular system <http://purl.obolibrary.org/obo/UBERON_0007798>`_
         - The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class OrganismSystem(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `cardiovascular system <http://purl.obolibrary.org/obo/UBERON_0004535>`_
         - 'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.
       * - `central nervous system <http://purl.obolibrary.org/obo/UBERON_0001017>`_
         - The 'central nervous system' is the main processing center in most organisms. Its function is to take in sensory information, process information, and send out motor signals.
       * - `musculoskeletal system <http://purl.obolibrary.org/obo/UBERON_0002204>`_
         - The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.
       * - `digestive system <http://purl.obolibrary.org/obo/UBERON_0001007>`_
         - The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.
       * - `vascular system <http://purl.obolibrary.org/obo/UBERON_0007798>`_
         - The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/OrganismSystem"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the organism system."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the organism system."),
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
