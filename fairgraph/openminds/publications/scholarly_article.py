"""
<description not available>
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property

from fairgraph.utility import as_list
from .publication_issue import PublicationIssue
from .periodical import Periodical
from datetime import date
from fairgraph.base import IRI


class ScholarlyArticle(KGObject):
    """
    <description not available>
    """

    default_space = "livepapers"
    type_ = "https://openminds.ebrains.eu/publications/ScholarlyArticle"
    properties = [
        Property("abstract", str, "vocab:abstract", doc="no description available"),
        Property(
            "authors",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:author",
            multiple=True,
            required=True,
            doc="Creator of a literary or creative work, as well as a dataset publication.",
        ),
        Property(
            "cited_publications",
            ["openminds.core.DOI", "openminds.core.ISBN"],
            "vocab:citedPublication",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "copyright",
            "openminds.core.Copyright",
            "vocab:copyright",
            doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
        ),
        Property("creation_date", date, "vocab:creationDate", doc="no description available"),
        Property(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Property(
            "digital_identifier",
            "openminds.core.DOI",
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property("editors", "openminds.core.Person", "vocab:editor", multiple=True, doc="no description available"),
        Property(
            "funding",
            "openminds.core.Funding",
            "vocab:funding",
            multiple=True,
            doc="Money provided by a legal person for a particular purpose.",
        ),
        Property(
            "iri",
            IRI,
            "vocab:IRI",
            doc="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
        ),
        Property(
            "is_part_of",
            ["openminds.publications.PublicationIssue", "openminds.publications.PublicationVolume"],
            "vocab:isPartOf",
            required=True,
            doc="Reference to the ensemble of multiple things or beings.",
        ),
        Property(
            "keywords",
            [
                "openminds.controlled_terms.ActionStatusType",
                "openminds.controlled_terms.AgeCategory",
                "openminds.controlled_terms.AnalysisTechnique",
                "openminds.controlled_terms.AnatomicalAxesOrientation",
                "openminds.controlled_terms.AnatomicalIdentificationType",
                "openminds.controlled_terms.AnatomicalPlane",
                "openminds.controlled_terms.AnnotationCriteriaType",
                "openminds.controlled_terms.AnnotationType",
                "openminds.controlled_terms.AtlasType",
                "openminds.controlled_terms.AuditoryStimulusType",
                "openminds.controlled_terms.BiologicalOrder",
                "openminds.controlled_terms.BiologicalProcess",
                "openminds.controlled_terms.BiologicalSex",
                "openminds.controlled_terms.BreedingType",
                "openminds.controlled_terms.CellCultureType",
                "openminds.controlled_terms.CellType",
                "openminds.controlled_terms.ChemicalMixtureType",
                "openminds.controlled_terms.Colormap",
                "openminds.controlled_terms.ContributionType",
                "openminds.controlled_terms.CranialWindowConstructionType",
                "openminds.controlled_terms.CranialWindowReinforcementType",
                "openminds.controlled_terms.CriteriaQualityType",
                "openminds.controlled_terms.DataType",
                "openminds.controlled_terms.DeviceType",
                "openminds.controlled_terms.DifferenceMeasure",
                "openminds.controlled_terms.Disease",
                "openminds.controlled_terms.DiseaseModel",
                "openminds.controlled_terms.EducationalLevel",
                "openminds.controlled_terms.ElectricalStimulusType",
                "openminds.controlled_terms.EthicsAssessment",
                "openminds.controlled_terms.ExperimentalApproach",
                "openminds.controlled_terms.FileBundleGrouping",
                "openminds.controlled_terms.FileRepositoryType",
                "openminds.controlled_terms.FileUsageRole",
                "openminds.controlled_terms.GeneticStrainType",
                "openminds.controlled_terms.GustatoryStimulusType",
                "openminds.controlled_terms.Handedness",
                "openminds.controlled_terms.Language",
                "openminds.controlled_terms.Laterality",
                "openminds.controlled_terms.LearningResourceType",
                "openminds.controlled_terms.MRAcquisitionType",
                "openminds.controlled_terms.MRIPulseSequence",
                "openminds.controlled_terms.MRIWeighting",
                "openminds.controlled_terms.MeasuredQuantity",
                "openminds.controlled_terms.MeasuredSignalType",
                "openminds.controlled_terms.MetaDataModelType",
                "openminds.controlled_terms.ModelAbstractionLevel",
                "openminds.controlled_terms.ModelScope",
                "openminds.controlled_terms.MolecularEntity",
                "openminds.controlled_terms.OlfactoryStimulusType",
                "openminds.controlled_terms.OperatingDevice",
                "openminds.controlled_terms.OperatingSystem",
                "openminds.controlled_terms.OpticalStimulusType",
                "openminds.controlled_terms.Organ",
                "openminds.controlled_terms.OrganismSubstance",
                "openminds.controlled_terms.OrganismSystem",
                "openminds.controlled_terms.PatchClampVariation",
                "openminds.controlled_terms.PreparationType",
                "openminds.controlled_terms.ProductAccessibility",
                "openminds.controlled_terms.ProgrammingLanguage",
                "openminds.controlled_terms.QualitativeOverlap",
                "openminds.controlled_terms.SemanticDataType",
                "openminds.controlled_terms.Service",
                "openminds.controlled_terms.SetupType",
                "openminds.controlled_terms.SoftwareApplicationCategory",
                "openminds.controlled_terms.SoftwareFeature",
                "openminds.controlled_terms.Species",
                "openminds.controlled_terms.StimulationApproach",
                "openminds.controlled_terms.StimulationTechnique",
                "openminds.controlled_terms.SubcellularEntity",
                "openminds.controlled_terms.SubjectAttribute",
                "openminds.controlled_terms.TactileStimulusType",
                "openminds.controlled_terms.Technique",
                "openminds.controlled_terms.TermSuggestion",
                "openminds.controlled_terms.Terminology",
                "openminds.controlled_terms.TissueSampleAttribute",
                "openminds.controlled_terms.TissueSampleType",
                "openminds.controlled_terms.TypeOfUncertainty",
                "openminds.controlled_terms.UBERONParcellation",
                "openminds.controlled_terms.UnitOfMeasurement",
                "openminds.controlled_terms.VisualStimulusType",
            ],
            "vocab:keyword",
            multiple=True,
            doc="Significant word or concept that are representative of the scholarly article.",
        ),
        Property(
            "license",
            "openminds.core.License",
            "vocab:license",
            doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
        ),
        Property("modification_date", date, "vocab:modificationDate", doc="no description available"),
        Property(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the scholarly article.",
        ),
        Property("pagination", str, "vocab:pagination", doc="no description available"),
        Property("publication_date", date, "vocab:publicationDate", required=True, doc="no description available"),
        Property(
            "publisher",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:publisher",
            doc="no description available",
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            doc="Term or code used to identify the version of something.",
        ),
    ]
    reverse_properties = [
        Property(
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
            doc="reverse of 'related_publications'",
        ),
    ]
    existence_query_properties = ("name",)

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
        related_to=None,
        version_identifier=None,
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
            related_to=related_to,
            version_identifier=version_identifier,
        )

    def get_journal(self, client, with_volume=False, with_issue=False):
        journal = volume = issue = None
        if self.is_part_of:
            issue_or_volume = self.is_part_of.resolve(client, scope=self.scope, follow_links={"is_part_of": {}})
            if isinstance(issue_or_volume, PublicationIssue):
                volume = issue_or_volume.is_part_of
                issue = issue_or_volume
            else:
                volume = issue_or_volume
                issue = None
            journal = volume.is_part_of
            assert isinstance(journal, Periodical)
        retval = [journal]
        if with_volume:
            retval.append(volume)
        if with_issue:
            retval.append(issue)
        if not with_volume and not with_issue:
            return journal
        else:
            return tuple(retval)

    def get_citation_string(self, client):
        # Eyal, G., Verhoog, M. B., Testa-Silva, G., Deitcher, Y., Lodder, '
        #     -              'J. C., Benavides-Piccione, R., ... & Segev, I. (2016). Unique '
        #     -              'membrane properties and enhanced signal processing in human '
        #     -              'neocortical neurons. Elife, 5, e16553.
        self.resolve(client, follow_links={"is_part_of": {}, "authors": {}})
        authors = as_list(self.authors)
        if len(authors) == 1:
            author_str = authors[0].full_name
        elif len(authors) > 1:
            author_str = ", ".join(au.full_name for au in authors[:-1])
            author_str += " & " + self.authors[-1].full_name
        journal, volume, issue = self.get_journal(client, with_volume=True, with_issue=True)
        title = self.name
        if title and title[-1] != ".":
            title += "."
        journal_name = journal.name if journal else ""
        volume_number = f"{volume.volume_number}: " if (volume and volume.volume_number != "placeholder") else ""
        return f"{author_str} ({self.publication_date.year}). {title} {journal_name}, {volume_number}{self.pagination or ''}."
