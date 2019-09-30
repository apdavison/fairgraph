from fairgraph import minds, uniminds

# this query will be applied to all classes of all namepsaces:
COMMON_QUERIES = [
    {'query_name': 'name_contains_id_equals',
     'quantities':['name', '@id'],
     'operators':['contains', 'equals'],
     'parameters':['name', 'id']}
]


# then a set of custom queries
CUSTOM_QUERIES = {
    'Minds-Dataset':[
        {'query_name': 'contributors_contains', # explicit name of the query
         'quantities':['contributors'], # quantities that will have the filter
         'operators':['contains'], # operator for the filter
         'parameters':['contributors']}, # parameter (usually same than quantity)
        {'query_name': 'id_equals',
         'quantities':['@id'],
         'operators':['equals'],
         'parameters':['id']},
    ],
    'Uniminds-Project':[
        {'query_name': 'contributors_equals', # explicit name of the query
         'quantities':['contributors'], # quantities that will have the filter
         'operators':['equals'], # operator for the filter
         'parameters':['contributors']}, # parameter (usually same than quantity)
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
