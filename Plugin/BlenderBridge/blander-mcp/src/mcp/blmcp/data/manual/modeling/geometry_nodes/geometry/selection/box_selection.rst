.. index:: Geometry Nodes; Box Selection

******************
Box Selection Node
******************

.. figure:: /images/node-types_GeometryNodeBoxSelection.webp
   :align: right
   :alt: Box Selection node.

The *Box Selection* node creates a selection of elements located within a defined 3D box.
It can be used to isolate geometry inside a specific region of space, such as selecting
points, faces, or instances within a bounded area.


Inputs
======

Center
   The center position of the selection box in 3D space.

Size
   The size of the box in each axis (X, Y, Z).
   Defines the width, height, and depth of the selection region.


Outputs
=======

Selection
   A boolean field indicating which elements fall inside the box volume.
   True for elements inside or intersecting the box; false otherwise.
