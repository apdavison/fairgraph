# Scripts for building fairgraph classes for openMINDS schemas

To update the `fairgraph.openminds` module, run:

```
python update_openminds.py /path/to/openMINDS/schemas/v4.0
```

Where /path/to/openMINDS is a clone of the main branch of https://github.com/openMetadataInitiative/openMINDS.git

Before committing the resulting generated files, check that any changed introduced seem correct.
Currently a few changes are applied by hand on top of the generated files, be sure not to overwrite these.
