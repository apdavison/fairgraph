"""

    Here we show the first 20 possible values, an additional 35 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `neostriatum cholinergic interneuron <http://uri.neuinfo.org/nif/nifstd/sao1866881837>`_
         - An inhibitory interneuron in the caudate nucleus and putamen which mainly uses the neurotrasmitter acetylcholine (ACh).
       * - microglial cell
         - 'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.
       * - granule neuron
         - The term 'granule neuron' refers to a set of neuron types typically found in granular layers across brain regions whose only common feature is that they all have very small cell bodies [[adapted from Wikipedia](https://en.wikipedia.org/wiki/Granule_cell)].
       * - granule cell
         -
       * - neocortex layer 5 tufted pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body found in layer 5 of the neocortex and projects to subcortical areas.
       * - cholecystokinin expressing neuron
         - Any neuron that expresses cholecystokinin.
       * - macroglial cell
         - 'Macroglial cells' are large glial cells in the central nervous system.
       * - `striatum medium spiny neuron <http://uri.interlex.org/npo/uris/neurons/35>`_
         - A special type of GABAergic neuron with large dendritic trees that is located in the striatum.
       * - `cerebellum stellate neuron <http://uri.neuinfo.org/nif/nifstd/nifext_130>`_
         - Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.
       * - pyramidal cell
         -
       * - `cerebellum basket cell <http://uri.neuinfo.org/nif/nifstd/sao666951243>`_
         - An inhibitory GABAergic interneurons of the cerebellum, enmeshing the cell body of another neuron with its terminal axon ramifications.
       * - `cholinergic neuron <http://uri.neuinfo.org/nif/nifstd/nlx_148005>`_
         - Any neuron that releases some acetylcholine as a neurotransmitter
       * - `hippocampus CA1 pyramidal neuron <http://uri.neuinfo.org/nif/nifstd/sao830368389>`_
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
       * - `cerebellum granule cell <http://uri.neuinfo.org/nif/nifstd/nifext_128>`_
         - 'Cerebellum granule cells' form the thick granular layer of the cerebellar cortex and typically have small cell bodies but varying functions.
       * - nitric oxide synthase expressing neuron
         - Any neuron that expresses nitric oxide synthase.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class CellType(KGObject):
    """

    Here we show the first 20 possible values, an additional 35 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `neostriatum cholinergic interneuron <http://uri.neuinfo.org/nif/nifstd/sao1866881837>`_
         - An inhibitory interneuron in the caudate nucleus and putamen which mainly uses the neurotrasmitter acetylcholine (ACh).
       * - microglial cell
         - 'Microglial cells' are small, migratory, phagocytic, interstitial glial cells in the central nervous system.
       * - granule neuron
         - The term 'granule neuron' refers to a set of neuron types typically found in granular layers across brain regions whose only common feature is that they all have very small cell bodies [[adapted from Wikipedia](https://en.wikipedia.org/wiki/Granule_cell)].
       * - granule cell
         -
       * - neocortex layer 5 tufted pyramidal neuron
         - An excitatory neuron type with a pyramidal-shaped cell body found in layer 5 of the neocortex and projects to subcortical areas.
       * - cholecystokinin expressing neuron
         - Any neuron that expresses cholecystokinin.
       * - macroglial cell
         - 'Macroglial cells' are large glial cells in the central nervous system.
       * - `striatum medium spiny neuron <http://uri.interlex.org/npo/uris/neurons/35>`_
         - A special type of GABAergic neuron with large dendritic trees that is located in the striatum.
       * - `cerebellum stellate neuron <http://uri.neuinfo.org/nif/nifstd/nifext_130>`_
         - Any cerebellar neuron that has a star-like shape formed by dendritic processes radiating from the cell body.
       * - pyramidal cell
         -
       * - `cerebellum basket cell <http://uri.neuinfo.org/nif/nifstd/sao666951243>`_
         - An inhibitory GABAergic interneurons of the cerebellum, enmeshing the cell body of another neuron with its terminal axon ramifications.
       * - `cholinergic neuron <http://uri.neuinfo.org/nif/nifstd/nlx_148005>`_
         - Any neuron that releases some acetylcholine as a neurotransmitter
       * - `hippocampus CA1 pyramidal neuron <http://uri.neuinfo.org/nif/nifstd/sao830368389>`_
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
       * - `cerebellum granule cell <http://uri.neuinfo.org/nif/nifstd/nifext_128>`_
         - 'Cerebellum granule cells' form the thick granular layer of the cerebellar cortex and typically have small cell bodies but varying functions.
       * - nitric oxide synthase expressing neuron
         - Any neuron that expresses nitric oxide synthase.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/CellType"]
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
            doc="Word or phrase that constitutes the distinctive designation of the cell type.",
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
            doc="Longer statement or account giving the characteristics of the cell type.",
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
            "is_location_of",
            ["openminds.ephys.ElectrodeArrayUsage", "openminds.ephys.ElectrodeUsage", "openminds.ephys.PipetteUsage"],
            ["^vocab:anatomicalLocation", "^vocab:anatomicalLocationOfElectrodes"],
            reverse=["anatomical_locations", "anatomical_location_of_electrodes"],
            multiple=True,
            doc="reverse of anatomicalLocation, anatomicalLocationOfElectrodes",
        ),
        Field(
            "is_used_to_group",
            "openminds.core.FileBundle",
            "^vocab:groupedBy",
            reverse="grouped_by",
            multiple=True,
            doc="reverse of 'groupedBy'",
        ),
        Field(
            "samples",
            ["openminds.core.TissueSample", "openminds.core.TissueSampleCollection"],
            "^vocab:origin",
            reverse="origins",
            multiple=True,
            doc="reverse of 'origin'",
        ),
        Field(
            "studied_in",
            [
                "openminds.computation.DataAnalysis",
                "openminds.computation.DataCopy",
                "openminds.computation.GenericComputation",
                "openminds.computation.ModelValidation",
                "openminds.computation.Optimization",
                "openminds.computation.Simulation",
                "openminds.computation.ValidationTest",
                "openminds.computation.Visualization",
                "openminds.core.Model",
                "openminds.core.ProtocolExecution",
                "openminds.ephys.CellPatching",
                "openminds.ephys.ElectrodePlacement",
                "openminds.ephys.RecordingActivity",
                "openminds.specimenprep.CranialWindowPreparation",
                "openminds.specimenprep.TissueCulturePreparation",
                "openminds.specimenprep.TissueSampleSlicing",
                "openminds.stimulation.StimulationActivity",
            ],
            "^vocab:studyTarget",
            reverse="study_targets",
            multiple=True,
            doc="reverse of 'studyTarget'",
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
        is_location_of=None,
        is_used_to_group=None,
        samples=None,
        studied_in=None,
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
            is_location_of=is_location_of,
            is_used_to_group=is_used_to_group,
            samples=samples,
            studied_in=studied_in,
        )
