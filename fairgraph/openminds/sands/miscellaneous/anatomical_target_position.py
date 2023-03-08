"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class AnatomicalTargetPosition(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/sands/AnatomicalTargetPosition"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("anatomical_targets", ["openminds.controlledterms.CellType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:anatomicalTarget", multiple=True, required=True,
              doc="no description available"),
        Field("coordinates", "openminds.sands.CoordinatePoint", "vocab:coordinates", multiple=False, required=False,
              doc="Pair or triplet of numbers defining a location in a given coordinate space."),
        Field("target_identification_type", "openminds.controlledterms.AnatomicalIdentificationType", "vocab:targetIdentificationType", multiple=False, required=True,
              doc="no description available"),

    ]
