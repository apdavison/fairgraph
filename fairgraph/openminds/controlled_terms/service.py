"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import Service as OMService
from fairgraph import KGObject


from openminds import IRI


class Service(KGObject, OMService):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Service"
    default_space = "controlled"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.LearningResource",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.publications.ScholarlyArticle",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "keyword",
            reverse="keywords",
            multiple=True,
            description="reverse of 'keywords'",
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
            "linked_from",
            "openminds.latest.core.ServiceLink",
            "service",
            reverse="service",
            multiple=True,
            description="reverse of 'service'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        describes=None,
        description=None,
        hosts=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        linked_from=None,
        preferred_ontology_identifier=None,
        synonyms=None,
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
            definition=definition,
            describes=describes,
            description=description,
            hosts=hosts,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            linked_from=linked_from,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )
