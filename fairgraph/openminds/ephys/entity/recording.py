"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Recording(KGObject):
    """

    """
    default_space = "electrophysiology"
    type = ["https://openminds.ebrains.eu/ephys/Recording"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the recording."),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("channels", "openminds.ephys.Channel", "vocab:channel", multiple=True, required=True,
              doc="no description available"),
        Field("data_location", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:dataLocation", multiple=False, required=True,
              doc="no description available"),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the recording within a particular product."),
        Field("previous_recording", "openminds.ephys.Recording", "vocab:previousRecording", multiple=False, required=False,
              doc="no description available"),
        Field("recorded_with", ["openminds.ephys.ElectrodeArrayUsage", "openminds.ephys.ElectrodeUsage", "openminds.ephys.PipetteUsage"], "vocab:recordedWith", multiple=False, required=True,
              doc="no description available"),
        Field("sampling_frequency", "openminds.core.QuantitativeValue", "vocab:samplingFrequency", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('channels', 'data_location', 'recorded_with', 'sampling_frequency')
