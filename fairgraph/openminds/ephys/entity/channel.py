"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.ephys import Channel as OMChannel
from fairgraph import EmbeddedMetadata


class Channel(EmbeddedMetadata, OMChannel):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Channel"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, internal_identifier=None, unit=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, internal_identifier=internal_identifier, unit=unit)


# cast openMINDS instances to their fairgraph subclass
Channel.set_error_handling(None)
for key, value in OMChannel.__dict__.items():
    if isinstance(value, OMChannel):
        fg_instance = Channel.from_jsonld(value.to_jsonld())
        fg_instance._space = Channel.default_space
        setattr(Channel, key, fg_instance)
Channel.set_error_handling("log")
