"""
Structured information about a measurement performed during a scientific experiment.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import Measurement as OMMeasurement
from fairgraph import EmbeddedMetadata


from datetime import datetime


class Measurement(EmbeddedMetadata, OMMeasurement):
    """
    Structured information about a measurement performed during a scientific experiment.
    """

    type_ = "https://openminds.om-i.org/types/Measurement"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = []

    def __init__(
        self,
        additional_remarks=None,
        measured_quantity=None,
        measured_with=None,
        timestamp=None,
        values=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return EmbeddedMetadata.__init__(
            self,
            data=data,
            additional_remarks=additional_remarks,
            measured_quantity=measured_quantity,
            measured_with=measured_with,
            timestamp=timestamp,
            values=values,
        )


# cast openMINDS instances to their fairgraph subclass
Measurement.set_error_handling(None)
for key, value in OMMeasurement.__dict__.items():
    if isinstance(value, OMMeasurement):
        fg_instance = Measurement.from_jsonld(value.to_jsonld())
        fg_instance._space = Measurement.default_space
        setattr(Measurement, key, fg_instance)
Measurement.set_error_handling("log")
