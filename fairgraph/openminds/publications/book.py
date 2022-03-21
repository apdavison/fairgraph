"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Book(KGObject):
    """

    """
    default_space = "publications"
    type = ["https://openminds.ebrains.eu/publications/Book"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the book."),
        Field("alias", str, "vocab:shortName", multiple=False, required=False,
              doc="Shortened or fully abbreviated name of the book."),
        Field("iri", IRI, "vocab:IRI", multiple=False, required=False,
              doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646."),
        Field("abouts", ["openminds.core.DatasetVersion", "openminds.core.ModelVersion", "openminds.core.SoftwareVersion"], "vocab:about", multiple=True, required=False,
              doc="no description available"),
        Field("abstract", str, "vocab:abstract", multiple=False, required=False,
              doc="no description available"),
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("citations", ["openminds.publications.Book", "openminds.publications.Chapter", "openminds.publications.LivePaper", "openminds.publications.ScholarlyArticle"], "vocab:citation", multiple=True, required=False,
              doc="no description available"),
        Field("copyright", "openminds.core.Copyright", "vocab:copyright", multiple=False, required=False,
              doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period."),
        Field("creation_date", date, "vocab:creationDate", multiple=False, required=False,
              doc="no description available"),
        Field("custodian", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=False, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
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
        Field("release_date", date, "vocab:releaseDate", multiple=False, required=False,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=False,
              doc="Term or code used to identify the version of something."),

    ]
    existence_query_fields = ('name',)
