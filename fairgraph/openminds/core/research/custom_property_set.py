"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class CustomPropertySet(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/core/CustomPropertySet"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("context", str, "vocab:context", multiple=False, required=True,
              doc="no description available"),
        Field("defined_in", ["openminds.core.Configuration", "openminds.core.File", "openminds.core.PropertyValueList"], "vocab:definedIn", multiple=False, required=True,
              doc="Reference to a file instance in which something is stored."),
        Field("relevant_for", "openminds.controlledterms.Technique", "vocab:relevantFor", multiple=False, required=True,
              doc="Reference to what or whom the custom property set bears siginificance."),

    ]
