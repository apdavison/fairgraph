"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


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
    fields = [
        Field(
            "name",
            str,
            "vocab:fullName",
            multiple=False,
            required=True,
            doc="Whole, non-abbreviated name of the brain atlas.",
        ),
        Field(
            "alias",
            str,
            "vocab:shortName",
            multiple=False,
            required=True,
            doc="Shortened or fully abbreviated name of the brain atlas.",
        ),
        Field(
            "abbreviation",
            str,
            "vocab:abbreviation",
            multiple=False,
            required=False,
            doc="no description available",
        ),
        Field(
            "authors",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:author",
            multiple=True,
            required=True,
            doc="Creator of a literary or creative work, as well as a dataset publication.",
        ),
        Field(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            required=False,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            multiple=False,
            required=True,
            doc="Longer statement or account giving the characteristics of the brain atlas.",
        ),
        Field(
            "digital_identifier",
            ["openminds.core.DOI", "openminds.core.ISBN", "openminds.core.RRID"],
            "vocab:digitalIdentifier",
            multiple=False,
            required=False,
            doc="Digital handle to identify objects or legal persons.",
        ),
        Field(
            "has_terminology",
            "openminds.sands.ParcellationTerminology",
            "vocab:hasTerminology",
            multiple=False,
            required=True,
            doc="no description available",
        ),
        Field(
            "versions",
            "openminds.sands.BrainAtlasVersion",
            "vocab:hasVersion",
            multiple=True,
            required=True,
            doc="Reference to variants of an original.",
        ),
        Field(
            "homepage",
            IRI,
            "vocab:homepage",
            multiple=False,
            required=False,
            doc="Main website of the brain atlas.",
        ),
        Field(
            "how_to_cite",
            str,
            "vocab:howToCite",
            multiple=False,
            required=False,
            doc="Preferred format for citing a particular object or legal person.",
        ),
        Field(
            "ontology_identifier",
            IRI,
            "vocab:ontologyIdentifier",
            multiple=False,
            required=False,
            doc="Term or code used to identify the brain atlas registered within a particular ontology.",
        ),
        Field(
            "used_species",
            "openminds.controlledterms.Species",
            "vocab:usedSpecies",
            multiple=False,
            required=False,
            doc="no description available",
        ),
    ]
    existence_query_fields = ("digital_identifier",)

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
        versions=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifier=None,
        used_species=None,
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
            versions=versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifier=ontology_identifier,
            used_species=used_species,
        )
