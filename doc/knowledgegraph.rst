=========================
About the Knowledge Graph
=========================

The EBRAINS Knowledge Graph is a metadata store for neuroscience.

When sharing neuroscience data, it is essential to also share all of the context and background
information needed to interpret and understand the data:
the age of the subject, the sampling rate of the recording system, etc.
For the EBRAINS data sharing platform, the actual data files are stored at various European
HPC Centres. All of the metadata associated with these files (including the
precise file locations) are stored in the Knowledge Graph.

There are many ways to access the contents of the Knowledge Graph: through a
`graphical search interface`_, with an anatomical search through the EBRAINS brain atlases_,
through web services, and through Python clients.

**fairgraph** is a high-level Python client for the Knowledge Graph, which aims to
be convenient, powerful and easy-to-use.
Alternative ways to access the Knowledge Graph programmatically are summarized in the section
"Alternatives" below.


Structure
=========

The EBRAINS Knowledge Graph is a semantic graph database (in the sense of `graph theory`_).
It consists of "nodes", each of which contains metadata about a specific aspect of a neuroscience
experiment. These nodes are connected to each other, and the connections represent the
relationships between the different pieces of metadata (for example, a node representing a
slice of rat hippocampus will be connected to other nodes representing each of the neurons
in that slice that was recorded from with an electrode, or reconstructed from microscopy images).
The connections between nodes are of many different types, so that we can represent precisely
the meaning of the connection, the type of the relationship
(this is why we call it a _semantic_ graph).
This graph structure gives great flexibility and ease of evolution compared to a traditional
database.

.. todo:: insert a figure here showing a part of the graph

**fairgraph** maps the Knowledge Graph onto connected Python objects.
For example, a node in the graph containing metadata about a neuron whose activity was
recorded using patch-clamp electrophysiology is represented by a Python object
:class:`~fairgraph.openminds.core.TissueSample`, whose :attr:`type` property is a link to
a :class:`~fairgraph.openminds.controlled_terms.TissueSampleType`
object with name "single cell", and which is the :attr:`output` of a
:class:`~fairgraph.openminds.ephys.RecordingActivity` node.

The types (classes) and properties (attributes) of the Python objects are defined by the
openMINDS_ schemas.


Alternatives
------------

For more information about developer access to the KG, see https://kg.ebrains.eu/develop.html.



.. _`graphical search interface`: https://search.kg.ebrains.eu
.. _`atlases`: https://ebrains.eu/services/atlases/
.. _`graph theory`: https://en.wikipedia.org/wiki/Graph_theory
.. _openMINDS: https://openminds.docs.om-i.org
