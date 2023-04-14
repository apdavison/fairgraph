"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ParcellationEntity(KGObject):
    """ """

    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/ParcellationEntity"]
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
            doc="Word or phrase that constitutes the distinctive designation of the parcellation entity.",
        ),
        Field(
            "lookup_label", str, "vocab:lookupLabel", multiple=False, required=False, doc="no description available"
        ),
        Field(
            "abbreviation", str, "vocab:abbreviation", multiple=False, required=False, doc="no description available"
        ),
        Field(
            "alternate_names",
            str,
            "vocab:alternateName",
            multiple=True,
            required=False,
            doc="no description available",
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
            "has_parents",
            "openminds.sands.ParcellationEntity",
            "vocab:hasParent",
            multiple=True,
            required=False,
            doc="Reference to a parent object or legal person.",
        ),
        Field(
            "versions",
            "openminds.sands.ParcellationEntityVersion",
            "vocab:hasVersion",
            multiple=True,
            required=False,
            doc="Reference to variants of an original.",
        ),
        Field(
            "ontology_identifiers",
            str,
            "vocab:ontologyIdentifier",
            multiple=True,
            required=False,
            doc="Term or code used to identify the parcellation entity registered within a particular ontology.",
        ),
        Field(
            "related_uberon_term",
            ["openminds.controlledterms.Organ", "openminds.controlledterms.UBERONParcellation"],
            "vocab:relatedUBERONTerm",
            multiple=False,
            required=False,
            doc="no description available",
        ),
    ]
    existence_query_fields = ("name",)

    def __init__(
        self,
        name=None,
        lookup_label=None,
        abbreviation=None,
        alternate_names=None,
        definition=None,
        has_parents=None,
        versions=None,
        ontology_identifiers=None,
        related_uberon_term=None,
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
            lookup_label=lookup_label,
            abbreviation=abbreviation,
            alternate_names=alternate_names,
            definition=definition,
            has_parents=has_parents,
            versions=versions,
            ontology_identifiers=ontology_identifiers,
            related_uberon_term=related_uberon_term,
        )
