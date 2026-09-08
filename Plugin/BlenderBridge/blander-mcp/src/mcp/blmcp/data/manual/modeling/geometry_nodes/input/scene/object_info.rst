.. index:: Geometry Nodes; Object Info
.. _bpy.types.GeometryNodeObjectInfo:

****************
Object Info Node
****************

.. figure:: /images/node-types_GeometryNodeObjectInfo.webp
   :align: right
   :alt: Object Info node.

The *Object Info* node gets information from objects.
This can be useful to control parameters in the geometry node tree with an external object,
either directly by using its geometry, or via its transformation properties.

An *Object Info* node can be added quickly by dragging an object into the node editor.


Inputs
======

Object
   Object to get the properties from.

As Instance
   Output the entire object as single instance instead of realized geometry.
   This allows instancing non-geometry object types, because the output will contain an instance of the object.


Properties
==========

Transform Space
   The transformation of the vector and geometry outputs.

   :Original:
      Output the geometry relative to the input object transform, and the location,
      rotation and scale relative to the world origin.
   :Relative:
      Bring the input object geometry, location, rotation and scale into the modified object,
      maintaining the relative position between the two objects in the scene.


Outputs
=======

Transform
   :term:`Transformation Matrix` containing the location, rotation and scale of the object.
Location
   Location of the object in world space.
Rotation
   Rotation of the object in world space.
Scale
   Scale of the object in world space.
Geometry
   Geometry of the object in world space with all its modifiers applied.
