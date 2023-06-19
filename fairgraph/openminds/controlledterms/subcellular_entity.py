"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - neurite
         - A 'neurite' is a small neuronal process on developing neurons that ultimately grow out into axons or dendrites under the control of growth stimulating or inhibiting factors from their direct extracellular environment.
       * - symmetric synapse
         - A 'symmetric synapse' has flattened or elongated vesicles, and does not contain a prominent postsynaptic density. Symmetric synapses are typically inhibitory.
       * - `nerve fiber <http://purl.obolibrary.org/obo/UBERON_0006134>`_
         - A threadlike extension of a nerve cell within the nervous system which consists of an axon and, if myelinated, a myelin sheath.
       * - `synaptic vesicle <http://uri.neuinfo.org/nif/nifstd/sao1071221672>`_
         - A 'synaptic vesicle' is a secretory organelle (~ 50 nm in diameter) released from the pre-synaptic nerve terminal. It accumulates high concentrations of neurotransmitters and secretes these into the synaptic cleft by fusion with the 'active zone' of the pre-synaptic plasma membrane (modified from Gene Ontology).
       * - `axon terminal <http://uri.neuinfo.org/nif/nifstd/sao2007137787>`_
         - The distal terminations of axons which are specialized for the release of neurotransmitters.
       * - `nucleus <http://uri.neuinfo.org/nif/nifstd/sao1702920020>`_
         - A 'nucleus' is a membrane-bounded organelle of eukaryotic cells that contains the chromosomes. It is the primary site of DNA replication and RNA synthesis in the cell (Gene Ontology)
       * - `neurofilament <http://uri.neuinfo.org/nif/nifstd/sao1316272517>`_
         - A 'neurofilament' is a type of intermediate filament found in the core of neuronal axons. Neurofilaments are responsible for the radial growth of an axon and determine axonal diameter.
       * - `synaptic protein <http://uri.neuinfo.org/nif/nifstd/sao936599761>`_
         - A 'synaptic protein' belongs to a family of neuron-specific phosphoric proteins associated with synaptic vesicles. Synaptic proteins are present on the surface of almost all synaptic particles and bind to the cytoskeleton.
       * - asymmetric synapse
         - An 'asymmetric synapse' is characterized by rounded vesicles in the presynaptic cell and a prominent postsynaptic density. Asymmetric synapses are typically excitatory.
       * - `synaptic bouton <http://uri.neuinfo.org/nif/nifstd/sao187426937>`_
         - A 'synaptic bouton' is a terminal pre-synaptic ending of an axon or axon collateral.
       * - `dendritic spine <http://uri.neuinfo.org/nif/nifstd/sao1799103720>`_
         - A 'dendritic spine' is a protrusion from a dendrite. Spines are specialised subcellular compartments involved in the synaptic transmission.
       * - `dendrite <http://uri.neuinfo.org/nif/nifstd/sao1211023249>`_
         - A 'dendrite' is a branching protoplasmic process of a neuron that receives and integrates signals coming from axons of other neurons, and conveys the resulting signal to the body of the cell (Gene Ontology).
       * - `mitochondrion <http://uri.neuinfo.org/nif/nifstd/sao1860313010>`_
         - A 'mitochondrion' is a semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration (Gene Ontology).
       * - `axon <http://uri.neuinfo.org/nif/nifstd/sao1770195789>`_
         - An 'axon' is the long process of a neuron that conducts nerve impulses, usually away from the cell body to the terminals which are the site of storage and release of neurotransmitter (Gene Ontology).

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class SubcellularEntity(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - neurite
         - A 'neurite' is a small neuronal process on developing neurons that ultimately grow out into axons or dendrites under the control of growth stimulating or inhibiting factors from their direct extracellular environment.
       * - symmetric synapse
         - A 'symmetric synapse' has flattened or elongated vesicles, and does not contain a prominent postsynaptic density. Symmetric synapses are typically inhibitory.
       * - `nerve fiber <http://purl.obolibrary.org/obo/UBERON_0006134>`_
         - A threadlike extension of a nerve cell within the nervous system which consists of an axon and, if myelinated, a myelin sheath.
       * - `synaptic vesicle <http://uri.neuinfo.org/nif/nifstd/sao1071221672>`_
         - A 'synaptic vesicle' is a secretory organelle (~ 50 nm in diameter) released from the pre-synaptic nerve terminal. It accumulates high concentrations of neurotransmitters and secretes these into the synaptic cleft by fusion with the 'active zone' of the pre-synaptic plasma membrane (modified from Gene Ontology).
       * - `axon terminal <http://uri.neuinfo.org/nif/nifstd/sao2007137787>`_
         - The distal terminations of axons which are specialized for the release of neurotransmitters.
       * - `nucleus <http://uri.neuinfo.org/nif/nifstd/sao1702920020>`_
         - A 'nucleus' is a membrane-bounded organelle of eukaryotic cells that contains the chromosomes. It is the primary site of DNA replication and RNA synthesis in the cell (Gene Ontology)
       * - `neurofilament <http://uri.neuinfo.org/nif/nifstd/sao1316272517>`_
         - A 'neurofilament' is a type of intermediate filament found in the core of neuronal axons. Neurofilaments are responsible for the radial growth of an axon and determine axonal diameter.
       * - `synaptic protein <http://uri.neuinfo.org/nif/nifstd/sao936599761>`_
         - A 'synaptic protein' belongs to a family of neuron-specific phosphoric proteins associated with synaptic vesicles. Synaptic proteins are present on the surface of almost all synaptic particles and bind to the cytoskeleton.
       * - asymmetric synapse
         - An 'asymmetric synapse' is characterized by rounded vesicles in the presynaptic cell and a prominent postsynaptic density. Asymmetric synapses are typically excitatory.
       * - `synaptic bouton <http://uri.neuinfo.org/nif/nifstd/sao187426937>`_
         - A 'synaptic bouton' is a terminal pre-synaptic ending of an axon or axon collateral.
       * - `dendritic spine <http://uri.neuinfo.org/nif/nifstd/sao1799103720>`_
         - A 'dendritic spine' is a protrusion from a dendrite. Spines are specialised subcellular compartments involved in the synaptic transmission.
       * - `dendrite <http://uri.neuinfo.org/nif/nifstd/sao1211023249>`_
         - A 'dendrite' is a branching protoplasmic process of a neuron that receives and integrates signals coming from axons of other neurons, and conveys the resulting signal to the body of the cell (Gene Ontology).
       * - `mitochondrion <http://uri.neuinfo.org/nif/nifstd/sao1860313010>`_
         - A 'mitochondrion' is a semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration (Gene Ontology).
       * - `axon <http://uri.neuinfo.org/nif/nifstd/sao1770195789>`_
         - An 'axon' is the long process of a neuron that conducts nerve impulses, usually away from the cell body to the terminals which are the site of storage and release of neurotransmitter (Gene Ontology).

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/SubcellularEntity"]
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
            doc="Word or phrase that constitutes the distinctive designation of the subcellular entity.",
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
            doc="Longer statement or account giving the characteristics of the subcellular entity.",
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
            [
                "openminds.core.TissueSample",
                "openminds.core.TissueSampleCollection",
                "openminds.ephys.ElectrodeArrayUsage",
                "openminds.ephys.ElectrodeUsage",
                "openminds.ephys.PipetteUsage",
            ],
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
            studied_in=studied_in,
        )
