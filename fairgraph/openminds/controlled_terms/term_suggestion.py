"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from fairgraph.base import IRI


class TermSuggestion(KGObject):
    """
    <description not available>
    """

    default_space = "controlled"
    type_ = "https://openminds.ebrains.eu/controlledTerms/TermSuggestion"
    properties = [
        Property(
            "add_existing_terminology",
            "openminds.controlled_terms.Terminology",
            "vocab:addExistingTerminology",
            doc="Reference to an existing terminology (distinct class to group related terms).",
        ),
        Property(
            "definition",
            str,
            "vocab:definition",
            doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the term suggestion.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "vocab:interlexIdentifier",
            doc="Persistent identifier for a term registered in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "vocab:knowledgeSpaceLink",
            doc="Persistent link to an encyclopedia entry in the Knowledge Space project.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the term suggestion.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "vocab:preferredOntologyIdentifier",
            doc="Persistent identifier of a preferred ontological term.",
        ),
        Property(
            "suggest_new_terminology",
            str,
            "vocab:suggestNewTerminology",
            doc="Proposal of a new distinct class to group related terms.",
        ),
        Property(
            "synonyms",
            str,
            "vocab:synonym",
            multiple=True,
            doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
        ),
    ]
    reverse_properties = [
        Property(
            "describes",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
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
            doc="reverse of 'keywords'",
        ),
        Property(
            "is_used_to_group",
            "openminds.core.FileBundle",
            "^vocab:groupedBy",
            reverse="grouped_by",
            multiple=True,
            doc="reverse of 'grouped_by'",
        ),
        Property(
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
                "openminds.core.DatasetVersion",
                "openminds.core.Model",
                "openminds.core.ProtocolExecution",
                "openminds.ephys.CellPatching",
                "openminds.ephys.ElectrodePlacement",
                "openminds.ephys.RecordingActivity",
                "openminds.specimen_prep.CranialWindowPreparation",
                "openminds.specimen_prep.TissueCulturePreparation",
                "openminds.specimen_prep.TissueSampleSlicing",
                "openminds.stimulation.StimulationActivity",
            ],
            "^vocab:studyTarget",
            reverse="study_targets",
            multiple=True,
            doc="reverse of 'study_targets'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        add_existing_terminology=None,
        definition=None,
        describes=None,
        description=None,
        interlex_identifier=None,
        is_used_to_group=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        studied_in=None,
        suggest_new_terminology=None,
        synonyms=None,
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
            add_existing_terminology=add_existing_terminology,
            definition=definition,
            describes=describes,
            description=description,
            interlex_identifier=interlex_identifier,
            is_used_to_group=is_used_to_group,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            studied_in=studied_in,
            suggest_new_terminology=suggest_new_terminology,
            synonyms=synonyms,
        )
