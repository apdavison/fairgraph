"""

    Here we show the first 20 possible values, an additional 62 values are not shown.

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

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Terminology(KGObject):
    """

    Here we show the first 20 possible values, an additional 62 values are not shown.

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

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Terminology"]
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
            doc="Word or phrase that constitutes the distinctive designation of the terminology.",
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
            doc="Longer statement or account giving the characteristics of the terminology.",
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
            "suggested_in",
            "openminds.controlledterms.TermSuggestion",
            "^vocab:addExistingTerminology",
            reverse="add_existing_terminologies",
            multiple=True,
            doc="reverse of 'addExistingTerminology'",
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
        suggested_in=None,
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
            suggested_in=suggested_in,
        )
