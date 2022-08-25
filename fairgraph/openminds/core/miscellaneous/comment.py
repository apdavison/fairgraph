"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Comment(KGObject):
    """

    """
    default_space = "common"
    type = ["https://openminds.ebrains.eu/core/Comment"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("commenter", "openminds.core.Person", "vocab:commenter", multiple=False, required=True,
              doc="no description available"),
        Field("content", str, "vocab:content", multiple=False, required=True,
              doc="Something that is contained."),
        Field("subject", ["openminds.computation.ValidationTest", "openminds.computation.ValidationTestVersion", "openminds.computation.WorkflowRecipe", "openminds.computation.WorkflowRecipeVersion", "openminds.core.Dataset", "openminds.core.DatasetVersion", "openminds.core.MetaDataModel", "openminds.core.MetaDataModelVersion", "openminds.core.Model", "openminds.core.ModelVersion", "openminds.core.Software", "openminds.core.SoftwareVersion", "openminds.publications.LivePaper", "openminds.publications.LivePaperVersion", "openminds.sands.BrainAtlas", "openminds.sands.BrainAtlasVersion"], "vocab:subject", multiple=False, required=True,
              doc="no description available"),
        Field("timestamp", datetime, "vocab:timestamp", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('commenter', 'content', 'subject', 'timestamp')
