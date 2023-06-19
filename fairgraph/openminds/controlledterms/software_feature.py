"""

    Here we show the first 20 possible values, an additional 12 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `raster image data types <https://www.wikidata.org/wiki/Q182270>`_
         - https://www.wikidata.org/wiki/Q182270
       * - `simulation <https://www.wikidata.org/wiki/Q925667>`_
         - https://www.wikidata.org/wiki/Q925667
       * - 3D scalar data types
         -
       * - `control <https://www.wikidata.org/wiki/Q29017603>`_
         - https://www.wikidata.org/wiki/Q29017603
       * - interactive analysis
         -
       * - `provenance <https://www.wikidata.org/wiki/Q30105403>`_
         - https://www.wikidata.org/wiki/Q30105403
       * - 3D vector data types
         -
       * - `statistical data types <https://www.wikidata.org/wiki/Q7604387>`_
         - https://www.wikidata.org/wiki/Q7604387
       * - tiled display wall
         -
       * - scripting interface
         -
       * - `mobile device <https://www.wikidata.org/wiki/Q5082128>`_
         - https://www.wikidata.org/wiki/Q5082128
       * - `augmented reality <https://www.wikidata.org/wiki/Q254183>`_
         - https://www.wikidata.org/wiki/Q254183
       * - `time series data types <https://www.wikidata.org/wiki/Q186588>`_
         - https://www.wikidata.org/wiki/Q186588
       * - `metadata data types <https://www.wikidata.org/wiki/Q180160>`_
         - https://www.wikidata.org/wiki/Q180160
       * - `graphical user interface <https://www.wikidata.org/wiki/Q782543>`_
         - https://www.wikidata.org/wiki/Q782543
       * - `modelling <https://www.wikidata.org/wiki/Q1116876>`_
         - https://www.wikidata.org/wiki/Q1116876
       * - `presentation visualisation <https://www.wikidata.org/wiki/Q451553>`_
         - https://www.wikidata.org/wiki/Q451553
       * - `graph data types <https://www.wikidata.org/wiki/Q2479726>`_
         - https://www.wikidata.org/wiki/Q2479726
       * - `heterogeneous architecture <https://www.wikidata.org/wiki/Q17111997>`_
         - https://www.wikidata.org/wiki/Q17111997
       * - `positional data types <https://www.wikidata.org/wiki/Q1477538>`_
         - https://www.wikidata.org/wiki/Q1477538

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class SoftwareFeature(KGObject):
    """

    Here we show the first 20 possible values, an additional 12 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `raster image data types <https://www.wikidata.org/wiki/Q182270>`_
         - https://www.wikidata.org/wiki/Q182270
       * - `simulation <https://www.wikidata.org/wiki/Q925667>`_
         - https://www.wikidata.org/wiki/Q925667
       * - 3D scalar data types
         -
       * - `control <https://www.wikidata.org/wiki/Q29017603>`_
         - https://www.wikidata.org/wiki/Q29017603
       * - interactive analysis
         -
       * - `provenance <https://www.wikidata.org/wiki/Q30105403>`_
         - https://www.wikidata.org/wiki/Q30105403
       * - 3D vector data types
         -
       * - `statistical data types <https://www.wikidata.org/wiki/Q7604387>`_
         - https://www.wikidata.org/wiki/Q7604387
       * - tiled display wall
         -
       * - scripting interface
         -
       * - `mobile device <https://www.wikidata.org/wiki/Q5082128>`_
         - https://www.wikidata.org/wiki/Q5082128
       * - `augmented reality <https://www.wikidata.org/wiki/Q254183>`_
         - https://www.wikidata.org/wiki/Q254183
       * - `time series data types <https://www.wikidata.org/wiki/Q186588>`_
         - https://www.wikidata.org/wiki/Q186588
       * - `metadata data types <https://www.wikidata.org/wiki/Q180160>`_
         - https://www.wikidata.org/wiki/Q180160
       * - `graphical user interface <https://www.wikidata.org/wiki/Q782543>`_
         - https://www.wikidata.org/wiki/Q782543
       * - `modelling <https://www.wikidata.org/wiki/Q1116876>`_
         - https://www.wikidata.org/wiki/Q1116876
       * - `presentation visualisation <https://www.wikidata.org/wiki/Q451553>`_
         - https://www.wikidata.org/wiki/Q451553
       * - `graph data types <https://www.wikidata.org/wiki/Q2479726>`_
         - https://www.wikidata.org/wiki/Q2479726
       * - `heterogeneous architecture <https://www.wikidata.org/wiki/Q17111997>`_
         - https://www.wikidata.org/wiki/Q17111997
       * - `positional data types <https://www.wikidata.org/wiki/Q1477538>`_
         - https://www.wikidata.org/wiki/Q1477538

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/SoftwareFeature"]
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
            doc="Word or phrase that constitutes the distinctive designation of the software feature.",
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
            doc="Longer statement or account giving the characteristics of the software feature.",
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
        )
