====================================
Creating and updating metadata nodes
====================================

To create a new metadata node, create an instance of the appropriate Python class,
then use the :meth:`save()` method, e.g.::

    from fairgraph.openminds.core import SoftwareVersion

    sv = SoftwareVersion(
        name="numpy",
        alias="numpy",
        version_identifier="1.14.9"
    )
    sv.save(client, space="myspace")

To update a node, edit the attributes of the corresponding Python object, then :meth:`save()` again::

    from fairgraph.base import IRI

    sv.homepage = IRI("https://numpy.org")
    sv.save(client)

(Note that for updating existing objects you don't need to specify the space.)

How does fairgraph distinguish between creating a new node and modifying an existing one?
=========================================================================================

If a previously-created node has been retrieved from the Knowledge Graph, it will have a unique ID,
and therefore calling :meth:`save()` will update the node with this ID.

If a new Python object is created with the same or similar metadata, **fairgraph** queries for
a node with matching metadata for a *subset* of the properties.
If you want to know which properties are included in the match, examine the :attr:`existence_query_properties`
attribute, e.g.::

    >>> SoftwareVersion.existence_query_properties
    ('alias', 'version_identifier')


Permissions
===========

If you get an error message when trying to create or update a node, it may be because you do not
have the necessary permissions. See :doc:`permissions` for more information.
