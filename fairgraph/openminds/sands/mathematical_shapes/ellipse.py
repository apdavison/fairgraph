"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import Ellipse as OMEllipse
from fairgraph import EmbeddedMetadata


class Ellipse(EmbeddedMetadata, OMEllipse):
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


# cast openMINDS instances to their fairgraph subclass
Ellipse.set_error_handling(None)
for key, value in OMEllipse.__dict__.items():
    if isinstance(value, OMEllipse):
        fg_instance = Ellipse.from_jsonld(value.to_jsonld())
        fg_instance._space = Ellipse.default_space
        setattr(Ellipse, key, fg_instance)
Ellipse.set_error_handling("log")
