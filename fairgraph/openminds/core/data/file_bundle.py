"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class FileBundle(KGObject):
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
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the file bundle."),
        Field("content_description", str, "vocab:contentDescription", multiple=False, required=False,
              doc="no description available"),
        Field("descended_from", ["openminds.computation.LocalFile", "openminds.controlledterms.Technique", "openminds.core.BehavioralProtocol", "openminds.core.File", "openminds.core.FileBundle", "openminds.core.Subject", "openminds.core.SubjectGroup", "openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSample", "openminds.core.TissueSampleCollection", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"], "vocab:descendedFrom", multiple=False, required=False,
              doc="no description available"),
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=False,
              doc="Method of digitally organizing and structuring data or information."),
        Field("grouping_type", "openminds.controlledterms.FileBundleGrouping", "vocab:groupingType", multiple=False, required=False,
              doc="no description available"),
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("is_part_of", ["openminds.core.FileBundle", "openminds.core.FileRepository"], "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = ('name', 'is_part_of')
