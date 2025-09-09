"""
Structured information on a research project.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Project as OMProject
from fairgraph import KGObject


from openminds import IRI


class Project(KGObject, OMProject):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.om-i.org/types/Project"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("short_name",)

    def __init__(
        self,
        name=None,
        alias=None,
        coordinators=None,
        description=None,
        full_name=None,
        has_parts=None,
        homepage=None,
        short_name=None,
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
            alias=alias,
            coordinators=coordinators,
            description=description,
            full_name=full_name,
            has_parts=has_parts,
            homepage=homepage,
            short_name=short_name,
        )


# cast openMINDS instances to their fairgraph subclass
Project.set_error_handling(None)
for key, value in OMProject.__dict__.items():
    if isinstance(value, OMProject):
        fg_instance = Project.from_jsonld(value.to_jsonld())
        fg_instance._space = Project.default_space
        setattr(Project, key, fg_instance)
Project.set_error_handling("log")
