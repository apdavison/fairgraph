"""
Structured information on the life cycle (semantic term) of a specific age group.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `perinatal <http://purl.obolibrary.org/obo/UBERON_0012101>`_
         - 'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.
       * - young adult
         - 'Young adult' categorizes the early adult stage of an animal or human when sexual maturity has been reached, but not the cessation of growth.
       * - `adult <http://purl.obolibrary.org/obo/UBERON_0000113>`_
         - 'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity.
       * - `embryo <http://purl.obolibrary.org/obo/UBERON_0000068>`_
         - 'Embryo' categorizes the life cycle stage of an animal or human that starts with fertilitzation and ends with the fully formed embryo.
       * - adolescent
         - 'Adolescent' categorizes a transitional life cycle stage of growth and development between childhood and adulthood, often described as 'puberty'.
       * - `neonate <http://purl.obolibrary.org/obo/UBERON_0007221>`_
         - 'Neonate' categorizes the life cycle stage of an animal or human that immediately follows birth.
       * - `infant <http://purl.obolibrary.org/obo/UBERON_0034920>`_
         - 'Infant' categorizes the life cycle stage of mammals (animal or human) that follows the neonate stage and ends at weaning.
       * - `prime adult <http://purl.obolibrary.org/obo/UBERON_0018241>`_
         - 'Prime adult' categorizes the life cycle stage of an animal or human that starts at the onset of sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.
       * - `juvenile <http://purl.obolibrary.org/obo/UBERON_0034919>`_
         - 'Juvenile' categorizes the life cycle stage of an animal or human that starts with the independence of the nest and/or caregivers and ends with sexual maturity.
       * - `late adult <http://purl.obolibrary.org/obo/UBERON_0007222>`_
         - 'Late adult' categorizes the life cycle stage of an animal or human that follows the prime adult stage.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class AgeCategory(KGObject):
    """
    Structured information on the life cycle (semantic term) of a specific age group.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `perinatal <http://purl.obolibrary.org/obo/UBERON_0012101>`_
         - 'Perinatal' categorizes the life cycle stage of an animal or human that starts right before birth and ends right after birth.
       * - young adult
         - 'Young adult' categorizes the early adult stage of an animal or human when sexual maturity has been reached, but not the cessation of growth.
       * - `adult <http://purl.obolibrary.org/obo/UBERON_0000113>`_
         - 'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity.
       * - `embryo <http://purl.obolibrary.org/obo/UBERON_0000068>`_
         - 'Embryo' categorizes the life cycle stage of an animal or human that starts with fertilitzation and ends with the fully formed embryo.
       * - adolescent
         - 'Adolescent' categorizes a transitional life cycle stage of growth and development between childhood and adulthood, often described as 'puberty'.
       * - `neonate <http://purl.obolibrary.org/obo/UBERON_0007221>`_
         - 'Neonate' categorizes the life cycle stage of an animal or human that immediately follows birth.
       * - `infant <http://purl.obolibrary.org/obo/UBERON_0034920>`_
         - 'Infant' categorizes the life cycle stage of mammals (animal or human) that follows the neonate stage and ends at weaning.
       * - `prime adult <http://purl.obolibrary.org/obo/UBERON_0018241>`_
         - 'Prime adult' categorizes the life cycle stage of an animal or human that starts at the onset of sexual maturity or the cessation of growth, whichever comes last, and ends before senescence.
       * - `juvenile <http://purl.obolibrary.org/obo/UBERON_0034919>`_
         - 'Juvenile' categorizes the life cycle stage of an animal or human that starts with the independence of the nest and/or caregivers and ends with sexual maturity.
       * - `late adult <http://purl.obolibrary.org/obo/UBERON_0007222>`_
         - 'Late adult' categorizes the life cycle stage of an animal or human that follows the prime adult stage.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/AgeCategory"]
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
            doc="Word or phrase that constitutes the distinctive designation of the age category.",
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
            doc="Longer statement or account giving the characteristics of the age category.",
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
            "is_age_category_of",
            ["openminds.core.SubjectGroupState", "openminds.core.SubjectState"],
            "^vocab:ageCategory",
            reverse="age_categories",
            multiple=True,
            doc="reverse of 'ageCategory'",
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
        is_age_category_of=None,
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
            is_age_category_of=is_age_category_of,
        )
