"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class ElectrodeUsage(KGObject):
    """

    """
    default_space = "in-depth"
    type_ = ["https://openminds.ebrains.eu/ephys/ElectrodeUsage"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("anatomical_location", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalLocation", multiple=False, required=False,
              doc="no description available"),
        Field("contact_resistance", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:contactResistance", multiple=False, required=False,
              doc="no description available"),
        Field("device", "openminds.ephys.Electrode", "vocab:device", multiple=False, required=True,
              doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function."),
        Field("metadata_locations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:metadataLocation", multiple=True, required=False,
              doc="no description available"),
        Field("spatial_location", "openminds.sands.CoordinatePoint", "vocab:spatialLocation", multiple=False, required=False,
              doc="no description available"),
        Field("used_specimen", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:usedSpecimen", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)

    def __init__(self, lookup_label=None, anatomical_location=None, contact_resistance=None, device=None, metadata_locations=None, spatial_location=None, used_specimen=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, lookup_label=lookup_label, anatomical_location=anatomical_location, contact_resistance=contact_resistance, device=device, metadata_locations=metadata_locations, spatial_location=spatial_location, used_specimen=used_specimen)