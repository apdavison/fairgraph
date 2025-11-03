"""
Structured information about the properties or parameters of an entity or process.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Configuration as OMConfiguration
from fairgraph import KGObject


class Configuration(KGObject, OMConfiguration):
    """
    Structured information about the properties or parameters of an entity or process.
    """

    type_ = "https://openminds.om-i.org/types/Configuration"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_configuration_of",
            [
                "openminds.latest.computation.Environment",
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowExecution",
                "openminds.latest.core.ModelVersion",
            ],
            "configuration",
            reverse="configuration",
            multiple=True,
            description="reverse of 'configuration'",
        ),
        Property(
            "specifies",
            "openminds.latest.stimulation.EphysStimulus",
            "specification",
            reverse="specifications",
            multiple=True,
            description="reverse of 'specifications'",
        ),
    ]
    existence_query_properties = ("configuration",)

    def __init__(
        self,
        lookup_label=None,
        configuration=None,
        format=None,
        is_configuration_of=None,
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
            configuration=configuration,
            format=format,
            is_configuration_of=is_configuration_of,
            specifies=specifies,
        )
