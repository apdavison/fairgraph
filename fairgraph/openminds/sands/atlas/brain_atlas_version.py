"""
Structured information on a brain atlas (version level).
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class BrainAtlasVersion(KGObjectV3):
    """
    Structured information on a brain atlas (version level).
    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/BrainAtlasVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("coordinate_space", "openminds.sands.CommonCoordinateSpace", "vocab:coordinateSpace", multiple=False, required=True,
              doc="Two or three dimensional geometric setting."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.ISBN"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("has_terminology_version", "openminds.sands.ParcellationTerminologyVersion", "vocab:hasTerminologyVersion", multiple=False, required=True,
              doc="no description available"),
        Field("is_alternative_version_of", "openminds.sands.BrainAtlasVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.sands.BrainAtlasVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("license", "openminds.core.License", "vocab:license", multiple=False, required=True,
              doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something."),
        Field("ontology_identifier", IRI, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the brain atlas version registered within a particular ontology."),
        
    ]
    existence_query_fields = ('alias', 'version_identifier')

