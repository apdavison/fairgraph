"""
A persistent identifier for a research resource provided by the Resource Identification Initiative.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import RRID
from fairgraph import KGObject


class RRID(KGObject, RRID):
    """
    A persistent identifier for a research resource provided by the Resource Identification Initiative.
    """

    type_ = "https://openminds.om-i.org/types/RRID"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            [
                "openminds.latest.chemicals.ProductSource",
                "openminds.latest.core.Organization",
                "openminds.latest.core.Software",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.Strain",
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
                "openminds.latest.sands.BrainAtlas",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpace",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
                "openminds.latest.specimen_prep.SlicingDevice",
            ],
            "digitalIdentifier",
            reverse="digital_identifier",
            multiple=True,
            description="reverse of 'digital_identifier'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(self, identifier=None, identifies=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self, id=id, space=space, scope=scope, data=data, identifier=identifier, identifies=identifies
        )
