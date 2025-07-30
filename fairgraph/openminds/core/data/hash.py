"""
Structured information on a hash.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Hash
from fairgraph import EmbeddedMetadata


class Hash(EmbeddedMetadata, Hash):
    """
    Structured information on a hash.
    """

    type_ = "https://openminds.ebrains.eu/core/Hash"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, algorithm=None, digest=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, algorithm=algorithm, digest=digest)
