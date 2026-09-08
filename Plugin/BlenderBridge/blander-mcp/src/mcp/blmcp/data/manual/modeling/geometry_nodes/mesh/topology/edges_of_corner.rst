.. index:: Geometry Nodes; Edges of Corner
.. _bpy.types.GeometryNodeEdgesOfCorner:

********************
Edges of Corner Node
********************

.. figure:: /images/node-types_GeometryNodeEdgesOfCorner.webp
   :align: right
   :alt: Edges of Corner node.

The *Edges of Corner* node retrieves the edges on both sides of a face corner.


Inputs
======

Corner Index
   The index of the input face corner.

   .. note::

      By default this uses the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      from the field context, which makes it important that the node is evaluated on
      the face corner domain.


Outputs
=======

Next Edge Index
   The index of the neighboring edge in the face, in the direction of increasing face corner indices.

Previous Edge Index
   The index of the neighboring edge in the face, in the direction of decreasing face corner indices.
