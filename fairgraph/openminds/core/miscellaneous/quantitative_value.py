"""
Structured information on a quantitative value.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class QuantitativeValue(EmbeddedMetadata):
    """
    Structured information on a quantitative value.
    """
    type = ["https://openminds.ebrains.eu/core/QuantitativeValue"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("type_of_uncertainty", "openminds.controlledterms.TypeOfUncertainty", "vocab:typeOfUncertainty", multiple=False, required=False,
              doc="Distinct technique used to quantify the uncertainty of a measurement."),
        Field("uncertainties", float, "vocab:uncertainty", multiple=True, required=False,
              doc="Quantitative value range defining the uncertainty of a measurement."),
        Field("unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:unit", multiple=False, required=False,
              doc="Determinate quantity adopted as a standard of measurement."),
        Field("value", float, "vocab:value", multiple=False, required=True,
              doc="Entry for a property."),

    ]
