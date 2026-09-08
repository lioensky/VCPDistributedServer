.. index:: Geometry Nodes; Sphere Selection

*********************
Sphere Selection Node
*********************

.. figure:: /images/node-types_GeometryNodeSphereSelection.webp
   :align: right
   :alt: Sphere Selection node.

The *Sphere Selection* node creates a selection of elements that lie within a defined spherical region.
It can be used to isolate points, faces, or instances inside or near a sphere, making it useful for
localized effects, falloffs, or region-based operations.


Inputs
======

Center
   The center position of the sphere in 3D space.

Radius
   The radius of the sphere, defining the distance from the center within which elements are selected.


Outputs
=======

Selection
   A boolean field indicating which elements fall inside or on the surface of the sphere.
   True for elements within the radius; false for those outside.
