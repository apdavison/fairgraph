"""
Structured information about an execution of a computational workflow.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import WorkflowExecution as OMWorkflowExecution
from fairgraph import KGObject


class WorkflowExecution(KGObject, OMWorkflowExecution):
    """
    Structured information about an execution of a computational workflow.
    """

    type_ = "https://openminds.om-i.org/types/WorkflowExecution"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("stages",)

    def __init__(
        self, configuration=None, recipe=None, stages=None, started_by=None, id=None, data=None, space=None, scope=None
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            configuration=configuration,
            recipe=recipe,
            stages=stages,
            started_by=started_by,
        )
