"""
Structured information on a file instances.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field


import os
import hashlib
import mimetypes
from .hash import Hash
from .content_type import ContentType
from ..miscellaneous.quantitative_value import QuantitativeValue
from ...controlledterms.unit_of_measurement import UnitOfMeasurement

mimetypes.init()

def sha1sum(filename):
    BUFFER_SIZE = 128*1024
    h = hashlib.sha1()
    with open(filename, 'rb') as fp:
        while True:
            data = fp.read(BUFFER_SIZE)
            if not data:
                break
            h.update(data)
    return h.hexdigest()



class File(KGObjectV3):
    """
    Structured information on a file instances.
    """
    default_space = "files"
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
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=True, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("iri", IRI, "vocab:IRI", multiple=False, required=True,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("is_part_of", "openminds.core.FileBundle", "vocab:isPartOf", multiple=True, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the file."),
        Field("special_usage_role", "openminds.controlledterms.FileUsageRole", "vocab:specialUsageRole", multiple=False, required=False,
              doc="Particular function of something when it is used."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = ('iri', 'hash')


    @classmethod
    def from_local_file(cls, relative_path):
        cls.set_strict_mode(False)
        obj = cls(
            name=relative_path,
            storage_size=QuantitativeValue(value=float(
                os.stat(relative_path).st_size), unit=UnitOfMeasurement(name="bytes")),
            hash=Hash(algorithm="SHA1", digest=sha1sum(relative_path)),
            format=ContentType(name=mimetypes.guess_type(relative_path)[0])
            # todo: query ContentTypes since that contains additional, EBRAINS-specific content types
        )
        cls.set_strict_mode(True)
        return obj
