"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `visual stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00132>`_
         - A stimulation of the visual (sight) system.
       * - `olfactory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00130>`_
         - A stimulation of the olfactory (smelling) system.
       * - `tactile stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00131>`_
         - A stimulation of the tactile (touch) system.
       * - `gustatory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00123>`_
         - A stimulation of the gustatory (taste and flavor perception) system.
       * - `interoceptive stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00128>`_
         - A stimulation that arises from inside an organism.
       * - `auditory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00125>`_
         - A stimulation of the auditory (hearing) system.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class StimulationApproach(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `visual stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00132>`_
         - A stimulation of the visual (sight) system.
       * - `olfactory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00130>`_
         - A stimulation of the olfactory (smelling) system.
       * - `tactile stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00131>`_
         - A stimulation of the tactile (touch) system.
       * - `gustatory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00123>`_
         - A stimulation of the gustatory (taste and flavor perception) system.
       * - `interoceptive stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00128>`_
         - A stimulation that arises from inside an organism.
       * - `auditory stimulation <http://www.cogpo.org/ontologies/CogPOver1.owl#COGPO_00125>`_
         - A stimulation of the auditory (hearing) system.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/StimulationApproach"]
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
            doc="Word or phrase that constitutes the distinctive designation of the stimulation approach.",
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
            doc="Longer statement or account giving the characteristics of the stimulation approach.",
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
