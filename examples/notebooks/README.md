# fairgraph example notebooks

Tutorial notebooks for working with the [EBRAINS Knowledge Graph](https://docs.kg.ebrains.eu) through
[fairgraph](https://fairgraph.readthedocs.io).

Each link below opens the notebook in the [EBRAINS Lab](https://lab.ebrains.eu), copying this repository
into your Lab session first. You need an [EBRAINS account](https://www.ebrains.eu/page/sign-up); fairgraph
is already installed in the EBRAINS Software Distribution kernels, so there is nothing to set up.

| Notebook | What it covers | |
|---|---|---|
| **Exploring the Knowledge Graph** <br> `data_consumer_tutorial.ipynb` | Finding, inspecting and downloading EBRAINS datasets, models and software. Filtering, following links, controlled terms, local JSON-LD snapshots, custom queries. Read-only. | [Open in the EBRAINS Lab](https://lab.ebrains.eu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FHumanBrainProject%2Ffairgraph&urlpath=lab%2Ftree%2Ffairgraph%2Fexamples%2Fnotebooks%2Fdata_consumer_tutorial.ipynb&branch=master) |
| **Creating EBRAINS metadata** <br> `data_provider_tutorial.ipynb` | Building, validating and saving metadata of your own: research products, authors, licences, files and repositories, spaces and permissions, and how metadata reaches EBRAINS curators. | [Open in the EBRAINS Lab](https://lab.ebrains.eu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FHumanBrainProject%2Ffairgraph&urlpath=lab%2Ftree%2Ffairgraph%2Fexamples%2Fnotebooks%2Fdata_provider_tutorial.ipynb&branch=master) |
| **Advanced tutorial** <br> `advanced_tutorial.ipynb` | An earlier, general fairgraph tutorial, covering the library together with the `ebrains-kg-core` client and the openMINDS schemas it builds on. | [Open in the EBRAINS Lab](https://lab.ebrains.eu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FHumanBrainProject%2Ffairgraph&urlpath=lab%2Ftree%2Ffairgraph%2Fexamples%2Fnotebooks%2Fadvanced_tutorial.ipynb&branch=master) |

The two tutorial notebooks are independent: the first only reads from the Knowledge Graph, the second only
writes, and neither assumes you have done the other.

**The data provider notebook writes to the pre-production Knowledge Graph**
(`core.kg-ppd.ebrains.eu`), never to production, and only to your own private space. Nothing you create
while working through it is publicly visible, and the notebook's last section deletes it again.

## About the links

The links use [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/). Following one clones this
repository into your Lab session and opens the notebook; your session's copy lives only as long as the
session, so you can edit freely and start again by following the link in a new session.

They point at the `master` branch, so you always get the current version of a notebook. If you want a
specific version, change `branch=master` in the link to the branch you want — note that nbgitpuller
selects branches only, not tags or commits.

## Running them elsewhere

The notebooks are ordinary Jupyter notebooks and run anywhere you have fairgraph installed:

```
pip install fairgraph
jupyter lab examples/notebooks/
```

Outside the EBRAINS Lab you will need to authenticate yourself — see
[the fairgraph documentation](https://fairgraph.readthedocs.io) for the options.
