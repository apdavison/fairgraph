"""
Structured information on a file repository.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class FileRepository(KGObjectV3):
    """
    Structured information on a file repository.
    """
    default_space = "model"
    type = ["https://openminds.ebrains.eu/core/FileRepository"]
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
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("hosted_by", "openminds.core.Organization", "vocab:hostedBy", multiple=False, required=True,
              doc="Reference to an organization that provides facilities and services for something."),
        Field("iri", str, "vocab:IRI", multiple=False, required=True,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("repository_type", "openminds.controlledterms.FileRepositoryType", "vocab:repositoryType", multiple=False, required=False,
              doc="no description available"),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = None