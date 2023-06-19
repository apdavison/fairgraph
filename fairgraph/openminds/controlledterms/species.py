"""
Structured information on the species.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `Mustela putorius furo <http://purl.obolibrary.org/obo/NCBITaxon_9669>`_
         - The species *Mustela putorius furo* (domestic ferret) belongs to the family of *mustelidae* (mustelids).
       * - `Macaca fascicularis <http://purl.obolibrary.org/obo/NCBITaxon_9541>`_
         - The species *Macaca fascicularis* (crab-eating macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Chlorocebus pygerythrus <http://purl.obolibrary.org/obo/NCBITaxon_60710>`_
         - The species *Chlorocebus pygerythrus* (vervet marmoset) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Macaca fuscata <http://purl.obolibrary.org/obo/NCBITaxon_9542>`_
         - The species *Macaca fuscata* (Japanese macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Macaca mulatta <http://purl.obolibrary.org/obo/NCBITaxon_9544>`_
         - The species *Macaca mulatta* (rhesus macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Sus scrofa domesticus <http://purl.obolibrary.org/obo/NCBITaxon_9825>`_
         - The species *Sus scrofa domesticus* (domestic pig) belongs to the family of suidae (suids).
       * - `Monodelphis domestica <http://purl.obolibrary.org/obo/NCBITaxon_13616>`_
         - The species *Monodelphis domestica* (gray short-tailed opossum) belongs to the family of *didelphidae* (American possums).
       * - `Callithrix jacchus <http://purl.obolibrary.org/obo/NCBITaxon_9483>`_
         - The species *Callithrix jacchus* (common marmoset) belongs to the family of *callitrichidae* (new world monkeys).
       * - `Homo sapiens <http://purl.obolibrary.org/obo/NCBITaxon_9606>`_
         - The species *Homo sapiens* (humans) belongs to the family of *hominidae* (great apes).
       * - `Danio rerio <http://purl.obolibrary.org/obo/NCBITaxon_7955>`_
         - The species *Danio rerio* (zebrafish) belongs to the family of *cyprinidae* (cyprinids, freshwater fish).
       * - `Rattus norvegicus <http://purl.obolibrary.org/obo/NCBITaxon_10116>`_
         - The species *Rattus norvegicus* (brown rat) belongs to the family of *muridae* (murids).
       * - `Berghia stephanieae <http://purl.obolibrary.org/obo/NCBITaxon_1287507>`_
         - The species *Berghia stephanieae* belongs to the family of *aeolidiidae* (family of sea slugs, shell-less marine gastropod molluscs).
       * - `Chlorocebus aethiops sabaeus <http://purl.obolibrary.org/obo/NCBITaxon_60711>`_
         - The species *Chlorocebus aethiops sabaeus* (green monkey) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Ovis aries <http://purl.obolibrary.org/obo/NCBITaxon_9940>`_
         - The species *Ovis aries* (domestic sheep) belongs to the family of bovidae (bovids).
       * - `Mus musculus <http://purl.obolibrary.org/obo/NCBITaxon_10090>`_
         - The species *Mus musculus* (house mouse) belongs to the family of *muridae* (murids).
       * - `Mustela putorius <http://purl.obolibrary.org/obo/NCBITaxon_9668>`_
         - The species *Mustela putorius* (European polecat) belongs to the family of *mustelidae* (mustelids).
       * - `Trachemys scripta elegans <http://purl.obolibrary.org/obo/NCBITaxon_31138>`_
         - The red-eared slider or red-eared terrapin (Trachemys scripta elegans) is a subspecies of the pond slider (Trachemys scripta), a semiaquatic turtle belonging to the family Emydidae ([Wikipedia](https://en.wikipedia.org/wiki/Red-eared_slider)).
       * - `Felis catus <http://purl.obolibrary.org/obo/NCBITaxon_9685>`_
         - The species *Felis catus* (domestic cat) belongs to the family of *Felidae*, subfamily *Felinae*.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Species(KGObject):
    """
    Structured information on the species.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `Mustela putorius furo <http://purl.obolibrary.org/obo/NCBITaxon_9669>`_
         - The species *Mustela putorius furo* (domestic ferret) belongs to the family of *mustelidae* (mustelids).
       * - `Macaca fascicularis <http://purl.obolibrary.org/obo/NCBITaxon_9541>`_
         - The species *Macaca fascicularis* (crab-eating macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Chlorocebus pygerythrus <http://purl.obolibrary.org/obo/NCBITaxon_60710>`_
         - The species *Chlorocebus pygerythrus* (vervet marmoset) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Macaca fuscata <http://purl.obolibrary.org/obo/NCBITaxon_9542>`_
         - The species *Macaca fuscata* (Japanese macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Macaca mulatta <http://purl.obolibrary.org/obo/NCBITaxon_9544>`_
         - The species *Macaca mulatta* (rhesus macaque) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Sus scrofa domesticus <http://purl.obolibrary.org/obo/NCBITaxon_9825>`_
         - The species *Sus scrofa domesticus* (domestic pig) belongs to the family of suidae (suids).
       * - `Monodelphis domestica <http://purl.obolibrary.org/obo/NCBITaxon_13616>`_
         - The species *Monodelphis domestica* (gray short-tailed opossum) belongs to the family of *didelphidae* (American possums).
       * - `Callithrix jacchus <http://purl.obolibrary.org/obo/NCBITaxon_9483>`_
         - The species *Callithrix jacchus* (common marmoset) belongs to the family of *callitrichidae* (new world monkeys).
       * - `Homo sapiens <http://purl.obolibrary.org/obo/NCBITaxon_9606>`_
         - The species *Homo sapiens* (humans) belongs to the family of *hominidae* (great apes).
       * - `Danio rerio <http://purl.obolibrary.org/obo/NCBITaxon_7955>`_
         - The species *Danio rerio* (zebrafish) belongs to the family of *cyprinidae* (cyprinids, freshwater fish).
       * - `Rattus norvegicus <http://purl.obolibrary.org/obo/NCBITaxon_10116>`_
         - The species *Rattus norvegicus* (brown rat) belongs to the family of *muridae* (murids).
       * - `Berghia stephanieae <http://purl.obolibrary.org/obo/NCBITaxon_1287507>`_
         - The species *Berghia stephanieae* belongs to the family of *aeolidiidae* (family of sea slugs, shell-less marine gastropod molluscs).
       * - `Chlorocebus aethiops sabaeus <http://purl.obolibrary.org/obo/NCBITaxon_60711>`_
         - The species *Chlorocebus aethiops sabaeus* (green monkey) belongs to the family of *cercopithecidae* (old world monkeys).
       * - `Ovis aries <http://purl.obolibrary.org/obo/NCBITaxon_9940>`_
         - The species *Ovis aries* (domestic sheep) belongs to the family of bovidae (bovids).
       * - `Mus musculus <http://purl.obolibrary.org/obo/NCBITaxon_10090>`_
         - The species *Mus musculus* (house mouse) belongs to the family of *muridae* (murids).
       * - `Mustela putorius <http://purl.obolibrary.org/obo/NCBITaxon_9668>`_
         - The species *Mustela putorius* (European polecat) belongs to the family of *mustelidae* (mustelids).
       * - `Trachemys scripta elegans <http://purl.obolibrary.org/obo/NCBITaxon_31138>`_
         - The red-eared slider or red-eared terrapin (Trachemys scripta elegans) is a subspecies of the pond slider (Trachemys scripta), a semiaquatic turtle belonging to the family Emydidae ([Wikipedia](https://en.wikipedia.org/wiki/Red-eared_slider)).
       * - `Felis catus <http://purl.obolibrary.org/obo/NCBITaxon_9685>`_
         - The species *Felis catus* (domestic cat) belongs to the family of *Felidae*, subfamily *Felinae*.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Species"]
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
            doc="Word or phrase that constitutes the distinctive designation of the species.",
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
            doc="Longer statement or account giving the characteristics of the species.",
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
            "common_coordinate_spaces",
            ["openminds.sands.BrainAtlas", "openminds.sands.CommonCoordinateSpace"],
            "^vocab:usedSpecies",
            reverse="used_species",
            multiple=True,
            doc="reverse of 'usedSpecies'",
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
            "is_species_of",
            [
                "openminds.core.Strain",
                "openminds.core.Subject",
                "openminds.core.SubjectGroup",
                "openminds.core.TissueSample",
                "openminds.core.TissueSampleCollection",
            ],
            "^vocab:species",
            reverse="species",
            multiple=True,
            doc="reverse of 'species'",
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
        common_coordinate_spaces=None,
        describes=None,
        is_species_of=None,
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
            common_coordinate_spaces=common_coordinate_spaces,
            describes=describes,
            is_species_of=is_species_of,
            is_used_to_group=is_used_to_group,
            studied_in=studied_in,
        )
