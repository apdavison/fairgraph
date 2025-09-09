"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import AnalysisTechnique as OMAnalysisTechnique
from fairgraph import KGObject


from openminds import IRI


class AnalysisTechnique(KGObject, OMAnalysisTechnique):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/AnalysisTechnique"
    default_space = "controlled"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "describes",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
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
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "used_in",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.Protocol",
            ],
            "technique",
            reverse="techniques",
            multiple=True,
            description="reverse of 'techniques'",
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
        is_used_to_group=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        synonyms=None,
        used_in=None,
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
            is_used_to_group=is_used_to_group,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
            used_in=used_in,
        )


# cast openMINDS instances to their fairgraph subclass
AnalysisTechnique.set_error_handling(None)
for key, value in OMAnalysisTechnique.__dict__.items():
    if isinstance(value, OMAnalysisTechnique):
        fg_instance = AnalysisTechnique.from_jsonld(value.to_jsonld())
        fg_instance._space = AnalysisTechnique.default_space
        setattr(AnalysisTechnique, key, fg_instance)
AnalysisTechnique.set_error_handling("log")
