# setting up the KG objects handled by fairgraph
KG_OBJECTS = [
    {
        'namespace':'Minds',
        'version':'v1.0.0',
        'classes':[
            'Activity',
            'Dataset',
            'Person',
        ],
    },
    {
        'namespace':'Uniminds',
        'version':'v1.0.0',
        'classes':[
            'Dataset',
            'Project',
            'Person',
        ],
    },
]


# this query will be applid to all classes of all namepsaces:
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
for kgo in KG_OBJECTS:
    for cls in kgo['classes']:
        key = '%s-%s' % (kgo['namespace'], cls)
        QUERIES[key] = COMMON_QUERIES.copy()
        if key in CUSTOM_QUERIES:
            for query in CUSTOM_QUERIES[key]:
                QUERIES[key].append(query)

