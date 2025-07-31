"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ResearchProductGroup
from fairgraph import KGObject


class ResearchProductGroup(KGObject, ResearchProductGroup):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ResearchProductGroup"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("context", "has_parts")

    def __init__(self, context=None, has_parts=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self, id=id, space=space, scope=scope, data=data, context=context, has_parts=has_parts
        )
