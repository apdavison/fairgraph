"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class WorkflowExecution(KGObjectV3):
    """

    """
    space = "model"
    type = ["https://openminds.ebrains.eu/computation/WorkflowExecution"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("stages", ["openminds.computation.Simulation", "openminds.computation.DataAnalysis", "openminds.computation.Visualization"], "vocab:stages", multiple=False, required=True,
              doc="no description available"),
        Field("started_by", ["openminds.core.Person", "openminds.computation.SoftwareAgent"], "vocab:startedBy", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = None