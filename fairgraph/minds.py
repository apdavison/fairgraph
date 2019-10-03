import sys, inspect
from datetime import datetime
from tabulate import tabulate

from fairgraph.base import KGObject, KGProxy, KGQuery, cache, as_list, Field
from fairgraph.data import FileAssociation, CSCSFile
from fairgraph.commons import QuantitativeValue

try:
    basestring
except NameError:
    basestring = str


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


class Activity(MINDSObject):
    """
    docstring
    """
    _path = "/core/activity/v1.0.0"
    type = ["minds:Activity"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("activity", "Activity", "https://schema.hbp.eu/minds/activity", required=False, multiple=False),
      Field("ethics_approval", basestring, "https://schema.hbp.eu/minds/ethicsApproval", required=False, multiple=False),
      Field("ethics_authority", basestring, "https://schema.hbp.eu/minds/ethicsAuthority", required=False, multiple=False),
      Field("methods", "Method", "https://schema.hbp.eu/minds/methods", required=False, multiple=True),
      Field("preparation", "Preparation", "https://schema.hbp.eu/minds/preparation", required=False, multiple=False),
      Field("protocols", "Protocol", "https://schema.hbp.eu/minds/protocols", required=False, multiple=True))
    


class AgeCategory(MINDSObject):
    """
    docstring
    """
    _path = "/core/agecategory/v1.0.0"
    type = ["minds:AgeCategory"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("age_category", "AgeCategory", "https://schema.hbp.eu/minds/age_category", required=False, multiple=False))
    


class EthicsApproval(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/approval/v1.0.0"
    type = ["minds:EthicsApproval"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("ethics_approval", "EthicsApproval", "https://schema.hbp.eu/minds/ethicsApproval", required=False, multiple=False),
      Field("generated_by", KGObject, "https://schema.hbp.eu/minds/generatedBy", required=False, multiple=False))
    


class EthicsAuthority(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/authority/v1.0.0"
    type = ["minds:EthicsAuthority"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("ethics_authority", "EthicsAuthority", "https://schema.hbp.eu/minds/ethicsAuthority", required=False, multiple=False),
      Field("generated_by", KGObject, "https://schema.hbp.eu/minds/generatedBy", required=False, multiple=False))
    


class Dataset(MINDSObject):
    """
    docstring
    """
    _path = "/core/dataset/v1.0.0"
    type = ["minds:Dataset"]
    fields = (
      Field("activity", "Activity", "https://schema.hbp.eu/minds/activity", required=False, multiple=False),
      # to be merged in a method:
      Field("container_url_as_ZIP", basestring, "https://schema.hbp.eu/minds/containerUrlAsZIP", required=False, multiple=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False, multiple=False),
      Field("datalink", basestring, "http://schema.org/datalink", required=False, multiple=False),
        
      Field("dataset_doi", basestring, "https://schema.hbp.eu/minds/datasetDOI", required=False, multiple=False),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("external_datalink", basestring, "https://schema.hbp.eu/minds/external_datalink", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("release_date", datetime, "https://schema.hbp.eu/minds/release_date", required=False, multiple=False),
      Field("component", basestring, "https://schema.hbp.eu/minds/component", required=False, multiple=False),
      Field("contributors", "Person", "https://schema.hbp.eu/minds/contributors", required=False, multiple=True),
      Field("dataset", "Dataset", "https://schema.hbp.eu/seeg/dataset", required=False, multiple=False),
      Field("doireference", basestring, "https://schema.hbp.eu/minds/doireference", required=False, multiple=False),
      Field("embargo_status", "EmbargoStatus", "https://schema.hbp.eu/minds/embargo_status", required=False, multiple=False),
      Field("formats", "Format", "https://schema.hbp.eu/minds/formats", required=False, multiple=True),
      Field("license", basestring, "https://schema.hbp.eu/minds/license", required=False, multiple=False),
      Field("license_info", basestring, "https://schema.hbp.eu/minds/license_info", required=False, multiple=False),
      Field("modality", "Modality", "https://schema.hbp.eu/minds/modality", required=False, multiple=False),
      Field("owners", "Person", "https://schema.hbp.eu/minds/owners", required=False, multiple=True),
      Field("parcellation_atlas", "ParcellationAtlas", "https://schema.hbp.eu/minds/parcellationAtlas", required=False, multiple=False),
      Field("parcellation_region", "ParcellationRegion", "https://schema.hbp.eu/minds/parcellationRegion", required=False, multiple=False),
      Field("part_of", basestring, "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/partOf", required=False, multiple=False),
      Field("publications", "Publication", "https://schema.hbp.eu/minds/publications", required=False, multiple=True),
      Field("reference_space", "ReferenceSpace", "https://schema.hbp.eu/minds/reference_space", required=False, multiple=False),
      Field("specimen_group", "SpecimenGroup", "https://schema.hbp.eu/minds/specimen_group", required=False, multiple=False))
    


class EmbargoStatus(MINDSObject):
    """
    docstring
    """
    _path = "/core/embargostatus/v1.0.0"
    type = ["minds:EmbargoStatus"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("embargo_status", "EmbargoStatus", "https://schema.hbp.eu/minds/embargo_status", required=False, multiple=False))
    


class File(MINDSObject):
    """
    docstring
    """
    _path = "/core/file/v0.0.4"
    type = ["minds:File"]
    fields = (
      Field("absolute_path", basestring, "http://hbp.eu/minds#absolute_path", required=False, multiple=False),
      Field("byte_size", basestring, "http://hbp.eu/minds#byte_size", required=False, multiple=False),
      Field("content_type", basestring, "http://hbp.eu/minds#content_type", required=False, multiple=False),
      Field("hash", basestring, "http://hbp.eu/minds#hash", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("last_modified", datetime, "http://hbp.eu/minds#last_modified", required=False, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("relative_path", basestring, "http://hbp.eu/minds#relative_path", required=False, multiple=False),
      Field("file", "File", "http://hbp.eu/minds#file", required=False, multiple=False))
    


class FileAssociation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fileassociation/v1.0.0"
    type = ["minds:FileAssociation"]
    fields = (
      Field("from", basestring, "https://schema.hbp.eu/linkinginstance/from", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("to", basestring, "https://schema.hbp.eu/linkinginstance/to", required=False, multiple=False))
    


class Format(MINDSObject):
    """
    docstring
    """
    _path = "/core/format/v1.0.0"
    type = ["minds:Format"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("formats", "Format", "https://schema.hbp.eu/minds/formats", required=False, multiple=True))
    


class LicenseType(MINDSObject):
    """
    docstring
    """
    _path = "/core/licensetype/v1.0.0"
    type = ["minds:LicenseType"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("license", basestring, "https://schema.hbp.eu/minds/license", required=False, multiple=False))
    


class Method(MINDSObject):
    """
    docstring
    """
    _path = "/core/method/v1.0.0"
    type = ["minds:Method"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False))
    


class Modality(MINDSObject):
    """
    docstring
    """
    _path = "/core/modality/v1.0.0"
    type = ["minds:Modality"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("modality", "Modality", "https://schema.hbp.eu/minds/modality", required=False, multiple=False))
    


class Parcellationatlas(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationatlas/v1.0.0"
    type = ["minds:Parcellationatlas"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("parcellation_atlas", "ParcellationAtlas", "https://schema.hbp.eu/minds/parcellationAtlas", required=False, multiple=False))
    


class ParcellationRegion(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationregion/v1.0.0"
    type = ["minds:ParcellationRegion"]
    fields = (
      Field("alias", basestring, "https://schema.hbp.eu/minds/alias", required=False, multiple=False),
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("url", basestring, "https://schema.hbp.eu/viewer/url", required=False, multiple=False),
      Field("parcellation_region", "ParcellationRegion", "https://schema.hbp.eu/minds/parcellationRegion", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/minds/species", required=False, multiple=False))
    


class Person(MINDSObject):
    """
    docstring
    """
    _path = "/core/person/v1.0.0"
    type = ["minds:Person"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("shortname", basestring, "https://schema.hbp.eu/minds/shortName", required=False, multiple=False),
      Field("authors", "Person", "https://schema.hbp.eu/minds/authors", required=False, multiple=True),
      Field("contributors", "Person", "https://schema.hbp.eu/minds/contributors", required=False, multiple=True),
      Field("owners", "Person", "https://schema.hbp.eu/minds/owners", required=False, multiple=True))
    


class PLAComponent(MINDSObject):
    """
    docstring
    """
    _path = "/core/placomponent/v1.0.0"
    type = ["minds:PLAComponent"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("component", basestring, "https://schema.hbp.eu/minds/component", required=False, multiple=False))
    


class Preparation(MINDSObject):
    """
    docstring
    """
    _path = "/core/preparation/v1.0.0"
    type = ["minds:Preparation"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("preparation", "Preparation", "https://schema.hbp.eu/minds/preparation", required=False, multiple=False))
    


class Protocol(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/protocol/v1.0.0"
    type = ["minds:Protocol"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("protocols", "Protocol", "https://schema.hbp.eu/minds/protocols", required=False, multiple=True))
    


class Publication(MINDSObject):
    """
    docstring
    """
    _path = "/core/publication/v1.0.0"
    type = ["minds:Publication"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("cite", basestring, "https://schema.hbp.eu/minds/cite", required=False, multiple=False),
      Field("doi", basestring, "https://schema.hbp.eu/minds/doi", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("authors", "Person", "https://schema.hbp.eu/minds/authors", required=False, multiple=True),
      Field("publications", "Publication", "https://schema.hbp.eu/minds/publications", required=False, multiple=True))
    


class ReferenceSpace(MINDSObject):
    """
    docstring
    """
    _path = "/core/referencespace/v1.0.0"
    type = ["minds:ReferenceSpace"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("reference_space", "ReferenceSpace", "https://schema.hbp.eu/minds/reference_space", required=False, multiple=False))
    


class Role(MINDSObject):
    """
    docstring
    """
    _path = "/prov/role/v1.0.0"
    type = ["minds:Role"]
    fields = (
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("had_role", "Role", "http://www.w3.org/ns/prov#hadRole", required=False, multiple=False))
    


class Sample(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/sample/v1.0.0"
    type = ["minds:Sample"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("weight_post_fixation", QuantitativeValue, "https://schema.hbp.eu/minds/weightPostFixation", required=False, multiple=False),
      Field("weight_pre_fixation", QuantitativeValue, "https://schema.hbp.eu/minds/weightPreFixation", required=False, multiple=False),
      Field("methods", "Method", "https://schema.hbp.eu/minds/methods", required=False, multiple=True),
      Field("parcellation_atlas", "ParcellationAtlas", "https://schema.hbp.eu/minds/parcellationAtlas", required=False, multiple=False),
      Field("parcellation_region", "ParcellationRegion", "https://schema.hbp.eu/minds/parcellationRegion", required=False, multiple=False),
      Field("reference", basestring, "https://schema.hbp.eu/brainviewer/reference", required=False, multiple=False),
      Field("samples", "Sample", "https://schema.hbp.eu/minds/samples", required=False, multiple=True))
    


class Sex(MINDSObject):
    """
    docstring
    """
    _path = "/core/sex/v1.0.0"
    type = ["minds:Sex"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("sex", "Sex", "https://schema.hbp.eu/minds/sex", required=False, multiple=False))
    


class SoftwareAgent(MINDSObject):
    """
    docstring
    """
    _path = "/core/softwareagent/v1.0.0"
    type = ["minds:SoftwareAgent"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("agent", basestring, "http://www.w3.org/ns/prov#agent", required=False, multiple=False))
    


class Species(MINDSObject):
    """
    docstring
    """
    _path = "/core/species/v1.0.0"
    type = ["minds:Species"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("alternate_of", basestring, "http://www.w3.org/ns/prov#alternateOf", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/minds/species", required=False, multiple=False))
    


class SpecimenGroup(MINDSObject):
    """
    docstring
    """
    _path = "/core/specimengroup/v1.0.0"
    type = ["minds:SpecimenGroup"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("specimen_group", "SpecimenGroup", "https://schema.hbp.eu/minds/specimen_group", required=False, multiple=False),
      Field("subjects", "Subject", "https://schema.hbp.eu/minds/subjects", required=False, multiple=True))
    


class Subject(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/subject/v1.0.0"
    type = ["minds:Subject"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("cause_of_death", basestring, "https://schema.hbp.eu/minds/causeOfDeath", required=False, multiple=False),
      Field("genotype", basestring, "https://schema.hbp.eu/minds/genotype", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("associated_with", "Person", "http://www.w3.org/ns/prov#qualifiedAssociation", required=False, multiple=False),
      Field("strain", basestring, "https://schema.hbp.eu/minds/strain", required=False, multiple=False),
      Field("strains", basestring, "https://schema.hbp.eu/minds/strains", required=False, multiple=True),
      Field("weight", QuantitativeValue, "https://schema.hbp.eu/minds/weight", required=False, multiple=False),
      Field("age", QuantitativeValue, "https://schema.hbp.eu/minds/age", required=False, multiple=False),
      Field("age_category", "AgeCategory", "https://schema.hbp.eu/minds/age_category", required=False, multiple=False),
      Field("samples", "Sample", "https://schema.hbp.eu/minds/samples", required=False, multiple=True),
      Field("sex", "Sex", "https://schema.hbp.eu/minds/sex", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/minds/species", required=False, multiple=False),
      Field("subjects", "Subject", "https://schema.hbp.eu/minds/subjects", required=False, multiple=True))
    

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
