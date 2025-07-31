"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Contribution
from fairgraph import EmbeddedMetadata


class Contribution(EmbeddedMetadata, Contribution):
    """
    Structured information on the contribution made to a research product.
    """

    type_ = "https://openminds.om-i.org/types/Contribution"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, contributor=None, types=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, contributor=contributor, types=types)
