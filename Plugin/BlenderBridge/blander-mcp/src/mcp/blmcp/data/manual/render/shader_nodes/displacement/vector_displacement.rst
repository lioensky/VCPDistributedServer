.. _bpy.types.ShaderNodeVectorDisplacement:

************************
Vector Displacement Node
************************

.. figure:: /images/node-types_ShaderNodeVectorDisplacement.webp
   :align: right
   :alt: Vector Displacement Node.

The *Vector Displacement* node is used to displace the surface along arbitrary directions,
unlike the regular Displacement node which only displaces along the surface normal.

It is typically used to apply vector displacement maps created by other sculpting
software. Vector displacement maps can fully represent the high resolution detail to
be applied on a smooth base mesh, unlike regular displacement maps.

By default, Blender only uses :term:`Bump Mapping` to render displacement.
However with true displacement, the rendered geometry will be physically displaced. To use true displacement
the :ref:`Displacement method <bpy.types.Material.displacement_method>` must be set accordingly.

.. tip::

   For best results when using true displacement,
   the mesh must be subdivided finely to bring out the detail in the displacement texture.

.. seealso::

   :doc:`Material Displacement </render/materials/components/displacement>`
   for more details on displacement workflows.


Inputs
======

Vector
   Vector specifying the displacement along three axes.
   This is where a texture node can be connected.

   Typically a baked vector displacement image texture is used.
   For Object Space, RGB colors in the image are interpreted as an XYZ offset in object space.
   For Tangent Space, R is an offset along the tangent, G along the normal and B along the bitangent.
Midlevel
   Neutral displacement value that causes no displacement.
   With the default 0.0, any lower values will cause the surfaces to be pushed inwards,
   and any higher values will push them outwards.
Scale
   Increase or decrease the amount of displacement.


Properties
==========

Space
   Object Space maps work for static meshes, and will render slightly faster with less memory usage.
   Tangent Space maps can be used for meshes that will be deformed, like animated characters,
   so the displacement follows the deformation.


Outputs
=======

Displacement
   Displacement offset to be connected into the Material Output.


Examples
========

.. figure:: /images/render_shader-nodes_vector_vector-displacement_example.jpg

   Regular and exaggerated vector displacement on a smooth base mesh.
