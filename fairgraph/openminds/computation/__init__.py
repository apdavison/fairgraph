import sys
import inspect
from ...base_v3 import KGObject

from .launch_configuration import LaunchConfiguration
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


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)]
