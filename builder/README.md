# Scripts for building fairgraph classes for openMINDS schemas

To update the `fairgraph.openminds` module, run:

```
python update_openminds.py /path/to/openMINDS/schemas/v4.0
```

Where /path/to/openMINDS is a clone of the main branch of https://github.com/openMetadataInitiative/openMINDS.git

Before committing the resulting generated files, check that any changes introduced seem correct.

## Hand-written methods

Everything under `fairgraph/openminds` is generated, and hand edits made there will be lost
the next time this script runs.

Methods that cannot be derived from the schema (e.g. `Person.me()`, `DatasetVersion.download()`)
are kept in `additional_methods/`, one file per class, named `<ClassName>.py.txt`. The builder
inserts the contents of the matching file verbatim into the body of the generated class, so each
file holds method definitions only - no `class` statement - indented as they will appear in the
class body.

To change the behaviour of a generated class, edit its file in `additional_methods/` and re-run
the script, then commit the overlay and the regenerated file together.

See "Building the openMINDS module" and "Hand-written methods on generated classes" in
`doc/contributing.rst` for the full description.
