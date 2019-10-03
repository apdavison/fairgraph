"""
needs a temporary file "temp.json",
maybe should be put in a system temporarry directory with tempfile (but adds a dependency)
"""
import requests, os, json, pprint
import numpy as np
from query_config import QUERIES, from_fairgraph_key_to_KG_attribute

access_token = os.environ['HBP_token']

def query_url(namespace, cls_version,
              extension=''):
    """
    """
    url = 'https://kg.humanbrainproject.org/query/%s/%s/fg' %\
          (namespace.lower(), cls_version)
    return url+extension


def add_filter_to_query(attribute_name, query):
    """
    add a filter for the query
    """
    i0 = np.argwhere(np.array(query['quantities'],dtype=str)==attribute_name).flatten()
    if len(i0)>0:
        quant = from_fairgraph_key_to_KG_attribute(query['quantities'][i0[0]])
        if quant=='@id':
            param = 'id'
        else:
            param = quant
        return "'filter':{'op':'%s', 'parameter':'%s'}," % (query['operators'][i0[0]], param)
    else:
        return ''

def format_query(namespace, cls,
                 query={'quantities':[], 'operators':[], 'parameters':[]},
                 queryID='fg'):

    FIELDS_STRING = ''
    for f in cls.fields:

        FIELDS_STRING += "    {'field':'%s'," % from_fairgraph_key_to_KG_attribute(f.name)
        if f.name in query['quantities']:
            FIELDS_STRING += add_filter_to_query(f.name, query)
        FIELDS_STRING += "'relative_path':'%s'},\n" % f.path
    return """
    {
    '@context': {'@vocab': 'https://schema.hbp.eu/graphQuery/',
    'fieldname': {'@id': 'fieldname', '@type': '@id'},
    'merge': {'@id': 'merge', '@type': '@id'},
    'relative_path': {'@id': 'relative_path', '@type': '@id'}},
    'fields': [
    %s],
    'http://schema.org/identifier': 'minds%s/%s',
    'https://schema.hbp.eu/graphQuery/root_schema': {'@id': 'https://nexus.humanbrainproject.org/v0/schemas/minds%s'}
    }""" % (FIELDS_STRING[:-2], cls._path, queryID, cls._path)


def upload_faigraph_query(query_string, namespace, cls_version,
                          extension=''):

    with open('temp.json', 'w') as f:
        f.write(query_string)

    r=requests.put(query_url(namespace, cls_version, extension),
                   data = open('temp.json', 'r'),
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(access_token)})
    
    if r.ok:
        print('Successfully stored the query at %s ' % query_url(namespace, cls_version, extension))
    else:
        print(r)
        print('Problem with "put" protocol on url: %s ' % query_url(namespace, cls_version, extension))
        print('---> Check your HBP token validity and/or your HBP credential permissions')

if __name__=='__main__':
    LIMITING_N = 1000000 # set to a lower value for troubleshooting (e.g. 3)
    from fairgraph import minds, uniminds
    n = 0
    for namespace, Namespace in zip([minds, uniminds], ['Minds', 'Uniminds']):
        for cls in namespace.list_kg_classes():
            if cls.__name__!='MINDSObject' and n<LIMITING_N:
                key = '%s-%s' % (Namespace, cls.__name__)
                neutral_query = format_query(namespace, cls)
                upload_faigraph_query(neutral_query, Namespace, cls._path[1:])
                key = '%s-%s' % (Namespace, cls.__name__)
                for query in QUERIES[key]:
                    filtered_query = format_query(namespace, cls, query=query)
                    upload_faigraph_query(filtered_query, Namespace, cls._path[1:], extension='_'+query['query_name'])
                n+=1
        
