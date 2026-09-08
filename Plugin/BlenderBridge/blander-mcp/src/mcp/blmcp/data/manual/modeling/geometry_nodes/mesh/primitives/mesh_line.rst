.. index:: Geometry Nodes; Mesh Line
.. _bpy.types.GeometryNodeMeshLine:

**************
Mesh Line Node
**************

.. figure:: /images/node-types_GeometryNodeMeshLine.webp
   :align: right
   :alt: Mesh Line Node.

The *Mesh Line* node generates vertices in a line and connects them with edges.


Inputs
======

Count
   Number of vertices on the line.

Resolution
   Length of individual edges.
   The node tries to fit as many vertices as possible between the start and end point.
   The exact end point might not be hit.
   This is only available when the mode is set to *End Points* and the count mode is set to *Resolution*.

Start Location
   Position of the first vertex.

Offset
   Controls the direction of the line and distance between the vertices.
   This is only available when the mode is set to *Offset*.

End Location
   Position of the last vertex.
   This is only available when the mode is set to *End Points*.


Properties
==========

Mode
   Inputs to use to control the line.

   :Offset: Specify the offset from one vertex to the next.
   :End Points: Specify the start and end point of the line.

Count Mode
   Determines how the number of vertices is chosen.
   This is only available when the mode is set to *End Points*.

   :Count: Specify the total number of vertices.
   :Resolution: Specify the distance between vertices.


Outputs
=======

Mesh
   Standard geometry output.
