import sys
import inspect
from ...base_v3 import KGObject

from .chemical_mixture import ChemicalMixture
from .product_source import ProductSource
from .amount_of_chemical import AmountOfChemical
from .chemical_substance import ChemicalSubstance


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)]
