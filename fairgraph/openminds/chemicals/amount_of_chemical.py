"""
Structured information about the amount of a given chemical that was used.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.chemicals import AmountOfChemical as OMAmountOfChemical
from fairgraph import EmbeddedMetadata


class AmountOfChemical(EmbeddedMetadata, OMAmountOfChemical):
    """
    Structured information about the amount of a given chemical that was used.
    """

    type_ = "https://openminds.om-i.org/types/AmountOfChemical"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(self, amount=None, chemical_product=None, id=None, data=None, space=None, scope=None):
        return EmbeddedMetadata.__init__(self, data=data, amount=amount, chemical_product=chemical_product)


# cast openMINDS instances to their fairgraph subclass
AmountOfChemical.set_error_handling(None)
for key, value in OMAmountOfChemical.__dict__.items():
    if isinstance(value, OMAmountOfChemical):
        fg_instance = AmountOfChemical.from_jsonld(value.to_jsonld())
        fg_instance._space = AmountOfChemical.default_space
        setattr(AmountOfChemical, key, fg_instance)
AmountOfChemical.set_error_handling("log")
