"""
A persistent identifier for an information resource provided by the Handle System of the Corporation for National Research Initiatives.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import HANDLE as OMHANDLE
from fairgraph import KGObject


class HANDLE(KGObject, OMHANDLE):
    """
    A persistent identifier for an information resource provided by the Handle System of the Corporation for National Research Initiatives.
    """

    type_ = "https://openminds.om-i.org/types/HANDLE"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "related_to",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "relatedPublication",
            reverse="related_publications",
            multiple=True,
            description="reverse of 'related_publications'",
        ),
    ]
    existence_query_properties = ("identifier",)

    def __init__(self, identifier=None, related_to=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(
            self, id=id, space=space, scope=scope, data=data, identifier=identifier, related_to=related_to
        )


# cast openMINDS instances to their fairgraph subclass
HANDLE.set_error_handling(None)
for key, value in OMHANDLE.__dict__.items():
    if isinstance(value, OMHANDLE):
        fg_instance = HANDLE.from_jsonld(value.to_jsonld())
        fg_instance._space = HANDLE.default_space
        setattr(HANDLE, key, fg_instance)
HANDLE.set_error_handling("log")
