"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import CoordinatePoint as OMCoordinatePoint
from fairgraph import EmbeddedMetadata


class CoordinatePoint(EmbeddedMetadata, OMCoordinatePoint):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CoordinatePoint"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, coordinate_space=None, coordinates=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, coordinate_space=coordinate_space, coordinates=coordinates)


# cast openMINDS instances to their fairgraph subclass
CoordinatePoint.set_error_handling(None)
for key, value in OMCoordinatePoint.__dict__.items():
    if isinstance(value, OMCoordinatePoint):
        fg_instance = CoordinatePoint.from_jsonld(value.to_jsonld())
        fg_instance._space = CoordinatePoint.default_space
        setattr(CoordinatePoint, key, fg_instance)
CoordinatePoint.set_error_handling("log")
