"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class ElectrodeArrayUsage(KGObject):
    """ """

    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", doc="no description available"),
        Field(
            "anatomical_location_of_arraies",
            [
                "openminds.controlledterms.CellType",
                "openminds.controlledterms.Organ",
                "openminds.controlledterms.OrganismSubstance",
                "openminds.controlledterms.SubcellularEntity",
                "openminds.controlledterms.UBERONParcellation",
                "openminds.sands.CustomAnatomicalEntity",
                "openminds.sands.ParcellationEntity",
                "openminds.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocationOfArray",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "anatomical_location_of_electrodes",
            [
                "openminds.controlledterms.CellType",
                "openminds.controlledterms.Organ",
                "openminds.controlledterms.OrganismSubstance",
                "openminds.controlledterms.SubcellularEntity",
                "openminds.controlledterms.UBERONParcellation",
                "openminds.sands.CustomAnatomicalEntity",
                "openminds.sands.ParcellationEntity",
                "openminds.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocationOfElectrodes",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "contact_resistances",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:contactResistances",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "device",
            "openminds.ephys.ElectrodeArray",
            "vocab:device",
            required=True,
            doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
        ),
        Field(
            "metadata_locations",
            ["openminds.core.File", "openminds.core.FileBundle"],
            "vocab:metadataLocation",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "spatial_location_of_electrodes",
            "openminds.sands.CoordinatePoint",
            "vocab:spatialLocationOfElectrodes",
            multiple=True,
            doc="no description available",
        ),
        Field("used_electrodes", str, "vocab:usedElectrode", multiple=True, doc="no description available"),
        Field(
            "used_specimen",
            ["openminds.core.SubjectState", "openminds.core.TissueSampleState"],
            "vocab:usedSpecimen",
            doc="no description available",
        ),
        Field(
            "placed_by",
            "openminds.ephys.ElectrodePlacement",
            "^vocab:device",
            reverse="devices",
            multiple=True,
            doc="reverse of 'device'",
        ),
        Field(
            "used_in",
            ["openminds.ephys.CellPatching", "openminds.ephys.RecordingActivity"],
            "^vocab:device",
            reverse="devices",
            multiple=True,
            doc="reverse of 'device'",
        ),
        Field(
            "used_to_record",
            "openminds.ephys.Recording",
            "^vocab:recordedWith",
            reverse="recorded_withs",
            multiple=True,
            doc="reverse of 'recordedWith'",
        ),
    ]
    existence_query_fields = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        anatomical_location_of_arraies=None,
        anatomical_location_of_electrodes=None,
        contact_resistances=None,
        device=None,
        metadata_locations=None,
        spatial_location_of_electrodes=None,
        used_electrodes=None,
        used_specimen=None,
        placed_by=None,
        used_in=None,
        used_to_record=None,
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
            lookup_label=lookup_label,
            anatomical_location_of_arraies=anatomical_location_of_arraies,
            anatomical_location_of_electrodes=anatomical_location_of_electrodes,
            contact_resistances=contact_resistances,
            device=device,
            metadata_locations=metadata_locations,
            spatial_location_of_electrodes=spatial_location_of_electrodes,
            used_electrodes=used_electrodes,
            used_specimen=used_specimen,
            placed_by=placed_by,
            used_in=used_in,
            used_to_record=used_to_record,
        )
