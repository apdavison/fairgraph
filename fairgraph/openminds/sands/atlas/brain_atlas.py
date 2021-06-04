"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class BrainAtlas(KGObjectV3):
    """
    Structured information on a brain atlas (concept level).
    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/sands/BrainAtlas"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the brain atlas."),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the brain atlas."),
        Field("versions", "openminds.sands.BrainAtlasVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of something or someone."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the brain atlas."),

    ]
    existence_query_fields = None