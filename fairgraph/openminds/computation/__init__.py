import sys
import inspect
from ...base_v3 import KGObjectV3

from .launch_configuration import LaunchConfiguration
from .optimization import Optimization
from .visualization import Visualization
from .data_analysis import DataAnalysis
from .environment import Environment
from .workflow_execution import WorkflowExecution
from .software_agent import SoftwareAgent
from .hardware_system import HardwareSystem
from .simulation import Simulation


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObjectV3) and obj.__module__.startswith(__name__)]
