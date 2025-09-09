"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import SingleColor as OMSingleColor
from fairgraph import KGObject


class SingleColor(KGObject, OMSingleColor):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SingleColor"
    default_space = "atlas"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("value",)

    def __init__(self, value=None, id=None, data=None, space=None, scope=None):
        return KGObject.__init__(self, id=id, space=space, scope=scope, data=data, value=value)


# cast openMINDS instances to their fairgraph subclass
SingleColor.set_error_handling(None)
for key, value in OMSingleColor.__dict__.items():
    if isinstance(value, OMSingleColor):
        fg_instance = SingleColor.from_jsonld(value.to_jsonld())
        fg_instance._space = SingleColor.default_space
        setattr(SingleColor, key, fg_instance)
SingleColor.set_error_handling("log")
