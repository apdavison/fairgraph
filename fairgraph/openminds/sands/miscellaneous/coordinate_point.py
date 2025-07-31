"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CoordinatePoint
from fairgraph import EmbeddedMetadata


class CoordinatePoint(EmbeddedMetadata, CoordinatePoint):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CoordinatePoint"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, coordinate_space=None, coordinates=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, coordinate_space=coordinate_space, coordinates=coordinates)
