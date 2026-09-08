.. _bpy.types.BakeSettings:

*************
Render Baking
*************

Cycles shaders and lighting can be baked to image textures.
This has a few different purposes, most commonly:

- Baking textures like base color or normal maps for export to game engines.
- Baking ambient occlusion or procedural textures,
  as a base for texture painting or further edits.
- Creating light maps to provide global illumination or speed up rendering in games.


Setup
=====

Baking requires a mesh to have a UV map, and either a Color Attribute
or an Image Texture node with an image to be baked to.
The :term:`Active` :doc:`Image Texture </render/shader_nodes/textures/image>`
node or :doc:`Color Attribute </sculpt_paint/vertex_paint/index>` is used as the baking target.

Use Render Bake in intensive light/shadow solutions,
such as AO or soft shadows from area lights. If you bake AO for the main objects,
you will not have to enable it for the full render, saving render time.
Cycles uses the render settings (samples, bounces, ...) for baking.
This way the quality of the baked textures should match the result you get from the rendered scene.


Settings
========

.. reference::

   :Panel:     :menuselection:`Render --> Bake`

.. _bpy.ops.object.bake:

Bake
   Executes the bake operation using the current settings.

.. _bpy.types.RenderSettings.use_bake_multires:

Bake from Multires
   Bakes a *Normal* or *Displacement* map directly from a mesh that has a
   :doc:`Multiresolution Modifier </modeling/modifiers/generate/multiresolution>`.

   This method compares two resolution levels of the modifier:

   - *Viewport Levels* Used as the *low-resolution* base mesh.
   - *Render Levels* Used as the *high-resolution* detailed mesh.

   The resulting bake represents the difference between these two levels, allowing detailed sculpted
   information to be captured as a texture map.

   .. _bpy.types.BakeSettings.type:

   Bake Type
      Determines what kind of surface information is extracted from the Multiresolution modifier.
      See :ref:`multrires-bake-types` for more information.

      :Normals:
         Bakes surface normal direction differences between the two levels.
      :Displacement:
         Bakes height differences as a grayscale displacement map.
      :Vector Displacement:
         Bakes full 3D positional offsets as a vector displacement map.

.. _bpy.types.CyclesRenderSettings.bake_type:

Bake Type
   Type of pass to bake.

   :Combined:
      Bakes all materials, textures, and lighting except specularity.
      The passes that contribute to the combined pass can be toggled individually to form the final map.
   :Ambient Occlusion:
      Bakes ambient occlusion as specified in the World panels. Ignores all lights in the scene.
   :Shadow:
      Bakes shadows and lighting.
   :Position:
      Bakes world-space position data into RGB channels.
      Each pixel encodes the XYZ position of the surface point in the scene, relative to the scene origin.
   :Normal:
      Bakes normals to an RGB image.
   :UV:
      Mapped UV coordinates, used to represent where on a mesh a texture gets mapped too.
      This is represented through the red and green channels of the image,
      the blue channel is encoded with a constant value of 1 but does not hold any information.
   :Roughness:
      Bakes the roughness pass of a material.
   :Emit:
      Bakes Emission, or the Glow color of a material.
   :Environment:
      Bakes the environment (i.e. the world surface shader defined for the scene) onto
      the selected object(s) as seen by rays cast from the world origin.
   :Diffuse:
      Bakes the diffuse pass of a material.
   :Glossy:
      Bakes the glossiness pass of a material.
   :Transmission:
      Bakes the transmission pass of a material.

.. _bpy.types.BakeSettings.view_from:

View From
   Source of reflection ray directions.

   :Above Surface: Cast rays from above the surface.
   :Active Camera: Use the active camera's position to cast rays.


Influence
---------

.. rubric:: Combined

.. _bpy.types.BakeSettings.use_pass_direct:

Lighting
   Direct
      Add direct lighting contribution.

   .. _bpy.types.BakeSettings.use_pass_indirect:

   Indirect
      Add indirect lighting contribution.

Contributions
   .. _py.types.BakeSettings.use_pass_diffuse:

   Diffuse
      Add diffuse contribution.

   .. _bpy.types.BakeSettings.use_pass_glossy:

   Glossy
      Add glossy contribution.

   .. _bpy.types.BakeSettings.use_pass_transmission:

   Transmission
      Add transmission contribution.

   .. _bpy.types.BakeSettings.use_pass_emit:

   Emit
      Add emission contribution.


.. rubric:: Diffuse, Glossy, Transmission

Contributions
   Direct
      See :ref:`above <bpy.types.BakeSettings.use_pass_direct>`.
   Indirect
      See :ref:`above <bpy.types.BakeSettings.use_pass_indirect>`.

   .. _bpy.types.BakeSettings.use_pass_color:

   Color
      Colorize the pass.

      - If only *Color* is selected you get the pass color,
        which is a property of the surface and independent of sampling refinement.
      - If *Color* is not selected, you get the direct and/or indirect contributions in gray-scale.
      - If *Color* and either *Direct* or *Indirect* are selected,
        you get the direct and/or indirect contributions colored.


.. rubric:: Normal

.. _bpy.types.BakeSettings.normal_space:

Space
   Normals can be baked in different spaces:

   For materials, the same spaces can be chosen in the image texture options
   next to the existing *Normal Map* setting. For correct results,
   the setting here should match the setting used for baking.

   :Object:
      Normals in object coordinates, independent of object transformation, but dependent on deformation.
   :Tangent:
      Normals in tangent space coordinates, independent of object transformation and deformation.
      This is the default, and the right choice in most cases, since then the normal map can be used for
      animated objects too.

.. _bpy.types.BakeSettings.normal_r:
.. _bpy.types.BakeSettings.normal_g:
.. _bpy.types.BakeSettings.normal_b:

Swizzle R, G, B
   Axis to bake into the red, green and blue channel.


.. _bpy.types.BakeSettings.use_selected_to_active:

Selected to Active
------------------

Bake shading on the surface of selected objects to the active object.
The rays are cast from the low-poly object inwards towards the high-poly object.
If the high-poly object is not entirely involved by the low-poly object, you can tweak the rays start point with
*Max Ray Distance* or *Extrusion* (depending on whether or not you are using cage).
For even more control you can use a *Cage Object*.

.. note::

   There is a CPU fixed memory footprint for every object used to bake from.
   In order to avoid crashes due to lack of memory, the high-poly objects can be joined before the baking process.

.. _bpy.types.BakeSettings.use_cage:

Cage
   Cast rays to active object from a cage.
   A cage is a ballooned-out version of the low-poly mesh created either automatically
   (by adjusting the ray distance) or manually (by specifying an object to use).
   When not using a cage the rays will conform to the mesh normals. This produces glitches on the edges,
   but it is a preferable method when baking into planes to avoid the need of adding extra loops around the edges.

   .. _bpy.types.BakeSettings.cage_object:

   Cage Object
      Object to use as cage instead of calculating the cage from the active object with the *Cage Extrusion*.

.. _bpy.types.BakeSettings.cage_extrusion:

Cage Extrusion
   Distance to use for the inward ray cast when using *Selected to Active* and *Cage*.
   The inward rays are cast from a version of the active object with disabled Edge Split Modifiers.
   Hard splits (e.g. when the Edge Split Modifier is applied) should be avoided because they will lead to non-smooth
   normals around the edges.

   .. note::

      When the base mesh extruded does not give good results,
      you can create a copy of the base mesh and modify it to use as a *Cage*.
      Both meshes need to have the same :term:`Topology` (number of faces and face order).

.. _bpy.types.BakeSettings.max_ray_distance:

Max Ray Distance
   Distance to use for the inward ray cast when using *Selected to Active*.
   Ray distance is only available when not using *Cage*.


Output
------

.. _bpy.types.BakeSettings.target:

Target
   Where to output the baked map.

   :Image Textures:
      Bake to the image data-block associated with the active and selected
      :doc:`Image Texture </render/shader_nodes/textures/image>` node. If a material does not contain an active and
      selected image texture node, nothing will be baked for this material.

      .. _bpy.types.BakeSettings.use_clear:

      Clear Image
         If selected, clears the image before baking render.

   :Active Color Attribute:
      Bake to the :term:`Active` :doc:`Color Attributes </sculpt_paint/vertex_paint/index>` layer on the active mesh.
      Note, the active object must be a mesh as other object types do not have Color Attributes.


Margin
------

When baking to images, by default a margin is generated around UV "islands".
This is important to avoid discontinuities at UV seams, due to texture filtering and mip-mapping.

.. _bpy.types.BakeSettings.margin_type:

Type
   Method to generate the margin.

   :Extend:
      Extend border pixels outwards.

   :Adjacent Faces:
      Fill margin using pixels from adjacent faces across UV seams.

.. _bpy.types.BakeSettings.margin:

Size
   Size of the margin in pixels.
