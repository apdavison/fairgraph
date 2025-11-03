"""
Structured information about the launch of a computational process.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import LaunchConfiguration as OMLaunchConfiguration
from fairgraph import KGObject


class LaunchConfiguration(KGObject, OMLaunchConfiguration):
    """
    Structured information about the launch of a computational process.
    """

    type_ = "https://openminds.om-i.org/types/LaunchConfiguration"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_launch_configuration_of",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "launchConfiguration",
            reverse="launch_configuration",
            multiple=True,
            description="reverse of 'launch_configuration'",
        ),
    ]
    existence_query_properties = ("executable", "name")

    def __init__(
        self,
        name=None,
        arguments=None,
        description=None,
        environment_variables=None,
        executable=None,
        is_launch_configuration_of=None,
        id=None,
        data=None,
        space=None,
        release_status=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            release_status=release_status,
            data=data,
            name=name,
            arguments=arguments,
            description=description,
            environment_variables=environment_variables,
            executable=executable,
            is_launch_configuration_of=is_launch_configuration_of,
        )
