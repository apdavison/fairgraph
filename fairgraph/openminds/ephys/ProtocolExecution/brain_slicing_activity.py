"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class BrainSlicingActivity(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/BrainSlicingActivity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("input", "openminds.core.SubjectState", "vocab:input", multiple=False, required=False,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("output", "openminds.core.TissueSampleState", "vocab:output", multiple=False, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("solution", str, "vocab:solution", multiple=False, required=False,
              doc="no description available"),
        Field("cutting_thickness", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:cuttingThickness", multiple=False, required=False,
              doc="no description available"),
        Field("slicing_angle", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:slicingAngle", multiple=False, required=False,
              doc="no description available"),
        Field("slicing_plane", "openminds.controlledterms.AnatomicalPlane", "vocab:slicingPlane", multiple=False, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ()
