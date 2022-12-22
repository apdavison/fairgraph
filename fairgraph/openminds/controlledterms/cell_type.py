"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - neostriatum cholinergic interneuron
         - An inhibitory interneuron in the caudate nucleus and putamen which mainly uses the neurotrasmitter acetylcholine (ACh).
       * - microglial cell
         - 'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.
       * - granule cell
         -
       * - neocortex layer 5 tufted pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body found in layer 5 of the neocortex and projects to subcortical areas.
       * - cholecystokinin expressing neuron
         - Any neuron that expresses cholecystokinin.
       * - macroglial cell
         - 'Macroglial cells' are large glial cells in the central nervous system.
       * - striatum medium spiny neuron
         - A special type of GABAergic neuron with large dendritic trees that is located in the striatum.
       * - cerebellum stellate neuron
         - Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.
       * - pyramidal cell
         -
       * - cerebellum basket cell
         - An inhibitory GABAergic interneurons of the cerebellum, enmeshing the cell body of another neuron with its terminal axon ramifications.
       * - cholinergic neuron
         - Any neuron that releases some acetylcholine as a neurotransmitter
       * - hippocampus CA1 pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body that is located in the cornu ammonis 1 (CA1) of the hippocampus.
       * - interneuron
         - An 'interneuron' is neuron that cannot be classified as sensory receptor or motor neuron.
       * - motor neuron
         -
       * - inhibitory neuron
         - An 'inhibitory neuron' releases neurotransmitters (e.g. GABA) that have a hyperpolarizing effect on the post-synaptic neuron, making it difficult to generate an action potential.
       * - choline acetyltransferase expressing neuron
         - Any neuron that expresses choline acetyltransferase.
       * - glial cell
         - A 'glial cell' is a non-neuronal cell of the nervous system. Glial cells provide physical support, respond to injury, regulate the ionic and chemical composition of the extracellular milieu, guide neuronal migration during development, and exchange metabolites with neurons.
       * - cerebellum granule cell
         - 'Cerebellum granule cells' form the thick granular layer of the cerebellar cortex and typically have small cell bodies but varying functions.
       * - nitric oxide synthase expressing neuron
         - Any neuron that expresses nitric oxide synthase.
       * - somatostatin expressing neuron
         - Any neuron that expresses somatostatin.

Here we show the first 20 values, an additional 34 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class CellType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - neostriatum cholinergic interneuron
         - An inhibitory interneuron in the caudate nucleus and putamen which mainly uses the neurotrasmitter acetylcholine (ACh).
       * - microglial cell
         - 'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.
       * - granule cell
         -
       * - neocortex layer 5 tufted pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body found in layer 5 of the neocortex and projects to subcortical areas.
       * - cholecystokinin expressing neuron
         - Any neuron that expresses cholecystokinin.
       * - macroglial cell
         - 'Macroglial cells' are large glial cells in the central nervous system.
       * - striatum medium spiny neuron
         - A special type of GABAergic neuron with large dendritic trees that is located in the striatum.
       * - cerebellum stellate neuron
         - Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.
       * - pyramidal cell
         -
       * - cerebellum basket cell
         - An inhibitory GABAergic interneurons of the cerebellum, enmeshing the cell body of another neuron with its terminal axon ramifications.
       * - cholinergic neuron
         - Any neuron that releases some acetylcholine as a neurotransmitter
       * - hippocampus CA1 pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body that is located in the cornu ammonis 1 (CA1) of the hippocampus.
       * - interneuron
         - An 'interneuron' is neuron that cannot be classified as sensory receptor or motor neuron.
       * - motor neuron
         -
       * - inhibitory neuron
         - An 'inhibitory neuron' releases neurotransmitters (e.g. GABA) that have a hyperpolarizing effect on the post-synaptic neuron, making it difficult to generate an action potential.
       * - choline acetyltransferase expressing neuron
         - Any neuron that expresses choline acetyltransferase.
       * - glial cell
         - A 'glial cell' is a non-neuronal cell of the nervous system. Glial cells provide physical support, respond to injury, regulate the ionic and chemical composition of the extracellular milieu, guide neuronal migration during development, and exchange metabolites with neurons.
       * - cerebellum granule cell
         - 'Cerebellum granule cells' form the thick granular layer of the cerebellar cortex and typically have small cell bodies but varying functions.
       * - nitric oxide synthase expressing neuron
         - Any neuron that expresses nitric oxide synthase.
       * - somatostatin expressing neuron
         - Any neuron that expresses somatostatin.

Here we show the first 20 values, an additional 34 values are not shown.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/CellType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the cell type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the cell type."),
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
