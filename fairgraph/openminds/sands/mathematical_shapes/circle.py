"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Circle as OMCircle
from fairgraph import EmbeddedMetadata


class Circle(EmbeddedMetadata, OMCircle):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Circle"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, radius=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, radius=radius)


# cast openMINDS instances to their fairgraph subclass
Circle.set_error_handling(None)
for key, value in OMCircle.__dict__.items():
    if isinstance(value, OMCircle):
        fg_instance = Circle.from_jsonld(value.to_jsonld())
        fg_instance._space = Circle.default_space
        setattr(Circle, key, fg_instance)
Circle.set_error_handling("log")
