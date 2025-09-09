"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import ChemicalMixtureType as OMChemicalMixtureType
from fairgraph import KGObject


from openminds import IRI


class ChemicalMixtureType(KGObject, OMChemicalMixtureType):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ChemicalMixtureType"
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
            "is_type_of",
            "openminds.latest.chemicals.ChemicalMixture",
            "type",
            reverse="type",
            multiple=True,
            description="reverse of 'type'",
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
        is_type_of=None,
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
            is_type_of=is_type_of,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )


# cast openMINDS instances to their fairgraph subclass
ChemicalMixtureType.set_error_handling(None)
for key, value in OMChemicalMixtureType.__dict__.items():
    if isinstance(value, OMChemicalMixtureType):
        fg_instance = ChemicalMixtureType.from_jsonld(value.to_jsonld())
        fg_instance._space = ChemicalMixtureType.default_space
        setattr(ChemicalMixtureType, key, fg_instance)
ChemicalMixtureType.set_error_handling("log")
