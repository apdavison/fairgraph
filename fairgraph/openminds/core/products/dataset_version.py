"""
Structured information on data originating from human/animal studies or simulations (version level).
"""

# this file was auto-generated

import os
from datetime import date, datetime
from urllib.parse import urlparse, quote_plus, parse_qs, urlencode
import requests
from tqdm import tqdm

from fairgraph.base_v3 import KGObjectV3, IRI
from fairgraph.fields import Field
from fairgraph.utility import in_notebook, TERMS_OF_USE



class DatasetVersion(KGObjectV3):
    """
    Structured information on data originating from human/animal studies or simulations (version level).
    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/DatasetVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=False,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("behavioral_protocols", "openminds.core.BehavioralProtocol", "vocab:behavioralProtocol", multiple=True, required=False,
              doc="no description available"),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=True,
              doc="Digital handle to identify objects or legal persons."),
        Field("ethics_assessment", "openminds.controlledterms.EthicsAssessment", "vocab:ethicsAssessment", multiple=False, required=True,
              doc="Judgment about the applied principles of conduct governing an individual or a group."),
        Field("experimental_approachs", "openminds.controlledterms.ExperimentalApproach", "vocab:experimentalApproach", multiple=True, required=True,
              doc="no description available"),
        Field("input_data", ["openminds.core.DOI", "openminds.core.File", "openminds.core.FileBundle"], "vocab:inputData", multiple=True, required=False,
              doc="Data that is put into a process or machine."),
        Field("is_alternative_version_of", "openminds.core.DatasetVersion", "vocab:isAlternativeVersionOf", multiple=True, required=False,
              doc="Reference to an original form where the essence was preserved, but presented in an alternative form."),
        Field("is_new_version_of", "openminds.core.DatasetVersion", "vocab:isNewVersionOf", multiple=False, required=False,
              doc="Reference to a previous (potentially outdated) particular form of something."),
        Field("license", "openminds.core.License", "vocab:license", multiple=False, required=True,
              doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something."),
        Field("preparation_designs", "openminds.controlledterms.PreparationType", "vocab:preparationDesign", multiple=True, required=False,
              doc="no description available"),
        Field("studied_specimens", ["openminds.core.Subject", "openminds.core.SubjectGroup", "openminds.core.TissueSample", "openminds.core.TissueSampleCollection"], "vocab:studiedSpecimen", multiple=True, required=False,
              doc="no description available"),
        Field("techniques", "openminds.controlledterms.Technique", "vocab:technique", multiple=True, required=True,
              doc="Method of accomplishing a desired aim."),
        Field("data_types", "openminds.controlledterms.SemanticDataType", "vocab:dataType", multiple=True, required=True,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.Handedness", "openminds.controlledterms.Organ", "openminds.controlledterms.Phenotype", "openminds.controlledterms.Species", "openminds.controlledterms.Strain", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),
        Field("accessibility", "openminds.controlledterms.ProductAccessibility", "vocab:accessibility", multiple=False, required=True,
              doc="Level to which something is accessible to the dataset version."),
        Field("copyright", "openminds.core.Copyright", "vocab:copyright", multiple=False, required=False,
              doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period."),
        Field("custodians", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="Legal person entrusted with guarding and maintaining property or records."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the dataset version."),
        Field("full_documentation", ["openminds.core.DOI", "openminds.core.File", "openminds.core.URL"], "vocab:fullDocumentation", multiple=False, required=True,
              doc="Non-abridged instructions, comments, and information for using a particular product."),
        Field("name", str, "vocab:fullName", multiple=False, required=False,
              doc="Whole, non-abbreviated name of the dataset version."),
        Field("funding", "openminds.core.Funding", "vocab:funding", multiple=True, required=False,
              doc="Money provided by a legal person for a particular purpose."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the dataset version."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("keywords", ["openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.Handedness", "openminds.controlledterms.Organ", "openminds.controlledterms.Phenotype", "openminds.controlledterms.Species", "openminds.controlledterms.Strain", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:keyword", multiple=True, required=False,
              doc="Significant word or concept that are representative of the dataset version."),
        Field("other_contributions", "openminds.core.Contribution", "vocab:otherContribution", multiple=True, required=False,
              doc="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere."),
        Field("related_publications", ["openminds.core.DOI", "openminds.core.ISBN"], "vocab:relatedPublication", multiple=True, required=False,
              doc="Reference to something that was made available for the general public to see or buy."),
        Field("release_date", date, "vocab:releaseDate", multiple=False, required=True,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("repository", "openminds.core.FileRepository", "vocab:repository", multiple=False, required=False,
              doc="Place, room, or container where something is deposited or stored."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the dataset version."),
        Field("support_channels", str, "vocab:supportChannel", multiple=True, required=False,
              doc="Way of communication used to interact with users or customers."),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),
        Field("version_innovation", str, "vocab:versionInnovation", multiple=False, required=True,
              doc="Documentation on what changed in comparison to a previously published form of something."),

    ]
    existence_query_fields = ('alias', 'version_identifier')

    def __init__(self, id=None, data=None, space=None, **properties):
        super().__init__(id=id, data=data, space=space, **properties)
        self.accepted_terms_of_use = False

    def download(self, client, local_directory, accept_terms_of_use=False):
        # todo: add support for download as zip
        # todo: check hashes
        if not (accept_terms_of_use or self.accepted_terms_of_use):
            if in_notebook():
                from IPython.display import display, Markdown
                display(Markdown(TERMS_OF_USE))
            else:
                print(TERMS_OF_USE)
            user_response = input("Do you accept the EBRAINS KG Terms of Service? ")
            if user_response in ('y', 'Y', 'yes', 'YES'):
                self.__class__.accepted_terms_of_use = True
            else:
                raise Exception("Please accept the terms of use before downloading the dataset")

        repository_url = self.repository.resolve(client, scope="in progress").iri.value
        parts = urlparse(repository_url)
        query_dict = parse_qs(parts.query)
        query_dict['format'] = "json"
        url = parts._replace(query=urlencode(query_dict, True)).geturl()
        response = requests.get(url)
        if response.status_code not in (200, 204):
            raise IOError(
                f"Unable to download dataset. Response code {response.status_code}")
        contents = response.json()
        total_data_size = sum(item["bytes"] for item in contents) // 1024
        progress_bar = tqdm(total=total_data_size)
        for entry in sorted(contents,
                            key=lambda entry: entry["content_type"] != "application/directory"):
            # take directories first
            local_path = os.path.join(local_directory, entry["name"])
            if entry["content_type"] == "application/directory":
                os.makedirs(local_path, exist_ok=True)
            else:
                response2 = requests.get(repository_url + "/" + entry["name"])
                if response2.status_code in (200, 204):
                    with open(local_path, "wb") as fp:
                        fp.write(response2.content)
                    progress_bar.update(entry["bytes"] // 1024)
                else:
                    raise IOError(
                        f"Unable to download file '{local_path}'. Response code {response2.status_code}")
        progress_bar.close()
