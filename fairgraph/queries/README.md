# Using the Knowledge graph Editor to build queries and namespace properties within fairgraph

We use the features of the [HBP Knowledge Graph editor](https://kg.humanbrainproject.org/editor) to build the queries and the namespace properties (e.g. its classes) within fairgraph.

Vocabulary:

- "Namespaces" refer to the different root schema considered: "Minds", "Uniminds", "Neuralactivity", ... They are associated to a given "Version".
- "Classes" refer to the different schemas of a given namespace: e.g. for the minds schema: "Dataset", "Person", ...
 - "Attributes" are the properties of the entries of a given class. E.g. a Dataset has the attributes: "name", "contributors", "identifier", ...
 
All those objects need to be included into "faigraph". We detail here the procedure 

 
## 1) Build a general query with the KG editor for a given Namespace and a given Class of interest

Let's build a general query for the case of the "Minds" namespace for the "Dataset" class.

Within the [Knowledge Graph editor](https://kg.humanbrainproject.org/editor), we select the [query-builder](https://kg.humanbrainproject.org/editor/query-builder).

We scroll over the root schema to find the "Minds" namepsace, and then we select the "Dataset" class within the "Minds" namespace.

![Screenshot of the KGE](doc/KGE-screenshot-1.png)

Then we add all "Attributes" of the class to the 

![Screenshot of the KGE](doc/KGE-screenshot-2.png)

In "Results JSON view", set the size to a large value (e.g. size=20000)

Then we save the query using the following format:
"fg-Namespace-Class-KGE", e.g. for that example

![Screenshot of the KGE](doc/KGE-screenshot-3.png)

The stored query should therefore appear in the following address:

https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-Minds-Dataset-KGE

## 2) Repeat for all Namespaces and Classes of interest

Here are a few example combinations:

1. Minds-Activity
2. Uniminds-Project
3. Uniminds-Person
4. ...

## 3) Configure the KG Objects handled by fairgraph

Open the [config.py](./config.py) file and write down all the Namespaces (with their version) and Classes that you have saved as a query in the KGE editor.

here is an example:
```
KG_OBJECTS = [
    {
        'namespace':'Minds',
        'version':'v1.0.0',
        'classes':[
            'Activity',
            'Dataset',
        ]
 	},
]
```


## 4) Add a set of queries

Adding a set of common queries (queries that are unspecific to a namespace and a class, i.e. where the attributes are shared among all objects). For example the "name" and "id " are always present. 

```
# this query will be applid to all classes of all namepsaces:
COMMON_QUERIES = [
    {'query_name': 'name_contains_id_equals',
     'quantities':['name', '@id'],
     'operators':['contains', 'equals'],
     'parameters':['name', 'id']}
    {'query_name': 'name_contains',
     'quantities':['name'],
     'operators':['contains'],
     'parameters':['name']}
]
```

Now you can also set explicitely a set of custom queries that will be "Namespace" and "class"-dependent (because it focuses on class-specific attributes). 

```
CUSTOM_QUERIES = {
    'Minds-Dataset':[
        {'query_name': contributors_contains', # explicit name of the query
         'quantities':['contributors], # quantities that will have the filter
         'operators':['contains'], # operator for the filter
         'parameters':['contributors]}, # parameter (usually same than quantity)
        {'query_name': 'name_contains_id_equals',
         'quantities':['name', '@id'],
         'operators':['contains', 'equals'],
         'parameters':['name', 'id']},
    ]
    'Uniminds-Project':[
        {'query_name': contributors_contains', # explicit name of the query
         'quantities':['contributors], # quantities that will have the filter
         'operators':['contains'], # operator for the filter
         'parameters':['contributors]}, # parameter (usually same than quantity)
    ]
}
```

## 5) Run the script to convert the KGE queries into "fairgraph-compatible" queries

Provided you have write access in you HBP account and the appropriate token (see ![fairgraph manual](../README.md)), Using the `requests` library and pro

run it with:

```
python process_config_file.py 
```

The fairgraph-compatible query should now appear in:

https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-Minds-Dataset

https://kg.humanbrainproject.org/query/minds/core/activity/v1.0.0/fg-Activity


## 6) Check that the fairgraph import works
