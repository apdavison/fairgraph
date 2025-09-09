"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FilePathPattern as OMFilePathPattern
from fairgraph import EmbeddedMetadata


class FilePathPattern(EmbeddedMetadata, OMFilePathPattern):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/FilePathPattern"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, grouping_types=None, regex=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, grouping_types=grouping_types, regex=regex)


# cast openMINDS instances to their fairgraph subclass
FilePathPattern.set_error_handling(None)
for key, value in OMFilePathPattern.__dict__.items():
    if isinstance(value, OMFilePathPattern):
        fg_instance = FilePathPattern.from_jsonld(value.to_jsonld())
        fg_instance._space = FilePathPattern.default_space
        setattr(FilePathPattern, key, fg_instance)
FilePathPattern.set_error_handling("log")
