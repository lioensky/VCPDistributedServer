.. index:: Geometry Nodes; Face of Corner
.. _bpy.types.GeometryNodeFaceOfCorner:

*******************
Face of Corner Node
*******************

.. figure:: /images/node-types_GeometryNodeFaceOfCorner.webp
   :align: right
   :alt: Face of Corner node.

Retrieves the face that a face corner is part of.


Inputs
======

Corner Index
   The geometry-wide index of the corner.

   .. note::

      If this input is not connected, it uses the
      :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`
      of the context item, which means it's important that the node is evaluated
      in the Face Corner domain.


Outputs
=======

Face Index
   The geometry-wide index of the face which the corner belongs to.

Index in Face
   The face-local index of the corner. This is 0 for the first corner of the face,
   1 for the next corner, and so on up to (number of corners - 1) for the last corner.
