"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import DifferenceMeasure as OMDifferenceMeasure
from fairgraph import KGObject


from openminds import IRI


class DifferenceMeasure(KGObject, OMDifferenceMeasure):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/DifferenceMeasure"
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
            "is_score_type_of",
            "openminds.latest.computation.ValidationTest",
            "scoreType",
            reverse="score_type",
            multiple=True,
            description="reverse of 'score_type'",
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
        is_score_type_of=None,
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
            is_score_type_of=is_score_type_of,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )


# cast openMINDS instances to their fairgraph subclass
DifferenceMeasure.set_error_handling(None)
for key, value in OMDifferenceMeasure.__dict__.items():
    if isinstance(value, OMDifferenceMeasure):
        fg_instance = DifferenceMeasure.from_jsonld(value.to_jsonld())
        fg_instance._space = DifferenceMeasure.default_space
        setattr(DifferenceMeasure, key, fg_instance)
DifferenceMeasure.set_error_handling("log")
