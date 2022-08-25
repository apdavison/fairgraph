"""
Structured information on a research project.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Project(KGObject):
    """
    Structured information on a research project.
    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Project"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the project."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the project."),
        Field("coordinators", ["openminds.core.Organization", "openminds.core.Person"], "vocab:coordinator", multiple=True, required=False,
              doc="Legal person who organizes the collaborative work of people or groups."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the project."),
        Field("has_research_products", ["openminds.computation.ValidationTest", "openminds.computation.ValidationTestVersion", "openminds.computation.WorkflowRecipe", "openminds.computation.WorkflowRecipeVersion", "openminds.core.Dataset", "openminds.core.DatasetVersion", "openminds.core.MetaDataModel", "openminds.core.MetaDataModelVersion", "openminds.core.Model", "openminds.core.ModelVersion", "openminds.core.Software", "openminds.core.SoftwareVersion", "openminds.publications.LivePaper", "openminds.publications.LivePaperVersion", "openminds.sands.BrainAtlas", "openminds.sands.BrainAtlasVersion"], "vocab:hasResearchProducts", multiple=True, required=True,
              doc="Reference to subsidiary research products."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the project."),

    ]
    existence_query_fields = ('alias',)
