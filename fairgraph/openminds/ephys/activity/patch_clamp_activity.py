"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class PatchClampActivity(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/PatchClampActivity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("bath_solution", str, "vocab:bathSolution", multiple=False, required=True,
              doc="no description available"),
        Field("temperature", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:temperature", multiple=False, required=True,
              doc="no description available"),
        Field("input", ["openminds.core.SubjectState", "openminds.core.TissueSampleState"], "vocab:input", multiple=False, required=False,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("outputs", "openminds.ephys.PatchedCell", "vocab:output", multiple=True, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("technique", "openminds.controlledterms.PatchClampVariation", "vocab:technique", multiple=False, required=False,
              doc="Method of accomplishing a desired aim."),

    ]
    existence_query_fields = ('bath_solution', 'temperature')
