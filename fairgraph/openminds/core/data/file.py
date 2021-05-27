"""
Structured information on a file instances.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class File(KGObject):
    """
    Structured information on a file instances.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/File"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("content", str, "vocab:content", multiple=False, required=False,
              doc="Something that is contained."),
        Field("file_repository", "openminds.core.FileRepository", "vocab:fileRepository", multiple=False, required=False,
              doc="no description available"),
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=False,
              doc="Method of digitally organizing and structuring data or information."),
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("iri", str, "vocab:IRI", multiple=False, required=True,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("is_part_ofs", "openminds.core.FileBundle", "vocab:isPartOf", multiple=True, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("special_usage_role", "openminds.controlledterms.FileUsageRole", "vocab:specialUsageRole", multiple=False, required=False,
              doc="Particular function of something when it is used."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),
        
    ]
    existence_query_fields = None