.. _bpy.types.ShaderNodeNewGeometry:

*************
Geometry Node
*************

.. figure:: /images/node-types_ShaderNodeNewGeometry.webp
   :align: right
   :alt: Geometry Node.

The *Geometry* node gives geometric information about the current shading point.
All vector coordinates are in *World Space*. For volume shaders,
only the position and incoming vector are available.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Position
   Position of the shading point.
Normal
   Shading normal at the surface (includes smooth normals and bump mapping).
Tangent
   Tangent at the surface.
True Normal
   Geometry or flat normal of the surface.
Incoming
   Vector pointing towards the point the shading point is being viewed from.
Parametric
   Parametric coordinates of the shading point on the surface.
   To area lights it outputs its UV coordinates in planar mapping and
   in spherical coordinates to point lights.
Backfacing
   1.0 if the face is being viewed from the back side, 0.0 for the front side.
Pointiness :guilabel:`Cycles Only`
   An approximation of the curvature of the mesh per vertex.
   Lighter values indicate convex angles, darker values indicate concave angles.
   It allows you to do effects like dirt maps and wear-off effects.
Random per Island :guilabel:`Cycles Only`
   A random value for each connected component (island) of the mesh.
   It is useful to add variations to meshes composed of separated units
   like tree leaves, wood planks, or curves of multiple splines.

   .. figure:: /images/render_shader-nodes_input_geometry_example-random-per-island.png

      Get a random value for each instance of the mesh when using an Array modifier.
