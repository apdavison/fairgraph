"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import SingleColor
from fairgraph import KGObject


class SingleColor(KGObject, SingleColor):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/SingleColor"
    default_space = "atlas"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("value",)

    def __init__(self, value=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(self, id=id, space=space, scope=scope, data=data, value=value)
