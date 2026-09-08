.. index:: Modeling Modifiers; Multiresolution Modifier
.. _bpy.types.MultiresModifier:

************************
Multiresolution Modifier
************************

The *Multiresolution* modifier (often shortened to "Multires")
gives you the ability to subdivide a mesh similarly
to the :doc:`Subdivision Surface </modeling/modifiers/generate/subdivision_surface>` modifier,
but also allows you to edit the new subdivision levels in
:doc:`Sculpt Mode </sculpt_paint/sculpting/introduction/adaptive>`.

.. note::

   *Multiresolution* is the only modifier that cannot be repositioned in the stack after any modifier that will
   change geometry or other object data (i.e. all *Generate*, some *Modify* and some *Simulate* modifiers
   cannot come before the *Multiresolution*).

Deform modifiers will be applied onto the Multires subdivision levels instead of the base mesh,
if they come after the Multires.

.. tip::

   This is especially useful for re-projecting details from another sculpt
   with a :doc:`Shrinkwrap modifier </modeling/modifiers/deform/shrinkwrap>`. For the best result make sure to set the
   wrap method to *Project*, snap mode to *Above Surface* and enable *Negative*.


Options
=======

.. figure:: /images/modeling_modifiers_generate_multiresolution_panel.png
   :align: right
   :width: 300px

   The Multiresolution modifier.

Levels Viewport
   Set the level of subdivisions to show in the viewport.
Sculpt
   Set the level of subdivisions to use specifically in Sculpt Mode.
   While in Sculpt mode use :kbd:`Alt-1` to decrease the level or :kbd:`Alt-2` to increase.
Render
   Set the level of subdivisions to show when rendering.

Sculpt Base Mesh
   Deform the unsubdivided base mesh instead of the higher levels.
   Meanwhile the set level will be previewed. This allows you to
   make much broader changes in visual context to higher sculpted details
   without creating surface noise and artifacts.

Optimal Display
   Only display the edges of the original geometry.
   So when rendering the wireframe of this object, the wires of the subdivided edges will be skipped.


Subdivision
-----------

.. _bpy.ops.object.multires_subdivide:

Subdivide
   Creates a smooth level of subdivision
   (using the default Catmull-Clark algorithm).

Simple
   Creates a level of subdivision with unsmoothed base mesh edges (using a simple interpolation by subdividing edges
   without any smoothing).
Linear
   Creates a completely unsmoothed level of subdivision (using linear interpolation of the current sculpted
   displacement).

.. _bpy.ops.object.multires_unsubdivide:

Unsubdivide
   Rebuild a lower subdivision level of the current base mesh.

.. _bpy.ops.object.multires_higher_levels_delete:

Delete Higher
   Deletes all subdivision levels that are higher than the current one.


Shape
-----

.. _bpy.ops.object.multires_reshape:

Reshape
   Copy the shape of another object onto the multires levels by copying its vertex coordinates.

   To use it, first select a different mesh object with matching topology and vertex indices,
   then :kbd:`Shift` select the object you wish to copy vertex coordinates to, and click *Reshape*.

.. _bpy.ops.object.multires_base_apply:

Apply Base
   Modifies the original unsubdivided mesh to match the form of the subdivided mesh. This operation applies
   a heuristic to the base mesh vertices that assumes that a Subdivision Surface modifier will be added to the mesh.

Conform Base
   Modifies the original unsubdivided mesh to match the form of the subdivided mesh. The resulting positions of the
   base mesh vertices will match their subdivided positions.


Generate
--------

.. _bpy.ops.object.multires_rebuild_subdiv:

Rebuild Subdivisions
   Rebuilds all possible subdivisions levels to generate a lower resolution base mesh.
   This is used to create an optimized multiresolution version of a preexisting sculpt.
   This option is only available when no subdivision level have been created through the modifier.

.. _bpy.ops.object.multires_external_save:

Save External
   Saves displacements to an external ``.btx`` file.


Advanced
--------

Quality
   How precisely the vertices are positioned (relatively to their theoretical position),
   can be lowered to get a better performance when working on high-poly meshes.

UV Smooth
   How to handle UVs during subdivision.

   :None: UVs remain unchanged.
   :Keep Corners: UV islands are smoothed, but their boundary remain unchanged.
   :Keep Corners, Junctions:
      UVs are smoothed, corners on discontinuous boundary and junctions of three or more regions are kept sharp.
   :Keep Corners, Junctions, Concave:
      UVs are smoothed, corners on discontinuous boundary,
      junctions of three or more regions and darts and concave corners are kept sharp.
   :Keep Boundaries: UVs are smoothed, boundaries are kept sharp.
   :All: UVs and their boundaries are smoothed.

Boundary Smooth
   Controls how open boundaries (and corners) are smoothed.

   :All: Smooth boundaries, including corners.
   :Keep Corners: Smooth boundaries, but corners are kept sharp.

Use Creases
   Use the :ref:`modifiers-generate-subsurf-creases` values stored in edges to control how smooth they are made.

Use Custom Normals
   Interpolates existing :ref:`modeling_meshes_normals_custom` of the resulting mesh.


Usage
=====

Baking
------

Baking converts high-resolution geometry details, such as sculpted displacement or surface normals,
into 2D texture maps. These maps can then be applied to a lower-resolution mesh to reproduce
the appearance of fine surface detail without the performance cost of dense geometry.

This process is essential for workflows where high-resolution sculpting data is transferred to
low-resolution meshes for rendering or game engines.

To generate a normal or displacement map, use the
:ref:`Bake from Multires <bpy.types.RenderSettings.use_bake_multires>` option in the Render panel.
This feature compares two resolution levels of the Multiresolution modifier:

- **Viewport Levels:** Used as the *low-resolution* base mesh.
- **Render Levels:** Used as the *high-resolution* detail mesh.

The difference between these two levels is baked into a texture map.


.. _multrires-bake-types:

Bake Types
^^^^^^^^^^

The *Bake Type* determines what kind of surface information is extracted from the Multiresolution modifier.

- **Normals:**
  Bakes surface normal direction differences between the base and detailed levels.
  The resulting normal map encodes lighting information that reproduces fine sculpted detail
  in shading without modifying the actual geometry.
  Ideal for use with normal-mapped materials in Cycles, Eevee, and real-time engines.

- **Displacement:**
  Bakes height differences between the base and high-resolution mesh as a grayscale image.
  Lighter areas represent raised regions and darker areas represent recessed areas.
  This map can be used for *true* displacement in render engines or for parallax/height-based shading.

- **Vector Displacement:**
  Bakes 3D displacement vectors representing the full spatial offset from the base to the detailed surface.
  Unlike regular displacement, this method can capture overhangs and non-vertical displacements,
  providing a more accurate representation of complex sculpted details.

  The resulting texture encodes XYZ displacement in the RGB color channels.

.. important::

   To ensure a correct bake:

   - Set the **Viewport Levels** of the Multiresolution modifier to **0**, so the base mesh is truly low-resolution.
   - Set the **Render Levels** to the highest sculpt level that contains the desired detail.
   - The object must have proper **UV unwrapping** and a selected **Image Texture** node in the Shader Editor
     to receive the baked map.

   If the Viewport Level is higher than 0, part of the sculpted displacement will already be applied,
   resulting in incorrect bakes.

.. tip::

   - Use 16-bit or 32-bit image formats (e.g., OpenEXR or TIFF) for displacement or vector displacement maps
     to preserve precision.
   - Always verify that the image's color space is set to *Non-Color* in the Image Editor or Shader Editor.

.. seealso::

   For more details on general baking settings and workflow, see :doc:`/render/cycles/baking`.
