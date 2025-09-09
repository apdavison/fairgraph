"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ParcellationTerminology as OMParcellationTerminology
from fairgraph import EmbeddedMetadata


class ParcellationTerminology(EmbeddedMetadata, OMParcellationTerminology):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationTerminology"
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


# cast openMINDS instances to their fairgraph subclass
ParcellationTerminology.set_error_handling(None)
for key, value in OMParcellationTerminology.__dict__.items():
    if isinstance(value, OMParcellationTerminology):
        fg_instance = ParcellationTerminology.from_jsonld(value.to_jsonld())
        fg_instance._space = ParcellationTerminology.default_space
        setattr(ParcellationTerminology, key, fg_instance)
ParcellationTerminology.set_error_handling("log")
