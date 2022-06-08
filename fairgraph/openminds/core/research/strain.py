"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Strain(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Strain"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the strain."),
        Field("rrid", "openminds.core.RRID", "vocab:RRID", multiple=False, required=False,
              doc="no description available"),
        Field("background_strains", "openminds.core.Strain", "vocab:backgroundStrain", multiple=True, required=False,
              doc="no description available"),
        Field("breeding_type", "openminds.controlledterms.BreedingType", "vocab:breedingType", multiple=False, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the strain."),
        Field("disease_models", ["openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel"], "vocab:diseaseModel", multiple=True, required=False,
              doc="no description available"),
        Field("genetic_strain_type", "openminds.controlledterms.GeneticStrainType", "vocab:geneticStrainType", multiple=False, required=True,
              doc="no description available"),
        Field("identifiers", str, "vocab:identifier", multiple=True, required=False,
              doc="Term or code used to identify the strain."),
        Field("laboratory_code", str, "vocab:laboratoryCode", multiple=False, required=False,
              doc="no description available"),
        Field("ontology_identifiers", str, "vocab:ontologyIdentifier", multiple=True, required=False,
              doc="Term or code used to identify the strain registered within a particular ontology."),
        Field("phenotype", str, "vocab:phenotype", multiple=False, required=False,
              doc="Physical expression of one or more genes of an organism."),
        Field("species", "openminds.controlledterms.Species", "vocab:species", multiple=False, required=True,
              doc="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective."),
        Field("stock_number", "openminds.core.StockNumber", "vocab:stockNumber", multiple=False, required=False,
              doc="no description available"),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name', 'genetic_strain_type', 'species')
