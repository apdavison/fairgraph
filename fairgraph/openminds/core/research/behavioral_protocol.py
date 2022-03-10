"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class BehavioralProtocol(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/BehavioralProtocol"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the behavioral protocol."),
        Field("described_in", ["openminds.core.DOI", "openminds.core.File", "openminds.core.URL"], "vocab:describedIn", multiple=False, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the behavioral protocol."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the behavioral protocol within a particular product."),
        Field("stimulations", "openminds.core.Stimulation", "vocab:stimulation", multiple=True, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'description')
