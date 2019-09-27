from reformat_KGE_generated_queries import *
# load the config file
from config import KG_OBJECTS, QUERIES

for kgo in KG_OBJECTS:
    for cls in kgo['classes']:
        new_query = clean_up_KGE_query_for_fairgraph(kgo['namespace'],
                                                     kgo['version'],
                                                     cls)
        upload_faigraph_compatible_query(new_query,
                                         kgo['namespace'],
                                         kgo['version'],
                                         cls)
        key = '%s-%s' % (kgo['namespace'], cls)
        for query in QUERIES[key]:
            new_query_with_filters = add_filter_to_query(new_query,
                                                         quantities=query['quantities'],
                                                         operators=query['operators'] ,
                                                         parameters=query['parameters'])
            upload_faigraph_compatible_query(new_query_with_filters,
                                             kgo['namespace'],
                                             kgo['version'],
                                             cls, extension='_'+query['query_name'])
            
