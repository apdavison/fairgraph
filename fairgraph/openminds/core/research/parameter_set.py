"""
Structured information on a used parameter set.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3, EmbeddedMetadata
from fairgraph.fields import Field


class ParameterSet(EmbeddedMetadata):
    """
    Structured information on a used parameter set.
    """
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
        Field("relevant_for", ["openminds.controlledterms.BehavioralTask", "openminds.controlledterms.Technique"], "vocab:relevantFor", multiple=False, required=False,
              doc="Reference to what or whom something or someone bears siginificance."),
        Field("parameters", ["openminds.core.NumericalParameter", "openminds.core.StringParameter"], "vocab:parameter", multiple=True, required=True,
              doc="Digital or physical property determining a particular function, characteristic or behavior of something."),

    ]
