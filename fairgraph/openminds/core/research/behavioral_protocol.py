"""
Structured information about a protocol used in an experiment studying human or animal behavior.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import BehavioralProtocol
from fairgraph import KGObject


class BehavioralProtocol(KGObject, BehavioralProtocol):
    """
    Structured information about a protocol used in an experiment studying human or animal behavior.
    """

    type_ = "https://openminds.ebrains.eu/core/BehavioralProtocol"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "used_in",
            ["openminds.latest.core.DatasetVersion", "openminds.latest.core.ProtocolExecution"],
            "behavioralProtocol",
            reverse="behavioral_protocols",
            multiple=True,
            description="reverse of 'behavioral_protocols'",
        ),
    ]
    existence_query_properties = ("description", "name")

    def __init__(
        self,
        name=None,
        described_in=None,
        description=None,
        internal_identifier=None,
        is_used_to_group=None,
        stimulations=None,
        stimulus_types=None,
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
            internal_identifier=internal_identifier,
            is_used_to_group=is_used_to_group,
            stimulations=stimulations,
            stimulus_types=stimulus_types,
            used_in=used_in,
        )
