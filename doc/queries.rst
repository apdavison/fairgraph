============================
Querying the Knowledge Graph
============================

Setting up a connection
=======================

Communication between fairgraph metadata objects and the Knowledge Graph web service is through
a client object, for which an access token associated with an HBP Identity account is needed.
To obtain an HBP Identity account, please see https://services.humanbrainproject.eu/oidc/account/request.

If you are working in an HBP Collaboratory Jupyter notebook, you have already logged in with your
user name and password, so you can get an access token as follows::

   from jupyter_collab_storage import oauth_token_handler
   token = oauth_token_handler.get_token()


If working outside the Collaboratory, you can obtain a token
from https://nexus-iam.humanbrainproject.org/v0/oauth2/authorize
We suggest you then save it as an environment variable, e.g. at a shell prompt::

   export HBP_AUTH_TOKEN=eyJhbGci...nPq

and then in Python::

   token = os.environ['HBP_AUTH_TOKEN']


Once you have a token::

   from fairgraph import KGClient

   client = KGClient(token)


Listing the available metadata types
====================================

Each type of metadata node in the Knowledge Graph is represented by a Python class.
These classes are organized into modules according to the domain, e.g. "electrophysiology"
or "brainsimulation". For a full list of domains, see :doc:`modules`.

To get a list of classes in a given module, import the module and then run
:func:`list_kg_classes()`, e.g.::

    >>> from fairgraph import electrophysiology

    >>> electrophysiology.list_kg_classes()
    [fairgraph.electrophysiology.BrainSlicingActivity,
     fairgraph.electrophysiology.IntraCellularSharpElectrodeExperiment,
     fairgraph.electrophysiology.IntraCellularSharpElectrodeRecordedCell,
     fairgraph.electrophysiology.IntraCellularSharpElectrodeRecordedCellCollection,
     fairgraph.electrophysiology.IntraCellularSharpElectrodeRecordedSlice,
     fairgraph.electrophysiology.IntraCellularSharpElectrodeRecording,
     fairgraph.electrophysiology.MultiChannelMultiTrialRecording,
     fairgraph.electrophysiology.PatchClampActivity,
     fairgraph.electrophysiology.PatchClampExperiment,
     fairgraph.electrophysiology.PatchedCell,
     fairgraph.electrophysiology.PatchedCellCollection,
     fairgraph.electrophysiology.PatchedSlice,
     fairgraph.electrophysiology.QualifiedMultiTraceGeneration,
     fairgraph.electrophysiology.QualifiedTraceGeneration,
     fairgraph.electrophysiology.Slice,
     fairgraph.electrophysiology.StepCurrentStimulus,
     fairgraph.electrophysiology.Trace]


Listing all metadata nodes of a given type
==========================================

To obtain a list of all the metadata nodes of a given type, import the associated class and use
the :meth:`list()` method, passing the `client` object you created previously,
e.g. to get a list of patched cells::

    from fairgraph.electrophysiology import PatchedCell

    cells = PatchedCell.list(client)

By default, this gives you the first 100 results.
You can change the number of results retrieved and the starting point, e.g. ::

    cells = PatchedCell.list(client, from_index=50, size=50)

This returns 50 nodes starting with the 50th. To see how many nodes there are in total::

    PatchedCell.count(client)

.. note:: if you consistently retrieve an empty list, it is probably because you do not
          yet have the necessary permissions. See :doc:`permissions` for more information.


Filtering/searching
===================

To obtain only metadata nodes that have certain properties, you can filter the list of nodes.
For example, to see only patched cells from the CA1 region of the hippocampus in the mouse::

    from fairgraph.commons import BrainRegion, Species

    hippocampus_cells = PatchedCell.list(client,
                                         brain_region=BrainRegion("hippocampus CA1"),
                                         species=Species("Mus musculus"))

.. warning:: the filtering system is currently primitive, and unaware of hierarchies, e.g.
             filtering by "hippocampus" **will not** return cells with the brain region set to
             "hippocampus CA1". This is on our list of things to fix soon!
             To see a list of possible search terms, use the :meth:`terms()` method,
             e.g. ``BrainRegion.terms()``, ``Species.terms()``


Retrieving a specific node based on its name or id
==================================================

If you know the name or unique id of a node in the KnowledgeGraph, you can retrieve it directly::

    cell_of_interest = PatchedCell.by_name('hbp00011_Sub3_Samp2__ExpE10', client)
    cell_of_interest = PatchedCell.from_id("8512c3a3-eee3-4c64-acbf-850ab0bd42ee", client)


Viewing metadata and connections
================================

Once you have retrieved a node of interest, the associated metadata are available as attributes of the
Python object, e.g.::

    >>> cell_of_interest.id
    'https://nexus.humanbrainproject.org/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/8512c3a3-eee3-4c64-acbf-850ab0bd42ee'

    >>> cell_of_interest.uuid
    '8512c3a3-eee3-4c64-acbf-850ab0bd42ee'

    >>> cell_of_interest.brain_location
    BrainRegion('hippocampus CA1', 'http://purl.obolibrary.org/obo/UBERON_0003881')

    >>> cell_of_interest.cell_type
    CellType('hippocampus CA1 pyramidal cell', 'http://uri.neuinfo.org/nif/nifstd/sao830368389')

Connections between graph nodes are also available as attributes::

    >>> cell_of_interest.collection
    KGQuery([<class 'fairgraph.electrophysiology.PatchedCellCollection'>], {'path': 'prov:hadMember', 'op': 'eq', 'value': 'https://nexus.humanbrainproject.org/v0/data/neuralactivity/experiment/patchedcell/v0.1.0/8512c3a3-eee3-4c64-acbf-850ab0bd42ee'})

By default, for performance reasons, connections are not followed, and instead you will see either
a :class:`KGQuery` or :class:`KGProxy` object. In both these cases, follow the connection using the
:meth:`resolve()` method, e.g.::

    >>> cell_collection = cell_of_interest.collection.resolve(client)

    >>> patched_slice = cell_collection.slice.resolve(client)

    >>> original_slice = patched_slice.slice.resolve(client)

    >>> subject = original_slice.subject.resolve(client)

    >>> subject.name
    'hbp00011_Sub3'

    >>> subject.species
    Species('Mus musculus', 'http://purl.obolibrary.org/obo/NCBITaxon_10090')

    >>> subject.sex
    Sex('female', 'schema:Female')

    >>> subject.age
    Age(QuantitativeValue(3.0 'months'), 'Post-natal')

This could be chained together in a single line!

::

    >>> subject = cell_of_interest.collection.resolve(client).slice.resolve(client).slice.resolve(client).subject.resolve(client)

.. note:: It is rather cumbersome to have to follow all these connections manually.
          In the near future, you will be able to ask fairgraph to resolve the connections for you,
          although with the risk of poor performance if your node of interest is indirectly
          connected to many other nodes in the graph.

Strict mode
===========

fairgraph is quite strict about which metadata attributes and data types are expected,
somewhat stricter than the Knowledge Graph itself.
If you find that certain queries produce errors, you can relax this strict checking for
a given node type as follows::

    PatchedCell.set_strict_mode(False)
