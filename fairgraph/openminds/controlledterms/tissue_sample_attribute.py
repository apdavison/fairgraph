"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - stained
         - A specimen that has been dyed using chemical or biochemical substances for general colorization of e.g., molecules or subcellular components, that can be visualized under the right light exposure.
       * - labeled
         - A specimen that has been modified using chemical or biochemical substances for selective tagging of e.g., molecules or subcellular components, which does not necessarily leads to a visual observable colorization.
       * - unstained
         - A specimen that was not artificially modified in colorization using chemical or biochemical substances.
       * - untreated
         - A specimen that has not been modified or treated (e.g., with chemicals) compared to its natural state.
       * - fixated
         - A specimen that was treated with a fixative (e.g., paraformaldehyde) to preserve its existing form and structure.
       * - free floating
         - A specimen that has been suspended in solution for further handling or experimental steps (e.g., immunohistochemical staining), or temporary storage before further use.
       * - mounted
         - A specimen that has been put ('mounted') on e.g., a glass slide with mounting medium in order to be supported for further handling and/or long term preservation.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class TissueSampleAttribute(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - stained
         - A specimen that has been dyed using chemical or biochemical substances for general colorization of e.g., molecules or subcellular components, that can be visualized under the right light exposure.
       * - labeled
         - A specimen that has been modified using chemical or biochemical substances for selective tagging of e.g., molecules or subcellular components, which does not necessarily leads to a visual observable colorization.
       * - unstained
         - A specimen that was not artificially modified in colorization using chemical or biochemical substances.
       * - untreated
         - A specimen that has not been modified or treated (e.g., with chemicals) compared to its natural state.
       * - fixated
         - A specimen that was treated with a fixative (e.g., paraformaldehyde) to preserve its existing form and structure.
       * - free floating
         - A specimen that has been suspended in solution for further handling or experimental steps (e.g., immunohistochemical staining), or temporary storage before further use.
       * - mounted
         - A specimen that has been put ('mounted') on e.g., a glass slide with mounting medium in order to be supported for further handling and/or long term preservation.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/TissueSampleAttribute"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the tissue sample attribute."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the tissue sample attribute."),
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
