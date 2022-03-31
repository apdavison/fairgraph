"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class LocalFile(KGObject):
    """

    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/LocalFile"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the local file."),
        Field("content_description", str, "vocab:contentDescription", multiple=False, required=False,
              doc="no description available"),
        Field("data_types", "openminds.controlledterms.DataType", "vocab:dataType", multiple=True, required=False,
              doc="no description available"),
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=False,
              doc="Method of digitally organizing and structuring data or information."),
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("path", str, "vocab:path", multiple=False, required=True,
              doc="no description available"),
        Field("special_usage_role", "openminds.controlledterms.FileUsageRole", "vocab:specialUsageRole", multiple=False, required=False,
              doc="Particular function of something when it is used."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = ('name', 'path')
