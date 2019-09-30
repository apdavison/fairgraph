"""

"""
try:
    basestring
except NameError:
    basestring = str

from tabulate import tabulate
from fairgraph.base import KGObject, KGProxy, KGQuery, cache, as_list, Field
from fairgraph.data import FileAssociation, CSCSFile
import sys, inspect


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


##### The following code is generated by the script in queries/code_generation_from_KGE_queries

### end of script-generated code

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
