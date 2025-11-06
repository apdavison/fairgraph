# fairgraph: a Python API for the EBRAINS Knowledge Graph.

[![tests](https://github.com/HumanBrainProject/fairgraph/actions/workflows/tests.yml/badge.svg)](https://github.com/HumanBrainProject/fairgraph/actions/workflows/tests.yml)
[![Documentation](https://app.readthedocs.org/projects/fairgraph/badge/?version=latest)](https://fairgraph.readthedocs.io)
![PyPI - Version](https://img.shields.io/pypi/v/fairgraph)

Authors: Andrew P. Davison, Onur Ates, Nico Feld, Yann Zerlaut, Glynis Mattheisen, Peyman Najafi

Copyright CNRS 2019-2025

**fairgraph** is a Python library for working with metadata
in the EBRAINS Knowledge Graph, with a particular focus on data reuse,
although it is also useful in metadata registration/curation.

## Installation

To get the latest release:

```
pip install fairgraph
```

To get the development version:

```
git clone https://github.com/HumanBrainProject/fairgraph.git
pip install -U ./fairgraph
```

## Knowledge Graph and openMINDS versions

This version of fairgraph supports version 3 of the EBRAINS Knowledge Graph (KG),
and version 4 of the openMINDS metadata schemas.

## Basic setup

The basic idea of the library is to represent metadata nodes from the Knowledge Graph as Python objects.
Communication with the Knowledge Graph service is through a client object,
for which an access token associated with an EBRAINS account is needed.

If you are working in an EBRAINS Lab Jupyter notebook, the client will find your token automatically.

If working outside EBRAINS Lab, we recommend you use the `allow_interactive` option:

```
>>> client = KGClient(host="core.kg.ebrains.eu", allow_interactive=True)
```

This prints the URL of a log-in page, which you should open in a web-browser.
Once you have logged in, close the tab and return to your Python prompt.

You can also obtains a token elsewhere and pass it to the client:

```
>>> client = KGClient(host="core.kg.ebrains.eu", token)
```

## Retrieving metadata from the Knowledge Graph

The Knowledge Graph uses [openMINDS](https://github.com/HumanBrainProject/openMINDS) schemas.
Each openMINDS schema corresponds to a Python class, which are grouped into modules
following the openMINDS structure. For example:

```
>>> from fairgraph.openminds.core import DatasetVersion
>>> from fairgraph.openminds.controlled_terms import Technique
```

The following openMINDS modules are currently available: `core`, `controlled_terms`, `sands`, `computation`, `chemicals`, `specimen_prep`, `ephys`, `publications`, `stimulation`.
Using these classes, it is possible to list all metadata matching a particular criterion, e.g.

```
>>> patch_techniques = Technique.list(client, name="patch clamp")
>>> print([technique.name for technique in patch_techniques])
['cell attached patch clamp', 'multiple whole cell patch clamp', 'patch clamp', 'whole cell patch clamp']
>>> whole_cell_patch = patch_techniques[3]
```

```
>>> datasets = DatasetVersion.list(client, techniques=whole_cell_patch)
```

The associated metadata are accessible as attributes of the Python objects, e.g.:

```
>>> print(datasets[0].version_innovation)
'This is the only version of this dataset.'
```

You can also access any associated data:

```
>>> datasets[0].download(client, local_directory="downloads")
```

### Inherited attributes

For research products that are versioned, such as datasets, models, and software, certain attributes may be inherited from the parent (e.g., a DatasetVersion generally inherits its name from a Dataset).
In this case, we have a convenience method to retrieve the parent's name:

```
>>> print(datasets[0].get_full_name(client))
'Recordings of excitatory postsynaptic currents from cerebellar neurons'
```

### Unique identifiers

If you know the unique identifier of an object, you can retrieve it directly:

```
>>> dataset = DatasetVersion.from_id("17196b79-04db-4ea4-bb69-d20aab6f1d62", client)
```

### Following links in the knowledge graph

Links between metadata in the Knowledge Graph are not followed automatically,
to avoid unnecessary network traffic, but can be followed with the `resolve()` method:

```
>>> license = dataset.license.resolve(client)
>>> authors = [author.resolve(client) for author in dataset.get_authors(client)]
```

If you know in advance which links you wish to follow, you can use the `follow_links` option:

```
>>> dataset = DatasetVersion.from_id(
...     "17196b79-04db-4ea4-bb69-d20aab6f1d62",
...     client,
...     follow_links={
...         "license": {},
...         "is_version_of": {
...             "authors": {}
...         }
...     }
... )
>>> dataset.is_version_of[0].authors[0].given_name
'Francesca'
>>> dataset.license.short_name
'CC-BY-NC-SA-4.0'
```

Note that this can also be used to follow multiple links in the graph;
in the example above we asked for the authors of the parent `Dataset`.

To print out all the metadata for a given object, use the `show()` method:

```
>>> print(license.show())
id          https://kg.ebrains.eu/api/instances/6ebce971-7f99-4fbc-9621-eeae47a70d85
name        Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
legal_code  https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
alias       CC BY-NC-SA 4.0
webpages    ['https://creativecommons.org/licenses/by-nc-sa/4.0', 'https://spdx.org/licenses/CC-BY-NC-SA-4.0.html']
```

## Storing and editing metadata

For those users who have the necessary permissions to store and edit metadata in the Knowledge Graph,
**fairgraph** objects can be created or edited in Python, and then saved back to the Knowledge Graph, e.g.:

```
from datetime import date
from fairgraph.openminds.core import Person, Organization, Affiliation

mgm = Organization(full_name="Metro-Goldwyn-Mayer", short_name="MGM")
mgm.save(client, space="myspace")

affiliation = Affiliation(member_of=mgm, start_date=date(1941, 2, 23))
author = Person(family_name="Laurel", given_name="Stan", affiliations=[affiliation])
author.save(client, space="myspace")
```

## Getting help

In case of questions about **fairgraph**, please contact us via https://ebrains.eu/support/.
If you find a bug or would like to suggest an enhancement or new feature,
please open a ticket in the [issue tracker](https://github.com/HumanBrainProject/fairgraph/issues).

## Acknowledgements

<div><img src="https://www.braincouncil.eu/wp-content/uploads/2018/11/wsi-imageoptim-EU-Logo.jpg" alt="EU Logo" height="23%" width="15%" align="right" style="margin-left: 10px"></div>

This open source software code was developed in part or in whole in the Human Brain Project, funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreements No. 720270, No. 785907 and No. 945539 (Human Brain Project SGA1, SGA2 and SGA3) and in the EBRAINS research infrastructure,
funded from the European Union's Horizon Europe funding programme under grant agreement No. 101147319 (EBRAINS-2.0).
