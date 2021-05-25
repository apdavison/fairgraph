"""
Structured information on an electrode contact.
"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base import KGObject
from fairgraph.fields import Field


class ElectrodeContact(KGObject):
    """
    Structured information on an electrode contact.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/ElectrodeContact"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("coordinate_point", "openminds.sands.CoordinatePoint", "vocab:coordinatePoint", multiple=False, required=True,
              doc="Pair or triplet of numbers defining the position in a particular two- or three dimensional plane or space."),
        Field("defined_ins", "openminds.core.File", "vocab:definedIn", multiple=True, required=False,
              doc="Reference to a file instance in which something is stored."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=True,
              doc="Term or code that identifies the electrode contact within a particular product."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("related_recordings", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:relatedRecording", multiple=True, required=False,
              doc="Reference to the written, stored evidence of something."),
        Field("related_stimulations", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:relatedStimulation", multiple=True, required=False,
              doc="Reference to the written, stored function used as a physiological stimulus."),
        Field("visualized_ins", "openminds.core.File", "vocab:visualizedIn", multiple=True, required=False,
              doc="Reference to an image in which something is visible."),
        
    ]
    existence_query_fields = ('name',)