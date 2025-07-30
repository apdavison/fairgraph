"""
Structured information about the amount of a given chemical that was used.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.chemicals import AmountOfChemical
from fairgraph import EmbeddedMetadata


class AmountOfChemical(EmbeddedMetadata, AmountOfChemical):
    """
    Structured information about the amount of a given chemical that was used.
    """

    type_ = "https://openminds.ebrains.eu/chemicals/AmountOfChemical"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, amount=None, chemical_product=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, amount=amount, chemical_product=chemical_product)
