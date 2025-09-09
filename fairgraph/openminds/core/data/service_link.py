"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import ServiceLink as OMServiceLink
from fairgraph import KGObject


from openminds import IRI


class ServiceLink(KGObject, OMServiceLink):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ServiceLink"
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


# cast openMINDS instances to their fairgraph subclass
ServiceLink.set_error_handling(None)
for key, value in OMServiceLink.__dict__.items():
    if isinstance(value, OMServiceLink):
        fg_instance = ServiceLink.from_jsonld(value.to_jsonld())
        fg_instance._space = ServiceLink.default_space
        setattr(ServiceLink, key, fg_instance)
ServiceLink.set_error_handling("log")
