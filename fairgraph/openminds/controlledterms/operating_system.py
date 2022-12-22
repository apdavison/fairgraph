"""
Structured information on the operating system.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - platform independent
         - https://www.wikidata.org/wiki/Q174666
       * - Android
         - https://www.wikidata.org/wiki/Q94
       * - Windows Phone
         - https://www.wikidata.org/wiki/Q4885200
       * - Unix
         - https://www.wikidata.org/wiki/Q11368
       * - iOS
         - https://www.wikidata.org/wiki/Q48493
       * - Linux
         - https://www.wikidata.org/wiki/Q388
       * - Solaris
         - https://www.wikidata.org/wiki/Q14646
       * - Windows
         - https://www.wikidata.org/wiki/Q1406
       * - MacOS
         - https://www.wikidata.org/wiki/Q43627

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class OperatingSystem(KGObject):
    """
    Structured information on the operating system.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - platform independent
         - https://www.wikidata.org/wiki/Q174666
       * - Android
         - https://www.wikidata.org/wiki/Q94
       * - Windows Phone
         - https://www.wikidata.org/wiki/Q4885200
       * - Unix
         - https://www.wikidata.org/wiki/Q11368
       * - iOS
         - https://www.wikidata.org/wiki/Q48493
       * - Linux
         - https://www.wikidata.org/wiki/Q388
       * - Solaris
         - https://www.wikidata.org/wiki/Q14646
       * - Windows
         - https://www.wikidata.org/wiki/Q1406
       * - MacOS
         - https://www.wikidata.org/wiki/Q43627

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/OperatingSystem"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the operating system."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the operating system."),
        Field("interlex_identifier", IRI, "vocab:interlexIdentifier", multiple=False, required=False,
              doc="Persistent identifier for a term registered in the InterLex project."),
        Field("knowledge_space_link", IRI, "vocab:knowledgeSpaceLink", multiple=False, required=False,
              doc="Persistent link to an encyclopedia entry in the Knowledge Space project."),
        Field("preferred_ontology_identifier", IRI, "vocab:preferredOntologyIdentifier", multiple=False, required=False,
              doc="Persistent identifier of a preferred ontological term."),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name',)
