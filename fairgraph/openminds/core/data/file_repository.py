"""
Structured information on a file repository.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FileRepository
from fairgraph import KGObject


from openminds import IRI


class FileRepository(KGObject, FileRepository):
    """
    Structured information on a file repository.
    """

    type_ = "https://openminds.om-i.org/types/FileRepository"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "contains_content_of",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "repository",
            reverse="repository",
            multiple=True,
            description="reverse of 'repository'",
        ),
        Property(
            "files",
            "openminds.latest.core.File",
            "fileRepository",
            reverse="file_repository",
            multiple=True,
            description="reverse of 'file_repository'",
        ),
        Property(
            "has_parts",
            "openminds.latest.core.FileBundle",
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
    ]
    existence_query_properties = ("iri",)

    def __init__(
        self,
        name=None,
        contains_content_of=None,
        content_type_patterns=None,
        files=None,
        format=None,
        has_parts=None,
        hash=None,
        hosted_by=None,
        iri=None,
        storage_size=None,
        structure_pattern=None,
        type=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            contains_content_of=contains_content_of,
            content_type_patterns=content_type_patterns,
            files=files,
            format=format,
            has_parts=has_parts,
            hash=hash,
            hosted_by=hosted_by,
            iri=iri,
            storage_size=storage_size,
            structure_pattern=structure_pattern,
            type=type,
        )
