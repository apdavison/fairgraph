"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import StringProperty as OMStringProperty
from fairgraph import EmbeddedMetadata


class StringProperty(EmbeddedMetadata, OMStringProperty):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/StringProperty"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, name=None, value=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, name=name, value=value)


# cast openMINDS instances to their fairgraph subclass
StringProperty.set_error_handling(None)
for key, value in OMStringProperty.__dict__.items():
    if isinstance(value, OMStringProperty):
        fg_instance = StringProperty.from_jsonld(value.to_jsonld())
        fg_instance._space = StringProperty.default_space
        setattr(StringProperty, key, fg_instance)
StringProperty.set_error_handling("log")
