"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class SingleColor(KGObject):
    """
    <description not available>
    """

    default_space = "atlas"
    type_ = "https://openminds.ebrains.eu/sands/SingleColor"
    properties = [
        Property("value", str, "vocab:value", required=True, doc="Entry for a property."),
    ]
    reverse_properties = []
    existence_query_properties = ("value",)

    def __init__(self, value=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, space=space, scope=scope, data=data, value=value)
