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
                        operators=['contains'] ,
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
        

def clean_up_KGE_query_for_fairgraph(namespace, cls, cls_version):
    """
    Requirements:
    for all the NAMESPACES, you have generated a query using the builder in the Knowledge graph Editor
    https://kg.humanbrainproject.org/editor/query-builder

    For each namespace (e.g. "Dataset"), you have saved the query in the KGE with the "fg-KGE" suffix
    i.e. for the "Dataset" namespace, the query can be found at:
    https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-KGE

    Then the script will generate the new fairgraph-compatible query 
    """

    r=requests.get(query_url(namespace, cls_version)+'-KGE',
          headers={'Content-Type':'application/json',
                   'Authorization': 'Bearer {}'.format(access_token)})
    new_query_dict = {}
    if r.ok:
        open('temp.json', 'wb').write(r.content)
        with open('temp.json', 'r') as f:
            KGE_dict = json.load(f)

        for key, value in KGE_dict.items():
            if type(value)==dict:
                # new_query_dict[key] = {}
                # for key2, value2 in value.items():
                #     if key2!='fieldname':
                #         new_query_dict[key][key2] = value2
                new_query_dict[key] = value # no need to delete the fieldname entry here
            elif type(value)==list:
                new_query_dict[key] = []
                for value2 in value:
                    new_query_dict[key].append({})
                    for key3, value3 in value2.items():
                        if key3!='fieldname':
                            new_query_dict[key][-1][key3] = value3
                        else:
                            new_query_dict[key][-1]['field'] = value3.split('query:')[1]
                            
            else:
                new_query_dict[key] = value
    else:
        print('Problem with url: %s' % query_url(namespace, cls_version)+'-KGE')
        
    return new_query_dict
            

def upload_faigraph_compatible_query(new_query_dict, namespace, version, cls,
                                     extension=''):

    with open('temp.json', 'w') as f:
        json.dump(new_query_dict, f)

    r=requests.put(query_url(namespace, version, cls, extension),
                   data = open('temp.json', 'rb'),
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(access_token)})

    if r.ok:
        print('Successfully stored the query at %s ' % query_url(namespace, version, cls, extension))
    else:
        print('Problem with "put" protocol on url: %s ' % query_url(namespace, version, cls, extension))
        print('---> Check your HBP token validity and/or your HBP credential permissions')
            

if __name__=='__main__':
    
    # new_query = clean_up_KGE_query_for_fairgraph('Minds', 'v1.0.0', 'Activity')
    # upload_faigraph_compatible_query(new_query, 'Minds', 'v1.0.0', 'Activity')
    # print(add_filter_to_query(new_query))

    # json_text = pprint.pprint(d)
    # exec('d = %s' % str(r.content))
    # pprint.pprint(KGE_dict)
    print('----------------------------------')
    # pprint.pprint(new_query_dict)


