"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - holding potential
         - Measured membrane potential during a voltage-clamp protocol.
       * - compensation current
         - Current injected into a cell to maintain the membrane potential at a target value.
       * - input resistance
         - Total resistance observed by the amplifier during an electrophysiological recording.
       * - series resistance
         - Resistance of the electrode during an electrophysiological recording.
       * - liquid junction potential
         - A potential difference that develops when two solutions of electrolytes of different concentrations are in contact with each other.
       * - measured holding potential
         - Measured membrane potetial during a voltage-clamp protocol.
       * - seal resistance
         - Resistance of the seal between the pipette tip and cell membrane in patch-clamp recording.
       * - `membrane potential <http://uri.interlex.org/base/ilx_0106774>`_
         - A quality inhering in a cell's plasma membrane by virtue of the electric potential difference across it.
       * - chloride reversal potential
         - The reversal potential for chloride ions.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class MeasuredQuantity(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - holding potential
         - Measured membrane potential during a voltage-clamp protocol.
       * - compensation current
         - Current injected into a cell to maintain the membrane potential at a target value.
       * - input resistance
         - Total resistance observed by the amplifier during an electrophysiological recording.
       * - series resistance
         - Resistance of the electrode during an electrophysiological recording.
       * - liquid junction potential
         - A potential difference that develops when two solutions of electrolytes of different concentrations are in contact with each other.
       * - measured holding potential
         - Measured membrane potetial during a voltage-clamp protocol.
       * - seal resistance
         - Resistance of the seal between the pipette tip and cell membrane in patch-clamp recording.
       * - `membrane potential <http://uri.interlex.org/base/ilx_0106774>`_
         - A quality inhering in a cell's plasma membrane by virtue of the electric potential difference across it.
       * - chloride reversal potential
         - The reversal potential for chloride ions.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/MeasuredQuantity"]
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
            multiple=False,
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the measured quantity.",
        ),
        Field(
            "definition",
            str,
            "vocab:definition",
            multiple=False,
            required=False,
            doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            multiple=False,
            required=False,
            doc="Longer statement or account giving the characteristics of the measured quantity.",
        ),
        Field(
            "interlex_identifier",
            IRI,
            "vocab:interlexIdentifier",
            multiple=False,
            required=False,
            doc="Persistent identifier for a term registered in the InterLex project.",
        ),
        Field(
            "knowledge_space_link",
            IRI,
            "vocab:knowledgeSpaceLink",
            multiple=False,
            required=False,
            doc="Persistent link to an encyclopedia entry in the Knowledge Space project.",
        ),
        Field(
            "preferred_ontology_identifier",
            IRI,
            "vocab:preferredOntologyIdentifier",
            multiple=False,
            required=False,
            doc="Persistent identifier of a preferred ontological term.",
        ),
        Field(
            "synonyms",
            str,
            "vocab:synonym",
            multiple=True,
            required=False,
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
