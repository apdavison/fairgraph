"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import WebResource as OMWebResource
from fairgraph import KGObject


from openminds import IRI


class WebResource(KGObject, OMWebResource):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/WebResource"
    default_space = "common"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            ["openminds.latest.core.BehavioralProtocol", "openminds.latest.core.Protocol"],
            "describedIn",
            reverse="described_in",
            multiple=True,
            description="reverse of 'described_in'",
        ),
        Property(
            "fully_documents",
            [
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "fullDocumentation",
            reverse="full_documentation",
            multiple=True,
            description="reverse of 'full_documentation'",
        ),
        Property(
            "is_applied_to",
            "openminds.latest.core.DatasetVersion",
            "license",
            reverse="license",
            multiple=True,
            description="reverse of 'license'",
        ),
        Property(
            "is_output_of",
            "openminds.latest.core.ModelVersion",
            "outputData",
            reverse="output_data",
            multiple=True,
            description="reverse of 'output_data'",
        ),
        Property(
            "is_reference_for",
            "openminds.latest.computation.ValidationTestVersion",
            "referenceData",
            reverse="reference_data",
            multiple=True,
            description="reverse of 'reference_data'",
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
        return KGObject.__init__(
            self,
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


# cast openMINDS instances to their fairgraph subclass
WebResource.set_error_handling(None)
for key, value in OMWebResource.__dict__.items():
    if isinstance(value, OMWebResource):
        fg_instance = WebResource.from_jsonld(value.to_jsonld())
        fg_instance._space = WebResource.default_space
        setattr(WebResource, key, fg_instance)
WebResource.set_error_handling("log")
