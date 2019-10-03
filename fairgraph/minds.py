"""

"""
try:
    basestring
except NameError:
    basestring = str

import sys, inspect
from datetime import datetime
from tabulate import tabulate
from fairgraph.base import KGObject, KGProxy, KGQuery, cache, as_list, Field
from fairgraph.data import FileAssociation, CSCSFile

class MINDSObject(KGObject):
    """
    ...

    N.B. all MINDS objects have the same "fg" query ID, because the query url includes the namepsace/version/class path,
    e.g. for the Activity class, the url is : https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg
    """
    namespace = "minds"
    query_id = "fg" # same for all objects
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

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """docstring"""
        D = instance.data
        #assert cls.type[0] in D["@type"]
        data = {}
        for key, value in D.items():
            if key.startswith('http://hbp.eu/minds'):
                name = key.split("#")[1]
            elif key.startswith('https://schema.hbp.eu/minds/'):
                name = key.split('https://schema.hbp.eu/minds/')[1]
            elif key.startswith('https://schema.hbp.eu/uniminds/'):
                name = key.split('https://schema.hbp.eu/uniminds/')[1]
            elif key.startswith('http://schema.org/'):
                name = key.split('http://schema.org/')[1]
            elif key in ("http://www.w3.org/ns/prov#qualifiedAssociation", "prov:qualifiedAssociation"):
                name = "associated_with"
            elif ":" in key:
                name = key.split(":")[1]
            else:
                name = None
            if name in cls.property_names:
                if name in obj_types:
                    if  value is None:
                        data[name] = value
                    elif isinstance(value, list):
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value]
                    elif "@list" in value:
                        assert len(value) == 1
                        data[name] = [KGProxy(obj_types[name], item["@id"])
                                      for item in value['@list']]
                    else:
                        data[name] = KGProxy(obj_types[name], value["@id"])
                else:
                    data[name] = value
        data["id"] = D["@id"]
        data["instance"] = instance
        return cls(**data)

    def _build_data(self, client):
        """docstring"""
        data = {}
        for property_name in self.property_names:
            if hasattr(self, property_name):
                if property_name in ("name", "description", "identifier", "familyName",
                                     "givenName", "email", "version", "license", "url"):
                    property_url = "http://schema.org/" + property_name
                elif property_name == "associated_with":
                    property_url = "http://www.w3.org/ns/prov#qualifiedAssociation"
                else:
                    property_url = "https://schema.hbp.eu/uniminds/" + property_name

                value = getattr(self, property_name)
                if isinstance(value, (str, int, float, dict)):  # todo: extend with other simple types
                    data[property_url] = value
                elif isinstance(value, (KGObject, KGProxy)):
                    data[property_url] = {
                        "@id": value.id,
                        "@type": value.type
                    }
                elif isinstance(value, (list, tuple)):
                    if len(value) > 0:
                        if isinstance(value[0], KGObject):
                            data[property_url] = [{
                                "@id": item.id,
                                "@type": item.type
                            } for item in value]
                        elif "@id" in value[0]:
                            data[property_url] = value
                        else:
                            raise ValueError(str(value))
                elif value is None:
                    pass
                else:
                    raise NotImplementedError("Can't handle {}".format(type(value)))
        return data

    def show(self, max_width=None):
        #max_name_length = max(len(name) for name in self.property_names)
        #fmt =  "{:%d}   {}" % max_name_length
        #for property_name in sorted(self.property_names):
        #    print(fmt.format(property_name, getattr(self, property_name, None)))
        data = [("id", self.id)] + [(property_name, getattr(self, property_name, None))
                                    for property_name in self.property_names]
        if max_width:
            value_column_width = max_width - max(len(item[0]) for item in data)
            def fit_column(value):
                strv = str(value)
                if len(strv) > value_column_width:
                    strv = strv[:value_column_width - 4] + " ..."
                return strv
            data = [(k, fit_column(v)) for k, v in data]
        print(tabulate(data))


#################################################################################################
##### The following code is generated by the script in queries/code_generation_from_KGE_queries
#################################################################################################
class Activity(MINDSObject):
    """
    docstring
    """
    _path = "/core/activity/v1.0.0"
    type = ["minds:Activity"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("activity", KGObject, "https://schema.hbp.eu/minds/activity", required=False),
      Field("ethics_approval", basestring, "https://schema.hbp.eu/minds/ethicsApproval", required=False),
      Field("ethics_authority", basestring, "https://schema.hbp.eu/minds/ethicsAuthority", required=False),
      Field("methods", list, "https://schema.hbp.eu/minds/methods", required=False),
      Field("preparation", KGObject, "https://schema.hbp.eu/minds/preparation", required=False),
      Field("protocols", list, "https://schema.hbp.eu/minds/protocols", required=False))
    


class AgeCategory(MINDSObject):
    """
    docstring
    """
    _path = "/core/agecategory/v1.0.0"
    type = ["minds:AgeCategory"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("age_category", basestring, "https://schema.hbp.eu/minds/age_category", required=False))
    


class Approval(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/approval/v1.0.0"
    type = ["minds:Approval"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("ethics_approval", basestring, "https://schema.hbp.eu/minds/ethicsApproval", required=False),
      Field("generatedby", basestring, "https://schema.hbp.eu/minds/generatedBy", required=False))
    


class Authority(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/authority/v1.0.0"
    type = ["minds:Authority"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("ethics_authority", basestring, "https://schema.hbp.eu/minds/ethicsAuthority", required=False),
      Field("generatedby", basestring, "https://schema.hbp.eu/minds/generatedBy", required=False))
    


class Dataset(MINDSObject):
    """
    docstring
    """
    _path = "/core/dataset/v1.0.0"
    type = ["minds:Dataset"]
    fields = (
      Field("activity", KGObject, "https://schema.hbp.eu/minds/activity", required=False),
      Field("container_url_as_ZIP", basestring, "https://schema.hbp.eu/minds/containerUrlAsZIP", required=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False),
      Field("datalink", basestring, "http://schema.org/datalink", required=False),
      Field("dataset_doi", basestring, "https://schema.hbp.eu/minds/datasetDOI", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("external_datalink", basestring, "https://schema.hbp.eu/minds/external_datalink", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("release_date", datetime, "https://schema.hbp.eu/minds/release_date", required=False),
      Field("activity", KGObject, "https://schema.hbp.eu/minds/activity", required=False),
      Field("component", basestring, "https://schema.hbp.eu/minds/component", required=False),
      Field("contributors", basestring, "https://schema.hbp.eu/minds/contributors", required=False),
      Field("dataset", KGObject, "https://schema.hbp.eu/seeg/dataset", required=False),
      Field("doireference", basestring, "https://schema.hbp.eu/minds/doireference", required=False),
      Field("embargo_status", basestring, "https://schema.hbp.eu/minds/embargo_status", required=False),
      Field("formats", list, "https://schema.hbp.eu/minds/formats", required=False),
      Field("license", basestring, "https://schema.hbp.eu/minds/license", required=False),
      Field("license_info", basestring, "https://schema.hbp.eu/minds/license_info", required=False),
      Field("modality", KGObject, "https://schema.hbp.eu/minds/modality", required=False),
      Field("owners", basestring, "https://schema.hbp.eu/minds/owners", required=False),
      Field("parcellation_atlas", KGObject, "https://schema.hbp.eu/minds/parcellationAtlas", required=False),
      Field("parcellation_region", KGObject, "https://schema.hbp.eu/minds/parcellationRegion", required=False),
      Field("part_of", basestring, "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/partOf", required=False),
      Field("publications", list, "https://schema.hbp.eu/minds/publications", required=False),
      Field("reference_space", basestring, "https://schema.hbp.eu/minds/reference_space", required=False),
      Field("specimen_group", basestring, "https://schema.hbp.eu/minds/specimen_group", required=False))
    


class EmbargoStatus(MINDSObject):
    """
    docstring
    """
    _path = "/core/embargostatus/v1.0.0"
    type = ["minds:EmbargoStatus"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("embargo_status", basestring, "https://schema.hbp.eu/minds/embargo_status", required=False))
    


class File(MINDSObject):
    """
    docstring
    """
    _path = "/core/file/v0.0.4"
    type = ["minds:File"]
    fields = (
      Field("absolute_path", basestring, "http://hbp.eu/minds#absolute_path", required=False),
      Field("byte_size", basestring, "http://hbp.eu/minds#byte_size", required=False),
      Field("content_type", basestring, "http://hbp.eu/minds#content_type", required=False),
      Field("hash", basestring, "http://hbp.eu/minds#hash", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("last_modified", basestring, "http://hbp.eu/minds#last_modified", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relative_path", basestring, "http://hbp.eu/minds#relative_path", required=False),
      Field("file", KGObject, "http://hbp.eu/minds#file", required=False))
    


class FileAssociation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fileassociation/v1.0.0"
    type = ["minds:FileAssociation"]
    fields = (
      Field("from", basestring, "https://schema.hbp.eu/linkinginstance/from", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("to", basestring, "https://schema.hbp.eu/linkinginstance/to", required=False))
    


class Format(MINDSObject):
    """
    docstring
    """
    _path = "/core/format/v1.0.0"
    type = ["minds:Format"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("formats", list, "https://schema.hbp.eu/minds/formats", required=False))
    


class LicenseType(MINDSObject):
    """
    docstring
    """
    _path = "/core/licensetype/v1.0.0"
    type = ["minds:LicenseType"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("license", basestring, "https://schema.hbp.eu/minds/license", required=False))
    


class Method(MINDSObject):
    """
    docstring
    """
    _path = "/core/method/v1.0.0"
    type = ["minds:Method"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False))
    


class Modality(MINDSObject):
    """
    docstring
    """
    _path = "/core/modality/v1.0.0"
    type = ["minds:Modality"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("modality", KGObject, "https://schema.hbp.eu/minds/modality", required=False))
    


class Parcellationatlas(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationatlas/v1.0.0"
    type = ["minds:Parcellationatlas"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("parcellation_atlas", KGObject, "https://schema.hbp.eu/minds/parcellationAtlas", required=False))
    


class ParcellationRegion(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationregion/v1.0.0"
    type = ["minds:ParcellationRegion"]
    fields = (
      Field("alias", basestring, "https://schema.hbp.eu/minds/alias", required=False),
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("url", basestring, "https://schema.hbp.eu/viewer/url", required=False),
      Field("parcellation_region", KGObject, "https://schema.hbp.eu/minds/parcellationRegion", required=False),
      Field("species", KGObject, "https://schema.hbp.eu/minds/species", required=False))
    


class Person(MINDSObject):
    """
    docstring
    """
    _path = "/core/person/v1.0.0"
    type = ["minds:Person"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("shortname", basestring, "https://schema.hbp.eu/minds/shortName", required=False),
      Field("authors", basestring, "https://schema.hbp.eu/minds/authors", required=False),
      Field("contributors", basestring, "https://schema.hbp.eu/minds/contributors", required=False),
      Field("owners", basestring, "https://schema.hbp.eu/minds/owners", required=False))
    


class PLAComponent(MINDSObject):
    """
    docstring
    """
    _path = "/core/placomponent/v1.0.0"
    type = ["minds:PLAComponent"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("component", basestring, "https://schema.hbp.eu/minds/component", required=False))
    


class Preparation(MINDSObject):
    """
    docstring
    """
    _path = "/core/preparation/v1.0.0"
    type = ["minds:Preparation"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("preparation", KGObject, "https://schema.hbp.eu/minds/preparation", required=False))
    


class Protocol(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/protocol/v1.0.0"
    type = ["minds:Protocol"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("protocols", list, "https://schema.hbp.eu/minds/protocols", required=False))
    


class Publication(MINDSObject):
    """
    docstring
    """
    _path = "/core/publication/v1.0.0"
    type = ["minds:Publication"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("cite", basestring, "https://schema.hbp.eu/minds/cite", required=False),
      Field("doi", basestring, "https://schema.hbp.eu/minds/doi", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("authors", basestring, "https://schema.hbp.eu/minds/authors", required=False),
      Field("publications", list, "https://schema.hbp.eu/minds/publications", required=False))
    


class ReferenceSpace(MINDSObject):
    """
    docstring
    """
    _path = "/core/referencespace/v1.0.0"
    type = ["minds:ReferenceSpace"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("reference_space", basestring, "https://schema.hbp.eu/minds/reference_space", required=False))
    


class Role(MINDSObject):
    """
    docstring
    """
    _path = "/prov/role/v1.0.0"
    type = ["minds:Role"]
    fields = (
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("had_role", basestring, "http://www.w3.org/ns/prov#hadRole", required=False))
    


class Sample(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/sample/v1.0.0"
    type = ["minds:Sample"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("weight_post_fixation", basestring, "https://schema.hbp.eu/minds/weightPostFixation", required=False),
      Field("weight_pre_fixation", basestring, "https://schema.hbp.eu/minds/weightPreFixation", required=False),
      Field("methods", list, "https://schema.hbp.eu/minds/methods", required=False),
      Field("parcellation_atlas", KGObject, "https://schema.hbp.eu/minds/parcellationAtlas", required=False),
      Field("parcellation_region", KGObject, "https://schema.hbp.eu/minds/parcellationRegion", required=False),
      Field("reference", basestring, "https://schema.hbp.eu/brainviewer/reference", required=False),
      Field("samples", list, "https://schema.hbp.eu/minds/samples", required=False))
    


class Sex(MINDSObject):
    """
    docstring
    """
    _path = "/core/sex/v1.0.0"
    type = ["minds:Sex"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("sex", KGObject, "https://schema.hbp.eu/minds/sex", required=False))
    


class SoftwareAgent(MINDSObject):
    """
    docstring
    """
    _path = "/core/softwareagent/v1.0.0"
    type = ["minds:SoftwareAgent"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("agent", basestring, "http://www.w3.org/ns/prov#agent", required=False))
    


class Species(MINDSObject):
    """
    docstring
    """
    _path = "/core/species/v1.0.0"
    type = ["minds:Species"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("alternate_of", basestring, "http://www.w3.org/ns/prov#alternateOf", required=False),
      Field("species", KGObject, "https://schema.hbp.eu/minds/species", required=False))
    


class SpecimenGroup(MINDSObject):
    """
    docstring
    """
    _path = "/core/specimengroup/v1.0.0"
    type = ["minds:SpecimenGroup"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("specimen_group", basestring, "https://schema.hbp.eu/minds/specimen_group", required=False),
      Field("subjects", list, "https://schema.hbp.eu/minds/subjects", required=False))
    


class Subject(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/subject/v1.0.0"
    type = ["minds:Subject"]
    fields = (
      Field("alternatives", list, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("cause_of_death", basestring, "https://schema.hbp.eu/minds/causeOfDeath", required=False),
      Field("genotype", basestring, "https://schema.hbp.eu/minds/genotype", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("associated_with", KGObject, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("strain", basestring, "https://schema.hbp.eu/minds/strain", required=False),
      Field("strains", basestring, "https://schema.hbp.eu/minds/strains", required=False),
      Field("weight", basestring, "https://schema.hbp.eu/minds/weight", required=False),
      Field("age", basestring, "https://schema.hbp.eu/minds/age", required=False),
      Field("age_category", basestring, "https://schema.hbp.eu/minds/age_category", required=False),
      Field("samples", list, "https://schema.hbp.eu/minds/samples", required=False),
      Field("sex", KGObject, "https://schema.hbp.eu/minds/sex", required=False),
      Field("species", KGObject, "https://schema.hbp.eu/minds/species", required=False),
      Field("subjects", list, "https://schema.hbp.eu/minds/subjects", required=False))
################################################################    
### end of script-generated code
################################################################    

def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


# Alias some classes to reflect names used in KG Search
Project = PLAComponent

if __name__=='__main__':

    import os
    from fairgraph import minds, KGClient
    token = os.environ['HBP_token']
    client = KGClient(token)
    for cls in minds.list_kg_classes():
        print(cls.__name__)
