"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class ParcellationTerminologyVersion(KGObjectV3):
    """
    
    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("defined_ins", "openminds.core.File", "vocab:definedIn", multiple=True, required=False,
              doc="Reference to a file instance in which something is stored."),
        Field("name", str, "vocab:fullName", multiple=False, required=False,
              doc="Whole, non-abbreviated name of the parcellation terminology version."),
        Field("has_entity_versions", "openminds.sands.ParcellationEntityVersion", "vocab:hasEntityVersion", multiple=True, required=True,
              doc="no description available"),
        Field("is_alternative_version_of", "openminds.sands.ParcellationTerminologyVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.sands.ParcellationTerminologyVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("ontology_identifier", IRI, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the parcellation terminology version registered within a particular ontology."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the parcellation terminology version."),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),
        
    ]
    existence_query_fields = ('alias', 'version_identifier')

