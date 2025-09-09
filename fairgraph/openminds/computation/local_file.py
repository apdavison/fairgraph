"""
Structured information about a file that is not accessible via a URL.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import LocalFile as OMLocalFile
from fairgraph import KGObject


class LocalFile(KGObject, OMLocalFile):
    """
    Structured information about a file that is not accessible via a URL.
    """

    type_ = "https://openminds.om-i.org/types/LocalFile"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_output_of",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "output",
            reverse="outputs",
            multiple=True,
            description="reverse of 'outputs'",
        ),
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
    ]
    existence_query_properties = ("name", "path")

    def __init__(
        self,
        name=None,
        content_description=None,
        copy_of=None,
        data_types=None,
        format=None,
        hash=None,
        is_output_of=None,
        is_used_to_group=None,
        path=None,
        special_usage_role=None,
        storage_size=None,
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
            content_description=content_description,
            copy_of=copy_of,
            data_types=data_types,
            format=format,
            hash=hash,
            is_output_of=is_output_of,
            is_used_to_group=is_used_to_group,
            path=path,
            special_usage_role=special_usage_role,
            storage_size=storage_size,
        )


# cast openMINDS instances to their fairgraph subclass
LocalFile.set_error_handling(None)
for key, value in OMLocalFile.__dict__.items():
    if isinstance(value, OMLocalFile):
        fg_instance = LocalFile.from_jsonld(value.to_jsonld())
        fg_instance._space = LocalFile.default_space
        setattr(LocalFile, key, fg_instance)
LocalFile.set_error_handling("log")
