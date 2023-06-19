"""

    Here we show the first 20 possible values, an additional 19 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - chemogenetics
         - Any experimental approach focused on using genetically encoded chemically sensitive proteins in combination with a specific agonist delivered systemically in order to manipulate the behavior of populations of cells.
       * - `epigenomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Epigenomics>`_
         - Any experimental approach focused on processes that modulate transcription but that do not directly alter the primary sequences of an organism's DNA.
       * - `cell population manipulation <http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationManipulation>`_
         - Any experimental approach focused on manipulation of biochemical, molecular, or physiological characteristics of populations of cells.
       * - `ecology <http://uri.interlex.org/tgbugs/uris/readable/modality/Ecology>`_
         - Any experimental approach focused on interrelationship of organisms and their environments, including causes and consequences.
       * - `neuroimaging <http://uri.interlex.org/tgbugs/uris/readable/modality/Neuroimaging>`_
         - Any experimental approach focused on the non-invasive direct or indirect imaging of the structure, function, or pharmacology of the nervous system.
       * - `microscopy <http://uri.interlex.org/tgbugs/uris/readable/modality/Microscopy>`_
         - Any experimental approach focused on using differential contrast of microscopic structures to form an image.
       * - optogenetics
         - Any experimental approach focused on using genetically encoded light-sensitive proteins in combination with targeted delivery of light in order to manipulate the behavior of populations of cells.
       * - `electrophysiology <http://uri.interlex.org/tgbugs/uris/readable/modality/Electrophysiology>`_
         - Any experimental approach focused on electrical phenomena associated with living systems, most notably the nervous system, cardiac system, and musculoskeletal system.
       * - `histology <http://uri.interlex.org/tgbugs/uris/readable/modality/Histology>`_
         - Any experimental approach focused on structure of biological tissue.
       * - `pharmacology <http://edamontology.org/topic_0202>`_
         - 'Pharmacology' is an experimental approach in which the composition, properties, functions, sources, synthesis and design of drugs (any artificial, natural, or endogenous molecule) and their biochemical or physiological effect (normal or abnormal) on a cell, tissue, organ, or organism are studied. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Pharmacology)]
       * - `proteomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Proteomics>`_
         - Any experimental approach focused on the composition, structure, and activity of an entire set of proteins in organisms or their parts.
       * - informatics
         - Any experimental approach focused on collection, classification, storage, retrieval, analysis, visualization, and dissemination of recorded knowledge in computational systems.
       * - `multimodal research <http://uri.interlex.org/tgbugs/uris/readable/modality/Multimodal>`_
         - Any experimental approach that employs multiple experimental approaches in significant ways.
       * - `transcriptomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Transcriptomics>`_
         - Any experimental approach focused on the transcriptome (all RNA transcripts) of one or more cells, tissues, or organisms.
       * - `physiology <http://uri.interlex.org/tgbugs/uris/readable/modality/Physiology>`_
         - Any experimental approach focused on normal functions of living organisms and their parts.
       * - `cell population imaging <http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationImaging>`_
         - Any experimental approach focused on imaging biochemical, molecular, or physiological characteristics of populations of cells.
       * - `omics <http://uri.interlex.org/tgbugs/uris/readable/modality/Omics>`_
         - Any experimental approach focused on characterization and quantification of biological molecules that give rise to the structure, function, and dynamics of organisms or their parts.
       * - `cell biology <http://uri.interlex.org/tgbugs/uris/readable/modality/Cellular>`_
         - Any experimental approach focused on structure, function, multiplication, pathology, and life history of biological cells.
       * - `morphology <http://uri.interlex.org/tgbugs/uris/readable/modality/Morphology>`_
         - Any experimental approach focused on the shape and structure of living organisms or their parts.
       * - `metabolomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Metabolomics>`_
         - Any experimental approach focused on chemical processes involving metabolites, the small molecule substrates, intermediates and products of cell metabolism.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ExperimentalApproach(KGObject):
    """

    Here we show the first 20 possible values, an additional 19 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - chemogenetics
         - Any experimental approach focused on using genetically encoded chemically sensitive proteins in combination with a specific agonist delivered systemically in order to manipulate the behavior of populations of cells.
       * - `epigenomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Epigenomics>`_
         - Any experimental approach focused on processes that modulate transcription but that do not directly alter the primary sequences of an organism's DNA.
       * - `cell population manipulation <http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationManipulation>`_
         - Any experimental approach focused on manipulation of biochemical, molecular, or physiological characteristics of populations of cells.
       * - `ecology <http://uri.interlex.org/tgbugs/uris/readable/modality/Ecology>`_
         - Any experimental approach focused on interrelationship of organisms and their environments, including causes and consequences.
       * - `neuroimaging <http://uri.interlex.org/tgbugs/uris/readable/modality/Neuroimaging>`_
         - Any experimental approach focused on the non-invasive direct or indirect imaging of the structure, function, or pharmacology of the nervous system.
       * - `microscopy <http://uri.interlex.org/tgbugs/uris/readable/modality/Microscopy>`_
         - Any experimental approach focused on using differential contrast of microscopic structures to form an image.
       * - optogenetics
         - Any experimental approach focused on using genetically encoded light-sensitive proteins in combination with targeted delivery of light in order to manipulate the behavior of populations of cells.
       * - `electrophysiology <http://uri.interlex.org/tgbugs/uris/readable/modality/Electrophysiology>`_
         - Any experimental approach focused on electrical phenomena associated with living systems, most notably the nervous system, cardiac system, and musculoskeletal system.
       * - `histology <http://uri.interlex.org/tgbugs/uris/readable/modality/Histology>`_
         - Any experimental approach focused on structure of biological tissue.
       * - `pharmacology <http://edamontology.org/topic_0202>`_
         - 'Pharmacology' is an experimental approach in which the composition, properties, functions, sources, synthesis and design of drugs (any artificial, natural, or endogenous molecule) and their biochemical or physiological effect (normal or abnormal) on a cell, tissue, organ, or organism are studied. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Pharmacology)]
       * - `proteomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Proteomics>`_
         - Any experimental approach focused on the composition, structure, and activity of an entire set of proteins in organisms or their parts.
       * - informatics
         - Any experimental approach focused on collection, classification, storage, retrieval, analysis, visualization, and dissemination of recorded knowledge in computational systems.
       * - `multimodal research <http://uri.interlex.org/tgbugs/uris/readable/modality/Multimodal>`_
         - Any experimental approach that employs multiple experimental approaches in significant ways.
       * - `transcriptomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Transcriptomics>`_
         - Any experimental approach focused on the transcriptome (all RNA transcripts) of one or more cells, tissues, or organisms.
       * - `physiology <http://uri.interlex.org/tgbugs/uris/readable/modality/Physiology>`_
         - Any experimental approach focused on normal functions of living organisms and their parts.
       * - `cell population imaging <http://uri.interlex.org/tgbugs/uris/readable/modality/CellPopulationImaging>`_
         - Any experimental approach focused on imaging biochemical, molecular, or physiological characteristics of populations of cells.
       * - `omics <http://uri.interlex.org/tgbugs/uris/readable/modality/Omics>`_
         - Any experimental approach focused on characterization and quantification of biological molecules that give rise to the structure, function, and dynamics of organisms or their parts.
       * - `cell biology <http://uri.interlex.org/tgbugs/uris/readable/modality/Cellular>`_
         - Any experimental approach focused on structure, function, multiplication, pathology, and life history of biological cells.
       * - `morphology <http://uri.interlex.org/tgbugs/uris/readable/modality/Morphology>`_
         - Any experimental approach focused on the shape and structure of living organisms or their parts.
       * - `metabolomics <http://uri.interlex.org/tgbugs/uris/readable/modality/Metabolomics>`_
         - Any experimental approach focused on chemical processes involving metabolites, the small molecule substrates, intermediates and products of cell metabolism.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/ExperimentalApproach"]
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
            doc="Word or phrase that constitutes the distinctive designation of the experimental approach.",
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
            doc="Longer statement or account giving the characteristics of the experimental approach.",
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
        )
