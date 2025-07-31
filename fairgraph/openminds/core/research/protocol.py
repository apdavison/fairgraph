"""
Structured information on a research project.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Protocol
from fairgraph import KGObject


class Protocol(KGObject, Protocol):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.om-i.org/types/Protocol"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "used_in",
            [
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "protocol",
            reverse="protocols",
            multiple=True,
            description="reverse of 'protocols'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        described_in=None,
        description=None,
        stimulus_types=None,
        techniques=None,
        used_in=None,
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
            described_in=described_in,
            description=description,
            stimulus_types=stimulus_types,
            techniques=techniques,
            used_in=used_in,
        )
