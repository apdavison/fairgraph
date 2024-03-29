"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.fields import Field


from datetime import date
from fairgraph.base import IRI


class Chapter(KGObject):
    """
    <description not available>
    """

    default_space = "livepapers"
    type_ = ["https://openminds.ebrains.eu/publications/Chapter"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the chapter.",
        ),
        Field("abstract", str, "vocab:abstract", doc="no description available"),
        Field(
            "authors",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:author",
            multiple=True,
            required=True,
            doc="Creator of a literary or creative work, as well as a dataset publication.",
        ),
        Field(
            "cited_publications",
            ["openminds.core.DOI", "openminds.core.ISBN"],
            "vocab:citedPublication",
            multiple=True,
            doc="no description available",
        ),
        Field(
            "copyright",
            "openminds.core.Copyright",
            "vocab:copyright",
            doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
        ),
        Field("creation_date", date, "vocab:creationDate", doc="no description available"),
        Field(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Field(
            "digital_identifier",
            "openminds.core.DOI",
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Field("editors", "openminds.core.Person", "vocab:editor", multiple=True, doc="no description available"),
        Field(
            "funding",
            "openminds.core.Funding",
            "vocab:funding",
            multiple=True,
            doc="Money provided by a legal person for a particular purpose.",
        ),
        Field(
            "iri",
            IRI,
            "vocab:IRI",
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
        Field(
            "is_part_of",
            "openminds.publications.Book",
            "vocab:isPartOf",
            required=True,
            doc="Reference to the ensemble of multiple things or beings.",
        ),
        Field(
            "keywords",
            [
                "openminds.controlledterms.ActionStatusType",
                "openminds.controlledterms.AgeCategory",
                "openminds.controlledterms.AnalysisTechnique",
                "openminds.controlledterms.AnatomicalAxesOrientation",
                "openminds.controlledterms.AnatomicalIdentificationType",
                "openminds.controlledterms.AnatomicalPlane",
                "openminds.controlledterms.AnnotationCriteriaType",
                "openminds.controlledterms.AnnotationType",
                "openminds.controlledterms.AtlasType",
                "openminds.controlledterms.AuditoryStimulusType",
                "openminds.controlledterms.BiologicalOrder",
                "openminds.controlledterms.BiologicalProcess",
                "openminds.controlledterms.BiologicalSex",
                "openminds.controlledterms.BreedingType",
                "openminds.controlledterms.CellCultureType",
                "openminds.controlledterms.CellType",
                "openminds.controlledterms.ChemicalMixtureType",
                "openminds.controlledterms.Colormap",
                "openminds.controlledterms.ContributionType",
                "openminds.controlledterms.CranialWindowConstructionType",
                "openminds.controlledterms.CranialWindowReinforcementType",
                "openminds.controlledterms.CriteriaQualityType",
                "openminds.controlledterms.DataType",
                "openminds.controlledterms.DeviceType",
                "openminds.controlledterms.DifferenceMeasure",
                "openminds.controlledterms.Disease",
                "openminds.controlledterms.DiseaseModel",
                "openminds.controlledterms.EducationalLevel",
                "openminds.controlledterms.ElectricalStimulusType",
                "openminds.controlledterms.EthicsAssessment",
                "openminds.controlledterms.ExperimentalApproach",
                "openminds.controlledterms.FileBundleGrouping",
                "openminds.controlledterms.FileRepositoryType",
                "openminds.controlledterms.FileUsageRole",
                "openminds.controlledterms.GeneticStrainType",
                "openminds.controlledterms.GustatoryStimulusType",
                "openminds.controlledterms.Handedness",
                "openminds.controlledterms.Language",
                "openminds.controlledterms.Laterality",
                "openminds.controlledterms.LearningResourceType",
                "openminds.controlledterms.MeasuredQuantity",
                "openminds.controlledterms.MeasuredSignalType",
                "openminds.controlledterms.MetaDataModelType",
                "openminds.controlledterms.ModelAbstractionLevel",
                "openminds.controlledterms.ModelScope",
                "openminds.controlledterms.MolecularEntity",
                "openminds.controlledterms.OlfactoryStimulusType",
                "openminds.controlledterms.OperatingDevice",
                "openminds.controlledterms.OperatingSystem",
                "openminds.controlledterms.OpticalStimulusType",
                "openminds.controlledterms.Organ",
                "openminds.controlledterms.OrganismSubstance",
                "openminds.controlledterms.OrganismSystem",
                "openminds.controlledterms.PatchClampVariation",
                "openminds.controlledterms.PreparationType",
                "openminds.controlledterms.ProductAccessibility",
                "openminds.controlledterms.ProgrammingLanguage",
                "openminds.controlledterms.QualitativeOverlap",
                "openminds.controlledterms.SemanticDataType",
                "openminds.controlledterms.Service",
                "openminds.controlledterms.SetupType",
                "openminds.controlledterms.SoftwareApplicationCategory",
                "openminds.controlledterms.SoftwareFeature",
                "openminds.controlledterms.Species",
                "openminds.controlledterms.StimulationApproach",
                "openminds.controlledterms.StimulationTechnique",
                "openminds.controlledterms.SubcellularEntity",
                "openminds.controlledterms.SubjectAttribute",
                "openminds.controlledterms.TactileStimulusType",
                "openminds.controlledterms.Technique",
                "openminds.controlledterms.TermSuggestion",
                "openminds.controlledterms.Terminology",
                "openminds.controlledterms.TissueSampleAttribute",
                "openminds.controlledterms.TissueSampleType",
                "openminds.controlledterms.TypeOfUncertainty",
                "openminds.controlledterms.UBERONParcellation",
                "openminds.controlledterms.UnitOfMeasurement",
                "openminds.controlledterms.VisualStimulusType",
            ],
            "vocab:keyword",
            multiple=True,
            doc="Significant word or concept that are representative of the chapter.",
        ),
        Field(
            "license",
            "openminds.core.License",
            "vocab:license",
            doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
        ),
        Field("modification_date", date, "vocab:modificationDate", doc="no description available"),
        Field("pagination", str, "vocab:pagination", doc="no description available"),
        Field("publication_date", date, "vocab:publicationDate", required=True, doc="no description available"),
        Field(
            "publisher",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:publisher",
            doc="no description available",
        ),
        Field(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            doc="Term or code used to identify the version of something.",
        ),
        Field(
            "related_to",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.ModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.LivePaperVersion",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:relatedPublication",
            reverse="related_publications",
            multiple=True,
            doc="reverse of 'relatedPublication'",
        ),
    ]
    existence_query_fields = ("authors", "is_part_of", "name", "publication_date")

    def __init__(
        self,
        name=None,
        abstract=None,
        authors=None,
        cited_publications=None,
        copyright=None,
        creation_date=None,
        custodians=None,
        digital_identifier=None,
        editors=None,
        funding=None,
        iri=None,
        is_part_of=None,
        keywords=None,
        license=None,
        modification_date=None,
        pagination=None,
        publication_date=None,
        publisher=None,
        version_identifier=None,
        related_to=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            abstract=abstract,
            authors=authors,
            cited_publications=cited_publications,
            copyright=copyright,
            creation_date=creation_date,
            custodians=custodians,
            digital_identifier=digital_identifier,
            editors=editors,
            funding=funding,
            iri=iri,
            is_part_of=is_part_of,
            keywords=keywords,
            license=license,
            modification_date=modification_date,
            pagination=pagination,
            publication_date=publication_date,
            publisher=publisher,
            version_identifier=version_identifier,
            related_to=related_to,
        )
