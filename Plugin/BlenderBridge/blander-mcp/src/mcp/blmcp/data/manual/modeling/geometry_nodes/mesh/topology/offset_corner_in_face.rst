.. index:: Geometry Nodes; Offset Corner in Face
.. _bpy.types.GeometryNodeOffsetCornerInFace:

**************************
Offset Corner in Face Node
**************************

.. figure:: /images/node-types_GeometryNodeOffsetCornerInFace.webp
   :align: right
   :alt: Offset Corner in Face node.

Retrieves another corner in the same face as the input corner.
This is like "rotating" the input corner around in its face.

Conceptually the operation is similar to the
:doc:`/modeling/geometry_nodes/curve/topology/offset_point_in_curve`.


Inputs
======

Corner Index
   The index of the input face corner.

   .. note::

      If this input is not connected, it uses the
      :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      of the context item, which means it's important that the node is evaluated
      in the Face Corner domain.

Offset
   The number of corners to move around the face before finding the result,
   circling back to the first corner if necessary.


Outputs
=======

Corner Index
   The index of the offset face corner.
