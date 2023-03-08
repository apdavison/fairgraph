"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class ViewerSpecification(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/ViewerSpecification"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("anchor_point", "openminds.sands.CoordinatePoint", "vocab:anchorPoint", multiple=False, required=True,
              doc="no description available"),
        Field("camera_position", "openminds.sands.CoordinatePoint", "vocab:cameraPosition", multiple=False, required=False,
              doc="no description available"),
        Field("preferred_display_color", ["openminds.sands.ColorMap", "openminds.sands.SingleColor"], "vocab:preferredDisplayColor", multiple=False, required=False,
              doc="no description available"),

    ]
