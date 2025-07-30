"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ContentTypePattern
from fairgraph import KGObject


class ContentTypePattern(KGObject, ContentTypePattern):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ContentTypePattern"
    default_space = "files"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies_content_of",
            "openminds.latest.core.FileRepository",
            "contentTypePattern",
            reverse="content_type_patterns",
            multiple=True,
            description="reverse of 'content_type_patterns'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        content_type=None,
        identifies_content_of=None,
        regex=None,
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
            lookup_label=lookup_label,
            content_type=content_type,
            identifies_content_of=identifies_content_of,
            regex=regex,
        )
