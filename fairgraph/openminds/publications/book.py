"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Book(KGObject):
    """

    """
    default_space = "livepapers"
    type = ["https://openminds.ebrains.eu/publications/Book"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the book."),
        Field("iri", IRI, "vocab:IRI", multiple=False, required=False,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("abstract", str, "vocab:abstract", multiple=False, required=False,
              doc="no description available"),
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("cited_publications", ["openminds.core.DOI", "openminds.core.ISBN"], "vocab:citedPublication", multiple=True, required=False,
              doc="no description available"),
        Field("copyright", "openminds.core.Copyright", "vocab:copyright", multiple=False, required=False,
              doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period."),
        Field("custodians", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("date_created", date, "vocab:dateCreated", multiple=False, required=False,
              doc="no description available"),
        Field("date_modified", date, "vocab:dateModified", multiple=False, required=False,
              doc="no description available"),
        Field("date_published", date, "vocab:datePublished", multiple=False, required=True,
              doc="no description available"),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.ISBN"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("editors", "openminds.core.Person", "vocab:editor", multiple=True, required=False,
              doc="no description available"),
        Field("funding", "openminds.core.Funding", "vocab:funding", multiple=True, required=False,
              doc="Money provided by a legal person for a particular purpose."),
        Field("keywords", ["openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.Organ", "openminds.controlledterms.Species", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:keyword", multiple=True, required=False,
              doc="Significant word or concept that are representative of the book."),
        Field("license", "openminds.core.License", "vocab:license", multiple=False, required=False,
              doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something."),
        Field("publisher", ["openminds.core.Organization", "openminds.core.Person"], "vocab:publisher", multiple=False, required=False,
              doc="no description available"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the version of something."),

    ]
    existence_query_fields = ('name', 'date_published')
