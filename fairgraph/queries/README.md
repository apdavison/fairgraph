# Using the Knowledge graph Editor to build queries and namespace properties within fairgraph

We use the features of the Knowledge Graph Editor to build the queries and the namespace properties (e.g. its classes) within fairgraph.

- "Namespaces" refer to the different root schema considered: minds, uniminds, neuralactivity 
- "Classes" refer to the different entries of a given namespace: e.g. for the minds schema: "Dataset", "Person", ...

## 1) Build a general query with the KG editor for a given Namespace and a given Class of interest

Let's build a general query for the case of the "Minds" namespace for the "Dataset" class.

Within the !(Knowledge Graph editor)[https://kg.humanbrainproject.org/editor/query-builder], we select the !(query-builder)[https://kg.humanbrainproject.org/editor/query-builder].

We scroll over the root schema to find the "Minds" namepsace, and then we select the "Dataset" class within the "Minds" namespace.

![Screenshot of the KGE](doc/KGE-screenshot-1.png)

Then we add all "Attributes" of the class to the 

![Screenshot of the KGE](doc/KGE-screenshot-2.png)

In "Results JSON view", set the size to a large value (e.g. size=20000)

Then we save the query using the following format:
"fg-Namespace-Class-KGE"

![Screenshot of the KGE](doc/KGE-screenshot-3.png)

## 2) Repeat for all Namespaces and Classes of interest

## 3) Run the script to convert the KGE queries into fairgraph compatible queries

## 4) Checking that 

## 5) Try it out
