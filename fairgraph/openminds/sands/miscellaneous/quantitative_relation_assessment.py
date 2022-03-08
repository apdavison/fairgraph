"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class QuantitativeRelationAssessment(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/QuantitativeRelationAssessment"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("criteria", "openminds.core.ProtocolExecution", "vocab:criteria", multiple=False, required=False,
              doc="Aspects or standards on which a judgement or decision is based."),
        Field("in_relation_to", "openminds.sands.ParcellationEntityVersion", "vocab:inRelationTo", multiple=False, required=True,
              doc="Reference to a related element."),
        Field("quantitative_overlap", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:quantitativeOverlap", multiple=False, required=True,
              doc="Numerical characterization of how much two things occupy the same space."),

    ]
