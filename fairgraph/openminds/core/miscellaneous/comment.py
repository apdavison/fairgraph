"""
Structured information about a short text expressing an opinion on, or giving information about some entity.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Comment as OMComment
from fairgraph import KGObject


from datetime import datetime


class Comment(KGObject, OMComment):
    """
    Structured information about a short text expressing an opinion on, or giving information about some entity.
    """

    type_ = "https://openminds.om-i.org/types/Comment"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("about", "comment", "commenter", "timestamp")

    def __init__(
        self, about=None, comment=None, commenter=None, timestamp=None, id=None, data=None, space=None, scope=None
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            about=about,
            comment=comment,
            commenter=commenter,
            timestamp=timestamp,
        )


# cast openMINDS instances to their fairgraph subclass
Comment.set_error_handling(None)
for key, value in OMComment.__dict__.items():
    if isinstance(value, OMComment):
        fg_instance = Comment.from_jsonld(value.to_jsonld())
        fg_instance._space = Comment.default_space
        setattr(Comment, key, fg_instance)
Comment.set_error_handling("log")
