"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - photon stimulation
         -
       * - optogenetic stimulation
         - Using light of a particular wavelength, 'optogenetic stimulation' increases or inhibits the activity of neuron populations that express (typically due to genetic manipulation) light-sensitive ion channels, pumps or enzymes.
       * - microstimulation
         -
       * - figure-ground visual stimulation
         -
       * - drifting grating visual stimulation
         -
       * - static grating visual stimulation
         -
       * - whisker stimulation
         - 'Whisker stimulation' comprises all stimulation techniques in which a single whisker or a group of whiskers is deflected in repeatable manner.
       * - `electrical stimulation <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/188>`_
         - A technique used to elicit a reaction by an electrical stimulus.
       * - natural image visual stimulation
         - In a 'natural image visual stimulation' a subject is visually stimulated with a static image that shows a natural scene (e.g., landscape or a person).
       * - transcranial magnetic stimulation
         -
       * - current step stimulation
         - Current step stimulation is a technique in which an amount of current is applied in predefined steps, whilst measuring changes in neural/muscular activity.
       * - abstract image visual stimulation
         - In an 'abstract image visual stimulation' a subject is visually stimulated with a static image that does not show a natural scene but reduced information or forms (e.g., colored symbols or outlines of faces).
       * - random dot motion stimulation
         - In a 'random dot motion stimulation' a subject is visually stimulated with a video where simulated randomly distributed dot(s) are re-positioned at a new random location with each video frame [[Newsome & Paré, 1988](https://doi.org/10.1523/jneurosci.08-06-02201.1988).
       * - single pulse electrical stimulation
         - A 'single pulse electrical stimulation' is a cortical stimulation technique typically used in the field of epilepsy surgery.
       * - Gestalt visual stimulation
         -
       * - natural sound auditory stimulation
         -
       * - checkerboard visual stimulation
         - Stimulation technique that uses a checkerboard as visual stimulus.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class StimulationTechnique(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - photon stimulation
         -
       * - optogenetic stimulation
         - Using light of a particular wavelength, 'optogenetic stimulation' increases or inhibits the activity of neuron populations that express (typically due to genetic manipulation) light-sensitive ion channels, pumps or enzymes.
       * - microstimulation
         -
       * - figure-ground visual stimulation
         -
       * - drifting grating visual stimulation
         -
       * - static grating visual stimulation
         -
       * - whisker stimulation
         - 'Whisker stimulation' comprises all stimulation techniques in which a single whisker or a group of whiskers is deflected in repeatable manner.
       * - `electrical stimulation <http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/188>`_
         - A technique used to elicit a reaction by an electrical stimulus.
       * - natural image visual stimulation
         - In a 'natural image visual stimulation' a subject is visually stimulated with a static image that shows a natural scene (e.g., landscape or a person).
       * - transcranial magnetic stimulation
         -
       * - current step stimulation
         - Current step stimulation is a technique in which an amount of current is applied in predefined steps, whilst measuring changes in neural/muscular activity.
       * - abstract image visual stimulation
         - In an 'abstract image visual stimulation' a subject is visually stimulated with a static image that does not show a natural scene but reduced information or forms (e.g., colored symbols or outlines of faces).
       * - random dot motion stimulation
         - In a 'random dot motion stimulation' a subject is visually stimulated with a video where simulated randomly distributed dot(s) are re-positioned at a new random location with each video frame [[Newsome & Paré, 1988](https://doi.org/10.1523/jneurosci.08-06-02201.1988).
       * - single pulse electrical stimulation
         - A 'single pulse electrical stimulation' is a cortical stimulation technique typically used in the field of epilepsy surgery.
       * - Gestalt visual stimulation
         -
       * - natural sound auditory stimulation
         -
       * - checkerboard visual stimulation
         - Stimulation technique that uses a checkerboard as visual stimulus.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/StimulationTechnique"]
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
            doc="Word or phrase that constitutes the distinctive designation of the stimulation technique.",
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
            doc="Longer statement or account giving the characteristics of the stimulation technique.",
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
            "used_in",
            ["openminds.core.BehavioralProtocol", "openminds.core.Protocol"],
            ["^vocab:stimulation", "^vocab:technique"],
            reverse=["stimulations", "techniques"],
            multiple=True,
            doc="reverse of stimulation, technique",
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
        used_in=None,
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
            used_in=used_in,
        )
