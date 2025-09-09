"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.sands import ParcellationTerminologyVersion as OMParcellationTerminologyVersion
from fairgraph import EmbeddedMetadata


class ParcellationTerminologyVersion(EmbeddedMetadata, OMParcellationTerminologyVersion):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationTerminologyVersion"
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
ParcellationTerminologyVersion.set_error_handling(None)
for key, value in OMParcellationTerminologyVersion.__dict__.items():
    if isinstance(value, OMParcellationTerminologyVersion):
        fg_instance = ParcellationTerminologyVersion.from_jsonld(value.to_jsonld())
        fg_instance._space = ParcellationTerminologyVersion.default_space
        setattr(ParcellationTerminologyVersion, key, fg_instance)
ParcellationTerminologyVersion.set_error_handling("log")
