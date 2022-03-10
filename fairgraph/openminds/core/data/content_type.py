"""
Structured information on the content type of a file instance, bundle or repository.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ContentType(KGObject):
    """
    Structured information on the content type of a file instance, bundle or repository.
    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/core/ContentType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the content type."),
        Field("data_types", "openminds.controlledterms.DataType", "vocab:dataType", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the content type."),
        Field("display_label", str, "vocab:displayLabel", multiple=False, required=False,
              doc="no description available"),
        Field("file_extensions", str, "vocab:fileExtension", multiple=True, required=False,
              doc="String of characters attached as suffix to the names of files of a particular format."),
        Field("related_media_type", IRI, "vocab:relatedMediaType", multiple=False, required=False,
              doc="Reference to an official two-part identifier for file formats and format contents."),
        Field("specification", IRI, "vocab:specification", multiple=False, required=False,
              doc="Detailed and precise presentation of, or proposal for something."),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name',)
