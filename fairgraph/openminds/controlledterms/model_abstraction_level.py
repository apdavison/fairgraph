"""
Structured information on abstraction level of the computational model.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - systems biology
         - Modelling of neural systems below the level of individual neurons
       * - population modelling
         - Modelling of neural circuits at the population level
       * - systems biology: discrete
         - Systems biology modelling using representations of individual particles
       * - spiking neurons
         - Modelling neural networks in which the action potentials of individual neurons are represented
       * - algorithm
         - Modelling of a neural structure or process as an algorithm
       * - spiking neurons: point neuron
         - Modelling neural networks in which individual neurons are represented by point neuron models
       * - spiking neurons: biophysical
         - Modelling neural networks in which individual neurons are represented by models with detailed morphology and biophysical models of ion channels
       * - systems biology: continuous
         - Systems biology modelling using concentrations
       * - statistical model
         - Statistical modelling of neural data generation
       * - protein structure
         - Modelling of protein structure
       * - systems biology: flux balance
         - Systems biology modelling using flux balance analysis
       * - population modelling: neural field
         - Modelling neural populations using the approximation of a neural field
       * - population modelling: neural mass
         - Modelling neural populations using the approximation of neural masses
       * - cognitive modelling
         - Modelling of cognitive processes
       * - rate neurons
         - Modelling neural networks in which individual neurons are represented by their firing rate

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ModelAbstractionLevel(KGObject):
    """
    Structured information on abstraction level of the computational model.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - systems biology
         - Modelling of neural systems below the level of individual neurons
       * - population modelling
         - Modelling of neural circuits at the population level
       * - systems biology: discrete
         - Systems biology modelling using representations of individual particles
       * - spiking neurons
         - Modelling neural networks in which the action potentials of individual neurons are represented
       * - algorithm
         - Modelling of a neural structure or process as an algorithm
       * - spiking neurons: point neuron
         - Modelling neural networks in which individual neurons are represented by point neuron models
       * - spiking neurons: biophysical
         - Modelling neural networks in which individual neurons are represented by models with detailed morphology and biophysical models of ion channels
       * - systems biology: continuous
         - Systems biology modelling using concentrations
       * - statistical model
         - Statistical modelling of neural data generation
       * - protein structure
         - Modelling of protein structure
       * - systems biology: flux balance
         - Systems biology modelling using flux balance analysis
       * - population modelling: neural field
         - Modelling neural populations using the approximation of a neural field
       * - population modelling: neural mass
         - Modelling neural populations using the approximation of neural masses
       * - cognitive modelling
         - Modelling of cognitive processes
       * - rate neurons
         - Modelling neural networks in which individual neurons are represented by their firing rate

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/ModelAbstractionLevel"]
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
            doc="Word or phrase that constitutes the distinctive designation of the model abstraction level.",
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
            doc="Longer statement or account giving the characteristics of the model abstraction level.",
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
            "is_abstraction_level_of",
            "openminds.core.Model",
            "^vocab:abstractionLevel",
            reverse="abstraction_levels",
            multiple=True,
            doc="reverse of 'abstractionLevel'",
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
        is_abstraction_level_of=None,
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
            is_abstraction_level_of=is_abstraction_level_of,
        )
