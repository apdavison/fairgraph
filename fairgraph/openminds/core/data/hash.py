"""
Structured information on a hash.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Hash as OMHash
from fairgraph import EmbeddedMetadata


class Hash(EmbeddedMetadata, OMHash):
    """
    Structured information on a hash.
    """

    type_ = "https://openminds.om-i.org/types/Hash"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, algorithm=None, digest=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, algorithm=algorithm, digest=digest)


# cast openMINDS instances to their fairgraph subclass
Hash.set_error_handling(None)
for key, value in OMHash.__dict__.items():
    if isinstance(value, OMHash):
        fg_instance = Hash.from_jsonld(value.to_jsonld())
        fg_instance._space = Hash.default_space
        setattr(Hash, key, fg_instance)
Hash.set_error_handling("log")
