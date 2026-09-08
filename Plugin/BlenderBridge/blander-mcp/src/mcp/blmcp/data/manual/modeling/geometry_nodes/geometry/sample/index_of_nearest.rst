.. index:: Geometry Nodes; Index of Nearest
.. _bpy.types.GeometryNodeIndexOfNearest:

****************
Index of Nearest
****************

.. figure:: /images/node-types_GeometryNodeIndexOfNearest.webp
   :align: right
   :alt: Index of Nearest node.
   :width: 300px


The **Index of Nearest** node is a way to find other close elements in the same geometry.
If needed you can use Group ID to determine the group of neighbors to be analyzed together.

This is an alternative to the :doc:`/modeling/geometry_nodes/geometry/sample/sample_nearest` node.
The main difference is that this node does not require a geometry input, because the geometry
from the :ref:`field context <field-context>` is used.

.. tip::

    This is often combined with the :doc:`/modeling/geometry_nodes/utilities/field/evaluate_at_index` or
    the :doc:`/modeling/geometry_nodes/geometry/sample/sample_index` node.


Inputs
======

Position
   The position for each element to search.
   By default, this is the same as if the :doc:`/modeling/geometry_nodes/geometry/read/position` was connected.

Group ID
   ID to group elements together.


Outputs
=======

Index
   The :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
   of the closest element in the same geometry component.

Has Neighbor
   This is true when the group of the element has at least two elements.
   This is only relevant when using *Group ID*.
