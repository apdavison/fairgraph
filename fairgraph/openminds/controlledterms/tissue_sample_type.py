"""
Structured information on the general type of the tissue sample.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - homogeneous cell population
         - A sample of multiple cells/a population of cells that are of the same cell type.
       * - nerve
         - A nerve sample (i.e. a whole nerve or a part of a nerve) from a living or deceased multicellular organism body.
       * - hemisphere
         - One of the symmetric halves excised from a bilateral organ tissue sample (e.g., a brain) from a living or deceased multicellular organism body.
       * - single cell
         - A single cell sample from a living or deceased multicellular organism body.
       * - `biopsy sample <http://purl.obolibrary.org/obo/OBI_0002650>`_
         - Typically very small sample of tissue that was excised from a living or deceased multicellular organism body.
       * - brain hemisphere
         -
       * - tissue slice
         - A thin and often flat sample of tissue that was excised from a larger tissue sample (e.g., a tissue block or a whole organ) from a living or deceased multicellular organism body.
       * - fluid specimen
         - A fluid sample either taken directly from a living or deceased multicellular organism body (i.e. body fluids) or produced in a laboratory.
       * - `cell culture <http://purl.obolibrary.org/obo/BTO_0000214>`_
         - Cells taken from a living organism and grown under controlled conditions (in culture).
       * - tissue block
         - A cube-like sample of tissue that was excised from a larger tissue sample (e.g., a whole organ) from a living or deceased multicellular organism body.
       * - whole brain
         -
       * - heterogeneous cell population
         - A sample of multiple cells/a population of cells that are of two or more different cell types.
       * - whole organ
         - A whole organ sample from a living or deceased multicellular organism body.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class TissueSampleType(KGObject):
    """
    Structured information on the general type of the tissue sample.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - homogeneous cell population
         - A sample of multiple cells/a population of cells that are of the same cell type.
       * - nerve
         - A nerve sample (i.e. a whole nerve or a part of a nerve) from a living or deceased multicellular organism body.
       * - hemisphere
         - One of the symmetric halves excised from a bilateral organ tissue sample (e.g., a brain) from a living or deceased multicellular organism body.
       * - single cell
         - A single cell sample from a living or deceased multicellular organism body.
       * - `biopsy sample <http://purl.obolibrary.org/obo/OBI_0002650>`_
         - Typically very small sample of tissue that was excised from a living or deceased multicellular organism body.
       * - brain hemisphere
         -
       * - tissue slice
         - A thin and often flat sample of tissue that was excised from a larger tissue sample (e.g., a tissue block or a whole organ) from a living or deceased multicellular organism body.
       * - fluid specimen
         - A fluid sample either taken directly from a living or deceased multicellular organism body (i.e. body fluids) or produced in a laboratory.
       * - `cell culture <http://purl.obolibrary.org/obo/BTO_0000214>`_
         - Cells taken from a living organism and grown under controlled conditions (in culture).
       * - tissue block
         - A cube-like sample of tissue that was excised from a larger tissue sample (e.g., a whole organ) from a living or deceased multicellular organism body.
       * - whole brain
         -
       * - heterogeneous cell population
         - A sample of multiple cells/a population of cells that are of two or more different cell types.
       * - whole organ
         - A whole organ sample from a living or deceased multicellular organism body.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/TissueSampleType"]
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
            doc="Word or phrase that constitutes the distinctive designation of the tissue sample type.",
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
            doc="Longer statement or account giving the characteristics of the tissue sample type.",
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
            "is_type_of",
            ["openminds.core.TissueSample", "openminds.core.TissueSampleCollection"],
            "^vocab:type",
            reverse="types",
            multiple=True,
            doc="reverse of 'type'",
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
        is_type_of=None,
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
            is_type_of=is_type_of,
        )
