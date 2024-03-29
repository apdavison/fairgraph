"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.fields import Field


from datetime import date
from fairgraph.base import IRI


class MetaDataModelVersion(KGObject):
    """
    <description not available>
    """

    default_space = "metadatamodel"
    type_ = ["https://openminds.ebrains.eu/core/MetaDataModelVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("name", str, "vocab:fullName", doc="Whole, non-abbreviated name of the meta data model version."),
        Field(
            "alias",
            str,
            "vocab:shortName",
            required=True,
            doc="Shortened or fully abbreviated name of the meta data model version.",
        ),
        Field(
            "accessibility",
            "openminds.controlledterms.ProductAccessibility",
            "vocab:accessibility",
            required=True,
            doc="Level to which something is accessible to the meta data model version.",
        ),
        Field(
            "copyright",
            "openminds.core.Copyright",
            "vocab:copyright",
            doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
        ),
        Field(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the meta data model version.",
        ),
        Field(
            "developers",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:developer",
            multiple=True,
            doc="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
        ),
        Field(
            "digital_identifier",
            ["openminds.core.DOI", "openminds.core.SWHID"],
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Field(
            "full_documentation",
            ["openminds.core.DOI", "openminds.core.File", "openminds.core.WebResource"],
            "vocab:fullDocumentation",
            required=True,
            doc="Non-abridged instructions, comments, and information for using a particular product.",
        ),
        Field(
            "funding",
            "openminds.core.Funding",
            "vocab:funding",
            multiple=True,
            doc="Money provided by a legal person for a particular purpose.",
        ),
        Field("homepage", IRI, "vocab:homepage", doc="Main website of the meta data model version."),
        Field(
            "how_to_cite",
            str,
            "vocab:howToCite",
            doc="Preferred format for citing a particular object or legal person.",
        ),
        Field(
            "is_alternative_version_of",
            "openminds.core.MetaDataModelVersion",
            "vocab:isAlternativeVersionOf",
            multiple=True,
            doc="Reference to an original form where the essence was preserved, but presented in an alternative form.",
        ),
        Field(
            "is_new_version_of",
            "openminds.core.MetaDataModelVersion",
            "vocab:isNewVersionOf",
            doc="Reference to a previous (potentially outdated) particular form of something.",
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
            doc="Significant word or concept that are representative of the meta data model version.",
        ),
        Field(
            "license",
            "openminds.core.License",
            "vocab:license",
            required=True,
            doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
        ),
        Field(
            "other_contributions",
            "openminds.core.Contribution",
            "vocab:otherContribution",
            multiple=True,
            doc="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
        ),
        Field(
            "related_publications",
            [
                "openminds.core.DOI",
                "openminds.core.HANDLE",
                "openminds.core.ISBN",
                "openminds.core.ISSN",
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.ScholarlyArticle",
            ],
            "vocab:relatedPublication",
            multiple=True,
            doc="Reference to something that was made available for the general public to see or buy.",
        ),
        Field(
            "release_date",
            date,
            "vocab:releaseDate",
            required=True,
            doc="Fixed date on which a product is due to become or was made available for the general public to see or buy",
        ),
        Field(
            "repository",
            "openminds.core.FileRepository",
            "vocab:repository",
            doc="Place, room, or container where something is deposited or stored.",
        ),
        Field(
            "serialization_formats",
            "openminds.core.ContentType",
            "vocab:serializationFormat",
            multiple=True,
            doc="Form in which a particular data structure or object state is translated to for storage.",
        ),
        Field(
            "specification_formats",
            "openminds.core.ContentType",
            "vocab:specificationFormat",
            multiple=True,
            doc="Form in which a particular data structure or object state is specified in.",
        ),
        Field(
            "support_channels",
            str,
            "vocab:supportChannel",
            multiple=True,
            doc="Way of communication used to interact with users or customers.",
        ),
        Field(
            "type",
            "openminds.controlledterms.MetaDataModelType",
            "vocab:type",
            required=True,
            doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
        ),
        Field(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            required=True,
            doc="Term or code used to identify the version of something.",
        ),
        Field(
            "version_innovation",
            str,
            "vocab:versionInnovation",
            required=True,
            doc="Documentation on what changed in comparison to a previously published form of something.",
        ),
        Field(
            "comments",
            "openminds.core.Comment",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
        Field(
            "is_old_version_of",
            "openminds.core.MetaDataModelVersion",
            "^vocab:isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            doc="reverse of 'isNewVersionOf'",
        ),
        Field(
            "is_part_of",
            ["openminds.core.Project", "openminds.core.ResearchProductGroup"],
            "^vocab:hasPart",
            reverse="has_parts",
            multiple=True,
            doc="reverse of 'hasPart'",
        ),
        Field(
            "is_version_of",
            "openminds.core.MetaDataModel",
            "^vocab:hasVersion",
            reverse="versions",
            multiple=True,
            doc="reverse of 'hasVersion'",
        ),
        Field(
            "learning_resources",
            "openminds.publications.LearningResource",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
    ]
    existence_query_fields = ("alias", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        accessibility=None,
        copyright=None,
        custodians=None,
        description=None,
        developers=None,
        digital_identifier=None,
        full_documentation=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        keywords=None,
        license=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        serialization_formats=None,
        specification_formats=None,
        support_channels=None,
        type=None,
        version_identifier=None,
        version_innovation=None,
        comments=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        learning_resources=None,
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
            alias=alias,
            accessibility=accessibility,
            copyright=copyright,
            custodians=custodians,
            description=description,
            developers=developers,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            keywords=keywords,
            license=license,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            serialization_formats=serialization_formats,
            specification_formats=specification_formats,
            support_channels=support_channels,
            type=type,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
            comments=comments,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            learning_resources=learning_resources,
        )
