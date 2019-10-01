# Integrating Knowledge Graph queries into fairgraph

### Motivation

Fairgraph uses queries to interact with the Knowledge Graph database. For speed considerations, the queries used have to be predefined and stored within the Knowledge Graph architecture.

### Implementation

The means that all queries used by fairgraph will be constructed and uploaded on the KG server. For example, the query with argument "XXX" looking either for a name containing "XXX" or for the ID of a dataset being "XXX" is stored at the following address:

https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg_name_contains_id_equals

So for each new faigraph function relying on a new query. The query needs to be added. This is performed in the following two steps procedure:

#### 1) Incrementing the 'query_config.py' file

The file 'query_config.py' stores all queries used by faigraph, it is located in: `./fairgraph/faigraph/queries/query_config.py`

The queries are divided into common and custom queries. You should add a new query in one or the other depending on whether your new query applies to all classes of all namespaces or whether it is specific to a given class.

##### Common queries

Those queries are stored in the `COMMON_QUERIES` list of the 'query_config.py' file. An example value is:

```
COMMON_QUERIES = [
    {'query_name': 'name_contains_id_equals',
     'quantities':['name', 'id'],
     'operators':['contains', 'equals']},
    {'query_name': 'identifier_contains',
     'quantities':['identifier'],
     'operators':['contains']}
]
```
You should add a new dictionary for each new query to this list, with name for the query ("query_name") a set of quantitites on which it applies ("quantities") and a corresponding set of operators ("operators").

##### Custom queries

Then a set of custom queries specific to specific classes of specific namespaces. Those queries are stored in the `CUSTOM_QUERIES` list of the 'query_config.py' file. For a given class of a given namespace (e.g. class "Dataset" in the "Minds" namespace), the key of the dictionary should be "Namespace-Class" (e.g. "Minds-Dataset" here). Each element of the "Namespace-Class" key is a set of queries (i.e. a list of dictionaries) as in the case of "COMMON_QUERIES".

```
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
```

#### 2) Upload the queries to the Knowledge Graph

Once you have built the "query_config.py" file, run the following command in the `faigraph/queries/` subdirectory.

```
$ python build_KG_queries.py
```

The output should look like this:

```
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg 
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg_name_contains_id_equals 
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/core/agecategory/v1.0.0/fg 
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/core/agecategory/v1.0.0/fg_name_contains_id_equals 
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/ethics/approval/v1.0.0/fg 
Successfully stored the query at https://kg.humanbrainproject.org/query/minds/ethics/approval/v1.0.0/fg_name_contains_id_equals 
[...]
```

<!-- # 2) Integrating Knowledge graph queries into fairgraph -->

<!-- We use the features of the [HBP Knowledge Graph editor](https://kg.humanbrainproject.org/editor) to build the queries and the namespace properties (e.g. its classes) within fairgraph. -->

<!-- Vocabulary: -->

<!-- - "Namespaces" refer to the different root schema considered: "Minds", "Uniminds", "Neuralactivity", ... They are associated to a given "Version". -->
<!-- - "Classes" refer to the different schemas of a given namespace: e.g. for the minds schema: "Dataset", "Person", ... -->
<!--  - "Attributes" are the properties of the entries of a given class. E.g. a Dataset has the attributes: "name", "contributors", "identifier", ... -->
 
<!-- All those objects need to be included into "faigraph". We detail here the procedure to do this. -->

<!-- ## 1) Build a general query with the KG editor for a given Namespace and a given Class of interest -->

<!-- Let's build a general query for the case of the "Minds" namespace for the "Dataset" class. -->

<!-- Within the [Knowledge Graph editor](https://kg.humanbrainproject.org/editor), we select the [query-builder](https://kg.humanbrainproject.org/editor/query-builder). -->

<!-- We scroll over the root schema to find the "Minds" namepsace, and then we select the "Dataset" class within the "Minds" namespace. -->

<!-- ![Screenshot of the KGE](doc/KGE-screenshot-1.png) -->

<!-- Then we add all "Attributes" of the class to the  -->

<!-- ![Screenshot of the KGE](doc/KGE-screenshot-2.png) -->

<!-- In "Results JSON view", set the size to a large value (e.g. size=20000) -->

<!-- Then we save the query using the following format: -->
<!-- "fg-Namespace-Class-KGE", e.g. for that example -->

<!-- ![Screenshot of the KGE](doc/KGE-screenshot-3.png) -->

<!-- The stored query should therefore appear in the following address: -->

<!-- https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-Minds-Dataset-KGE -->

<!-- ## 2) Repeat for all Namespaces and Classes of interest -->

<!-- Here are a few example combinations: -->

<!-- 1. Minds-Activity -->
<!-- 2. Uniminds-Project -->
<!-- 3. Uniminds-Person -->
<!-- 4. ... -->

<!-- ## 3) Configure the KG Objects handled by fairgraph -->

<!-- Open the [config.py](./config.py) file and write down all the Namespaces (with their version) and Classes that you have saved as a query in the KGE editor. -->

<!-- here is an example: -->
<!-- ``` -->
<!-- KG_OBJECTS = [ -->
<!--     { -->
<!--         'namespace':'Minds', -->
<!--         'version':'v1.0.0', -->
<!--         'classes':[ -->
<!--             'Activity', -->
<!--             'Dataset', -->
<!--             'Person', -->
<!--         ], -->
<!--     }, -->
<!--     { -->
<!--         'namespace':'Uniminds', -->
<!--         'version':'v1.0.0', -->
<!--         'classes':[ -->
<!--             'Project', -->
<!--             'Person', -->
<!--         ], -->
<!--     }, -->
<!-- ] -->
<!-- ``` -->

<!-- ## 4) Add a set of queries -->

<!-- Adding a set of common queries (queries that are unspecific to a namespace and a class, i.e. where the attributes are shared among all objects). For example the "name" and "id " are always present.  -->
<!-- ``` -->
<!-- # this query will be applid to all classes of all namepsaces: -->
<!-- COMMON_QUERIES = [ -->
<!--     {'query_name': 'name_contains_id_equals', -->
<!--      'quantities':['name', '@id'], -->
<!--      'operators':['contains', 'equals'], -->
<!--      'parameters':['name', 'id']} -->
<!--     {'query_name': 'name_contains', -->
<!--      'quantities':['name'], -->
<!--      'operators':['contains'], -->
<!--      'parameters':['name']} -->
<!-- ] -->
<!-- ``` -->

<!-- Now you can also set explicitely a set of custom queries that will be "Namespace" and "class"-dependent (because it focuses on class-specific attributes).  -->
<!-- ``` -->
<!-- CUSTOM_QUERIES = { -->
<!--     'Minds-Dataset':[ -->
<!--         {'query_name': contributors_contains', # explicit name of the query -->
<!--          'quantities':['contributors], # quantities that will have the filter -->
<!--          'operators':['contains'], # operator for the filter -->
<!--          'parameters':['contributors]}, # parameter (usually same than quantity) -->
<!--         {'query_name': 'name_contains_id_equals', -->
<!--          'quantities':['name', '@id'], -->
<!--          'operators':['contains', 'equals'], -->
<!--          'parameters':['name', 'id']}, -->
<!--     ] -->
<!--     'Uniminds-Project':[ -->
<!--         {'query_name': contributors_contains', # explicit name of the query -->
<!--          'quantities':['contributors], # quantities that will have the filter -->
<!--          'operators':['contains'], # operator for the filter -->
<!--          'parameters':['contributors]}, # parameter (usually same than quantity) -->
<!--     ] -->
<!-- } -->
<!-- ``` -->

<!-- ## 5) Run the script to convert the KGE queries into "fairgraph-compatible" queries -->

<!-- Provided you have write access in you HBP account and the appropriate token (see ![fairgraph manual](../README.md)), you can now run the script that reformats the queries and upload them in the KG query storage. -->

<!-- ``` -->
<!-- python process_config_file.py  -->
<!-- ``` -->

<!-- The list of uploaded url queries should appear. -->

<!-- For the above [config.py](./config.py) the list is: -->

<!-- https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg-Activity -->

<!-- https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg-Activity_name_contains_id_equals -->

<!-- ... -->

<!-- https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-Dataset_contributors_contains  -->

<!-- https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-Dataset_id_equals  -->

<!-- ... -->

<!-- https://kg.humanbrainproject.org/query/uniminds/core/person/v1.0.0/fg-Person  -->

<!-- https://kg.humanbrainproject.org/query/uniminds/core/person/v1.0.0/fg-Person_name_contains_id_equals  -->


<!-- ## 6) Check that the fairgraph import works -->

<!-- [...] -->

<!-- maybe build the properties of the classes wrt the "field" entries of the KGE generated queries -->

