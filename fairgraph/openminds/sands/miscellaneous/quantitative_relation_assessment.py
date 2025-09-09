"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import QuantitativeRelationAssessment as OMQuantitativeRelationAssessment
from fairgraph import EmbeddedMetadata


class QuantitativeRelationAssessment(EmbeddedMetadata, OMQuantitativeRelationAssessment):
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


# cast openMINDS instances to their fairgraph subclass
QuantitativeRelationAssessment.set_error_handling(None)
for key, value in OMQuantitativeRelationAssessment.__dict__.items():
    if isinstance(value, OMQuantitativeRelationAssessment):
        fg_instance = QuantitativeRelationAssessment.from_jsonld(value.to_jsonld())
        fg_instance._space = QuantitativeRelationAssessment.default_space
        setattr(QuantitativeRelationAssessment, key, fg_instance)
QuantitativeRelationAssessment.set_error_handling("log")
