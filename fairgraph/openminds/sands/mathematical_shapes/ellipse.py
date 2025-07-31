"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Ellipse
from fairgraph import EmbeddedMetadata


class Ellipse(EmbeddedMetadata, Ellipse):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Ellipse"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, semi_major_axis=None, semi_minor_axis=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(
            self, data=data, semi_major_axis=semi_major_axis, semi_minor_axis=semi_minor_axis
        )
