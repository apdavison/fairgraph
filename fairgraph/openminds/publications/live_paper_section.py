"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class LivePaperSection(KGObject):
    """

    """
    default_space = "livepapers"
    type_ = ["https://openminds.ebrains.eu/publications/LivePaperSection"]
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
        Field("type", str, "vocab:type", multiple=False, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]
    existence_query_fields = ('name', 'is_part_of', 'order', 'type')

    def __init__(self, name=None, description=None, is_part_of=None, order=None, type=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, description=description, is_part_of=is_part_of, order=order, type=type)