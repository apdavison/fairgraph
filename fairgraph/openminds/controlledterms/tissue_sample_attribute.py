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
from fairgraph import KGObject, IRI
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
    type_ = ["https://openminds.ebrains.eu/controlledTerms/TissueSampleAttribute"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the tissue sample attribute.",
        ),
        Field(
            "definition",
            str,
            "vocab:definition",
            doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the tissue sample attribute.",
        ),
        Field(
            "interlex_identifier",
            IRI,
            "vocab:interlexIdentifier",
            doc="Persistent identifier for a term registered in the InterLex project.",
        ),
        Field(
            "knowledge_space_link",
            IRI,
            "vocab:knowledgeSpaceLink",
            doc="Persistent link to an encyclopedia entry in the Knowledge Space project.",
        ),
        Field(
            "preferred_ontology_identifier",
            IRI,
            "vocab:preferredOntologyIdentifier",
            doc="Persistent identifier of a preferred ontological term.",
        ),
        Field(
            "synonyms",
            str,
            "vocab:synonym",
            multiple=True,
            doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
        ),
        Field(
            "describes",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.ModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.LivePaperVersion",
                "openminds.publications.ScholarlyArticle",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:keyword",
            reverse="keywords",
            multiple=True,
            doc="reverse of 'keyword'",
        ),
        Field(
            "is_attribute_of",
            ["openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"],
            "^vocab:attribute",
            reverse="attributes",
            multiple=True,
            doc="reverse of 'attribute'",
        ),
    ]
    existence_query_fields = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        synonyms=None,
        describes=None,
        is_attribute_of=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
            describes=describes,
            is_attribute_of=is_attribute_of,
        )
