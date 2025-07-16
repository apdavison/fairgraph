"""
Structured information about a relationship between two entities, such as a person and their employer.
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


from datetime import date


class Affiliation(EmbeddedMetadata):
    """
    Structured information about a relationship between two entities, such as a person and their employer.
    """

    type_ = "https://openminds.ebrains.eu/core/Affiliation"
    properties = [
        Property(
            "end_date",
            date,
            "vocab:endDate",
            doc="Date in the Gregorian calendar at which something terminates in time.",
        ),
        Property(
            "member_of",
            ["openminds.core.Consortium", "openminds.core.Organization"],
            "vocab:memberOf",
            required=True,
            doc="no description available",
        ),
        Property(
            "start_date",
            date,
            "vocab:startDate",
            doc="Date in the Gregorian calendar at which something begins in time",
        ),
    ]
    reverse_properties = []

    def __init__(self, end_date=None, member_of=None, start_date=None, id=None, data=None, space=None, scope=None):
        return super().__init__(data=data, end_date=end_date, member_of=member_of, start_date=start_date)
