"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ParcellationTerminology
from fairgraph import EmbeddedMetadata


class ParcellationTerminology(EmbeddedMetadata, ParcellationTerminology):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ParcellationTerminology"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        data_locations=None,
        has_entities=None,
        ontology_identifiers=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            data_locations=data_locations,
            has_entities=has_entities,
            ontology_identifiers=ontology_identifiers,
        )
