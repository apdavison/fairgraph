"""
Structured information on a research project.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class Project(KGObject):
    """
    Structured information on a research project.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/Project"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the project."),
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the project."),
        Field("has_research_productss", ["openminds.core.Dataset", "openminds.core.DatasetVersion", "openminds.core.MetaDataModel", "openminds.core.MetaDataModelVersion", "openminds.core.Model", "openminds.core.ModelVersion", "openminds.core.Software", "openminds.core.SoftwareVersion"], "vocab:hasResearchProducts", multiple=True, required=True,
              doc="Reference to subsidiary research products."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of something or someone."),
        Field("coordinators", ["openminds.core.Organization", "openminds.core.Person"], "vocab:coordinator", multiple=True, required=False,
              doc="Legal person who organizes the collaborative work of people or groups."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the project."),
        
    ]
    existence_query_fields = None