"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class BrainAtlas(KGObjectV3):
    """
    Structured information on a brain atlas (concept level).
    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/BrainAtlas"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=True,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.ISBN"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("has_terminology", "openminds.sands.ParcellationTerminology", "vocab:hasTerminology", multiple=False, required=True,
              doc="no description available"),
        Field("versions", "openminds.sands.BrainAtlasVersion", "vocab:hasVersion", multiple=True, required=False,
              doc="Reference to variants of an original."),
        
    ]
    existence_query_fields = ('digital_identifier',)

