"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import QualitativeRelationAssessment as OMQualitativeRelationAssessment
from fairgraph import EmbeddedMetadata


class QualitativeRelationAssessment(EmbeddedMetadata, OMQualitativeRelationAssessment):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/QualitativeRelationAssessment"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self, criteria=None, in_relation_to=None, qualitative_overlap=None, id=None, data=None, space=None, scope=None
    ):
        return EmbeddedMetadata.__init__(
            self, data=data, criteria=criteria, in_relation_to=in_relation_to, qualitative_overlap=qualitative_overlap
        )


# cast openMINDS instances to their fairgraph subclass
QualitativeRelationAssessment.set_error_handling(None)
for key, value in OMQualitativeRelationAssessment.__dict__.items():
    if isinstance(value, OMQualitativeRelationAssessment):
        fg_instance = QualitativeRelationAssessment.from_jsonld(value.to_jsonld())
        fg_instance._space = QualitativeRelationAssessment.default_space
        setattr(QualitativeRelationAssessment, key, fg_instance)
QualitativeRelationAssessment.set_error_handling("log")
