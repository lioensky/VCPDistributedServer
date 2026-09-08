.. index:: Geometry Nodes; Vertex of Corner
.. _bpy.types.GeometryNodeVertexOfCorner:

*********************
Vertex of Corner Node
*********************

.. figure:: /images/node-types_GeometryNodeVertexOfCorner.webp
   :align: right
   :alt: Vertex of Corner node.

Outputs the index of the vertex that a face corner is attached to.


Inputs
======

Corner Index
   The index of the face corner.

   .. note::

      If this input is not connected, it uses the
      :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      of the context item, which means it's important that the node is evaluated
      in the Face Corner domain.


Outputs
=======

Vertex Index
   The index of the vertex that the face corner is attached to.
