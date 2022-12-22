"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - chemogenetics
         - Any experimental approach focused on using genetically encoded chemically sensitive proteins in combination with a specific agonist delivered systemically in order to manipulate the behavior of populations of cells.
       * - epigenomics
         - Any experimental approach focused on processes that modulate transcription but that do not directly alter the primary sequences of an organism's DNA.
       * - cell population manipulation
         - Any experimental approach focused on manipulation of biochemical, molecular, or physiological characteristics of populations of cells.
       * - ecology
         - Any experimental approach focused on interrelationship of organisms and their environments, including causes and consequences.
       * - neuroimaging
         - Any experimental approach focused on the non-invasive direct or indirect imaging of the structure, function, or pharmacology of the nervous system.
       * - microscopy
         - Any experimental approach focused on using differential contrast of microscopic structures to form an image.
       * - optogenetics
         - Any experimental approach focused on using genetically encoded light-sensitive proteins in combination with targeted delivery of light in order to manipulate the behavior of populations of cells.
       * - electrophysiology
         - Any experimental approach focused on electrical phenomena associated with living systems, most notably the nervous system, cardiac system, and musculoskeletal system.
       * - histology
         - Any experimental approach focused on structure of biological tissue.
       * - pharmacology
         - 'Pharmacology' is an experimental approach in which the composition, properties, functions, sources, synthesis and design of drugs (any artificial, natural, or endogenous molecule) and their biochemical or physiological effect (normal or abnormal) on a cell, tissue, organ, or organism are studied. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Pharmacology)]
       * - proteomics
         - Any experimental approach focused on the composition, structure, and activity of an entire set of proteins in organisms or their parts.
       * - informatics
         - Any experimental approach focused on collection, classification, storage, retrieval, analysis, visualization, and dissemination of recorded knowledge in computational systems.
       * - multimodal research
         - Any experimental approach that employs multiple experimental approaches in significant ways.
       * - transcriptomics
         - Any experimental approach focused on the transcriptome (all RNA transcripts) of one or more cells, tissues, or organisms.
       * - physiology
         - Any experimental approach focused on normal functions of living organisms and their parts.
       * - cell population imaging
         - Any experimental approach focused on imaging biochemical, molecular, or physiological characteristics of populations of cells.
       * - omics
         - Any experimental approach focused on characterization and quantification of biological molecules that give rise to the structure, function, and dynamics of organisms or their parts.
       * - cell biology
         - Any experimental approach focused on structure, function, multiplication, pathology, and life history of biological cells.
       * - morphology
         - Any experimental approach focused on the shape and structure of living organisms or their parts.
       * - metabolomics
         - Any experimental approach focused on chemical processes involving metabolites, the small molecule substrates, intermediates and products of cell metabolism.

Here we show the first 20 values, an additional 19 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ExperimentalApproach(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - chemogenetics
         - Any experimental approach focused on using genetically encoded chemically sensitive proteins in combination with a specific agonist delivered systemically in order to manipulate the behavior of populations of cells.
       * - epigenomics
         - Any experimental approach focused on processes that modulate transcription but that do not directly alter the primary sequences of an organism's DNA.
       * - cell population manipulation
         - Any experimental approach focused on manipulation of biochemical, molecular, or physiological characteristics of populations of cells.
       * - ecology
         - Any experimental approach focused on interrelationship of organisms and their environments, including causes and consequences.
       * - neuroimaging
         - Any experimental approach focused on the non-invasive direct or indirect imaging of the structure, function, or pharmacology of the nervous system.
       * - microscopy
         - Any experimental approach focused on using differential contrast of microscopic structures to form an image.
       * - optogenetics
         - Any experimental approach focused on using genetically encoded light-sensitive proteins in combination with targeted delivery of light in order to manipulate the behavior of populations of cells.
       * - electrophysiology
         - Any experimental approach focused on electrical phenomena associated with living systems, most notably the nervous system, cardiac system, and musculoskeletal system.
       * - histology
         - Any experimental approach focused on structure of biological tissue.
       * - pharmacology
         - 'Pharmacology' is an experimental approach in which the composition, properties, functions, sources, synthesis and design of drugs (any artificial, natural, or endogenous molecule) and their biochemical or physiological effect (normal or abnormal) on a cell, tissue, organ, or organism are studied. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Pharmacology)]
       * - proteomics
         - Any experimental approach focused on the composition, structure, and activity of an entire set of proteins in organisms or their parts.
       * - informatics
         - Any experimental approach focused on collection, classification, storage, retrieval, analysis, visualization, and dissemination of recorded knowledge in computational systems.
       * - multimodal research
         - Any experimental approach that employs multiple experimental approaches in significant ways.
       * - transcriptomics
         - Any experimental approach focused on the transcriptome (all RNA transcripts) of one or more cells, tissues, or organisms.
       * - physiology
         - Any experimental approach focused on normal functions of living organisms and their parts.
       * - cell population imaging
         - Any experimental approach focused on imaging biochemical, molecular, or physiological characteristics of populations of cells.
       * - omics
         - Any experimental approach focused on characterization and quantification of biological molecules that give rise to the structure, function, and dynamics of organisms or their parts.
       * - cell biology
         - Any experimental approach focused on structure, function, multiplication, pathology, and life history of biological cells.
       * - morphology
         - Any experimental approach focused on the shape and structure of living organisms or their parts.
       * - metabolomics
         - Any experimental approach focused on chemical processes involving metabolites, the small molecule substrates, intermediates and products of cell metabolism.

Here we show the first 20 values, an additional 19 values are not shown.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/ExperimentalApproach"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the experimental approach."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the experimental approach."),
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
