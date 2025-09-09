"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import FileArchive as OMFileArchive
from fairgraph import KGObject


from openminds import IRI


class FileArchive(KGObject, OMFileArchive):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/FileArchive"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_location_of",
            "openminds.latest.core.ServiceLink",
            "dataLocation",
            reverse="data_location",
            multiple=True,
            description="reverse of 'data_location'",
        ),
        Property(
            "is_output_of",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "output",
            reverse="outputs",
            multiple=True,
            description="reverse of 'outputs'",
        ),
    ]
    existence_query_properties = ("iri", "format")

    def __init__(
        self,
        format=None,
        iri=None,
        is_location_of=None,
        is_output_of=None,
        source_data=None,
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
            format=format,
            iri=iri,
            is_location_of=is_location_of,
            is_output_of=is_output_of,
            source_data=source_data,
        )


# cast openMINDS instances to their fairgraph subclass
FileArchive.set_error_handling(None)
for key, value in OMFileArchive.__dict__.items():
    if isinstance(value, OMFileArchive):
        fg_instance = FileArchive.from_jsonld(value.to_jsonld())
        fg_instance._space = FileArchive.default_space
        setattr(FileArchive, key, fg_instance)
FileArchive.set_error_handling("log")
