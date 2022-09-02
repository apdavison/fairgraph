"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class LivePaperSection(KGObject):
    """

    """
    default_space = "livepapers"
    type = ["https://openminds.ebrains.eu/publications/LivePaperSection"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the live paper section."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the live paper section."),
        Field("is_part_of", "openminds.publications.LivePaperVersion", "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("order", int, "vocab:order", multiple=False, required=True,
              doc="no description available"),
        Field("section_type", str, "vocab:sectionType", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'is_part_of', 'order', 'section_type')
