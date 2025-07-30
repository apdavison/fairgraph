"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ServiceLink
from fairgraph import KGObject


from openminds import IRI


class ServiceLink(KGObject, ServiceLink):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ServiceLink"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("data_location", "open_data_in", "service")

    def __init__(
        self,
        data_location=None,
        display_label=None,
        open_data_in=None,
        preview_image=None,
        service=None,
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
            data_location=data_location,
            display_label=display_label,
            open_data_in=open_data_in,
            preview_image=preview_image,
            service=service,
        )
