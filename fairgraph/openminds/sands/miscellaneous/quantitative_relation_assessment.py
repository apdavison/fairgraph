"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class QuantitativeRelationAssessment(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/QuantitativeRelationAssessment"
    properties = [
        Property(
            "criteria",
            "openminds.core.ProtocolExecution",
            "vocab:criteria",
            doc="Aspects or standards on which a judgement or decision is based.",
        ),
        Property(
            "in_relation_to",
            "openminds.sands.ParcellationEntityVersion",
            "vocab:inRelationTo",
            required=True,
            doc="Reference to a related element.",
        ),
        Property(
            "quantitative_overlap",
            ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"],
            "vocab:quantitativeOverlap",
            required=True,
            doc="Numerical characterization of how much two things occupy the same space.",
        ),
    ]
    reverse_properties = []

    def __init__(
        self, criteria=None, in_relation_to=None, quantitative_overlap=None, id=None, data=None, space=None, scope=None
    ):
        return super().__init__(
            data=data, criteria=criteria, in_relation_to=in_relation_to, quantitative_overlap=quantitative_overlap
        )
