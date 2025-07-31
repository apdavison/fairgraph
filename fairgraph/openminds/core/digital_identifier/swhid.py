"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import SWHID
from fairgraph import KGObject


class SWHID(KGObject, SWHID):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SWHID"
    default_space = "software"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "identifies",
            [
                "openminds.latest.core.MetaDataModel",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.Model",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.Software",
                "openminds.latest.core.SoftwareVersion",
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
