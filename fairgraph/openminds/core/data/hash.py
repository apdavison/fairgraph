"""
Structured information on a hash.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.v4.core import Hash as OMHash
from fairgraph import EmbeddedMetadata


class Hash(EmbeddedMetadata, OMHash):
    """
    Structured information on a hash.
    """

    type_ = "https://openminds.om-i.org/types/Hash"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("algorithm", "digest")

    def __init__(self, algorithm=None, digest=None, id=None, data=None, space=None, release_status=None):
        return EmbeddedMetadata.__init__(self, data=data, algorithm=algorithm, digest=digest)
