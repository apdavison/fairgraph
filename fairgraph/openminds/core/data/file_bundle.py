"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class FileBundle(KGObjectV3):
    """
    Structured information on a bundle of file instances.
    """
    default_space = "files"
    type = ["https://openminds.ebrains.eu/core/FileBundle"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=False,
              doc="Method of digitally organizing and structuring data or information."),
        Field("pattern_of_filenames", str, "vocab:patternOfFilenames", multiple=False, required=False,
              doc="Reliable sample / structure of characters valid for all names in a particular collection of files."),
        Field("grouped_by", "openminds.controlledterms.FileBundleGrouping", "vocab:groupedBy", multiple=False, required=False,
              doc="Reference to the aspect used to group something."),
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("is_part_of", ["openminds.core.FileBundle", "openminds.core.FileRepository"], "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = ("hash",)
