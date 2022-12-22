================
Metadata domains
================


KG version 3
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

**fairgraph** currently provides the following modules for working with KG v3:

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


KG version 2
------------

.. toctree::
   :hidden:

   modules/minds
   modules/uniminds
   modules/electrophysiology
   modules/brainsimulation
   modules/software
   modules/core
   modules/commons


**fairgraph** currently provides the following modules for working with KG v2:

:doc:`modules/minds`
    "Minimal Information for Neuroscience DataSets" - metadata common to all neuroscience
    datasets independent of the type of investigation

:doc:`modules/uniminds`
    an updated version of MINDS

:doc:`modules/electrophysiology`
    metadata relating to patch clamp and sharp electrode intracellular recordings *in vitro*.
    Support for extracellular recording, tetrodes, multi-electrode arrays and *in vivo* recordings
    coming soon.

:doc:`modules/brainsimulation`
    metadata relating to modelling, simulation and validation

:doc:`modules/software`
    metadata relating to software used in neuroscience (for simulation, data analysis, stimulus
    presentation, etc.)

:doc:`modules/core`
    metadata for entities that are used in multiple contexts (e.g. in both electrophysiology and
    in simulation).

:doc:`modules/commons`
    metadata that are not specific to EBRAINS, typically these refer to URIs in standard
    ontologies, outside the Knowledge Graph.

Additional modules are planned, e.g. for fMRI, functional optical imaging.
In addition, the base, commons, and utility modules provide additional tools for structuring
metadata and for working with fairgraph objects.