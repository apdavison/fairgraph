"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ParcellationEntityVersion(KGObject):
    """

    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/ParcellationEntityVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the parcellation entity version."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("additional_remarks", str, "vocab:additionalRemarks", multiple=False, required=False,
              doc="Mention of what deserves additional attention or notice."),
        Field("alternative_names", str, "vocab:alternativeName", multiple=True, required=False,
              doc="no description available"),
        Field("corrected_name", str, "vocab:correctedName", multiple=False, required=False,
              doc="no description available"),
        Field("has_annotations", "openminds.sands.AtlasAnnotation", "vocab:hasAnnotation", multiple=True, required=False,
              doc="no description available"),
        Field("has_parents", ["openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:hasParent", multiple=True, required=False,
              doc="Reference to a parent object or legal person."),
        Field("ontology_identifiers", str, "vocab:ontologyIdentifier", multiple=True, required=False,
              doc="Term or code used to identify the parcellation entity version registered within a particular ontology."),
        Field("relation_assessments", ["openminds.sands.QualitativeRelationAssessment", "openminds.sands.QuantitativeRelationAssessment"], "vocab:relationAssessment", multiple=True, required=False,
              doc="no description available"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=False,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = ('name', 'version_identifier')
