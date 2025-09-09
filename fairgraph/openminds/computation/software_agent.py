"""
Structured information about a piece of software or web service that can perform a task autonomously.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import SoftwareAgent as OMSoftwareAgent
from fairgraph import KGObject


class SoftwareAgent(KGObject, OMSoftwareAgent):
    """
    Structured information about a piece of software or web service that can perform a task autonomously.
    """

    type_ = "https://openminds.om-i.org/types/SoftwareAgent"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "activities",
            [
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "performedBy",
            reverse="performed_by",
            multiple=True,
            description="reverse of 'performed_by'",
        ),
        Property(
            "started",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
                "openminds.latest.computation.WorkflowExecution",
            ],
            "startedBy",
            reverse="started_by",
            multiple=True,
            description="reverse of 'started_by'",
        ),
    ]
    existence_query_properties = ("name", "software")

    def __init__(
        self,
        name=None,
        activities=None,
        environment=None,
        software=None,
        started=None,
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
            name=name,
            activities=activities,
            environment=environment,
            software=software,
            started=started,
        )


# cast openMINDS instances to their fairgraph subclass
SoftwareAgent.set_error_handling(None)
for key, value in OMSoftwareAgent.__dict__.items():
    if isinstance(value, OMSoftwareAgent):
        fg_instance = SoftwareAgent.from_jsonld(value.to_jsonld())
        fg_instance._space = SoftwareAgent.default_space
        setattr(SoftwareAgent, key, fg_instance)
SoftwareAgent.set_error_handling("log")
