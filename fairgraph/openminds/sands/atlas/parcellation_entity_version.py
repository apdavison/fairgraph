"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field




class ParcellationEntityVersion(KGObjectV3):
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
        Field("has_annotation", "openminds.sands.AtlasAnnotation", "vocab:hasAnnotation", multiple=False, required=False,
              doc="no description available"),
        Field("has_parents", ["openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:hasParent", multiple=True, required=False,
              doc="Reference to a parent object or legal person."),
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the parcellation entity version."),
        Field("ontology_identifier", IRI, "vocab:ontologyIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the parcellation entity version registered within a particular ontology."),
        Field("relation_assessments", ["openminds.sands.QualitativeRelationAssessment", "openminds.sands.QuantitativeRelationAssessment"], "vocab:relationAssessment", multiple=True, required=False,
              doc="no description available"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=False,
              doc="Documentation on what changed in comparison to a previously published form of something."),
        
    ]
    existence_query_fields = ('name', 'version_identifier')

