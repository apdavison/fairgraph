================
Metadata domains
================

.. toctree::
   :hidden:

   modules/minds
   modules/uniminds
   modules/electrophysiology
   modules/brainsimulation
   modules/software
   modules/core
   modules/commons


**fairgraph** currently provides the following modules:

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