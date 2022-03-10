"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class CulturingActivity(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/CulturingActivity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("culture_age", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:cultureAge", multiple=False, required=False,
              doc="no description available"),
        Field("culture_solution", str, "vocab:cultureSolution", multiple=False, required=True,
              doc="no description available"),
        Field("culture_type", "openminds.controlledterms.CultureType", "vocab:cultureType", multiple=False, required=True,
              doc="no description available"),
        Field("input", ["openminds.core.SubjectGroupState", "openminds.core.SubjectState"], "vocab:input", multiple=False, required=False,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("output", "openminds.core.TissueSampleState", "vocab:output", multiple=False, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),

    ]
    existence_query_fields = ('culture_solution', 'culture_type')
