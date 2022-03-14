"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class LivePaperResourceItem(KGObject):
    """

    """
    default_space = "publications"
    type = ["https://openminds.ebrains.eu/publications/LivePaperResourceItem"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the live paper resource item."),
        Field("iri", IRI, "vocab:IRI", multiple=False, required=False,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("is_part_of", "openminds.publications.LivePaperSection", "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("resource_type", "openminds.publications.LivePaperResourceType", "vocab:resourceType", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'is_part_of', 'resource_type')
