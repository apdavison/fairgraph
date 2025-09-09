"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.stimulation import EphysStimulus as OMEphysStimulus
from fairgraph import KGObject


class EphysStimulus(KGObject, OMEphysStimulus):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/EphysStimulus"
    default_space = "in-depth"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "is_stimulus_for",
            "openminds.latest.stimulation.StimulationActivity",
            "stimulus",
            reverse="stimuli",
            multiple=True,
            description="reverse of 'stimuli'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        delivered_by=None,
        description=None,
        epoch=None,
        generated_by=None,
        internal_identifier=None,
        is_stimulus_for=None,
        specifications=None,
        type=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            delivered_by=delivered_by,
            description=description,
            epoch=epoch,
            generated_by=generated_by,
            internal_identifier=internal_identifier,
            is_stimulus_for=is_stimulus_for,
            specifications=specifications,
            type=type,
        )


# cast openMINDS instances to their fairgraph subclass
EphysStimulus.set_error_handling(None)
for key, value in OMEphysStimulus.__dict__.items():
    if isinstance(value, OMEphysStimulus):
        fg_instance = EphysStimulus.from_jsonld(value.to_jsonld())
        fg_instance._space = EphysStimulus.default_space
        setattr(EphysStimulus, key, fg_instance)
EphysStimulus.set_error_handling("log")
