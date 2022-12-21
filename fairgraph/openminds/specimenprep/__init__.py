import sys
import inspect
from ...base_v3 import KGObject

from .activity.cranial_window_preparation import CranialWindowPreparation
from .activity.tissue_culture_preparation import TissueCulturePreparation
from .activity.tissue_sample_slicing import TissueSampleSlicing
from .device.slicing_device import SlicingDevice
from .device.slicing_device_usage import SlicingDeviceUsage


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)]
