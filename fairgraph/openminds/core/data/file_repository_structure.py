"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FileRepositoryStructure as OMFileRepositoryStructure
from fairgraph import KGObject


class FileRepositoryStructure(KGObject, OMFileRepositoryStructure):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/FileRepositoryStructure"
    default_space = "files"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "structures",
            "openminds.latest.core.FileRepository",
            "structurePattern",
            reverse="structure_pattern",
            multiple=True,
            description="reverse of 'structure_pattern'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self, lookup_label=None, file_path_patterns=None, structures=None, id=None, data=None, space=None, scope=None
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            file_path_patterns=file_path_patterns,
            structures=structures,
        )


# cast openMINDS instances to their fairgraph subclass
FileRepositoryStructure.set_error_handling(None)
for key, value in OMFileRepositoryStructure.__dict__.items():
    if isinstance(value, OMFileRepositoryStructure):
        fg_instance = FileRepositoryStructure.from_jsonld(value.to_jsonld())
        fg_instance._space = FileRepositoryStructure.default_space
        setattr(FileRepositoryStructure, key, fg_instance)
FileRepositoryStructure.set_error_handling("log")
