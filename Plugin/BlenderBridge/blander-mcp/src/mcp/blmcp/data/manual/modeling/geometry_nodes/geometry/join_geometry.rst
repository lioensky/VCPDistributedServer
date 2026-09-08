.. index:: Geometry Nodes; Join Geometry
.. _bpy.types.GeometryNodeJoinGeometry:

******************
Join Geometry Node
******************

The *Join Geometry* node merges separately generated geometries into a single one.
If the geometry inputs contain different types of data, the output will also contain different data types.

.. figure:: /images/node-types_GeometryNodeJoinGeometry.webp
   :alt: Join Geometry node.

.. note::

   The node cannot handle the case when more than one geometry input has a volume component.


Materials
=========

When multiple mesh inputs contain different materials, the material slots from each mesh geometry
are merged so that the output mesh will contain all the input materials.


.. editors note: keep up to date with :doc:`/modeling/geometry_nodes/instances/realize_instances`

Attributes
==========

When merging attributes from multiple geometry inputs, the highest complexity data type is chosen
for the output attribute. For example, if a ``weight`` attribute is a Boolean on one geometry input
and a vector on another, the ``weight`` attribute on the output geometry will use the vector data type.

.. note::

   Vertex groups are preserved when realizing instances or joining geometries.
   If the domain and type propagation rules above result with the vertex domain and float type,
   then an attribute will be a vertex group on the output mesh.


Inputs
======

Geometry
   Geometry that will be joined. Multiple inputs are allowed.
   When the node is muted, only the first link will be passed through.


Output
======

Geometry
   Standard geometry output.
