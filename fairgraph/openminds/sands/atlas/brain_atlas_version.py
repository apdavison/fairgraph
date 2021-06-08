"""
Structured information on a brain atlas (version level).
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class BrainAtlasVersion(KGObjectV3):
    """
    Structured information on a brain atlas (version level).
    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/sands/BrainAtlasVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("coordinate_space", "openminds.sands.CommonCoordinateSpace", "vocab:coordinateSpace", multiple=False, required=True,
              doc="Two or three dimensional geometric setting."),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the brain atlas version."),
        Field("has_terminology", "openminds.sands.ParcellationTerminology", "vocab:hasTerminology", multiple=False, required=True,
              doc="no description available"),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of something or someone."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("is_alternative_version_ofs", "openminds.sands.BrainAtlasVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.sands.BrainAtlasVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        Field("release_date", str, "vocab:releaseDate", multiple=False, required=True,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the brain atlas version."),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = ("alias", "version_identifier")
