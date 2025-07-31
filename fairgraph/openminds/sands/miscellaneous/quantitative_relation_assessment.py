"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import QuantitativeRelationAssessment
from fairgraph import EmbeddedMetadata


class QuantitativeRelationAssessment(EmbeddedMetadata, QuantitativeRelationAssessment):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/QuantitativeRelationAssessment"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self, criteria=None, in_relation_to=None, quantitative_overlap=None, id=None, data=None, space=None, scope=None
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            criteria=criteria,
            in_relation_to=in_relation_to,
            quantitative_overlap=quantitative_overlap,
        )
