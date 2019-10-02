from fairgraph import minds, uniminds


def from_fairgraph_key_to_KG_attribute(key):
    """
    function to handle the potential differences between fairgraph and the KG in terms of attribute names
    """
    if key=='id':
        return '@id'
    else:
        return key

# here everything should be written in terms of 'fairgraph' definition (e.g. 'id' instead of '@id')
    
    
# this query will be applied to all classes of all namepsaces:
COMMON_QUERIES = [
    {'query_name': 'name_contains_id_equals',
     'quantities':['name', 'id'],
     'operators':['contains', 'equals']}
]

# then a set of custom queries
CUSTOM_QUERIES = {
    'Minds-Dataset':[
        {'query_name': 'contributors_contains', # explicit name of the query
         'quantities':['contributors'], # quantities that will have the filter
         'operators':['contains']}, # parameter (usually same than quantity)
        {'query_name': 'id_equals',
         'quantities':['id'],
         'operators':['equals']},
    ],
    'Uniminds-Project':[
        {'query_name': 'contributors_equals', # explicit name of the query
         'quantities':['contributors'], # quantities that will have the filter
         'operators':['equals']}, # parameter (usually same than quantity)
    ]
}

QUERIES = {}

for namespace, Namespace in zip([minds, uniminds], ['Minds', 'Uniminds']):
    for cls in namespace.list_kg_classes():
        key = '%s-%s' % (Namespace, cls.__name__)
        QUERIES[key] = COMMON_QUERIES.copy()
        if key in CUSTOM_QUERIES:
            for query in CUSTOM_QUERIES[key]:
                QUERIES[key].append(query)

if __name__=='__main__':
    print(QUERIES)
