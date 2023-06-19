"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `glutamatergic system <http://purl.obolibrary.org/obo/UBERON_0025592>`_
         - The glutamatergic system is composed of any molecule, protein, cell, tissue or organ that is related to glutamate (when in the role of a neurotransmitter).
       * - `cardiovascular system <http://purl.obolibrary.org/obo/UBERON_0004535>`_
         - 'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.
       * - `gabaergic system <http://purl.obolibrary.org/obo/UBERON_0025591>`_
         - The gabaergic system is composed of any molecule, protein, cell, tissue or organ that is related to GABA.
       * - `noradrenergic system <http://purl.obolibrary.org/obo/UBERON_0027225>`_
         - The noradrenergic system is composed of any molecule, protein, cell, tissue or organ that is related to norepinephrine (also known as noradrenaline).
       * - `central nervous system <http://purl.obolibrary.org/obo/UBERON_0001017>`_
         - The 'central nervous system' is the main processing center in most organisms. Its function is to take in sensory information, process information, and send out motor signals.
       * - `cholinergic system <http://purl.obolibrary.org/obo/UBERON_0002204http://purl.obolibrary.org/obo/UBERON_0025595>`_
         - The cholinergic system is composed of any molecule, protein, cell, tissue or organ that is related to acetylcholine.
       * - `musculoskeletal system <http://purl.obolibrary.org/obo/UBERON_0002204>`_
         - The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.
       * - `serotonergic system <http://purl.obolibrary.org/obo/UBERON_0025593>`_
         - The serotonergic system is composed of any molecule, protein, cell, tissue or organ that is related to serotonin.
       * - `digestive system <http://purl.obolibrary.org/obo/UBERON_0001007>`_
         - The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.
       * - `vascular system <http://purl.obolibrary.org/obo/UBERON_0007798>`_
         - The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class OrganismSystem(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `glutamatergic system <http://purl.obolibrary.org/obo/UBERON_0025592>`_
         - The glutamatergic system is composed of any molecule, protein, cell, tissue or organ that is related to glutamate (when in the role of a neurotransmitter).
       * - `cardiovascular system <http://purl.obolibrary.org/obo/UBERON_0004535>`_
         - 'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.
       * - `gabaergic system <http://purl.obolibrary.org/obo/UBERON_0025591>`_
         - The gabaergic system is composed of any molecule, protein, cell, tissue or organ that is related to GABA.
       * - `noradrenergic system <http://purl.obolibrary.org/obo/UBERON_0027225>`_
         - The noradrenergic system is composed of any molecule, protein, cell, tissue or organ that is related to norepinephrine (also known as noradrenaline).
       * - `central nervous system <http://purl.obolibrary.org/obo/UBERON_0001017>`_
         - The 'central nervous system' is the main processing center in most organisms. Its function is to take in sensory information, process information, and send out motor signals.
       * - `cholinergic system <http://purl.obolibrary.org/obo/UBERON_0002204http://purl.obolibrary.org/obo/UBERON_0025595>`_
         - The cholinergic system is composed of any molecule, protein, cell, tissue or organ that is related to acetylcholine.
       * - `musculoskeletal system <http://purl.obolibrary.org/obo/UBERON_0002204>`_
         - The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.
       * - `serotonergic system <http://purl.obolibrary.org/obo/UBERON_0025593>`_
         - The serotonergic system is composed of any molecule, protein, cell, tissue or organ that is related to serotonin.
       * - `digestive system <http://purl.obolibrary.org/obo/UBERON_0001007>`_
         - The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.
       * - `vascular system <http://purl.obolibrary.org/obo/UBERON_0007798>`_
         - The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/OrganismSystem"]
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
            doc="Word or phrase that constitutes the distinctive designation of the organism system.",
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
            doc="Longer statement or account giving the characteristics of the organism system.",
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
            is_used_to_group=is_used_to_group,
            studied_in=studied_in,
        )
