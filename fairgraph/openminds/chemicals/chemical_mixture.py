"""
Structured information about a mixture of chemical substances.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ChemicalMixture(KGObject):
    """
    Structured information about a mixture of chemical substances.
    """

    default_space = "in-depth"
    type_ = "https://openminds.ebrains.eu/chemicals/ChemicalMixture"
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            doc="Mention of what deserves additional attention or notice.",
        ),
        Property(
            "has_parts",
            "openminds.chemicals.AmountOfChemical",
            "vocab:hasPart",
            multiple=True,
            required=True,
            doc="no description available",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            doc="Word or phrase that constitutes the distinctive designation of the chemical mixture.",
        ),
        Property(
            "product_source",
            "openminds.chemicals.ProductSource",
            "vocab:productSource",
            doc="no description available",
        ),
        Property(
            "type",
            "openminds.controlled_terms.ChemicalMixtureType",
            "vocab:type",
            required=True,
            doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
        ),
    ]
    reverse_properties = [
        Property(
            "composes",
            ["openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"],
            ["^vocab:insulatorMaterial", "^vocab:material"],
            reverse=["insulator_material", "material"],
            multiple=True,
            doc="reverse of insulator_material, material",
        ),
        Property(
            "used_in",
            [
                "openminds.ephys.CellPatching",
                "openminds.ephys.PipetteUsage",
                "openminds.specimen_prep.TissueCulturePreparation",
                "openminds.specimen_prep.TissueSampleSlicing",
            ],
            ["^vocab:cultureMedium", "^vocab:pipetteSolution", "^vocab:tissueBathSolution"],
            reverse=["culture_medium", "pipette_solution", "tissue_bath_solution"],
            multiple=True,
            doc="reverse of culture_medium, pipette_solution, tissue_bath_solution",
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
        return super().__init__(
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
