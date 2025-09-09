"""
Structured information about a relationship between two entities, such as a person and their employer.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Affiliation as OMAffiliation
from fairgraph import EmbeddedMetadata


from datetime import date


class Affiliation(EmbeddedMetadata, OMAffiliation):
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


# cast openMINDS instances to their fairgraph subclass
Affiliation.set_error_handling(None)
for key, value in OMAffiliation.__dict__.items():
    if isinstance(value, OMAffiliation):
        fg_instance = Affiliation.from_jsonld(value.to_jsonld())
        fg_instance._space = Affiliation.default_space
        setattr(Affiliation, key, fg_instance)
Affiliation.set_error_handling("log")
