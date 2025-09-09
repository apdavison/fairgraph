"""
An identifiable list of property-value pairs.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import PropertyValueList as OMPropertyValueList
from fairgraph import KGObject


class PropertyValueList(KGObject, OMPropertyValueList):
    """
    An identifiable list of property-value pairs.
    """

    type_ = "https://openminds.om-i.org/types/PropertyValueList"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "defines_environment_of",
            "openminds.latest.computation.LaunchConfiguration",
            "environmentVariable",
            reverse="environment_variable",
            multiple=True,
            description="reverse of 'environment_variable'",
        ),
        Property(
            "is_configuration_of",
            ["openminds.latest.computation.ValidationTestVersion", "openminds.latest.core.ModelVersion"],
            "configuration",
            reverse="configuration",
            multiple=True,
            description="reverse of 'configuration'",
        ),
        Property(
            "specifies",
            ["openminds.latest.sands.CustomAnnotation", "openminds.latest.stimulation.EphysStimulus"],
            "specification",
            reverse="specification",
            multiple=True,
            description="reverse of 'specification'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        defines_environment_of=None,
        is_configuration_of=None,
        property_value_pairs=None,
        specifies=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            defines_environment_of=defines_environment_of,
            is_configuration_of=is_configuration_of,
            property_value_pairs=property_value_pairs,
            specifies=specifies,
        )


# cast openMINDS instances to their fairgraph subclass
PropertyValueList.set_error_handling(None)
for key, value in OMPropertyValueList.__dict__.items():
    if isinstance(value, OMPropertyValueList):
        fg_instance = PropertyValueList.from_jsonld(value.to_jsonld())
        fg_instance._space = PropertyValueList.default_space
        setattr(PropertyValueList, key, fg_instance)
PropertyValueList.set_error_handling("log")
