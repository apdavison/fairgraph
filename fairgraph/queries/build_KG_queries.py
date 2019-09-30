"""
needs a temporary file "temp.json",
maybe should be put in a system temporarry directory with tempfile (but adds a dependency)
"""
import requests, os, json, pprint
access_token = os.environ['HBP_token']
import numpy as np

def query_url(namespace, cls_version,
              extension=''):
    """
    """
    url = 'https://kg.humanbrainproject.org/query/%s/%s/fg' %\
          (namespace.lower(), cls_version)
    return url+extension


def add_filter_to_query(query_dict,
                        quantities=['name'],
                        operators=['contains'],
                        parameters=['name']):
    """
    add a filter for the query
    """
    new_query_dict = query_dict.copy()
    for i, dictionary in enumerate(new_query_dict['fields']):
        i0 = np.argwhere(dictionary['field']==np.array(quantities,dtype=str)).flatten()
        if len(i0)>0:
            new_query_dict['fields'][i]['filter'] = {'op':operators[i0[0]], 'parameter':parameters[i0[0]]}
    return new_query_dict



def upload_faigraph_query(query_string, namespace, cls_version,
                          extension=''):

    with open('temp.json', 'w') as f:
        json.dump(query_string, f)

    r=requests.put(query_url(namespace, cls_version, extension),
                   data = open('temp.json', 'r'),
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(access_token)})
    
    if r.ok:
        print('Successfully stored the query at %s ' % query_url(namespace, cls_version, extension))
    else:
        print('Problem with "put" protocol on url: %s ' % query_url(namespace, cls_version, extension))
        print('---> Check your HBP token validity and/or your HBP credential permissions')


def format_query(namespace, cls,
                 queryID='fg'):

    FIELDS_STRING = ''
    for f in cls.fields:

        FIELDS_STRING += "{'field':%s," % f.name
        FIELDS_STRING += "'relative_path':%s}," % f.path
    return """
{'@context': {'@vocab': 'https://schema.hbp.eu/graphQuery/',
 'fieldname': {'@id': 'fieldname', '@type': '@id'},
 'merge': {'@id': 'merge', '@type': '@id'},
 'relative_path': {'@id': 'relative_path', '@type': '@id'}},
 'fields': [%s],
 'http://schema.org/identifier': 'minds%s/%s',
 'https://schema.hbp.eu/graphQuery/root_schema': {'@id': 'https://nexus.humanbrainproject.org/v0/schemas/minds%s'}}
""" % (FIELDS_STRING, cls._path, queryID, cls._path)

if __name__=='__main__':

    from fairgraph import minds, uniminds
    n = 0
    for namespace, Namespace in zip([minds, uniminds], ['Minds', 'Uniminds']):
        for cls in namespace.list_kg_classes():
            if cls.__name__!='MINDSObject' and n<3:
                key = '%s-%s' % (Namespace, cls.__name__)
                neutral_query = format_query(namespace, cls)
                upload_faigraph_query(neutral_query, Namespace, cls._path[1:])
                n+=1
        
    # upload_faigraph_compatible_query(new_query, 'Minds', 'v1.0.0', 'Activity')
    # print(add_filter_to_query(new_query))
    
    # json_text = pprint.pprint(d)
    # exec('d = %s' % str(r.content))
    # pprint.pprint(KGE_dict)
    # print('----------------------------------')
    # pprint.pprint(new_query_dict)


