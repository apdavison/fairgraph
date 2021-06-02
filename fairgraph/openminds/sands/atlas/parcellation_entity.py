"""

"""

# this file was auto-generated

from datetime import datetime
from fairgraph.base_v3 import KGObjectV3
from fairgraph.fields import Field


class ParcellationEntity(KGObjectV3):
    """

    """
    space = "model"
    type = ["https://openminds.ebrains.eu/sands/ParcellationEntity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("has_annotation", "openminds.sands.AtlasAnnotation", "vocab:hasAnnotation", multiple=False, required=False,
              doc="no description available"),
        Field("has_parent", "openminds.sands.ParcellationEntity", "vocab:hasParent", multiple=False, required=False,
              doc="Reference to a parent object or legal person."),
        Field("is_part_ofs", "openminds.sands.ParcellationTerminology", "vocab:isPartOf", multiple=True, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of a being or thing."),
        Field("ontology_identifier", str, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify something or someone registered within a particular ontology."),
        Field("related_uberon_term", "openminds.controlledterms.UBERONParcellation", "vocab:relatedUBERONTerm", multiple=False, required=False,
              doc="no description available"),
        Field("relation_assessments", ["openminds.sands.QualitativeRelationAssessment", "openminds.sands.QuantitativeRelationAssessment"], "vocab:relationAssessment", multiple=True, required=False,
              doc="no description available"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=False,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = None