
************
Introduction
************

Blender's physics system allows you to simulate a number of different real-world physical phenomena.
You can use these systems to create a variety of static and dynamic effects such as:

- Hair, grass, and flocks
- Rain
- Smoke and dust
- Water
- Cloth
- Jello
- etc.


.. _bpy.ops.object.quick:

Quick Effects
=============

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Quick Effects`

Sets up a basic simulation scene or effect including the selected objects.
The tool will add essential objects like domains or particle systems both with predefined settings,
so that there will be instant viewable result.


.. _bpy.ops.object.quick_fur:

Quick Fur
---------

Adds a fur setup to the selected objects.
The fur setup is based on :doc:`/modeling/geometry_nodes/index` and built with
:doc:`Hair Node Groups </modeling/geometry_nodes/hair/index>` that come with Blender as bundled assets.

Density
   Surface density of generated hair curves.
Length
   Length of the generated hair curves.
Hair Radius
   The width of the hair, used for rendering engines.
View Percentage
   Factor applied on the density for the viewport.
Apply Hair Curves
   Applies the modifier that uses the :doc:`/modeling/geometry_nodes/hair/generation/generate_hair_curves` node group.
Noise
   Deforms hair curves using a noise texture.
   See the :doc:`/modeling/geometry_nodes/hair/deformation/hair_curves_noise` node group for more information.
Frizz
   Deforms hair curves using a random vector per point to frizz them.
   See the :doc:`/modeling/geometry_nodes/hair/deformation/frizz_hair_curves` node group for more information.
