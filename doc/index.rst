.. fairgraph documentation master file, created by
   sphinx-quickstart on Tue Oct 29 17:04:38 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================================================
fairgraph: a Python API for the EBRAINS Knowledge Graph
=======================================================

**fairgraph** is an experimental Python library for working with metadata
in the HBP/EBRAINS Knowledge Graph, with a particular focus on data reuse,
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
   contributing
   gettinghelp
   authors

Quickstart
==========

Installation
------------

To get the latest release::

   pip install fairgraph


To get the development version::

   git clone https://github.com/HumanBrainProject/fairgraph.git
   pip install -r ./fairgraph/requirements.txt
   pip install -U ./fairgraph


Basic setup
-----------

The basic idea of the library is to represent metadata nodes from the Knowledge Graph as Python objects.
Communication with the Knowledge Graph service is through a client object,
for which an access token associated with an EBRAINS account is needed.

If you are working in a Collaboratory Jupyter notebook, the client will take its access token from the notebook automatically::

   from fairgraph import KGClient

   client = KGClient()

If working outside the Collaboratory, you will need to obtain a token
(for example from the KG Editor if you are a curator, or using `clb_oauth.get_token()` in a Collaboratory Jupyter notebook)
and save it as an environment variable, e.g. at a shell prompt::

   export KG_AUTH_TOKEN=eyJhbGci...nPq

and then in Python::

   token = os.environ['KG_AUTH_TOKEN']

Once you have a token::

   from fairgraph import KGClient

   client = KGClient(token)


Retrieving metadata from the Knowledge Graph
--------------------------------------------

The different metadata/data types available in the Knowledge Graph are grouped into modules
within the `openminds` module.
For example::

   from fairgraph.openminds.core import DatasetVersion

Using these classes, it is possible to list all metadata matching a particular criterion, e.g.::

   datasets = DatasetVersion.list(client, from_index=10, size=10)

If you know the unique identifier of an object, you can retrieve it directly::

   dataset_of_interest = Dataset.from_id("153ec151-b1ae-417b-96b5-4ce9950a3c56", client)
   dataset_of_interest.show()

Links between metadata in the Knowledge Graph are not followed automatically,
to avoid unnecessary network traffic, but can be followed with the `resolve()` method::

   dataset_license = dataset_of_interest.license.resolve(client)

The associated metadata are accessible as attributes of the Python objects, e.g.::

   print(dataset_of_interest.description)

You can also access any associated data::

   print(dataset.files)
   dataset.download(dataset.files[0])


Advanced queries
----------------

While certain filters and queries are built in (such as the filter by brain region, above),
more complex queries are possible using the Nexus query API.

::

   from fairgraph.base import KGQuery
   from fairgraph.minds import Dataset

   query = {
      "path": "minds:specimen_group / minds:subjects / minds:samples / minds:methods / schema:name",
      "op": "in",
      "value": ["Electrophysiology recording",
               "Voltage clamp recording",
               "Single electrode recording",
               "functional magnetic resonance imaging"]
   }
   context = {
               "schema": "http://schema.org/",
               "minds": "https://schema.hbp.eu/minds/"
   }

   activity_datasets = KGQuery(Dataset, query, context).resolve(client)
   for dataset in activity_datasets:
      print("* " + dataset.name)


Storing and editing metadata
----------------------------

For those users who have the necessary permissions to store and edit metadata in the Knowledge Graph,
**fairgraph** objects can be created or edited in Python, and then saved back to the Knowledge Graph, e.g.::

   from fairgraph.core import Person, Organization, use_namespace
   from fairgraph.commons import Address

   use_namespace("neuralactivity")

   mgm = Organization("Metro-Goldwyn-Mayer")
   mgm.save(client)
   author = Person("Laurel", "Stan", "laurel@example.com", affiliation=mgm)
   author.save(client)

::

   mgm.address = Address(locality='Hollywood', country='United States')
   mgm.save(client)


Getting help
------------

In case of questions about **fairgraph**, please e-mail support@humanbrainproject.eu.
If you find a bug or would like to suggest an enhancement or new feature,
please open a ticket in the `issue tracker`_.

Acknowledgements
----------------

.. image:: https://www.braincouncil.eu/wp-content/uploads/2018/11/wsi-imageoptim-EU-Logo.jpg
   :alt: EU Logo
   :height: 100 px
   :align: right

This open source software code was developed in part or in whole in the Human Brain Project, funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreements No. 720270 and No. 785907 (Human Brain Project SGA1 and SGA2).


.. _`issue tracker`: https://github.com/HumanBrainProject/fairgraph/issues