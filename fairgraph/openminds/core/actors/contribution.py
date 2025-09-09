"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Contribution as OMContribution
from fairgraph import EmbeddedMetadata


class Contribution(EmbeddedMetadata, OMContribution):
    """
    Structured information on the contribution made to a research product.
    """

    type_ = "https://openminds.om-i.org/types/Contribution"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, contributor=None, types=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, contributor=contributor, types=types)


# cast openMINDS instances to their fairgraph subclass
Contribution.set_error_handling(None)
for key, value in OMContribution.__dict__.items():
    if isinstance(value, OMContribution):
        fg_instance = Contribution.from_jsonld(value.to_jsonld())
        fg_instance._space = Contribution.default_space
        setattr(Contribution, key, fg_instance)
Contribution.set_error_handling("log")
