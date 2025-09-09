"""
Structured information about a process of running simulations of a computational model.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.computation import Simulation as OMSimulation
from fairgraph import KGObject


from datetime import datetime, time


class Simulation(KGObject, OMSimulation):
    """
    Structured information about a process of running simulations of a computational model.
    """

    type_ = "https://openminds.om-i.org/types/Simulation"
    default_space = "computation"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "informed",
            [
                "openminds.latest.computation.DataAnalysis",
                "openminds.latest.computation.DataCopy",
                "openminds.latest.computation.GenericComputation",
                "openminds.latest.computation.ModelValidation",
                "openminds.latest.computation.Optimization",
                "openminds.latest.computation.Simulation",
                "openminds.latest.computation.Visualization",
            ],
            "wasInformedBy",
            reverse="was_informed_by",
            multiple=True,
            description="reverse of 'was_informed_by'",
        ),
        Property(
            "is_part_of",
            "openminds.latest.computation.WorkflowExecution",
            "stage",
            reverse="stages",
            multiple=True,
            description="reverse of 'stages'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        custom_property_sets=None,
        description=None,
        end_time=None,
        environment=None,
        informed=None,
        inputs=None,
        is_part_of=None,
        launch_configuration=None,
        outputs=None,
        performed_by=None,
        recipe=None,
        resource_usages=None,
        start_time=None,
        started_by=None,
        status=None,
        study_targets=None,
        tags=None,
        techniques=None,
        was_informed_by=None,
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
            lookup_label=lookup_label,
            custom_property_sets=custom_property_sets,
            description=description,
            end_time=end_time,
            environment=environment,
            informed=informed,
            inputs=inputs,
            is_part_of=is_part_of,
            launch_configuration=launch_configuration,
            outputs=outputs,
            performed_by=performed_by,
            recipe=recipe,
            resource_usages=resource_usages,
            start_time=start_time,
            started_by=started_by,
            status=status,
            study_targets=study_targets,
            tags=tags,
            techniques=techniques,
            was_informed_by=was_informed_by,
        )


# cast openMINDS instances to their fairgraph subclass
Simulation.set_error_handling(None)
for key, value in OMSimulation.__dict__.items():
    if isinstance(value, OMSimulation):
        fg_instance = Simulation.from_jsonld(value.to_jsonld())
        fg_instance._space = Simulation.default_space
        setattr(Simulation, key, fg_instance)
Simulation.set_error_handling("log")
