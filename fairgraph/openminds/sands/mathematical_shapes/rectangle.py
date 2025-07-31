"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Rectangle
from fairgraph import EmbeddedMetadata


class Rectangle(EmbeddedMetadata, Rectangle):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Rectangle"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, length=None, width=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, length=length, width=width)
