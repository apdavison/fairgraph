"""
Structured information on the unit of measurement.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.controlled_terms import UnitOfMeasurement
from fairgraph import KGObject


from openminds import IRI


class UnitOfMeasurement(KGObject, UnitOfMeasurement):
    """
    Structured information on the unit of measurement.
    """

    type_ = "https://openminds.om-i.org/types/UnitOfMeasurement"
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
            ],
            "keyword",
            reverse="keywords",
            multiple=True,
            description="reverse of 'keywords'",
        ),
        Property(
            "used_by",
            ["openminds.latest.sands.CommonCoordinateSpaceVersion", "openminds.latest.sands.CustomCoordinateSpace"],
            "nativeUnit",
            reverse="native_unit",
            multiple=True,
            description="reverse of 'native_unit'",
        ),
        Property(
            "used_in",
            "openminds.latest.ephys.Channel",
            "unit",
            reverse="unit",
            multiple=True,
            description="reverse of 'unit'",
        ),
        Property(
            "value",
            "openminds.latest.core.QuantitativeValueArray",
            "unit",
            reverse="unit",
            multiple=True,
            description="reverse of 'unit'",
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
        used_in=None,
        value=None,
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
            used_in=used_in,
            value=value,
        )
