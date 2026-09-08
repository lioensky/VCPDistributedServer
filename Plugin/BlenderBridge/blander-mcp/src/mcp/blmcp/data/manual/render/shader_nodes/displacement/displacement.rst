.. _bpy.types.ShaderNodeDisplacement:

*****************
Displacement Node
*****************

.. figure:: /images/node-types_ShaderNodeDisplacement.webp
   :align: right
   :alt: Displacement Node.

The *Displacement* node is used to displace the surface along the surface normal,
to add more detail to the geometry. Both procedural textures and baked displacement maps
can be used.

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

Height
   Distance to displace the surface along the normal.
   This is where a texture node can be connected.
Midlevel
   Neutral displacement value that causes no displacement.
   With the default 0.5, any lower values will cause the surfaces to be pushed inwards,
   and any higher values will push them outwards.
Scale
   Increase or decrease the amount of displacement.
Normal
   Standard normal input.


Properties
==========

Space
   Object Space means the displacement scales along with the object.
   When using World Space the object scale is ignored.


Outputs
=======

Displacement
   Displacement offset to be connected into the Material Output.


Examples
========

.. figure:: /images/render_materials_components_displacement_node-setup.png

   Typical displacement node setup.

.. figure:: /images/render_materials_components_displacement_example.jpg

   Bump only, displacement only, and displacement and bump combined.
