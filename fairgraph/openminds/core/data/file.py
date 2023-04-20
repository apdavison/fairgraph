"""
Structured information on a file instance that is accessible via a URL.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field

import os
import hashlib
import mimetypes
from pathlib import Path
from urllib.request import urlretrieve
from urllib.parse import quote, urlparse, urlunparse
from .hash import Hash
from .content_type import ContentType
from ..miscellaneous.quantitative_value import QuantitativeValue
from ...controlledterms.unit_of_measurement import UnitOfMeasurement
from fairgraph.utility import accepted_terms_of_use

mimetypes.init()


def sha1sum(filename):
    BUFFER_SIZE = 128 * 1024
    h = hashlib.sha1()
    with open(filename, "rb") as fp:
        while True:
            data = fp.read(BUFFER_SIZE)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


class File(KGObject):
    """
    Structured information on a file instance that is accessible via a URL.
    """

    default_space = "files"
    type_ = ["https://openminds.ebrains.eu/core/File"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the file.",
        ),
        Field(
            "iri",
            IRI,
            "vocab:IRI",
            required=True,
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
        Field("content_description", str, "vocab:contentDescription", doc="no description available"),
        Field(
            "data_types",
            "openminds.controlledterms.DataType",
            "vocab:dataType",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "file_repository", "openminds.core.FileRepository", "vocab:fileRepository", doc="no description available"
        ),
        Field(
            "format",
            "openminds.core.ContentType",
            "vocab:format",
            doc="Method of digitally organizing and structuring data or information.",
        ),
        Field(
            "hash",
            "openminds.core.Hash",
            "vocab:hash",
            multiple=True,
            doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
        ),
        Field(
            "is_part_of",
            "openminds.core.FileBundle",
            "vocab:isPartOf",
            multiple=True,
            doc="Reference to the ensemble of multiple things or beings.",
        ),
        Field(
            "special_usage_role",
            "openminds.controlledterms.FileUsageRole",
            "vocab:specialUsageRole",
            doc="Particular function of something when it is used.",
        ),
        Field(
            "storage_size",
            "openminds.core.QuantitativeValue",
            "vocab:storageSize",
            doc="Quantitative value defining how much disk space is used by an object on a computer system.",
        ),
    ]
    existence_query_fields = ("iri", "hash")

    def __init__(
        self,
        name=None,
        iri=None,
        content_description=None,
        data_types=None,
        file_repository=None,
        format=None,
        hash=None,
        is_part_of=None,
        special_usage_role=None,
        storage_size=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            iri=iri,
            content_description=content_description,
            data_types=data_types,
            file_repository=file_repository,
            format=format,
            hash=hash,
            is_part_of=is_part_of,
            special_usage_role=special_usage_role,
            storage_size=storage_size,
        )

    @classmethod
    def from_local_file(cls, relative_path):
        obj = cls(
            name=relative_path,
            storage_size=QuantitativeValue(
                value=float(os.stat(relative_path).st_size), unit=UnitOfMeasurement(name="bytes")
            ),
            hash=Hash(algorithm="SHA1", digest=sha1sum(relative_path)),
            format=ContentType(name=mimetypes.guess_type(relative_path)[0])
            # todo: query ContentTypes since that contains additional, EBRAINS-specific content types
        )
        return obj

    def download(self, local_path, client, accept_terms_of_use=False):
        if accepted_terms_of_use(client, accept_terms_of_use=accept_terms_of_use):
            local_path = Path(local_path)
            if local_path.is_dir():
                local_filename = local_path / self.name
            else:
                local_filename = local_path
                local_filename.parent.mkdir(parents=True, exist_ok=True)
            url_parts = urlparse(self.iri.value)
            url_parts = url_parts._replace(path=quote(url_parts.path))
            url = urlunparse(url_parts)
            local_filename, headers = urlretrieve(url, local_filename)
            # todo: check hash value of downloaded file
            # todo: if local_path isn't an existing directory but looks like a directory name
            #       rather than a filename, create that directory and save a file called self.name
            #       within it
            return local_filename
