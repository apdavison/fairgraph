import sys
import inspect
from ...base_v3 import KGObjectV3

from .launchconfiguration import LaunchConfiguration
from .optimization import Optimization
from .visualization import Visualization
from .data_analysis import DataAnalysis
from .environment import Environment
from .workflowexecution import WorkflowExecution
from .softwareagent import SoftwareAgent
from .computation import Computation
from .hardware import HardwareSystem
from .simulation import Simulation


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObjectV3) and obj.__module__.startswith(__name__)]
