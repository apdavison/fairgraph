"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.v4.sands import ParcellationTerminology as OMParcellationTerminology
from fairgraph import EmbeddedMetadata


class ParcellationTerminology(EmbeddedMetadata, OMParcellationTerminology):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationTerminology"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []
    existence_query_properties = ("has_entities",)

    def __init__(
        self,
        data_locations=None,
        has_entities=None,
        ontology_identifiers=None,
        id=None,
        data=None,
        space=None,
        release_status=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            data_locations=data_locations,
            has_entities=has_entities,
            ontology_identifiers=ontology_identifiers,
        )
