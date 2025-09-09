"""
Structured information on the copyright.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Copyright as OMCopyright
from fairgraph import EmbeddedMetadata


class Copyright(EmbeddedMetadata, OMCopyright):
    """
    Structured information on the copyright.
    """

    type_ = "https://openminds.om-i.org/types/Copyright"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, holders=None, years=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, holders=holders, years=years)


# cast openMINDS instances to their fairgraph subclass
Copyright.set_error_handling(None)
for key, value in OMCopyright.__dict__.items():
    if isinstance(value, OMCopyright):
        fg_instance = Copyright.from_jsonld(value.to_jsonld())
        fg_instance._space = Copyright.default_space
        setattr(Copyright, key, fg_instance)
Copyright.set_error_handling("log")
