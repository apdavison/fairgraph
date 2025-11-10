"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.v4.sands import Circle as OMCircle
from fairgraph import EmbeddedMetadata


class Circle(EmbeddedMetadata, OMCircle):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Circle"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("radius",)

    def __init__(self, radius=None, id=None, data=None, space=None, release_status=None):
        return EmbeddedMetadata.__init__(self, data=data, radius=radius)
