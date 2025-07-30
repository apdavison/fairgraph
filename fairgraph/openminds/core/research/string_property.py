"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import StringProperty
from fairgraph import EmbeddedMetadata


class StringProperty(EmbeddedMetadata, StringProperty):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/StringProperty"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, name=None, value=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, name=name, value=value)
