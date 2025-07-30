"""
Structured information about a mixture of chemical substances.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.chemicals import ChemicalMixture
from fairgraph import KGObject


class ChemicalMixture(KGObject, ChemicalMixture):
    """
    Structured information about a mixture of chemical substances.
    """

    type_ = "https://openminds.ebrains.eu/chemicals/ChemicalMixture"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "composes",
            [
                "openminds.latest.ephys.Electrode",
                "openminds.latest.ephys.ElectrodeArray",
                "openminds.latest.ephys.Pipette",
            ],
            ["insulatorMaterial", "material"],
            reverse=["insulator_material", "material"],
            multiple=True,
            description="reverse of insulator_material, material",
        ),
        Property(
            "used_in",
            [
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.PipetteUsage",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
            ],
            ["cultureMedium", "pipetteSolution", "tissueBathSolution"],
            reverse=["culture_medium", "pipette_solution", "tissue_bath_solution"],
            multiple=True,
            description="reverse of culture_medium, pipette_solution, tissue_bath_solution",
        ),
    ]
    existence_query_properties = ("has_parts", "type")

    def __init__(
        self,
        name=None,
        additional_remarks=None,
        composes=None,
        has_parts=None,
        product_source=None,
        type=None,
        used_in=None,
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
            name=name,
            additional_remarks=additional_remarks,
            composes=composes,
            has_parts=has_parts,
            product_source=product_source,
            type=type,
            used_in=used_in,
        )
