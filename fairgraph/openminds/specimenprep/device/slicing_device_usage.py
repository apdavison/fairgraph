"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class SlicingDeviceUsage(KGObject):
    """

    """
    default_space = "in-depth"
    type = ["https://openminds.ebrains.eu/specimenPrep/SlicingDeviceUsage"]
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
        Field("device", "openminds.specimenprep.SlicingDevice", "vocab:device", multiple=False, required=True,
              doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function."),
        Field("metadata_locations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:metadataLocation", multiple=True, required=False,
              doc="no description available"),
        Field("oscillation_amplitude", "openminds.core.QuantitativeValue", "vocab:oscillationAmplitude", multiple=False, required=False,
              doc="no description available"),
        Field("slice_thickness", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:sliceThickness", multiple=False, required=True,
              doc="no description available"),
        Field("slicing_angles", ["openminds.core.NumericalProperty", "openminds.core.QuantitativeValue"], "vocab:slicingAngle", multiple=True, required=False,
              doc="no description available"),
        Field("slicing_plane", "openminds.controlledterms.AnatomicalPlane", "vocab:slicingPlane", multiple=False, required=True,
              doc="no description available"),
        Field("slicing_speed", "openminds.core.QuantitativeValue", "vocab:slicingSpeed", multiple=False, required=False,
              doc="no description available"),
        Field("used_specimen", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:usedSpecimen", multiple=False, required=False,
              doc="no description available"),
        Field("vibration_frequency", "openminds.core.QuantitativeValue", "vocab:vibrationFrequency", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
