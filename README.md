# fairgraph: a Python API for the Human Brain Project Knowledge Graph.

Authors: Andrew P. Davison, Onur Ates, Nico Feld, Yann Zerlaut, Glynis Mattheisen

Copyright CNRS 2019-2022

**fairgraph** is an experimental Python library for working with metadata
in the EBRAINS Knowledge Graph, with a particular focus on data reuse,
although it is also useful in metadata registration/curation.
The API is not stable, and is subject to change.

## Installation

To get the latest release:

```
pip install https://github.com/HumanBrainProject/kg-core-python/archive/refs/heads/master.zip
pip install fairgraph
```

To get the development version:

```
git clone https://github.com/HumanBrainProject/fairgraph.git
pip install -r ./fairgraph/requirements.txt
pip install -U ./fairgraph
```

## Knowledge Graph versions

This version of fairgraph supports both version 2 and version 3 of the EBRAINS Knowledge Graph (KG).
Once all metadata and applications have been migrated to version 3, the version 2 features
will be removed. Unless otherwise specified, all documentation refers to accessing KG version 3.


## Basic setup

The basic idea of the library is to represent metadata nodes from the Knowledge Graph as Python objects.
Communication with the Knowledge Graph service is through a client object,
for which an access token associated with an EBRAINS account is needed.

If you are working in a Collaboratory Jupyter notebook, the client will find your token automatically.

If working outside the Collaboratory, we recommend you obtain a token from whichever authentication endpoint
is available to you, and save it as an environment variable so the client can find it, e.g. at a shell prompt:

```
export KG_AUTH_TOKEN=eyJhbGci...nPq
```

You can then create the client object:

```
>>> from fairgraph import KGClient

>>> client = KGClient()
```

You can also pass the token explicitly to the client:

```
>>> client = KGClient(token)
```


## Retrieving metadata from the Knowledge Graph

The Knowledge Graph uses [openMINDS](https://github.com/HumanBrainProject/openMINDS) schemas.
Each openMINDS schema corresponds to a Python class, which are grouped into modules
following the openMINDS structure. For example:

```
>>> from fairgraph.openminds.core import DatasetVersion
>>> from fairgraph.openminds.controlledterms import Technique
```

The following openMINDS modules are currently available: `core`, `controlledterms`, `sands`, `computation`, `ephys`, `publications`.
Using these classes, it is possible to list all metadata matching a particular criterion, e.g.

```
>>> patch_techniques = Technique.list(client, name="patch clamp")
>>> print([technique.name for technique in patch_techniques])
['cell attached patch clamp', 'multiple whole cell patch clamp', 'patch clamp', 'patch clamp technique', 'whole cell patch clamp']
>>> whole_cell_patch = patch_techniques[4]
```

```
>>> datasets = DatasetVersion.list(client, techniques=whole_cell_patch, scope="in progress")
```

For research products that are versioned, such as datasets, models, and software, certain attributes may be inherited from the parent (e.g. a DatasetVersion generally inherits its name from a Dataset). In this case, we have a convenience method to retrieve the parent's name:

```
>>> print(datasets[0].get_name(client, scope="in progress"))
'Cholinergic interneurons in the striatum - Single cell patch clamp recordings'
```

If you know the unique identifier of an object, you can retrieve it directly:

```
>>> dataset = DatasetVersion.from_id("17196b79-04db-4ea4-bb69-d20aab6f1d62", client, scope="in progress")
```

Links between metadata in the Knowledge Graph are not followed automatically,
to avoid unnecessary network traffic, but can be followed with the `resolve()` method:

```
>>> license = dataset.license.resolve(client, scope="in progress")
>>> authors = [author.resolve(client, scope="in progress") for author in dataset.authors]
```

The associated metadata is accessible as attributes of the Python objects, e.g.:

```
>>> print(dataset.version_innovation)
This is the first version of this research product.
```

To print out all the metadata for a given object, use the `show()` method:

```
>>> print(license.show())
id          https://kg.ebrains.eu/api/instances/6ebce971-7f99-4fbc-9621-eeae47a70d85
name        Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
legal_code  https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
alias       CC BY-NC-SA 4.0
webpages    ['https://creativecommons.org/licenses/by-nc-sa/4.0', 'https://spdx.org/licenses/CC-BY-NC-SA-4.0.html']
```

You can also access any associated data:

```
>>> dataset.download(client, local_directory=dataset.alias)
```


## Storing and editing metadata

For those users who have the necessary permissions to store and edit metadata in the Knowledge Graph,
**fairgraph** objects can be created or edited in Python, and then saved back to the Knowledge Graph, e.g.:

```
from datetime import datetime
from fairgraph.openminds.core import Person, Organization, Affiliation

mgm = Organization(name="Metro-Goldwyn-Mayer", alias="MGM")
mgm.save(client, space="myspace")

affiliation = Affiliation(organization=mgm, start_date=datetime(1942, 1, 1))
author = Person(family_name="Laurel", given_name="Stan", affiliations=affiliation)
author.save(client, space="myspace")
```

## Getting help

In case of questions about **fairgraph**, please contact us via https://ebrains.eu/support/.
If you find a bug or would like to suggest an enhancement or new feature,
please open a ticket in the [issue tracker](https://github.com/HumanBrainProject/fairgraph/issues).

## Acknowledgements

<div><img src="https://www.braincouncil.eu/wp-content/uploads/2018/11/wsi-imageoptim-EU-Logo.jpg" alt="EU Logo" height="23%" width="15%" align="right" style="margin-left: 10px"></div>

This open source software code was developed in part or in whole in the Human Brain Project, funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreements No. 720270, No. 785907 and No. 945539 (Human Brain Project SGA1, SGA2 and SGA3).
