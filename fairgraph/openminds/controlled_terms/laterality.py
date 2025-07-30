"""
Structured information on the lateral direction.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import Laterality
from fairgraph import KGObject


from openminds import IRI


class Laterality(KGObject, Laterality):
    """
    Structured information on the lateral direction.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Laterality"
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
            "is_laterality_of",
            [
                "openminds.latest.core.TissueSample",
                "openminds.latest.core.TissueSampleCollection",
                "openminds.latest.sands.AtlasAnnotation",
                "openminds.latest.sands.CustomAnnotation",
            ],
            "laterality",
            reverse="lateralities",
            multiple=True,
            description="reverse of 'lateralities'",
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
        is_laterality_of=None,
        knowledge_space_link=None,
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
            interlex_identifier=interlex_identifier,
            is_laterality_of=is_laterality_of,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )
