"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - outbred
         - 'Outbred' breeding (or outbreeding) is the production of offspring from mating organisms that belong to two different background breeds.
       * - coisogenic
         - 'Coisogenic' breeding  is a type of inbreeding where the offspring differs at only a single locus through a mutation occurring in the original inbred strain.
       * - selective inbred
         - 'Selective inbred' breeding (or selective inbreeding) is the production of offspring from mating organisms that are genetically closely related (same background breed) and have been selected based on a particular phenotype.
       * - congenic
         - 'Congenic' breeding is the production of offspring from repeated backcrossing into an inbred (background) strain, with selection for a particular marker, ideally a single gene from another strain.
       * - hybrid
         - A 'hybrid' is an organism that resulted from special outbreeding of two species (normally within the same genus).
       * - inbred
         - 'Inbred' breeding (or inbreeding) is the production of offspring from mating organisms that are genetically closely related (same background breed).

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class BreedingType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - outbred
         - 'Outbred' breeding (or outbreeding) is the production of offspring from mating organisms that belong to two different background breeds.
       * - coisogenic
         - 'Coisogenic' breeding  is a type of inbreeding where the offspring differs at only a single locus through a mutation occurring in the original inbred strain.
       * - selective inbred
         - 'Selective inbred' breeding (or selective inbreeding) is the production of offspring from mating organisms that are genetically closely related (same background breed) and have been selected based on a particular phenotype.
       * - congenic
         - 'Congenic' breeding is the production of offspring from repeated backcrossing into an inbred (background) strain, with selection for a particular marker, ideally a single gene from another strain.
       * - hybrid
         - A 'hybrid' is an organism that resulted from special outbreeding of two species (normally within the same genus).
       * - inbred
         - 'Inbred' breeding (or inbreeding) is the production of offspring from mating organisms that are genetically closely related (same background breed).

    """
    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/BreedingType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the breeding type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the breeding type."),
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
