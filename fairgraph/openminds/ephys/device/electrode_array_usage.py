"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class ElectrodeArrayUsage(KGObject):
    """

    """
    default_space = "in-depth"
    type = ["https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage"]
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
        Field("additional_informations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:additionalInformation", multiple=True, required=False,
              doc="no description available"),
        Field("anatomical_locations", ["openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalLocation", multiple=True, required=False,
              doc="no description available"),
        Field("contact_resistances", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:contactResistance", multiple=True, required=False,
              doc="no description available"),
        Field("coordinate_points", "openminds.sands.CoordinatePoint", "vocab:coordinatePoint", multiple=True, required=False,
              doc="Pair or triplet of numbers defining the position in a particular two- or three dimensional plane or space."),
        Field("electrode_array", "openminds.ephys.ElectrodeArray", "vocab:electrodeArray", multiple=False, required=True,
              doc="no description available"),
        Field("used_electrodes", str, "vocab:usedElectrode", multiple=True, required=False,
              doc="no description available"),
        Field("used_specimen", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:usedSpecimen", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
