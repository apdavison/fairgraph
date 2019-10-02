"""

"""
try:
    basestring
except NameError:
    basestring = str

import sys, inspect
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

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("created_at", basestring, "https://schema.hbp.eu/minds/created_at", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "", required=False))
    


class Agecategory(MINDSObject):
    """
    docstring
    """
    _path = "/core/agecategory/v1.0.0"
    type = ["minds:Agecategory"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Approval(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/approval/v1.0.0"
    type = ["minds:Approval"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Authority(MINDSObject):
    """
    docstring
    """
    _path = "/ethics/authority/v1.0.0"
    type = ["minds:Authority"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Dataset(MINDSObject):
    """
    docstring
    """
    _path = "/core/dataset/v1.0.0"
    type = ["minds:Dataset"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("activity", basestring, "https://schema.hbp.eu/minds/activity", required=False),
      Field("containerUrlAsZIP", basestring, "https://schema.hbp.eu/minds/containerUrlAsZIP", required=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False),
      Field("created_at", basestring, "https://schema.hbp.eu/minds/created_at", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("datalink", basestring, "http://schema.org/datalink", required=False),
      Field("datasetDOI", basestring, "https://schema.hbp.eu/minds/datasetDOI", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("external_datalink", basestring, "https://schema.hbp.eu/minds/external_datalink", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("reference", basestring, "https://schema.hbp.eu/neuroglancer/reference", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("release_date", basestring, "https://schema.hbp.eu/minds/release_date", required=False),
      Field("type", basestring, "", required=False))
    


class Embargostatus(MINDSObject):
    """
    docstring
    """
    _path = "/core/embargostatus/v1.0.0"
    type = ["minds:Embargostatus"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class File(MINDSObject):
    """
    docstring
    """
    _path = "/core/file/v0.0.4"
    type = ["minds:File"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("absolute_path", basestring, "http://hbp.eu/minds#absolute_path", required=False),
      Field("byte_size", basestring, "http://hbp.eu/minds#byte_size", required=False),
      Field("content_type", basestring, "http://hbp.eu/minds#content_type", required=False),
      Field("hash", basestring, "http://hbp.eu/minds#hash", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("last_modified", basestring, "http://hbp.eu/minds#last_modified", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relative_path", basestring, "http://hbp.eu/minds#relative_path", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Fileassociation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fileassociation/v1.0.0"
    type = ["minds:Fileassociation"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("from", basestring, "https://schema.hbp.eu/linkinginstance/from", required=False),
      Field("hashcode", basestring, "https://schema.hbp.eu/internal/hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("to", basestring, "https://schema.hbp.eu/linkinginstance/to", required=False),
      Field("type", basestring, "@type", required=False))
    


class Format(MINDSObject):
    """
    docstring
    """
    _path = "/core/format/v1.0.0"
    type = ["minds:Format"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Licensetype(MINDSObject):
    """
    docstring
    """
    _path = "/core/licensetype/v1.0.0"
    type = ["minds:Licensetype"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Method(MINDSObject):
    """
    docstring
    """
    _path = "/core/method/v1.0.0"
    type = ["minds:Method"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Modality(MINDSObject):
    """
    docstring
    """
    _path = "/core/modality/v1.0.0"
    type = ["minds:Modality"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Parcellationatlas(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationatlas/v1.0.0"
    type = ["minds:Parcellationatlas"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Parcellationregion(MINDSObject):
    """
    docstring
    """
    _path = "/core/parcellationregion/v1.0.0"
    type = ["minds:Parcellationregion"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alias", basestring, "https://schema.hbp.eu/minds/alias", required=False),
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False),
      Field("url", basestring, "https://schema.hbp.eu/viewer/url", required=False))
    


class Person(MINDSObject):
    """
    docstring
    """
    _path = "/core/person/v1.0.0"
    type = ["minds:Person"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("shortName", basestring, "https://schema.hbp.eu/minds/shortName", required=False),
      Field("type", basestring, "", required=False))
    


class Placomponent(MINDSObject):
    """
    docstring
    """
    _path = "/core/placomponent/v1.0.0"
    type = ["minds:Placomponent"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Preparation(MINDSObject):
    """
    docstring
    """
    _path = "/core/preparation/v1.0.0"
    type = ["minds:Preparation"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Protocol(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/protocol/v1.0.0"
    type = ["minds:Protocol"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Publication(MINDSObject):
    """
    docstring
    """
    _path = "/core/publication/v1.0.0"
    type = ["minds:Publication"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("cite", basestring, "https://schema.hbp.eu/minds/cite", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("doi", basestring, "https://schema.hbp.eu/minds/doi", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Referencespace(MINDSObject):
    """
    docstring
    """
    _path = "/core/referencespace/v1.0.0"
    type = ["minds:Referencespace"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Role(MINDSObject):
    """
    docstring
    """
    _path = "/prov/role/v1.0.0"
    type = ["minds:Role"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Sample(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/sample/v1.0.0"
    type = ["minds:Sample"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("container_url", basestring, "https://schema.hbp.eu/minds/container_url", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False),
      Field("weightPostFixation", basestring, "https://schema.hbp.eu/minds/weightPostFixation", required=False),
      Field("weightPreFixation", basestring, "https://schema.hbp.eu/minds/weightPreFixation", required=False))
    


class Sex(MINDSObject):
    """
    docstring
    """
    _path = "/core/sex/v1.0.0"
    type = ["minds:Sex"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Softwareagent(MINDSObject):
    """
    docstring
    """
    _path = "/core/softwareagent/v1.0.0"
    type = ["minds:Softwareagent"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("description", basestring, "http://schema.org/description", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Species(MINDSObject):
    """
    docstring
    """
    _path = "/core/species/v1.0.0"
    type = ["minds:Species"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Specimengroup(MINDSObject):
    """
    docstring
    """
    _path = "/core/specimengroup/v1.0.0"
    type = ["minds:Specimengroup"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("created_at", basestring, "https://schema.hbp.eu/minds/created_at", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("type", basestring, "@type", required=False))
    


class Subject(MINDSObject):
    """
    docstring
    """
    _path = "/experiment/subject/v1.0.0"
    type = ["minds:Subject"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.id!r})'.format(self=self))
    fields = (\
      Field("alternatives", basestring, "https://schema.hbp.eu/inference/alternatives", required=False),
      Field("causeOfDeath", basestring, "https://schema.hbp.eu/minds/causeOfDeath", required=False),
      Field("createdAt", basestring, "https://schema.hbp.eu/provenance/createdAt", required=False),
      Field("createdBy", basestring, "https://schema.hbp.eu/provenance/createdBy", required=False),
      Field("genotype", basestring, "https://schema.hbp.eu/minds/genotype", required=False),
      Field("hashcode", basestring, "http://hbp.eu/internal#hashcode", required=False),
      Field("id", basestring, "@id", required=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True),
      Field("immediateIndex", basestring, "https://schema.hbp.eu/provenance/immediateIndex", required=False),
      Field("lastModificationUserId", basestring, "https://schema.hbp.eu/provenance/lastModificationUserId", required=False),
      Field("modifiedAt", basestring, "https://schema.hbp.eu/provenance/modifiedAt", required=False),
      Field("name", basestring, "http://schema.org/name", required=True),
      Field("qualifiedAssociation", basestring, "http://www.w3.org/ns/prov#qualifiedAssociation", required=False),
      Field("relativeUrl", basestring, "https://schema.hbp.eu/relativeUrl", required=False),
      Field("strain", basestring, "https://schema.hbp.eu/minds/strain", required=False),
      Field("strains", basestring, "https://schema.hbp.eu/minds/strains", required=False),
      Field("weight", basestring, "https://schema.hbp.eu/minds/weight", required=False),
      Field("age", basestring, "https://schema.hbp.eu/minds/age", required=False),
      Field("type", basestring, "@type", required=False))
################################################################    
### end of script-generated code
################################################################    

def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


# Alias some classes to reflect names used in KG Search
Project = Placomponent

if __name__=='__main__':

    import os
    from fairgraph import minds, KGClient
    token = os.environ['HBP_token']
    client = KGClient(token)
    for cls in minds.list_kg_classes():
        print(cls.__name__)
