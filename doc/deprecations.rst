============
Deprecations
============

From time to time, a class, module or argument in fairgraph is renamed or replaced.
So that code written for an earlier version keeps working, the old name usually remains
available for a while as a *deprecated* name.

Deprecation policy
==================

- A deprecated name keeps working until the next major release (currently 1.0), in which it is removed.
- Using a deprecated name emits a :exc:`DeprecationWarning`, which says what to use instead,
  and in which release the deprecated name will be removed.
- Each deprecation, and each removal, is announced in the :doc:`release notes <release_notes>`.
  The names that are currently deprecated are listed below.

By default, Python only shows a :exc:`DeprecationWarning` when it is triggered by code in the
``__main__`` module (e.g., a script run directly, or a Jupyter notebook), so warnings triggered from
within your own modules or packages are hidden. To see all of them, run Python with
``-W default::DeprecationWarning``, or set the environment variable
``PYTHONWARNINGS=default::DeprecationWarning``. pytest shows deprecation warnings in its summary by default.

Currently deprecated
====================

.. list-table::
   :header-rows: 1
   :widths: 35 30 10 10 10

   * - Deprecated name
     - Use instead
     - Deprecated in
     - Warns since
     - To be removed in
   * - ``fairgraph.EmbeddedMetadata``, ``fairgraph.embedded.EmbeddedMetadata``
     - ``fairgraph.KGEmbedded``
     - 0.13.3
     - 0.16.0
     - 1.0
   * - ``fairgraph.node.ContainsMetadata``
     - ``fairgraph.node.KGNode``
     - 0.13.3
     - 0.16.0
     - 1.0
   * - ``fairgraph.base.RepresentsSingleObject``
     - ``fairgraph.base.Releasable``
     - 0.13.3
     - 0.16.0
     - 1.0
   * - ``fairgraph.registry.Node``
     - ``fairgraph.registry.NodeMeta``
     - 0.13.3
     - 0.16.0
     - 1.0
   * - the ``scope`` keyword argument (e.g., ``KGObject.list(client, scope=...)``)
     - ``release_status``
     - 0.13.0
     - 0.13.0
     - 1.0
   * - the ``fairgraph.openminds.controlledterms`` module
     - ``fairgraph.openminds.controlled_terms``
     - 0.12.0
     - 0.12.0
     - 1.0
   * - the ``fairgraph.openminds.specimenprep`` module
     - ``fairgraph.openminds.specimen_prep``
     - 0.12.0
     - 0.12.0
     - 1.0

.. note::

   ``fairgraph.EmbeddedMetadata`` is not the same as ``openminds.base.EmbeddedMetadata``,
   the base class for embedded nodes in the openMINDS Python library, which is not deprecated.
   Likewise, ``fairgraph.registry.Node`` is not ``openminds.base.Node``.
