"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import Channel
from fairgraph import EmbeddedMetadata


class Channel(EmbeddedMetadata, Channel):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/ephys/Channel"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, internal_identifier=None, unit=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, internal_identifier=internal_identifier, unit=unit)
