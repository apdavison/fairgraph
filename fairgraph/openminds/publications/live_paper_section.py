"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import LivePaperSection as OMLivePaperSection
from fairgraph import KGObject


class LivePaperSection(KGObject, OMLivePaperSection):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/LivePaperSection"
    default_space = "livepapers"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_parts",
            "openminds.latest.publications.LivePaperResourceItem",
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
    ]
    existence_query_properties = ("is_part_of", "name", "order", "type")

    def __init__(
        self,
        name=None,
        description=None,
        has_parts=None,
        is_part_of=None,
        order=None,
        type=None,
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
            description=description,
            has_parts=has_parts,
            is_part_of=is_part_of,
            order=order,
            type=type,
        )


# cast openMINDS instances to their fairgraph subclass
LivePaperSection.set_error_handling(None)
for key, value in OMLivePaperSection.__dict__.items():
    if isinstance(value, OMLivePaperSection):
        fg_instance = LivePaperSection.from_jsonld(value.to_jsonld())
        fg_instance._space = LivePaperSection.default_space
        setattr(LivePaperSection, key, fg_instance)
LivePaperSection.set_error_handling("log")
