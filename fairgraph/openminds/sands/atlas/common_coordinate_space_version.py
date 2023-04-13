"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class CommonCoordinateSpaceVersion(KGObject):
    """

    """
    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=False,
              doc="Whole, non-abbreviated name of the common coordinate space version."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the common coordinate space version."),
        Field("abbreviation", str, "vocab:abbreviation", multiple=False, required=False,
              doc="no description available"),
        Field("accessibility", "openminds.controlledterms.ProductAccessibility", "vocab:accessibility", multiple=False, required=True,
              doc="Level to which something is accessible to the common coordinate space version."),
        Field("anatomical_axes_orientation", "openminds.controlledterms.AnatomicalAxesOrientation", "vocab:anatomicalAxesOrientation", multiple=False, required=True,
              doc="Relation between reference planes used in anatomy and mathematics."),
        Field("authors", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("axes_origins", "openminds.core.QuantitativeValue", "vocab:axesOrigin", multiple=True, required=True,
              doc="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space."),
        Field("copyright", "openminds.core.Copyright", "vocab:copyright", multiple=False, required=False,
              doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period."),
        Field("custodians", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("default_images", "openminds.core.File", "vocab:defaultImage", multiple=True, required=False,
              doc="Two or three dimensional image that particluarly represents a specific coordinate space."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the common coordinate space version."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.ISBN", "openminds.core.RRID"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("full_documentation", ["openminds.core.DOI", "openminds.core.File", "openminds.core.WebResource"], "vocab:fullDocumentation", multiple=False, required=True,
              doc="Non-abridged instructions, comments, and information for using a particular product."),
        Field("funding", "openminds.core.Funding", "vocab:funding", multiple=True, required=False,
              doc="Money provided by a legal person for a particular purpose."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the common coordinate space version."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("is_alternative_version_of", "openminds.sands.CommonCoordinateSpaceVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.sands.CommonCoordinateSpaceVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("keywords", ["openminds.controlledterms.ActionStatusType", "openminds.controlledterms.AgeCategory", "openminds.controlledterms.AnalysisTechnique", "openminds.controlledterms.AnatomicalAxesOrientation", "openminds.controlledterms.AnatomicalIdentificationType", "openminds.controlledterms.AnatomicalPlane", "openminds.controlledterms.AnnotationCriteriaType", "openminds.controlledterms.AnnotationType", "openminds.controlledterms.AtlasType", "openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.ChemicalMixtureType", "openminds.controlledterms.Colormap", "openminds.controlledterms.ContributionType", "openminds.controlledterms.CranialWindowConstructionType", "openminds.controlledterms.CranialWindowReinforcementType", "openminds.controlledterms.CriteriaQualityType", "openminds.controlledterms.DataType", "openminds.controlledterms.DeviceType", "openminds.controlledterms.DifferenceMeasure", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.EducationalLevel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.EthicsAssessment", "openminds.controlledterms.ExperimentalApproach", "openminds.controlledterms.FileBundleGrouping", "openminds.controlledterms.FileRepositoryType", "openminds.controlledterms.FileUsageRole", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.Language", "openminds.controlledterms.Laterality", "openminds.controlledterms.LearningResourceType", "openminds.controlledterms.MeasuredQuantity", "openminds.controlledterms.MetaDataModelType", "openminds.controlledterms.ModelAbstractionLevel", "openminds.controlledterms.ModelScope", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OperatingDevice", "openminds.controlledterms.OperatingSystem", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.PatchClampVariation", "openminds.controlledterms.PreparationType", "openminds.controlledterms.ProductAccessibility", "openminds.controlledterms.ProgrammingLanguage", "openminds.controlledterms.QualitativeOverlap", "openminds.controlledterms.SemanticDataType", "openminds.controlledterms.Service", "openminds.controlledterms.SetupType", "openminds.controlledterms.SoftwareApplicationCategory", "openminds.controlledterms.SoftwareFeature", "openminds.controlledterms.Species", "openminds.controlledterms.StimulationApproach", "openminds.controlledterms.StimulationTechnique", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.SubjectAttribute", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.Technique", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.Terminology", "openminds.controlledterms.TissueSampleAttribute", "openminds.controlledterms.TissueSampleType", "openminds.controlledterms.TypeOfUncertainty", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.UnitOfMeasurement", "openminds.controlledterms.VisualStimulusType"], "vocab:keyword", multiple=True, required=False,
              doc="Significant word or concept that are representative of the common coordinate space version."),
        Field("license", "openminds.core.License", "vocab:license", multiple=False, required=False,
              doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something."),
        Field("native_unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:nativeUnit", multiple=False, required=True,
              doc="Determinate quantity used in the original measurement."),
        Field("ontology_identifiers", str, "vocab:ontologyIdentifier", multiple=True, required=False,
              doc="Term or code used to identify the common coordinate space version registered within a particular ontology."),
        Field("other_contributions", "openminds.core.Contribution", "vocab:otherContribution", multiple=True, required=False,
              doc="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere."),
        Field("related_publications", ["openminds.core.DOI", "openminds.core.HANDLE", "openminds.core.ISBN", "openminds.core.ISSN", "openminds.publications.Book", "openminds.publications.Chapter", "openminds.publications.ScholarlyArticle"], "vocab:relatedPublication", multiple=True, required=False,
              doc="Reference to something that was made available for the general public to see or buy."),
        Field("release_date", date, "vocab:releaseDate", multiple=False, required=True,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("repository", "openminds.core.FileRepository", "vocab:repository", multiple=False, required=False,
              doc="Place, room, or container where something is deposited or stored."),
        Field("support_channels", str, "vocab:supportChannel", multiple=True, required=False,
              doc="Way of communication used to interact with users or customers."),
        Field("used_specimens", ["openminds.core.Subject", "openminds.core.SubjectGroup", "openminds.core.TissueSample", "openminds.core.TissueSampleCollection"], "vocab:usedSpecimen", multiple=True, required=False,
              doc="no description available"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = ('alias', 'accessibility', 'anatomical_axes_orientation', 'axes_origins', 'full_documentation', 'native_unit', 'release_date', 'version_identifier', 'version_innovation')

    def __init__(self, name=None, alias=None, abbreviation=None, accessibility=None, anatomical_axes_orientation=None, authors=None, axes_origins=None, copyright=None, custodians=None, default_images=None, description=None, digital_identifier=None, full_documentation=None, funding=None, homepage=None, how_to_cite=None, is_alternative_version_of=None, is_new_version_of=None, keywords=None, license=None, native_unit=None, ontology_identifiers=None, other_contributions=None, related_publications=None, release_date=None, repository=None, support_channels=None, used_specimens=None, version_identifier=None, version_innovation=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, space=space, scope=scope, data=data, name=name, alias=alias, abbreviation=abbreviation, accessibility=accessibility, anatomical_axes_orientation=anatomical_axes_orientation, authors=authors, axes_origins=axes_origins, copyright=copyright, custodians=custodians, default_images=default_images, description=description, digital_identifier=digital_identifier, full_documentation=full_documentation, funding=funding, homepage=homepage, how_to_cite=how_to_cite, is_alternative_version_of=is_alternative_version_of, is_new_version_of=is_new_version_of, keywords=keywords, license=license, native_unit=native_unit, ontology_identifiers=ontology_identifiers, other_contributions=other_contributions, related_publications=related_publications, release_date=release_date, repository=repository, support_channels=support_channels, used_specimens=used_specimens, version_identifier=version_identifier, version_innovation=version_innovation)