"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from fairgraph.base import IRI


class BrainAtlas(KGObject):
    """
    Structured information on a brain atlas (concept level).
    """

    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/BrainAtlas"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    properties = [
        Property("name", str, "vocab:fullName", required=True, doc="Whole, non-abbreviated name of the brain atlas."),
        Property(
            "alias",
            str,
            "vocab:shortName",
            required=True,
            doc="Shortened or fully abbreviated name of the brain atlas.",
        ),
        Property("abbreviation", str, "vocab:abbreviation", doc="no description available"),
        Property(
            "authors",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:author",
            multiple=True,
            required=True,
            doc="Creator of a literary or creative work, as well as a dataset publication.",
        ),
        Property(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            required=True,
            doc="Longer statement or account giving the characteristics of the brain atlas.",
        ),
        Property(
            "digital_identifier",
            ["openminds.core.DOI", "openminds.core.ISBN", "openminds.core.RRID"],
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property(
            "has_terminology",
            "openminds.sands.ParcellationTerminology",
            "vocab:hasTerminology",
            required=True,
            doc="no description available",
        ),
        Property("homepage", IRI, "vocab:homepage", doc="Main website of the brain atlas."),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",
            doc="Preferred format for citing a particular object or legal person.",
        ),
        Property(
            "ontology_identifier",
            IRI,
            "vocab:ontologyIdentifier",
            doc="Term or code used to identify the brain atlas registered within a particular ontology.",
        ),
        Property(
            "used_species", "openminds.controlled_terms.Species", "vocab:usedSpecies", doc="no description available"
        ),
        Property(
            "versions",
            "openminds.sands.BrainAtlasVersion",
            "vocab:hasVersion",
            multiple=True,
            required=True,
            doc="Reference to variants of an original.",
        ),
        Property(
            "comments",
            "openminds.core.Comment",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
        Property(
            "is_input_to",
            "openminds.core.DatasetVersion",
            "^vocab:inputData",
            reverse="input_data",
            multiple=True,
            doc="reverse of 'inputData'",
        ),
        Property(
            "is_part_of",
            ["openminds.core.Project", "openminds.core.ResearchProductGroup"],
            "^vocab:hasPart",
            reverse="has_parts",
            multiple=True,
            doc="reverse of 'hasPart'",
        ),
        Property(
            "learning_resources",
            "openminds.publications.LearningResource",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
    ]
    existence_query_properties = ("digital_identifier",)

    def __init__(
        self,
        name=None,
        alias=None,
        abbreviation=None,
        authors=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        has_terminology=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifier=None,
        used_species=None,
        versions=None,
        comments=None,
        is_input_to=None,
        is_part_of=None,
        learning_resources=None,
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
            alias=alias,
            abbreviation=abbreviation,
            authors=authors,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            has_terminology=has_terminology,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifier=ontology_identifier,
            used_species=used_species,
            versions=versions,
            comments=comments,
            is_input_to=is_input_to,
            is_part_of=is_part_of,
            learning_resources=learning_resources,
        )
