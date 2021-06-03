"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class Visualization(KGObjectV3):
    """

    """
    space = "model"
    type = ["https://openminds.ebrains.eu/computation/Visualization"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("inputs", ["openminds.core.FileBundle", "openminds.core.File", "openminds.core.SoftwareVersion"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("outputs", ["openminds.core.FileBundle", "openminds.core.File"], "vocab:output", multiple=True, required=False,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("environment", "openminds.computation.Environment", "vocab:environment", multiple=False, required=True,
              doc="no description available"),
        Field("launch_configuration", "openminds.computation.LaunchConfiguration", "vocab:launchConfiguration", multiple=False, required=True,
              doc="no description available"),
        Field("started_at_time", datetime, "vocab:startedAtTime", multiple=False, required=True,
              doc="no description available"),
        Field("ended_at_time", datetime, "vocab:endedAtTime", multiple=False, required=False,
              doc="no description available"),
        Field("started_by", ["openminds.core.Person", "openminds.computation.SoftwareAgent"], "vocab:startedBy", multiple=False, required=False,
              doc="no description available"),
        Field("was_informed_by", "openminds.computation.Computation", "vocab:wasInformedBy", multiple=False, required=False,
              doc="no description available"),
        Field("status", "openminds.controlledterms.ActionStatusType", "vocab:status", multiple=False, required=False,
              doc="no description available"),
        Field("resource_usages", ["openminds.core.QuantitativeValue", "openminds.core.QuantitativeValueRange"], "vocab:resourceUsage", multiple=True, required=False,
              doc="no description available"),
        Field("tagss", str, "vocab:tags", multiple=True, required=False,
              doc="no description available"),

    ]
    existence_query_fields = None