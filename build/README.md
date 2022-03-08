# Scripts for building fairgraph classes for openMINDS schemas

To update the `fairgraph.openminds` module, run:

```
python update_openminds.py /path/to/openMINDS
```

Where the various submodules have already been cloned and the desired version branches checked out. 
This assumes that the `openMINDS_generator` repository has been cloned to `openMINDS/generator`.
If this is not the case, you can specify where to find it:

```
python update_openminds.py --generator-path=/path/to/generator /path/to/openMINDS
```

Before committing the resulting generated files, check that any changed introduced seem correct.
Currently a few changes are applied by hand on top of the generated files, be sure not to overwrite these.
