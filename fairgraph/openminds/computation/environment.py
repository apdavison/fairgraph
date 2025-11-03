"""
Structured information on the computer system or set of systems in which a computation is deployed and executed.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import Environment as OMEnvironment
from fairgraph import KGObject


class Environment(KGObject, OMEnvironment):
    """
    Structured information on the computer system or set of systems in which a computation is deployed and executed.
    """

    type_ = "https://openminds.om-i.org/types/Environment"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "used_for",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.SoftwareAgent",
                "openminds.latest.computation.Visualization",
            ],
            "environment",
            reverse="environment",
            multiple=True,
            description="reverse of 'environment'",
        ),
    ]
    existence_query_properties = ("hardware", "name")

    def __init__(
        self,
        name=None,
        configuration=None,
        description=None,
        hardware=None,
        software=None,
        used_for=None,
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
            configuration=configuration,
            description=description,
            hardware=hardware,
            software=software,
            used_for=used_for,
        )
