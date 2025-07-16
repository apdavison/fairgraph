"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from fairgraph.base import IRI


class FileArchive(KGObject):
    """
    <description not available>
    """

    default_space = "dataset"
    type_ = "https://openminds.ebrains.eu/core/FileArchive"
    properties = [
        Property(
            "format",
            "openminds.core.ContentType",
            "vocab:format",
            required=True,
            doc="Method of digitally organizing and structuring data or information.",
        ),
        Property(
            "iri",
            IRI,
            "vocab:IRI",
            required=True,
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
        Property(
            "source_data", "openminds.core.File", "vocab:sourceData", multiple=True, doc="no description available"
        ),
    ]
    reverse_properties = [
        Property(
            "is_location_of",
            "openminds.core.ServiceLink",
            "^vocab:dataLocation",
            reverse="data_location",
            multiple=True,
            doc="reverse of 'data_location'",
        ),
        Property(
            "is_output_of",
            [
                "openminds.computation.DataAnalysis",
                "openminds.computation.GenericComputation",
                "openminds.computation.Simulation",
                "openminds.computation.Visualization",
            ],
            "^vocab:output",
            reverse="outputs",
            multiple=True,
            doc="reverse of 'outputs'",
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
        return super().__init__(
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
