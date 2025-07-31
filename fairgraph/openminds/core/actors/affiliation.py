"""
Structured information about a relationship between two entities, such as a person and their employer.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Affiliation
from fairgraph import EmbeddedMetadata


from datetime import date


class Affiliation(EmbeddedMetadata, Affiliation):
    """
    Structured information about a relationship between two entities, such as a person and their employer.
    """

    type_ = "https://openminds.om-i.org/types/Affiliation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, end_date=None, member_of=None, start_date=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(
            self, data=data, end_date=end_date, member_of=member_of, start_date=start_date
        )
