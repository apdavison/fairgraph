"""
Structured information on a research project.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Protocol(KGObject):
    """
    Structured information on a research project.
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Protocol"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the protocol."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the protocol."),
        Field("stimulations", "openminds.core.Stimulation", "vocab:stimulation", multiple=True, required=False,
              doc="no description available"),
        Field("techniques", "openminds.controlledterms.Technique", "vocab:technique", multiple=True, required=True,
              doc="Method of accomplishing a desired aim."),

    ]
    existence_query_fields = ('name',)
