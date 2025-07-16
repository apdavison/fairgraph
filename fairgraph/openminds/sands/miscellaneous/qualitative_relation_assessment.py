"""
<description not available>
"""

# this file was auto-generated

from fairgraph import EmbeddedMetadata, IRI
from fairgraph.properties import Property


class QualitativeRelationAssessment(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/QualitativeRelationAssessment"
    properties = [
        Property(
            "criteria",
            "openminds.core.ProtocolExecution",
            "vocab:criteria",
            doc="Aspects or standards on which a judgement or decision is based.",
        ),
        Property(
            "in_relation_to",
            [
                "openminds.sands.CustomAnatomicalEntity",
                "openminds.sands.ParcellationEntity",
                "openminds.sands.ParcellationEntityVersion",
            ],
            "vocab:inRelationTo",
            required=True,
            doc="Reference to a related element.",
        ),
        Property(
            "qualitative_overlap",
            "openminds.controlled_terms.QualitativeOverlap",
            "vocab:qualitativeOverlap",
            required=True,
            doc="Semantic characterization of how much two things occupy the same space.",
        ),
    ]
    reverse_properties = []

    def __init__(
        self, criteria=None, in_relation_to=None, qualitative_overlap=None, id=None, data=None, space=None, scope=None
    ):
        return super().__init__(
            data=data, criteria=criteria, in_relation_to=in_relation_to, qualitative_overlap=qualitative_overlap
        )
