"""
Structured information on data originating from human/animal studies or simulations (version level).
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import DatasetVersion as OMDatasetVersion
from fairgraph import KGObject

from urllib.request import urlretrieve
from pathlib import Path
from ....utility import accepted_terms_of_use
from datetime import date
from openminds import IRI


class DatasetVersion(KGObject, OMDatasetVersion):
    """
    Structured information on data originating from human/animal studies or simulations (version level).
    """

    type_ = "https://openminds.om-i.org/types/DatasetVersion"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "comments",
            "openminds.latest.core.Comment",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
        Property(
            "has_parts",
            [
                "openminds.latest.core.ProtocolExecution",
                "openminds.latest.ephys.CellPatching",
                "openminds.latest.ephys.ElectrodePlacement",
                "openminds.latest.ephys.RecordingActivity",
                "openminds.latest.specimen_prep.CranialWindowPreparation",
                "openminds.latest.specimen_prep.TissueCulturePreparation",
                "openminds.latest.specimen_prep.TissueSampleSlicing",
                "openminds.latest.stimulation.StimulationActivity",
            ],
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
        Property(
            "is_input_to",
            "openminds.latest.computation.DataCopy",
            "input",
            reverse="inputs",
            multiple=True,
            description="reverse of 'inputs'",
        ),
        Property(
            "is_old_version_of",
            "openminds.latest.core.DatasetVersion",
            "isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            description="reverse of 'is_new_version_of'",
        ),
        Property(
            "is_part_of",
            ["openminds.latest.core.Project", "openminds.latest.core.ResearchProductGroup"],
            "hasPart",
            reverse="has_parts",
            multiple=True,
            description="reverse of 'has_parts'",
        ),
        Property(
            "is_version_of",
            "openminds.latest.core.Dataset",
            "hasVersion",
            reverse="has_versions",
            multiple=True,
            description="reverse of 'has_versions'",
        ),
        Property(
            "learning_resources",
            "openminds.latest.publications.LearningResource",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
        Property(
            "publication",
            "openminds.latest.publications.LivePaperVersion",
            "about",
            reverse="about",
            multiple=True,
            description="reverse of 'about'",
        ),
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("short_name", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        accessibility=None,
        authors=None,
        behavioral_protocols=None,
        comments=None,
        copyright=None,
        custodians=None,
        data_types=None,
        description=None,
        digital_identifier=None,
        ethics_assessment=None,
        experimental_approaches=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_parts=None,
        homepage=None,
        how_to_cite=None,
        input_data=None,
        is_alternative_version_of=None,
        is_input_to=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        license=None,
        other_contributions=None,
        preparation_designs=None,
        protocols=None,
        publication=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        studied_specimens=None,
        study_targets=None,
        support_channels=None,
        techniques=None,
        version_identifier=None,
        version_innovation=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            alias=alias,
            accessibility=accessibility,
            authors=authors,
            behavioral_protocols=behavioral_protocols,
            comments=comments,
            copyright=copyright,
            custodians=custodians,
            data_types=data_types,
            description=description,
            digital_identifier=digital_identifier,
            ethics_assessment=ethics_assessment,
            experimental_approaches=experimental_approaches,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_parts=has_parts,
            homepage=homepage,
            how_to_cite=how_to_cite,
            input_data=input_data,
            is_alternative_version_of=is_alternative_version_of,
            is_input_to=is_input_to,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            license=license,
            other_contributions=other_contributions,
            preparation_designs=preparation_designs,
            protocols=protocols,
            publication=publication,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            studied_specimens=studied_specimens,
            study_targets=study_targets,
            support_channels=support_channels,
            techniques=techniques,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )

    def download(self, local_path, client, accept_terms_of_use=False):
        if accepted_terms_of_use(client, accept_terms_of_use=accept_terms_of_use):
            repo = self.repository.resolve(client, scope=self.scope or None)
            if repo.iri.value.startswith("https://object.cscs.ch/v1/AUTH") or repo.iri.value.startswith(
                "https://data-proxy.ebrains.eu/api/v1/public"
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
