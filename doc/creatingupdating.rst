====================================
Creating and updating metadata nodes
====================================

To create a new metadata node, create an instance of the appropriate Python class,
then use the :meth:`save()` method, e.g.::

    from fairgraph.modelvalidation import AnalysisResult

    result = AnalysisResult(
        name="inter-spike-interval histograms from subject #f2009a33, white-noise stimulation",
        result_file="isi_f2009a33_wn.txt"
    )
    result.save(client)

To update a node, edit the attributes of the corresponding Python object, then :meth:`save()` again::

    result.description = "ISIs from 32 neurons, first column is bin left edges, remaining columns one per neuron"
    result.save(client)

How does fairgraph distinguish between creating a new node and modifying an existing one?
=========================================================================================

If a previously-created node has been retrieved from the Knowledge Graph, it will have a unique ID,
and therefore calling :meth:`save()` will update the node with this ID.

If a new Python object is created with the same or similar metadata, **fairgraph** queries for
a node with matching metadata for a *subset* of the fields.
In the case of :class:`AnalysisResult`, above, those fields are *name* and *timestamp*.

.. note:: at present, the only way to know which subset of fields are used in this query is
          to view the sourcecode, and inspect the :meth:`_existence_query()` method.

Permissions
===========

If you get an error message when trying to create or update a node, it may be because you do not
have the necessary permissions. See :doc:`permissions` for more information.
