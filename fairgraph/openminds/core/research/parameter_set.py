"""
Structured information on a used parameter set.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ParameterSet(KGObject):
    """
    Structured information on a used parameter set.
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/ParameterSet"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("context", str, "vocab:context", multiple=False, required=True,
              doc="no description available"),
        Field("parameters", ["openminds.core.NumericalParameter", "openminds.core.StringParameter"], "vocab:parameter", multiple=True, required=True,
              doc="Digital or physical property determining a particular function, characteristic or behavior of something."),
        Field("relevant_for", ["openminds.controlledterms.Technique", "openminds.core.Stimulation"], "vocab:relevantFor", multiple=False, required=True,
              doc="Reference to what or whom the parameter set bears siginificance."),

    ]
    existence_query_fields = ('context', 'parameters', 'relevant_for')
