"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Rectangle as OMRectangle
from fairgraph import EmbeddedMetadata


class Rectangle(EmbeddedMetadata, OMRectangle):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Rectangle"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, length=None, width=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, length=length, width=width)


# cast openMINDS instances to their fairgraph subclass
Rectangle.set_error_handling(None)
for key, value in OMRectangle.__dict__.items():
    if isinstance(value, OMRectangle):
        fg_instance = Rectangle.from_jsonld(value.to_jsonld())
        fg_instance._space = Rectangle.default_space
        setattr(Rectangle, key, fg_instance)
Rectangle.set_error_handling("log")
