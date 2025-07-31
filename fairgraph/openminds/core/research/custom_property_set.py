"""
Structured information about properties of an entity that are not represented in an openMINDS schema.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import CustomPropertySet
from fairgraph import EmbeddedMetadata


class CustomPropertySet(EmbeddedMetadata, CustomPropertySet):
    """
    Structured information about properties of an entity that are not represented in an openMINDS schema.
    """

    type_ = "https://openminds.om-i.org/types/CustomPropertySet"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self, context=None, data_location=None, relevant_for=None, id=None, data=None, space=None, scope=None
    ):
        return EmbeddedMetadata.__init__(
            self, data=data, context=context, data_location=data_location, relevant_for=relevant_for
        )
