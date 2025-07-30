"""
Structured information on the copyright.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Copyright
from fairgraph import EmbeddedMetadata


class Copyright(EmbeddedMetadata, Copyright):
    """
    Structured information on the copyright.
    """

    type_ = "https://openminds.ebrains.eu/core/Copyright"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, holders=None, years=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, holders=holders, years=years)
