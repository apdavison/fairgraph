=============
API reference
=============

All Python classes that represent openMINDS metadata, such as :class:`~fairgraph.openminds.core.Dataset`,
inherit from either :class:`~fairgraph.KGObject` (if the object has its own "id" attribute)
or from :class:`~fairgraph.EmbeddedMetadata` (if the object should be embedded inside another object,
without its own id.)

These base classes are documented here, along with :class:`~fairgraph.KGProxy`, :class:`~fairgraph.KGQuery`,
:class:`~fairgraph.KGClient`, and various utility classes and functions.

KGObject
========

.. autoclass:: fairgraph.KGObject
   :members:
   :inherited-members:
   :show-inheritance:

LinkedMetadata
==============

.. autoclass:: openminds.base.LinkedMetadata
   :members:
   :inherited-members:
   :show-inheritance:

EmbeddedMetadata
================

.. autoclass:: fairgraph.EmbeddedMetadata
   :members:
   :inherited-members:
   :show-inheritance:

KGProxy
=======

.. autoclass:: fairgraph.KGProxy
   :members:
   :inherited-members:
   :show-inheritance:

KGQuery
=======

.. autoclass:: fairgraph.KGQuery
   :members:
   :inherited-members:
   :show-inheritance:

KGClient
========

.. autoclass:: fairgraph.KGClient
   :members:
   :show-inheritance:


Collection
==========

.. autoclass:: fairgraph.Collection
   :members:
   :show-inheritance:

Queries
=======

.. autoclass:: fairgraph.queries.Query
   :members:
   :show-inheritance:

.. autoclass:: fairgraph.queries.QueryProperty
   :members:
   :show-inheritance:

.. autoclass:: fairgraph.queries.Filter
   :members:
   :show-inheritance:

Utility classes and functions
=============================

.. autofunction:: fairgraph.utility.as_list

.. autofunction:: fairgraph.utility.expand_uri

.. autofunction:: fairgraph.utility.compact_uri

.. autofunction:: fairgraph.utility.normalize_data

.. autoclass:: fairgraph.utility.ActivityLog
   :members:
   :show-inheritance:

.. autoclass:: fairgraph.utility.LogEntry
   :members:
   :show-inheritance:
