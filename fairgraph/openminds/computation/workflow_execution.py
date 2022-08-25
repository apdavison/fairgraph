"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class WorkflowExecution(KGObject):
    """

    """
    default_space = "computation"
    type = ["https://openminds.ebrains.eu/computation/WorkflowExecution"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("recipe", "openminds.computation.WorkflowRecipeVersion", "vocab:recipe", multiple=False, required=False,
              doc="no description available"),
        Field("stages", ["openminds.computation.DataAnalysis", "openminds.computation.ModelValidation", "openminds.computation.Optimization", "openminds.computation.Simulation", "openminds.computation.Visualization"], "vocab:stages", multiple=True, required=True,
              doc="no description available"),
        Field("started_by", ["openminds.computation.SoftwareAgent", "openminds.core.Person"], "vocab:startedBy", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('stages',)
