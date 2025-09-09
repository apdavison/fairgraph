"""
Structured information on the operating system.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import OperatingSystem as OMOperatingSystem
from fairgraph import KGObject


from openminds import IRI


class OperatingSystem(KGObject, OMOperatingSystem):
    """
    Structured information on the operating system.
    """

    type_ = "https://openminds.om-i.org/types/OperatingSystem"
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
            "used_by",
            "openminds.latest.core.SoftwareVersion",
            "operatingSystem",
            reverse="operating_systems",
            multiple=True,
            description="reverse of 'operating_systems'",
        ),
    ]
    existence_query_properties = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        describes=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        synonyms=None,
        used_by=None,
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
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
            used_by=used_by,
        )


# cast openMINDS instances to their fairgraph subclass
OperatingSystem.set_error_handling(None)
for key, value in OMOperatingSystem.__dict__.items():
    if isinstance(value, OMOperatingSystem):
        fg_instance = OperatingSystem.from_jsonld(value.to_jsonld())
        fg_instance._space = OperatingSystem.default_space
        setattr(OperatingSystem, key, fg_instance)
OperatingSystem.set_error_handling("log")
