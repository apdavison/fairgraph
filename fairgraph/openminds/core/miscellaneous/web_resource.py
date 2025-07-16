"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from fairgraph.base import IRI


class WebResource(KGObject):
    """
    <description not available>
    """

    default_space = "common"
    type_ = "https://openminds.ebrains.eu/core/WebResource"
    properties = [
        Property("content_description", str, "vocab:contentDescription", doc="no description available"),
        Property(
            "format",
            "openminds.core.ContentType",
            "vocab:format",
            doc="Method of digitally organizing and structuring data or information.",
        ),
        Property(
            "iri",
            IRI,
            "vocab:IRI",
            required=True,
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
    ]
    reverse_properties = [
        Property(
            "describes",
            ["openminds.core.BehavioralProtocol", "openminds.core.Protocol"],
            "^vocab:describedIn",
            reverse="described_in",
            multiple=True,
            doc="reverse of 'described_in'",
        ),
        Property(
            "fully_documents",
            [
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.LivePaperVersion",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:fullDocumentation",
            reverse="full_documentation",
            multiple=True,
            doc="reverse of 'full_documentation'",
        ),
        Property(
            "is_applied_to",
            "openminds.core.DatasetVersion",
            "^vocab:license",
            reverse="license",
            multiple=True,
            doc="reverse of 'license'",
        ),
        Property(
            "is_output_of",
            "openminds.core.ModelVersion",
            "^vocab:outputData",
            reverse="output_data",
            multiple=True,
            doc="reverse of 'output_data'",
        ),
        Property(
            "is_reference_for",
            "openminds.computation.ValidationTestVersion",
            "^vocab:referenceData",
            reverse="reference_data",
            multiple=True,
            doc="reverse of 'reference_data'",
        ),
    ]
    existence_query_properties = ("iri",)

    def __init__(
        self,
        content_description=None,
        describes=None,
        format=None,
        fully_documents=None,
        iri=None,
        is_applied_to=None,
        is_output_of=None,
        is_reference_for=None,
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
            content_description=content_description,
            describes=describes,
            format=format,
            fully_documents=fully_documents,
            iri=iri,
            is_applied_to=is_applied_to,
            is_output_of=is_output_of,
            is_reference_for=is_reference_for,
        )
