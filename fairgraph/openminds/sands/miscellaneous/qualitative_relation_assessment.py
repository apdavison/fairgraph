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
