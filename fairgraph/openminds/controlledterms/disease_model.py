"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - autism spectrum disorder model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal autism sprectrum disorder.
       * - Alzheimer's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Alzheimer's disease.
       * - Huntington's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Huntington's disease.
       * - fragile X syndrome model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal fragile X syndrome.
       * - Williams-Beuren syndrome model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Williams-Beuren syndrome.
       * - stroke model
         - An animal or cell displaying all or some of the pathological processes that are observed during stroke in humans or animals.
       * - Parkinson's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Parkinson's disease.
       * - epilepsy model
         - An animal or cell displaying all or some of the pathological processes that are observed for epilepsy in humans or animals.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class DiseaseModel(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - autism spectrum disorder model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal autism sprectrum disorder.
       * - Alzheimer's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Alzheimer's disease.
       * - Huntington's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Huntington's disease.
       * - fragile X syndrome model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal fragile X syndrome.
       * - Williams-Beuren syndrome model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Williams-Beuren syndrome.
       * - stroke model
         - An animal or cell displaying all or some of the pathological processes that are observed during stroke in humans or animals.
       * - Parkinson's disease model
         - An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Parkinson's disease.
       * - epilepsy model
         - An animal or cell displaying all or some of the pathological processes that are observed for epilepsy in humans or animals.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/DiseaseModel"]
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
            doc="Word or phrase that constitutes the distinctive designation of the disease model.",
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
            doc="Longer statement or account giving the characteristics of the disease model.",
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
        )
