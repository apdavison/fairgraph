"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FileRepositoryStructure
from fairgraph import KGObject


class FileRepositoryStructure(KGObject, FileRepositoryStructure):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/FileRepositoryStructure"
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
