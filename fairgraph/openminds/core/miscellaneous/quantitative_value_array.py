"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class QuantitativeValueArray(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/QuantitativeValueArray"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("negative_uncertainties", float, "vocab:negativeUncertainties", multiple=True, required=False,
              doc="no description available"),
        Field("positive_uncertainties", float, "vocab:positiveUncertainties", multiple=True, required=False,
              doc="no description available"),
        Field("type_of_uncertainty", "openminds.controlledterms.TypeOfUncertainty", "vocab:typeOfUncertainty", multiple=False, required=False,
              doc="Distinct technique used to quantify the uncertainty of a measurement."),
        Field("unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:unit", multiple=False, required=False,
              doc="Determinate quantity adopted as a standard of measurement."),
        Field("values", float, "vocab:values", multiple=True, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('values',)
