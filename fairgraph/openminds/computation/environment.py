"""
Structured information on the computer system or set of systems in which a computation is deployed and executed.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class Environment(KGObject):
    """
    Structured information on the computer system or set of systems in which a computation is deployed and executed.
    """

    default_space = "computation"
    type_ = "https://openminds.ebrains.eu/computation/Environment"
    properties = [
        Property(
            "configuration", "openminds.core.Configuration", "vocab:configuration", doc="no description available"
        ),
        Property(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the environment.",
        ),
        Property(
            "hardware",
            "openminds.computation.HardwareSystem",
            "vocab:hardware",
            required=True,
            doc="no description available",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the environment.",
        ),
        Property(
            "software",
            "openminds.core.SoftwareVersion",
            "vocab:software",
            multiple=True,
            doc="no description available",
        ),
    ]
    reverse_properties = [
        Property(
            "used_for",
            [
                "openminds.computation.DataAnalysis",
                "openminds.computation.DataCopy",
                "openminds.computation.GenericComputation",
                "openminds.computation.ModelValidation",
                "openminds.computation.Optimization",
                "openminds.computation.Simulation",
                "openminds.computation.SoftwareAgent",
                "openminds.computation.Visualization",
            ],
            "^vocab:environment",
            reverse="environment",
            multiple=True,
            doc="reverse of 'environment'",
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
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            configuration=configuration,
            description=description,
            hardware=hardware,
            software=software,
            used_for=used_for,
        )
