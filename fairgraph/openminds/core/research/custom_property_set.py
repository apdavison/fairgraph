"""
Structured information about properties of an entity that are not represented in an openMINDS schema.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import CustomPropertySet as OMCustomPropertySet
from fairgraph import EmbeddedMetadata


class CustomPropertySet(EmbeddedMetadata, OMCustomPropertySet):
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


# cast openMINDS instances to their fairgraph subclass
CustomPropertySet.set_error_handling(None)
for key, value in OMCustomPropertySet.__dict__.items():
    if isinstance(value, OMCustomPropertySet):
        fg_instance = CustomPropertySet.from_jsonld(value.to_jsonld())
        fg_instance._space = CustomPropertySet.default_space
        setattr(CustomPropertySet, key, fg_instance)
CustomPropertySet.set_error_handling("log")
