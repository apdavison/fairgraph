"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import WebService as OMWebService
from fairgraph import KGObject


from openminds import IRI


class WebService(KGObject, OMWebService):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/WebService"
    default_space = "webservice"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "comments",
            "openminds.latest.core.Comment",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
        Property(
            "has_accounts",
            "openminds.latest.core.AccountInformation",
            "service",
            reverse="service",
            multiple=True,
            description="reverse of 'service'",
        ),
        Property(
            "hosts",
            "openminds.latest.publications.LivePaperResourceItem",
            "hostedBy",
            reverse="hosted_by",
            multiple=True,
            description="reverse of 'hosted_by'",
        ),
        Property(
            "is_part_of",
            ["openminds.latest.core.Project", "openminds.latest.core.ResearchProductGroup"],
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "learning_resources",
            "openminds.latest.publications.LearningResource",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
    ]
    aliases = {"name": "full_name", "versions": "has_versions", "alias": "short_name"}
    existence_query_properties = ("short_name",)

    def __init__(
        self,
        name=None,
        alias=None,
        comments=None,
        custodians=None,
        description=None,
        developers=None,
        full_name=None,
        has_accounts=None,
        has_versions=None,
        homepage=None,
        hosts=None,
        how_to_cite=None,
        is_part_of=None,
        learning_resources=None,
        short_name=None,
        versions=None,
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
            comments=comments,
            custodians=custodians,
            description=description,
            developers=developers,
            full_name=full_name,
            has_accounts=has_accounts,
            has_versions=has_versions,
            homepage=homepage,
            hosts=hosts,
            how_to_cite=how_to_cite,
            is_part_of=is_part_of,
            learning_resources=learning_resources,
            short_name=short_name,
            versions=versions,
        )


# cast openMINDS instances to their fairgraph subclass
WebService.set_error_handling(None)
for key, value in OMWebService.__dict__.items():
    if isinstance(value, OMWebService):
        fg_instance = WebService.from_jsonld(value.to_jsonld())
        fg_instance._space = WebService.default_space
        setattr(WebService, key, fg_instance)
WebService.set_error_handling("log")
