"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Craniotomy(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Craniotomy"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("anesthesia", str, "vocab:anesthesia", multiple=False, required=True,
              doc="no description available"),
        Field("diameter", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:diameter", multiple=False, required=True,
              doc="no description available"),
        Field("fluorescence_labelling", str, "vocab:fluorescenceLabelling", multiple=False, required=False,
              doc="no description available"),
        Field("input", "openminds.core.SubjectState", "vocab:input", multiple=False, required=False,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("output", "openminds.core.SubjectState", "vocab:output", multiple=False, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("window_type", "openminds.controlledterms.CranialWindowType", "vocab:windowType", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('anesthesia', 'diameter', 'window_type')
