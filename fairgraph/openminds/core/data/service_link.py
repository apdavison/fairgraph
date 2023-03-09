"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class ServiceLink(KGObject):
    """

    """
    default_space = "dataset"
    type_ = ["https://openminds.ebrains.eu/core/ServiceLink"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("data_location", ["openminds.core.File", "openminds.core.FileArchive", "openminds.core.FileBundle", "openminds.core.ModelVersion", "openminds.publications.LivePaperResourceItem", "openminds.sands.ParcellationEntityVersion"], "vocab:dataLocation", multiple=False, required=True,
              doc="no description available"),
        Field("display_label", str, "vocab:displayLabel", multiple=False, required=False,
              doc="no description available"),
        Field("open_data_in", IRI, "vocab:openDataIn", multiple=False, required=True,
              doc="no description available"),
        Field("preview_image", "openminds.core.File", "vocab:previewImage", multiple=False, required=False,
              doc="no description available"),
        Field("service", "openminds.controlledterms.Service", "vocab:service", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('data_location', 'open_data_in', 'service')
