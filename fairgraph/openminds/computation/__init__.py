import sys
import inspect
from fairgraph.kgobject import KGObject
from fairgraph.embedded import EmbeddedMetadata

from .launch_configuration import LaunchConfiguration
from .data_copy import DataCopy
from .workflow_recipe_version import WorkflowRecipeVersion
from .optimization import Optimization
from .local_file import LocalFile
from .visualization import Visualization
from .data_analysis import DataAnalysis
from .environment import Environment
from .workflow_execution import WorkflowExecution
from .software_agent import SoftwareAgent
from .validation_test import ValidationTest
from .model_validation import ModelValidation
from .workflow_recipe import WorkflowRecipe
from .hardware_system import HardwareSystem
from .validation_test_version import ValidationTestVersion
from .simulation import Simulation
from .generic_computation import GenericComputation


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)
    ]


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and issubclass(obj, EmbeddedMetadata) and obj.__module__.startswith(__name__)
    ]


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required field is not provided).
            Possible values: "error", "warning", "log", None
    """
    for cls in list_kg_classes() + list_embedded_metadata_classes():
        cls.set_error_handling(value)
