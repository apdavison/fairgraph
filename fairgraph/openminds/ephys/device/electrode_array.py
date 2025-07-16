"""
Structured information on an electrode array.
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


class ElectrodeArray(KGObject):
    """
    Structured information on an electrode array.
    """

    default_space = "in-depth"
    type_ = "https://openminds.ebrains.eu/ephys/ElectrodeArray"
    properties = [
        Property(
            "conductor_material",
            [
                "openminds.chemicals.ChemicalMixture",
                "openminds.chemicals.ChemicalSubstance",
                "openminds.controlled_terms.MolecularEntity",
            ],
            "vocab:conductorMaterial",
            doc="no description available",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the electrode array.",
        ),
        Property(
            "device_type",
            "openminds.controlled_terms.DeviceType",
            "vocab:deviceType",
            required=True,
            doc="no description available",
        ),
        Property(
            "digital_identifier",
            ["openminds.core.DOI", "openminds.core.RRID"],
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property(
            "electrode_identifiers",
            str,
            "vocab:electrodeIdentifier",
            multiple=True,
            required=True,
            doc="no description available",
        ),
        Property(
            "insulator_material",
            [
                "openminds.chemicals.ChemicalMixture",
                "openminds.chemicals.ChemicalSubstance",
                "openminds.controlled_terms.MolecularEntity",
            ],
            "vocab:insulatorMaterial",
            doc="no description available",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            doc="Term or code that identifies the electrode array within a particular product.",
        ),
        Property(
            "intrinsic_resistance",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:intrinsicResistance",
            doc="no description available",
        ),
        Property("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Property(
            "manufacturers",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:manufacturer",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the electrode array.",
        ),
        Property(
            "number_of_electrodes", int, "vocab:numberOfElectrodes", required=True, doc="no description available"
        ),
        Property(
            "owners",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:owner",
            multiple=True,
            doc="no description available",
        ),
        Property("serial_number", str, "vocab:serialNumber", doc="no description available"),
    ]
    reverse_properties = [
        Property(
            "is_part_of",
            "openminds.core.Setup",
            "^vocab:hasPart",
            reverse="has_parts",
            multiple=True,
            doc="reverse of 'has_parts'",
        ),
        Property(
            "usage",
            "openminds.ephys.ElectrodeArrayUsage",
            "^vocab:device",
            reverse="device",
            multiple=True,
            doc="reverse of 'device'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        name=None,
        lookup_label=None,
        conductor_material=None,
        description=None,
        device_type=None,
        digital_identifier=None,
        electrode_identifiers=None,
        insulator_material=None,
        internal_identifier=None,
        intrinsic_resistance=None,
        is_part_of=None,
        manufacturers=None,
        number_of_electrodes=None,
        owners=None,
        serial_number=None,
        usage=None,
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
            lookup_label=lookup_label,
            conductor_material=conductor_material,
            description=description,
            device_type=device_type,
            digital_identifier=digital_identifier,
            electrode_identifiers=electrode_identifiers,
            insulator_material=insulator_material,
            internal_identifier=internal_identifier,
            intrinsic_resistance=intrinsic_resistance,
            is_part_of=is_part_of,
            manufacturers=manufacturers,
            number_of_electrodes=number_of_electrodes,
            owners=owners,
            serial_number=serial_number,
            usage=usage,
        )
