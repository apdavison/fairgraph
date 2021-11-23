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

   token = clb_oauth.get_token()


If working outside the Collaboratory, we recommend you obtain a token from whichever authentication endpoint
is available to you, and save it as an environment variable so the client can find it, e.g. at a shell prompt::

   export KG_AUTH_TOKEN=eyJhbGci...nPq


You can then create the client object::

   >>> from fairgraph.client_v3 import KGv3Client as KGClient
   >>> client = KGClient()

You can also pass the token explicitly to the client::

   >>> client = KGClient(token)


Listing the available metadata types
====================================

Each type of metadata node in the Knowledge Graph is represented by a Python class.
These classes are organized into modules according to the openMINDS schemas.
For a full list of modules, see :doc:`modules`.

To get a list of classes in a given module, import the module and then run
:func:`list_kg_classes()`, e.g.::

    >>> import fairgraph.openminds.core as omcore

    >>> omcore.list_kg_classes()
    [fairgraph.openminds.core.research.behavioral_protocol.BehavioralProtocol,
    fairgraph.openminds.core.actors.contact_information.ContactInformation,
    fairgraph.openminds.core.data.content_type.ContentType,
    fairgraph.openminds.core.miscellaneous.doi.DOI,
    fairgraph.openminds.core.products.dataset.Dataset,
    fairgraph.openminds.core.products.dataset_version.DatasetVersion,
    fairgraph.openminds.core.data.file.File,
    fairgraph.openminds.core.data.file_bundle.FileBundle,
    fairgraph.openminds.core.data.file_repository.FileRepository,
    fairgraph.openminds.core.data.file_repository_structure.FileRepositoryStructure,
    fairgraph.openminds.core.miscellaneous.funding.Funding,
    fairgraph.openminds.core.miscellaneous.gridid.GRIDID,
    fairgraph.openminds.core.miscellaneous.isbn.ISBN,
    fairgraph.openminds.core.data.license.License,
    fairgraph.openminds.core.products.meta_data_model.MetaDataModel,
    fairgraph.openminds.core.products.meta_data_model_version.MetaDataModelVersion,
    fairgraph.openminds.core.products.model.Model,
    fairgraph.openminds.core.products.model_version.ModelVersion,
    fairgraph.openminds.core.miscellaneous.orcid.ORCID,
    fairgraph.openminds.core.actors.organization.Organization,
    fairgraph.openminds.core.actors.person.Person,
    fairgraph.openminds.core.products.project.Project,
    fairgraph.openminds.core.research.protocol.Protocol,
    fairgraph.openminds.core.research.protocol_execution.ProtocolExecution,
    fairgraph.openminds.core.miscellaneous.rorid.RORID,
    fairgraph.openminds.core.miscellaneous.swhid.SWHID,
    fairgraph.openminds.core.data.service_link.ServiceLink,
    fairgraph.openminds.core.products.software.Software,
    fairgraph.openminds.core.products.software_version.SoftwareVersion,
    fairgraph.openminds.core.research.stimulation.Stimulation,
    fairgraph.openminds.core.research.subject.Subject,
    fairgraph.openminds.core.research.subject_group.SubjectGroup,
    fairgraph.openminds.core.research.subject_group_state.SubjectGroupState,
    fairgraph.openminds.core.research.subject_state.SubjectState,
    fairgraph.openminds.core.research.tissue_sample.TissueSample,
    fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection,
    fairgraph.openminds.core.research.tissue_sample_collection_state.TissueSampleCollectionState,
    fairgraph.openminds.core.research.tissue_sample_state.TissueSampleState,
    fairgraph.openminds.core.miscellaneous.url.URL]


Listing all metadata nodes of a given type
==========================================

To obtain a list of all the metadata nodes of a given type, import the associated class and use
the :meth:`list()` method, passing the `client` object you created previously,
e.g. to get a list of patched cells::

    from fairgraph.openminds.core import License

    licenses = License.list(client)

By default, this gives you the first 100 results.
You can change the number of results retrieved and the starting point, e.g. ::

    licenses = License.list(client, from_index=15, size=10)

This returns 10 nodes starting with the 15th. To see how many nodes there are in total::

    License.count(client)

.. note:: if you consistently retrieve an empty list, it is probably because you do not
          yet have the necessary permissions. See :doc:`permissions` for more information.


Filtering/searching
===================

To obtain only metadata nodes that have certain properties, you can filter the list of nodes.
For example, to see only datasets whose name contain the phrase 'patch-clamp'::

    from fairgraph.openminds.core import DatasetVersion

    datasets = DatasetVersion.list(client, name="patch-clamp")

.. warning:: the filtering system is currently primitive, and unaware of hierarchies, e.g.
             filtering by "hippocampus" **will not** return cells with the brain region set to
             "hippocampus CA1". This is on our list of things to fix soon!
             To see a list of possible search terms, use the :meth:`fields` attribute,
             e.g. ``DatasetVersion.fields``.


Retrieving a specific node based on its name or id
==================================================

If you know the name or unique id of a node in the KnowledgeGraph, you can retrieve it directly::

    dataset_of_interest = DatasetVersion.by_name('Whole cell patch-clamp recordings of cerebellar Golgi cells', client)
    dataset_of_interest = DatasetVersion.from_id('17196b79-04db-4ea4-bb69-d20aab6f1d62', client)


Viewing metadata and connections
================================

Once you have retrieved a node of interest, the associated metadata are available as attributes of the
Python object, e.g.::

    >>> dataset_of_interest.id
    'https://kg.ebrains.eu/api/instances/17196b79-04db-4ea4-bb69-d20aab6f1d62'

    >>> dataset_of_interest.uuid
    '17196b79-04db-4ea4-bb69-d20aab6f1d62'

    >>> dataset_of_interest.description[:100] + "..."
    'The Golgi cells, together with granule cells and mossy fibers, form a neuronal microcircuit regulati...'

Connections between graph nodes are also available as attributes::

    >>> dataset_of_interest.license
    KGProxyV3([<class 'fairgraph.openminds.core.data.license.License'>], 'https://kg.ebrains.eu/api/instances/6ebce971-7f99-4fbc-9621-eeae47a70d85')

By default, for performance reasons, connections are not followed, and instead you will see either
a :class:`KGQuery` or :class:`KGProxy` object. In both these cases, follow the connection using the
:meth:`resolve()` method, e.g.::

    >>> license = dataset_of_interest.license.resolve(client)

    >>> license.name
    'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International'


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

    DatasetVersion.set_strict_mode(False)
