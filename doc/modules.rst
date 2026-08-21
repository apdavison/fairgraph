================
Metadata domains
================

fairgraph supports both openMINDS v4 and v5 schemas. By default, modules are imported from v4
for backwards compatibility::

    import fairgraph.openminds.core as omcore          # v4 (default)
    import fairgraph.openminds.v4.core as omcore4      # explicit v4
    import fairgraph.openminds.v5.core as omcore5      # explicit v5

The two versions are entirely separate sets of classes: a v4 :class:`Person` and a v5
:class:`Person` are different Python classes, even though they share the same ``@type`` URI in
the Knowledge Graph. Since the URI alone cannot tell them apart, the client has to be told which
version to deserialize responses into, via the ``openminds_version`` argument. Omitting it keeps
the v4 behaviour::

    from fairgraph import KGClient
    import fairgraph.openminds.v5.core as omcore

    client = KGClient(host=host_serving_v5_metadata, openminds_version="v5")
    people = omcore.Person.list(client)

Take care to import the classes you use from the same version the client was created with:
passing a v4 class to a v5 client (or vice versa) will query for the wrong properties.

.. note:: The migration of the EBRAINS Knowledge Graph to openMINDS v5 is still in progress.
          The production and pre-production deployments serve openMINDS v4, which is what you
          should use against them. v5 metadata is so far only available from a development
          deployment with restricted access; if you need to work against it, contact EBRAINS
          Support.

openMINDS v4
------------

.. toctree::
   :hidden:

   modules/openminds_core
   modules/openminds_controlledterms
   modules/openminds_chemicals
   modules/openminds_sands
   modules/openminds_computation
   modules/openminds_specimenprep
   modules/openminds_ephys
   modules/openminds_stimulation
   modules/openminds_publications

:doc:`modules/openminds_core`
    covers general origin, location and content of research products.

:doc:`modules/openminds_sands`
    covers brain atlases, as well as anatomical locations and relations of non-atlas data.

:doc:`modules/openminds_controlledterms`
    covers consistent definition of neuroscience terms.

:doc:`modules/openminds_chemicals`
    covers chemical substances and mixtures used in neuroscience.

:doc:`modules/openminds_computation`
    covers provenance of simulations, data analysis and visualizations in neuroscience.

:doc:`modules/openminds_ephys`
    covers in-depth metadata for electrophysiology recordings, extending the basic information in openMINDS/core.

:doc:`modules/openminds_specimenprep`
    covers in-depth metadata for the preparation of specimens (e.g. cell culture, surgical procedures, tissue slicing).

:doc:`modules/openminds_stimulation`
    covers in-depth metadata about stimulation protocols in neuroscience experiments.

:doc:`modules/openminds_publications`
    covers scientific publications, particularly interactive publications such as live papers.


openMINDS v5
------------

.. toctree::
   :hidden:

   modules/openminds_v5_core
   modules/openminds_v5_controlledterms
   modules/openminds_v5_chemicals
   modules/openminds_v5_sands
   modules/openminds_v5_computation
   modules/openminds_v5_specimenprep
   modules/openminds_v5_ephys
   modules/openminds_v5_stimulation
   modules/openminds_v5_publications
   modules/openminds_v5_neuroimaging

v5 includes all v4 modules plus a new **neuroimaging** module. Some classes have been renamed
(e.g. ``BrainAtlas`` → ``AnatomicalAtlas``), and new classes have been added.

:doc:`modules/openminds_v5_core`
    covers general origin, location and content of research products.

:doc:`modules/openminds_v5_sands`
    covers brain atlases, as well as anatomical locations and relations of non-atlas data.

:doc:`modules/openminds_v5_controlledterms`
    covers consistent definition of neuroscience terms.

:doc:`modules/openminds_v5_chemicals`
    covers chemical substances and mixtures used in neuroscience.

:doc:`modules/openminds_v5_computation`
    covers provenance of simulations, data analysis and visualizations in neuroscience.

:doc:`modules/openminds_v5_ephys`
    covers in-depth metadata for electrophysiology recordings, extending the basic information in openMINDS/core.

:doc:`modules/openminds_v5_specimenprep`
    covers in-depth metadata for the preparation of specimens (e.g. cell culture, surgical procedures, tissue slicing).

:doc:`modules/openminds_v5_stimulation`
    covers in-depth metadata about stimulation protocols in neuroscience experiments.

:doc:`modules/openminds_v5_publications`
    covers scientific publications, particularly interactive publications such as live papers.

:doc:`modules/openminds_v5_neuroimaging`
    covers in-depth metadata for neuroimaging data, particularly MRI acquisitions and devices.
