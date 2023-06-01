.. fairgraph documentation master file, created by
   sphinx-quickstart on Tue Oct 29 17:04:38 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================================================
fairgraph: a Python API for the EBRAINS Knowledge Graph
=======================================================

**fairgraph** is a Python library for working with metadata
in the EBRAINS Knowledge Graph, with a particular focus on data reuse,
although it is also useful in metadata registration/curation.
The API is not stable, and is subject to change.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   knowledgegraph
   queries
   creatingupdating
   modules
   permissions
   api_reference
   contributing
   gettinghelp
   authors
   release_notes

Quickstart
==========

Installation
------------

To get the latest release::

   pip install fairgraph

To get the development version::

   git clone https://github.com/HumanBrainProject/fairgraph.git
   pip install -U ./fairgraph


Basic setup
-----------

The basic idea of the library is to represent metadata nodes from the Knowledge Graph as Python objects.
Communication with the Knowledge Graph service is through a client object,
for which an access token associated with an EBRAINS account is needed.

If you are working in a Collaboratory Jupyter notebook, the client will take its access token from the notebook automatically::

   >>> from fairgraph import KGClient

   >>> client = KGClient(host="core.kg.ebrains.eu")

If working outside the Collaboratory, you will need to obtain a token
(for example from the KG Editor if you are a curator, or using `clb_oauth.get_token()` in a Collaboratory Jupyter notebook)
and save it as an environment variable, e.g. at a shell prompt::

   export KG_AUTH_TOKEN=eyJhbGci...nPq

and then in Python::

   >>> token = os.environ['KG_AUTH_TOKEN']

Once you have a token::

   >>> from fairgraph import KGClient

   >>> client = KGClient(token)


Retrieving metadata from the Knowledge Graph
--------------------------------------------

The different metadata/data types available in the Knowledge Graph are grouped into modules
within the `openminds` module.
For example::

   >>> from fairgraph.openminds.core import DatasetVersion

Using these classes, it is possible to list all metadata matching a particular criterion, e.g.::

   >>> datasets = DatasetVersion.list(client, from_index=10, size=10)

If you know the unique identifier of an object, you can retrieve it directly::

   >>> dataset_of_interest = DatasetVersion.from_id("17196b79-04db-4ea4-bb69-d20aab6f1d62", client)
   >>> dataset_of_interest.show()
   id                         https://kg.ebrains.eu/api/instances/17196b79-04db-4ea4-bb69-d20aab6f1d62
   authors                    [KGProxy((<class 'fairgraph.openminds.core.actors.organization.Organization'>, <class 'fairgraph.openminds.core.actors.person.Person'>), 'https://kg.ebrains.eu/api/instances/56f86f58-add6-4684-aaf1-91083e1165e9'), KGProxy((<class 'fairgraph.openminds.core.actors.organization.Organization'>, <class 'fairgraph.openminds.core.actors.person.Person'>), 'https://kg.ebrains.eu/api/instances/3b0ceb13-5bcc-4f1d-8ddb-bd888a85b9c0'), KGProxy((<class 'fairgraph.openminds.core.actors.organization.Organization'>, <class 'fairgraph.openminds.core.actors.person.Person'>), 'https://kg.ebrains.eu/api/instances/6e3edece-60bc-4a4a-8399-45b1ee597d71')]
   behavioral_protocols       None
   digital_identifier         KGProxy([<class 'fairgraph.openminds.core.miscellaneous.doi.DOI'>], 'https://kg.ebrains.eu/api/instances/c03106e1-1f30-446b-8439-ce77fc8358d6')
   ethics_assessment          KGProxy([<class 'fairgraph.openminds.controlledterms.ethics_assessment.EthicsAssessment'>], 'https://kg.ebrains.eu/api/instances/a217a2f8-dcb8-4ca9-9923-517af2aebc5b')
   experimental_approachs     None
   input_data                 None
   is_alternative_version_of  None
   is_new_version_of          None
   license                    KGProxy([<class 'fairgraph.openminds.core.data.license.License'>], 'https://kg.ebrains.eu/api/instances/6ebce971-7f99-4fbc-9621-eeae47a70d85')
   preparation_designs        None
   studied_specimens          [KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/0ca86a6e-6fa0-4840-b62a-994170a9b6d4'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/3907e145-d2d1-42c7-8a05-a58e3dbf326f'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/f1336642-27a5-4e4f-a6f1-979610bd853d'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/a6e2336a-ba1b-4504-b69a-ef12002b2ed4'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/0d54e778-0a6a-4f90-9555-218643dd65a9'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/2675865a-5f7e-4d5f-bc86-c4b8dbd47d58'), KGProxy((<class 'fairgraph.openminds.core.research.subject.Subject'>, <class 'fairgraph.openminds.core.research.subject_group.SubjectGroup'>, <class 'fairgraph.openminds.core.research.tissue_sample.TissueSample'>, <class 'fairgraph.openminds.core.research.tissue_sample_collection.TissueSampleCollection'>), 'https://kg.ebrains.eu/api/instances/94664b6e-8979-4cf6-b358-ff04056a4754')]
   techniques                 None
   data_types                 None
   study_targets              None
   accessibility              KGProxy([<class 'fairgraph.openminds.controlledterms.product_accessibility.ProductAccessibility'>], 'https://kg.ebrains.eu/api/instances/b2ff7a47-b349-48d7-8ce4-cf51868675f1')
   copyright                  None
   custodians                 KGProxy((<class 'fairgraph.openminds.core.actors.organization.Organization'>, <class 'fairgraph.openminds.core.actors.person.Person'>), 'https://kg.ebrains.eu/api/instances/762bd286-9d46-4ac5-889f-63b08d33c895')
   description                The Golgi cells, together with granule cells and mossy fibers, form a neuronal microcircuit regulating information transfer at the cerebellum input stage. In order to further investigate the Golgi cells properties and their excitatory synapses, whole-cell patch-clamp recordings were performed on acute parasagittal cerebellar slices obtained from juvenile GlyT2-GFP mice (p16-p21). Passive Golgi cells parameters were extracted in voltage-clamp mode by analyzing current relaxation induced by step voltage changes (IV protocol). Excitatory synaptic transmission properties were investigated by electrical stimulation of the mossy fibers bundle (5 pulses at 50 Hz, EPSC protocol, voltage-clamp mode.
   full_documentation         KGProxy((<class 'fairgraph.openminds.core.miscellaneous.doi.DOI'>, <class 'fairgraph.openminds.core.data.file.File'>, <class 'fairgraph.openminds.core.miscellaneous.url.URL'>), 'https://kg.ebrains.eu/api/instances/d6cd3981-cdb1-460c-a4e4-29458fe0a47f')
   name                       Whole cell patch-clamp recordings of cerebellar Golgi cells
   funding                    None
   homepage                   None
   how_to_cite                None
   keywords                   None
   other_contributions        None
   related_publications       [KGProxy((<class 'fairgraph.openminds.core.miscellaneous.doi.DOI'>, <class 'fairgraph.openminds.core.miscellaneous.isbn.ISBN'>), 'https://kg.ebrains.eu/api/instances/477b3e5d-5903-4a68-84b3-d29e38214ca8'), KGProxy((<class 'fairgraph.openminds.core.miscellaneous.doi.DOI'>, <class 'fairgraph.openminds.core.miscellaneous.isbn.ISBN'>), 'https://kg.ebrains.eu/api/instances/9f1ec274-329a-4a9b-802a-abd301614c2c')]
   release_date               None
   repository                 KGProxy([<class 'fairgraph.openminds.core.data.file_repository.FileRepository'>], 'https://kg.ebrains.eu/api/instances/80e2ca84-b9fa-43b7-b21a-b5f99d89f051')
   alias                      Whole cell patch-clamp recordings of cerebellar Golgi cells
   support_channels           None
   version_identifier         None
   version_innovation         None

Links between metadata in the Knowledge Graph are not followed automatically,
to avoid unnecessary network traffic, but can be followed with the :meth:`resolve()` method::

   >>> dataset_license = dataset_of_interest.license.resolve(client)
   >>> dataset_license.show()
   id          https://kg.ebrains.eu/api/instances/6ebce971-7f99-4fbc-9621-eeae47a70d85
   name        Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
   legal_code  https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
   alias       CC BY-NC-SA 4.0
   webpages    ['https://creativecommons.org/licenses/by-nc-sa/4.0', 'https://spdx.org/licenses/CC-BY-NC-SA-4.0.html']

The associated metadata are accessible as attributes of the Python objects, e.g.::

   >>> print(dataset_of_interest.description)
   The Golgi cells, together with granule cells and mossy fibers, form a neuronal microcircuit
   regulating information transfer at the cerebellum input stage. In order to further investigate
   the Golgi cells properties and their excitatory synapses, whole-cell patch-clamp recordings
   were performed on acute parasagittal cerebellar slices obtained from juvenile GlyT2-GFP mice
   (p16-p21). Passive Golgi cells parameters were extracted in voltage-clamp mode by analyzing
   current relaxation induced by step voltage changes (IV protocol). Excitatory synaptic
   transmission properties were investigated by electrical stimulation of the mossy fibers bundle
   (5 pulses at 50 Hz, EPSC protocol, voltage-clamp mode.

You can also download any associated data::

   >>> dataset.download(client, "local_directory")


Filters
-------

The :meth:`list()` method also allows you to filter the list of metadata objects based on their properties.
For example, to filter by words in a dataset name::

   >>> patch_clamp_datasets = DatasetVersion.list(client, name="patch")
   >>> for ds in patch_clamp_datasets:
   ...     print(ds.name)
   ...
   Patch-clamp electrophysiological characterization of neurons in human dentate gyrus
   Whole cell patch-clamp recordings of cerebellar basket cells
   Whole cell patch-clamp recordings of cerebellar Golgi cells
   Whole cell patch-clamp recordings of cerebellar granule cells
   Whole cell patch-clamp recordings of cerebellar stellate cells

To filter by species, we first need to retrieve the species metadata::

   >>> from fairgraph.openminds.controlledterms import Species
   >>> rat = Species.by_name("Rattus norvegicus", client)

We can then use this as a filter::

   >>> rat_datasets = DatasetVersion.list(client, study_targets=rat)

To see a list of the fields that can be used for filtering::

   >>> DatasetVersion.field_names
   ['authors', 'behavioral_protocols', 'digital_identifier', 'ethics_assessment',
    'experimental_approachs', 'input_data', 'is_alternative_version_of', 'is_new_version_of',
    'license', 'preparation_designs', 'studied_specimens', 'techniques', 'data_types',
    'study_targets', 'accessibility', 'copyright', 'custodians', 'description',
    'full_documentation', 'name', 'funding', 'homepage', 'how_to_cite', 'keywords',
    'other_contributions', 'related_publications', 'release_date', 'repository', 'alias',
    'support_channels', 'version_identifier', 'version_innovation']


Storing and editing metadata
----------------------------

For those users who have the necessary permissions to store and edit metadata in the Knowledge Graph,
**fairgraph** objects can be created or edited in Python, and then saved back to the Knowledge Graph, e.g.::

   from fairgraph.openminds.core import Person, Organization, Affiliation

   >>> mgm = Organization(name="Metro-Goldwyn-Mayer", alias="MGM")
   >>> mgm.save(client, space="myspace")
   >>> author = Person(family_name="Laurel", given_name="Stan",
   ...                 affiliations=Affiliation(organization=mgm))
   >>> author.save(client, space="myspace")


Getting help
------------

In case of questions about **fairgraph**, please e-mail support@ebrains.eu.
If you find a bug or would like to suggest an enhancement or new feature,
please open a ticket in the `issue tracker`_.

Acknowledgements
----------------

.. image:: https://www.braincouncil.eu/wp-content/uploads/2018/11/wsi-imageoptim-EU-Logo.jpg
   :alt: EU Logo
   :height: 100 px
   :align: right

This open source software code was developed in part or in whole in the Human Brain Project,
funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation
under Specific Grant Agreements No. 720270, No. 785907 and No. 945539
(Human Brain Project SGA1, SGA2 and SGA3).


.. _`issue tracker`: https://github.com/HumanBrainProject/fairgraph/issues