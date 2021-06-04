"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class ParcellationTerminology(KGObjectV3):
    """

    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/sands/ParcellationTerminology"]
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
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the parcellation terminology."),
        Field("is_alternative_version_ofs", "openminds.sands.ParcellationTerminology", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.sands.ParcellationTerminology", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the parcellation terminology."),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = None