"""
Structured information on data originating from human/animal studies or simulations (version level).
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field

from urllib.request import urlretrieve
from pathlib import Path
from ....utility import accepted_terms_of_use


class DatasetVersion(KGObject):
    """
    Structured information on data originating from human/animal studies or simulations (version level).
    """
    default_space = "dataset"
    type_ = ["https://openminds.ebrains.eu/core/DatasetVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=False,
              doc="Whole, non-abbreviated name of the dataset version."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the dataset version."),
        Field("accessibility", "openminds.controlledterms.ProductAccessibility", "vocab:accessibility", multiple=False, required=True,
              doc="Level to which something is accessible to the dataset version."),
        Field("authors", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("behavioral_protocols", "openminds.core.BehavioralProtocol", "vocab:behavioralProtocol", multiple=True, required=False,
              doc="no description available"),
        Field("copyright", "openminds.core.Copyright", "vocab:copyright", multiple=False, required=False,
              doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period."),
        Field("custodians", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("data_types", "openminds.controlledterms.SemanticDataType", "vocab:dataType", multiple=True, required=True,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the dataset version."),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=True,
              doc="Digital handle to identify objects or legal persons."),
        Field("ethics_assessment", "openminds.controlledterms.EthicsAssessment", "vocab:ethicsAssessment", multiple=False, required=True,
              doc="Judgment about the applied principles of conduct governing an individual or a group."),
        Field("experimental_approaches", "openminds.controlledterms.ExperimentalApproach", "vocab:experimentalApproach", multiple=True, required=True,
              doc="no description available"),
        Field("full_documentation", ["openminds.core.DOI", "openminds.core.File", "openminds.core.WebResource"], "vocab:fullDocumentation", multiple=False, required=True,
              doc="Non-abridged instructions, comments, and information for using a particular product."),
        Field("funding", "openminds.core.Funding", "vocab:funding", multiple=True, required=False,
              doc="Money provided by a legal person for a particular purpose."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the dataset version."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("input_data", ["openminds.core.DOI", "openminds.core.File", "openminds.core.FileBundle", "openminds.core.WebResource", "openminds.sands.BrainAtlasVersion", "openminds.sands.CommonCoordinateSpace"], "vocab:inputData", multiple=True, required=False,
              doc="Data that is put into a process or machine."),
        Field("is_alternative_version_of", "openminds.core.DatasetVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.core.DatasetVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("keywords", ["openminds.controlledterms.ActionStatusType", "openminds.controlledterms.AgeCategory", "openminds.controlledterms.AnalysisTechnique", "openminds.controlledterms.AnatomicalAxesOrientation", "openminds.controlledterms.AnatomicalIdentificationType", "openminds.controlledterms.AnatomicalPlane", "openminds.controlledterms.AnnotationCriteriaType", "openminds.controlledterms.AnnotationType", "openminds.controlledterms.AtlasType", "openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.ChemicalMixtureType", "openminds.controlledterms.Colormap", "openminds.controlledterms.ContributionType", "openminds.controlledterms.CranialWindowConstructionType", "openminds.controlledterms.CranialWindowReinforcementType", "openminds.controlledterms.CriteriaQualityType", "openminds.controlledterms.DataType", "openminds.controlledterms.DeviceType", "openminds.controlledterms.DifferenceMeasure", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.EducationalLevel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.EthicsAssessment", "openminds.controlledterms.ExperimentalApproach", "openminds.controlledterms.FileBundleGrouping", "openminds.controlledterms.FileRepositoryType", "openminds.controlledterms.FileUsageRole", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.Language", "openminds.controlledterms.Laterality", "openminds.controlledterms.LearningResourceType", "openminds.controlledterms.MeasuredQuantity", "openminds.controlledterms.MetaDataModelType", "openminds.controlledterms.ModelAbstractionLevel", "openminds.controlledterms.ModelScope", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OperatingDevice", "openminds.controlledterms.OperatingSystem", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.PatchClampVariation", "openminds.controlledterms.PreparationType", "openminds.controlledterms.ProductAccessibility", "openminds.controlledterms.ProgrammingLanguage", "openminds.controlledterms.QualitativeOverlap", "openminds.controlledterms.SemanticDataType", "openminds.controlledterms.Service", "openminds.controlledterms.SetupType", "openminds.controlledterms.SoftwareApplicationCategory", "openminds.controlledterms.SoftwareFeature", "openminds.controlledterms.Species", "openminds.controlledterms.StimulationApproach", "openminds.controlledterms.StimulationTechnique", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.SubjectAttribute", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.Technique", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.Terminology", "openminds.controlledterms.TissueSampleAttribute", "openminds.controlledterms.TissueSampleType", "openminds.controlledterms.TypeOfUncertainty", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.UnitOfMeasurement", "openminds.controlledterms.VisualStimulusType"], "vocab:keyword", multiple=True, required=False,
              doc="Significant word or concept that are representative of the dataset version."),
        Field("license", "openminds.core.License", "vocab:license", multiple=False, required=True,
              doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something."),
        Field("other_contributions", "openminds.core.Contribution", "vocab:otherContribution", multiple=True, required=False,
              doc="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere."),
        Field("preparation_designs", "openminds.controlledterms.PreparationType", "vocab:preparationDesign", multiple=True, required=False,
              doc="no description available"),
        Field("protocols", "openminds.core.Protocol", "vocab:protocol", multiple=True, required=False,
              doc="Plan that describes the process of a scientific or medical experiment, treatment, or procedure."),
        Field("related_publications", ["openminds.core.DOI", "openminds.core.HANDLE", "openminds.core.ISBN", "openminds.core.ISSN", "openminds.publications.Book", "openminds.publications.Chapter", "openminds.publications.ScholarlyArticle"], "vocab:relatedPublication", multiple=True, required=False,
              doc="Reference to something that was made available for the general public to see or buy."),
        Field("release_date", date, "vocab:releaseDate", multiple=False, required=True,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("repository", "openminds.core.FileRepository", "vocab:repository", multiple=False, required=False,
              doc="Place, room, or container where something is deposited or stored."),
        Field("studied_specimens", ["openminds.core.Subject", "openminds.core.SubjectGroup", "openminds.core.TissueSample", "openminds.core.TissueSampleCollection"], "vocab:studiedSpecimen", multiple=True, required=False,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.Species", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.VisualStimulusType", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),
        Field("support_channels", str, "vocab:supportChannel", multiple=True, required=False,
              doc="Way of communication used to interact with users or customers."),
        Field("techniques", ["openminds.controlledterms.AnalysisTechnique", "openminds.controlledterms.StimulationApproach", "openminds.controlledterms.StimulationTechnique", "openminds.controlledterms.Technique"], "vocab:technique", multiple=True, required=True,
              doc="Method of accomplishing a desired aim."),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = ('alias', 'version_identifier')

    def __init__(self, name=None, alias=None, accessibility=None, authors=None, behavioral_protocols=None, copyright=None, custodians=None, data_types=None, description=None, digital_identifier=None, ethics_assessment=None, experimental_approaches=None, full_documentation=None, funding=None, homepage=None, how_to_cite=None, input_data=None, is_alternative_version_of=None, is_new_version_of=None, keywords=None, license=None, other_contributions=None, preparation_designs=None, protocols=None, related_publications=None, release_date=None, repository=None, studied_specimens=None, study_targets=None, support_channels=None, techniques=None, version_identifier=None, version_innovation=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, space=space, scope=scope, data=data, name=name, alias=alias, accessibility=accessibility, authors=authors, behavioral_protocols=behavioral_protocols, copyright=copyright, custodians=custodians, data_types=data_types, description=description, digital_identifier=digital_identifier, ethics_assessment=ethics_assessment, experimental_approaches=experimental_approaches, full_documentation=full_documentation, funding=funding, homepage=homepage, how_to_cite=how_to_cite, input_data=input_data, is_alternative_version_of=is_alternative_version_of, is_new_version_of=is_new_version_of, keywords=keywords, license=license, other_contributions=other_contributions, preparation_designs=preparation_designs, protocols=protocols, related_publications=related_publications, release_date=release_date, repository=repository, studied_specimens=studied_specimens, study_targets=study_targets, support_channels=support_channels, techniques=techniques, version_identifier=version_identifier, version_innovation=version_innovation)

    def download(self, local_path, client, accept_terms_of_use=False):
        if accepted_terms_of_use(client, accept_terms_of_use=accept_terms_of_use):
            repo = self.repository.resolve(client, scope=self.scope or None)
            if (repo.iri.value.startswith("https://object.cscs.ch/v1/AUTH")
                or repo.iri.value.startswith("https://data-proxy.ebrains.eu/api/v1/public")
            ):
                zip_archive_url = f"https://data.kg.ebrains.eu/zip?container={repo.iri.value}"
            else:
                raise NotImplementedError("Download not yet implemented for this repository type")
            if local_path.endswith(".zip"):
                local_filename = Path(local_path)
            else:
                local_filename = Path(local_path) / (zip_archive_url.split("/")[-1] + ".zip")
            local_filename.parent.mkdir(parents=True, exist_ok=True)
            local_filename, headers = urlretrieve(zip_archive_url, local_filename)
            return local_filename, repo.iri.value
