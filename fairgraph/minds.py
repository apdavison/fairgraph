import sys, inspect, os
from datetime import datetime
try:
    basestring
except NameError:
    basestring = str
    raw_input = input

import requests
from tqdm import tqdm

from fairgraph.base import KGObject, KGProxy, KGQuery, cache, as_list, Field
from fairgraph.data import FileAssociation, CSCSFile
from fairgraph.commons import QuantitativeValue
from fairgraph.utility import in_notebook


class MINDSObject(KGObject):
    """
    ...

    N.B. all MINDS objects have the same "fg" query ID, because the query url includes the namepsace/version/class path,
    e.g. for the Activity class, the url is : https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg
    """
    namespace = "minds"
    context = [
        "{{base}}/contexts/nexus/core/resource/v0.3.0",
        {
            "schema": "http://schema.org/",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "prov": "http://www.w3.org/ns/prov#",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "minds": 'https://schema.hbp.eu/',
            "uniminds": 'https://schema.hbp.eu/uniminds/',
        }
    ]


class Person(MINDSObject):
    """
    docstring
    """
    _path = "/core/person/v1.0.0"
    type = ["minds:Person"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      Field("shortname", basestring, "https://schema.hbp.eu/minds/shortName", required=False, multiple=False))


class Activity(MINDSObject):
    """
    docstring
    """
    _path = "/core/activity/v1.0.0"
    type = ["minds:Activity"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("ethics_approval", "minds.EthicsApproval", "https://schema.hbp.eu/minds/ethicsApproval", required=False, multiple=False),
      Field("ethics_authority", "minds.EthicsAuthority", "https://schema.hbp.eu/minds/ethicsAuthority", required=False, multiple=True),
      Field("methods", "minds.Method", "https://schema.hbp.eu/minds/methods", required=False, multiple=True),
      Field("preparation", "minds.Preparation", "https://schema.hbp.eu/minds/preparation", required=False, multiple=False),
      Field("protocols", "minds.Protocol", "https://schema.hbp.eu/minds/protocols", required=False, multiple=True))



class AgeCategory(MINDSObject):
    """
    docstring
    """
    _path = "/core/agecategory/v1.0.0"
    type = ["minds:Agecategory"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class EthicsApproval(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/approval/v1.0.0"
    type = ["minds:Approval"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("generated_by", "minds.EthicsAuthority", "https://schema.hbp.eu/minds/generatedBy", required=False, multiple=True))


class EthicsAuthority(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/authority/v1.0.0"
    type = ["minds:Authority"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      #Field("generated_by", KGObject, "https://schema.hbp.eu/minds/generatedBy", required=False, multiple=False))
    )

terms_of_use = """
# EBRAINS Knowledge Graph Data Platform Citation Requirements

This text is provided to describe the requirements for citing data found via
EBRAINS Knowledge Graph Data Platform (KG): https://kg.ebrains.eu/search.
It is meant to provide a more human-readable form of key parts of the KG Terms
of Service, but in the event of disagreement between the KG Terms of Service
and these Citation Requirements, the former is to be taken as authoritative.

## Dataset licensing

All datasets in the KG have explicit licensing conditions attached. The
license is typically one of the Creative Commons licenses. You must follow the
licensing conditions attached to the dataset, including all restrictions on
commercial use, requirements for attribution or requirements to share-alike.

## EBRAINS Knowledge Graph citation policy

If you use of the software and datasets found via the KG, the KG Pyxus API, KG
REST API or fairgraph library in your scientific publication you must follow
the following citation policy:

1. Cite "EBRAINS Knowledge Graph Data Platform: https://www.ebrains.eu/search"

2. For a dataset is released under a Creative Commons license which includes
   "Attribution", please cite:

    1. The primary publication listed under the dataset.

    2. The dataset DOI, if using a collection of single datasets.

    3. The parent project DOI, if using multiple dataset from the same project

    4. In cases where a primary publication is not provided, and only in such
       cases, the names of the Data Contributors should be cited (Data
       provided by Contributor 1, Contributor 2, ..., and Contributor N) in
       addition to the citation of the Site and the DOI for the data.

3. For software, you must cite software as defined in the software's
   respective citation policy. If you can not find a citation or
   acknowledgement policy for the software, please use the open source
   repository link as the citation link.

Failure to cite data or software used in a publication or presentation
constitutes scientific misconduct. Failure to cite data or software used in a
scientific publication must be corrected by issuing an official Erratum and
correction of the given article if it is discovered post-publication.
"""


class Dataset(MINDSObject):
    """
    docstring
    """
    _path = "/core/dataset/v1.0.0"
    type = ["minds:Dataset"]
    query_id = "fgDataset"
    query_id_resolved = "fgResolvedModified"
    accepted_terms_of_use = False
    fields = (
      Field("activity", Activity, "https://schema.hbp.eu/minds/activity", required=False, multiple=True),
      # to be merged in a method:
      Field("container_url_as_ZIP", bool, "https://schema.hbp.eu/minds/containerUrlAsZIP", required=False, multiple=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False, multiple=False),
      Field("datalink", basestring, "http://schema.org/datalink", required=False, multiple=False),

      Field("dataset_doi", basestring, "https://schema.hbp.eu/minds/datasetDOI", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("external_datalink", basestring, "https://schema.hbp.eu/minds/external_datalink", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("release_date", datetime, "https://schema.hbp.eu/minds/release_date", required=False, multiple=False, strict=False),
      Field("component", "minds.PLAComponent", "https://schema.hbp.eu/minds/component", required=False, multiple=True),
      Field("contributors", Person, "https://schema.hbp.eu/minds/contributors", required=False, multiple=True),
      Field("doireference", basestring, "https://schema.hbp.eu/minds/doireference", required=False, multiple=False),
      Field("embargo_status", "minds.EmbargoStatus", "https://schema.hbp.eu/minds/embargo_status", required=False, multiple=False),
      Field("formats", "minds.Format", "https://schema.hbp.eu/minds/formats", required=False, multiple=True),
      Field("license", "minds.License", "https://schema.hbp.eu/minds/license", required=False, multiple=False),
      #Field("license_info", basestring, "https://schema.hbp.eu/minds/license_info", required=False, multiple=False),
      Field("modality", "minds.Modality", "https://schema.hbp.eu/minds/modality", required=False, multiple=True),
      Field("owners", Person, "https://schema.hbp.eu/minds/owners", required=False, multiple=True),
      Field("parcellation_atlas", "minds.ParcellationAtlas", "https://schema.hbp.eu/minds/parcellationAtlas", required=False, multiple=True),
      Field("parcellation_region", "minds.ParcellationRegion", "https://schema.hbp.eu/minds/parcellationRegion", required=False, multiple=True),
      Field("part_of", basestring, "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/partOf", required=False, multiple=False),
      Field("publications", "minds.Publication", "https://schema.hbp.eu/minds/publications", required=False, multiple=True),
      Field("reference_space", "minds.ReferenceSpace", "https://schema.hbp.eu/minds/reference_space", required=False, multiple=True),
      Field("specimen_group", "minds.SpecimenGroup", "https://schema.hbp.eu/minds/specimen_group", required=False, multiple=True))

    def download(self, local_directory, accept_terms_of_use=False):
        # todo: add support for download as zip
        # todo: check hashes
        if not (accept_terms_of_use or self.accepted_terms_of_use):
            if in_notebook():
                from IPython.display import display, Markdown
                display(Markdown(terms_of_use))
            else:
                print(terms_of_use)
            user_response = raw_input("Do you accept the EBRAINS KG Terms of Service? ")
            if user_response in ('y', 'Y', 'yes', 'YES'):
                self.__class__.accepted_terms_of_use = True
            else:
                raise Exception("Please accept the terms of use before downloading the dataset")
        response = requests.get(self.container_url + "?format=json")
        if response.status_code != 200:
            raise IOError(
                "Unable to download dataset. Response code {}".format(response.status_code))
        contents = response.json()
        total_data_size = sum(item["bytes"] for item in contents) // 1024
        progress_bar = tqdm(total=total_data_size)
        for entry in contents:
            local_path = os.path.join(local_directory, entry["name"])
            print(local_path)
            if entry["name"].endswith("/"):
                os.makedirs(local_path, exist_ok=True)
            else:
                response2 = requests.get(self.container_url + "/" + entry["name"])
                if response2.status_code == 200:
                    with open(local_path, "wb") as fp:
                        fp.write(response2.content)
                    progress_bar.update(entry["bytes"] // 1024)
                else:
                    raise IOError(
                        "Unable to download file '{}'. Response code {}".format(
                            local_path, response2.status_code))
        progress_bar.close()


class EmbargoStatus(MINDSObject):
    """
    docstring
    """
    _path = "/core/embargostatus/v1.0.0"
    type = ["minds:Embargostatus"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )

class File(MINDSObject):
    """
    docstring
    """
    _path = "/core/file/v0.0.4"
    type = ["minds:File"]
    fields = (
      Field("absolute_path", basestring, "http://hbp.eu/minds#absolute_path", required=False, multiple=False),
      Field("byte_size", int, "http://hbp.eu/minds#byte_size", required=False, multiple=False),
      Field("content_type", basestring, "http://hbp.eu/minds#content_type", required=False, multiple=False),
      Field("hash", basestring, "http://hbp.eu/minds#hash", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("last_modified", datetime, "http://hbp.eu/minds#last_modified", required=False, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      Field("relative_path", basestring, "http://hbp.eu/minds#relative_path", required=False, multiple=False))


class FileAssociation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fileassociation/v1.0.0"
    type = ["minds:Fileassociation"]
    fields = (
      Field("from", File, "https://schema.hbp.eu/linkinginstance/from", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      Field("to", Dataset, "https://schema.hbp.eu/linkinginstance/to", required=False, multiple=False))


class Format(MINDSObject):
    """
    docstring
    """
    _path = "/core/format/v1.0.0"
    type = ["minds:Format"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class License(MINDSObject):
    """
    docstring
    """
    _path = "/core/licensetype/v1.0.0"
    type = ["minds:Licensetype"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #ield("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class Method(MINDSObject):
    """
    docstring
    """
    #_path = "/core/method/v1.0.0"
    _path = "/experiment/method/v1.0.0"
    type = ["minds:Method"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class Modality(MINDSObject):
    """
    docstring
    """
    _path = "/core/modality/v1.0.0"
    type = ["minds:Modality"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False))


class ParcellationAtlas(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationatlas/v1.0.0"
    type = ["minds:Parcellationatlas"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class ParcellationRegion(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationregion/v1.0.0"
    type = ["minds:Parcellationregion"]
    fields = (
      Field("alias", basestring, "https://schema.hbp.eu/minds/alias", required=False, multiple=False),
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("url", basestring, "https://schema.hbp.eu/viewer/url", required=False, multiple=False),
      Field("species", "minds.Species", "https://schema.hbp.eu/minds/species", required=False, multiple=False))


class PLAComponent(MINDSObject):
    """
    docstring
    """
    _path = "/core/placomponent/v1.0.0"
    type = ["minds:Placomponent"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("component", basestring, "https://schema.hbp.eu/minds/component", required=False, multiple=False))


class Preparation(MINDSObject):
    """
    docstring
    """
    _path = "/core/preparation/v1.0.0"
    type = ["minds:Preparation"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class Protocol(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/protocol/v1.0.0"
    type = ["minds:Protocol"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class Publication(MINDSObject):
    """
    docstring
    """
    _path = "/core/publication/v1.0.0"
    type = ["minds:Publication"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("cite", basestring, "https://schema.hbp.eu/minds/cite", required=False, multiple=False),
      Field("doi", basestring, "https://schema.hbp.eu/minds/doi", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("authors", Person, "https://schema.hbp.eu/minds/authors", required=False, multiple=True))


class ReferenceSpace(MINDSObject):
    """
    docstring
    """
    _path = "/core/referencespace/v1.0.0"
    type = ["minds:Referencespace"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    )


class Role(MINDSObject):
    """
    docstring
    """
    _path = "/prov/role/v1.0.0"
    type = ["minds:Role"]
    fields = (
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False))

class Sample(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/sample/v1.0.0"
    type = ["minds:Sample"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      #Field("weight_post_fixation", QuantitativeValue, "https://schema.hbp.eu/minds/weightPostFixation", required=False, multiple=False),
      Field("weight_post_fixation", basestring, "https://schema.hbp.eu/minds/weightPostFixation", required=False, multiple=False),
      #Field("weight_pre_fixation", QuantitativeValue, "https://schema.hbp.eu/minds/weightPreFixation", required=False, multiple=False),
      Field("weight_pre_fixation", basestring, "https://schema.hbp.eu/minds/weightPreFixation", required=False, multiple=False),
      Field("methods", Method, "https://schema.hbp.eu/minds/methods", required=False, multiple=True),
      Field("parcellation_atlas", ParcellationAtlas, "https://schema.hbp.eu/minds/parcellationAtlas", required=False, multiple=False),
      Field("parcellation_region", ParcellationRegion, "https://schema.hbp.eu/minds/parcellationRegion", required=False, multiple=True),
      Field("reference", basestring, "https://schema.hbp.eu/brainviewer/reference", required=False, multiple=False))


class Sex(MINDSObject):
    """
    docstring
    """
    _path = "/core/sex/v1.0.0"
    type = ["minds:Sex"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False))


class SoftwareAgent(MINDSObject):
    """
    docstring
    """
    _path = "/core/softwareagent/v1.0.0"
    type = ["minds:Softwareagent"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False))


class Species(MINDSObject):
    """
    docstring
    """
    _path = "/core/species/v1.0.0"
    type = ["minds:Species"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      #Field("alternate_of", KGObject, "http://www.w3.org/ns/prov#alternateOf", required=False, multiple=False))
    )


class SpecimenGroup(MINDSObject):
    """
    docstring
    """
    _path = "/core/specimengroup/v1.0.0"
    type = ["minds:Specimengroup"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("subjects", "minds.Subject", "https://schema.hbp.eu/minds/subjects", required=False, multiple=True))


class Subject(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/subject/v1.0.0"
    type = ["minds:Subject"]
    fields = (
      # Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("cause_of_death", basestring, "https://schema.hbp.eu/minds/causeOfDeath", required=False, multiple=False),
      Field("genotype", basestring, "https://schema.hbp.eu/minds/genotype", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=False, multiple=True),
      Field("name", basestring, "http://schema.org/name", required=False, multiple=False),
      #Field("associated_with", Person, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("strain", basestring, "https://schema.hbp.eu/minds/strain", required=False, multiple=False),
      Field("strains", basestring, "https://schema.hbp.eu/minds/strains", required=False, multiple=True),
      #Field("weight", QuantitativeValue, "https://schema.hbp.eu/minds/weight", required=False, multiple=False),
      Field("weight", basestring, "https://schema.hbp.eu/minds/weight", required=False, multiple=False),
      #Field("age", QuantitativeValue, "https://schema.hbp.eu/minds/age", required=False, multiple=False),
      Field("age", basestring, "https://schema.hbp.eu/minds/age", required=False, multiple=False),
      Field("age_category", AgeCategory, "https://schema.hbp.eu/minds/age_category", required=False, multiple=False),
      Field("samples", Sample, "https://schema.hbp.eu/minds/samples", required=False, multiple=True),
      Field("sex", Sex, "https://schema.hbp.eu/minds/sex", required=False, multiple=True),  # should be multiple=False, but some nodes have both
      Field("species", Species, "https://schema.hbp.eu/minds/species", required=False, multiple=False))


def list_kg_classes():
    """List all KG classes defined in this module"""
    classes = [obj for name, obj in inspect.getmembers(sys.modules[__name__])
               if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]
    classes.remove(MINDSObject)
    return classes


# Alias some classes to reflect names used in KG Search
Project = PLAComponent


if __name__=='__main__':

    import os
    from fairgraph import minds, KGClient
    token = os.environ['HBP_token']
    client = KGClient(token)
    for cls in minds.list_kg_classes():
        print(cls.__name__)
