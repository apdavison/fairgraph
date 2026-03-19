import sys
from fairgraph.openminds import (
    list_kg_classes as _lkgc,
    list_embedded_metadata_classes as _lemc,
    set_error_handling as _seh,
)

from .data_analysis import DataAnalysis
from .data_copy import DataCopy
from .environment import Environment
from .generic_computation import GenericComputation
from .hardware_system import HardwareSystem
from .launch_configuration import LaunchConfiguration
from .local_file import LocalFile
from .model_validation import ModelValidation
from .optimization import Optimization
from .simulation import Simulation
from .software_agent import SoftwareAgent
from .validation_test import ValidationTest
from .validation_test_version import ValidationTestVersion
from .visualization import Visualization
from .workflow_execution import WorkflowExecution
from .workflow_recipe import WorkflowRecipe
from .workflow_recipe_version import WorkflowRecipeVersion


def list_kg_classes():
    """List all KG classes defined in this module"""
    return _lkgc(sys.modules[__name__])


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return _lemc(sys.modules[__name__])


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
    """
    _seh(value, sys.modules[__name__])
