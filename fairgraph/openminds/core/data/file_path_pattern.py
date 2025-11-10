"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.v4.core import FilePathPattern as OMFilePathPattern
from fairgraph import EmbeddedMetadata


class FilePathPattern(EmbeddedMetadata, OMFilePathPattern):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/FilePathPattern"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("grouping_types", "regex")

    def __init__(self, grouping_types=None, regex=None, id=None, data=None, space=None, release_status=None):
        return EmbeddedMetadata.__init__(self, data=data, grouping_types=grouping_types, regex=regex)
