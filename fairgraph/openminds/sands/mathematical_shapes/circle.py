"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Circle
from fairgraph import EmbeddedMetadata


class Circle(EmbeddedMetadata, Circle):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Circle"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, radius=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, radius=radius)
