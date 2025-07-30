"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FilePathPattern
from fairgraph import EmbeddedMetadata


class FilePathPattern(EmbeddedMetadata, FilePathPattern):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/FilePathPattern"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, grouping_types=None, regex=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, grouping_types=grouping_types, regex=regex)
