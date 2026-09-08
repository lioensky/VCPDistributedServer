.. _bpy.types.RenderLayer:

******
Passes
******

.. reference::

   :Panel:     :menuselection:`Properties --> View Layer --> Passes`

A *Pass* is a type of intermediate rendering information that's extracted as a separate image.
Examples include the diffuse colors of the objects in the scene, the light distribution,
the depth map, and the normal map.

These images can be accessed using the :doc:`/compositing/types/input/scene/render_layers`
in the :doc:`/editors/compositor` and combined in a custom way that replaces the standard one.


.. _render_layers_passes_data:

Data
====

Include
   .. _bpy.types.ViewLayer.use_pass_combined:

   Combined :guilabel:`Cycles`, :guilabel:`EEVEE`, :guilabel:`Workbench`
      The render output before any compositing is applied.

   .. _bpy.types.ViewLayer.use_pass_z:

   Depth :guilabel:`Cycles`, :guilabel:`EEVEE`, :guilabel:`Workbench`
      Distance to the nearest visible surface.
      Can be used with the :doc:`/compositing/types/filter/blur/defocus`
      for a fake :term:`Depth of Field` effect.

      .. note::

         This pass produces noisy results if the render itself uses Depth of Field
         or motion blur. Use the Mist pass for a cleaner image.

   .. _bpy.types.ViewLayer.use_pass_mist:

   Mist :guilabel:`Cycles`, :guilabel:`EEVEE`
      Distance to the nearest visible surface, mapped to the 0.0 - 1.0 range.
      When enabled, settings become available in the
      :ref:`World tab <bpy.types.WorldMistSettings>`.

      This pass can be used to fade out objects that are farther away.
      An alternative is using the *Volume* slot of the
      :doc:`World Output </render/shader_nodes/output/world>` shading node.

   .. _bpy.types.ViewLayer.use_pass_position:

   Position :guilabel:`Cycles`, :guilabel:`EEVEE`
      Positions in world space.

   .. _bpy.types.ViewLayer.use_pass_normal:

   Normal :guilabel:`Cycles`, :guilabel:`EEVEE`
      Surface normals in world space.

   .. _bpy.types.ViewLayer.use_pass_vector:

   Vector :guilabel:`Cycles`, :guilabel:`EEVEE`
      Motion vectors for the :doc:`/compositing/types/filter/blur/vector_blur`.
      The four components consist of 2D vectors giving the screen-space motion
      based on the next and previous frames.

      This pass is disabled when :ref:`Motion Blur <bpy.types.RenderSettings.use_motion_blur>` is enabled.

   .. _bpy.types.ViewLayer.use_pass_uv:

   UV :guilabel:`Cycles`
      The UV coordinates within each object's
      :ref:`active UV map <bpy.types.MeshUVLoopLayer.active_render>`,
      represented through the red and green channels of the image.
      (The blue channel stores a constant value of 1 and does not hold any information.)
      Can be used with the :doc:`/compositing/types/transform/map_uv`.

   .. _bpy.types.ViewLayer.use_pass_grease_pencil:

   Grease Pencil :guilabel:`Cycles`, :guilabel:`EEVEE`, :guilabel:`Workbench`
      Outputs only the visible (non-occluded) strokes and fills from the
      :doc:`Grease Pencil </grease_pencil/index>` engine into a separate image layer.

      This pass is useful for compositing workflows where you want to isolate, enhance, or apply
      effects to Grease Pencil elements separately from the rest of the render.

      .. note::

         For most scenes, blending this pass over the rest of the image
         using an *Alpha Over* node will reproduce the *Combined* render result.
         However, some blending modes in Grease Pencil can modify the chromaticity of the alpha channel.
         In these cases, compositing the *Grease Pencil* pass separately can produce different results.

   Denoising Data :guilabel:`Cycles`
      Includes *Denoising Albedo*, *Denoising Normal*, and the combined image
      before denoising. Can be used with the :doc:`/compositing/types/filter/denoise`
      as a replacement for :ref:`automatic denoising <render-cycles-settings-viewport-denoising>`.

Indexes
   .. _bpy.types.ViewLayer.use_pass_object_index:

   Object Index :guilabel:`Cycles`
      A map where each pixel stores the user-defined ID of the object at that pixel.
      This map can be converted into a mask for a particular object using the
      :doc:`/compositing/types/mask/id_mask`.

   .. _bpy.types.ViewLayer.use_pass_material_index:

   Material Index :guilabel:`Cycles`
      A map where each pixel stores the user-defined ID of the material at that pixel.
      This map can be converted into a mask for a particular material using the
      ID Mask Node.

.. note:: The Depth, Position, Object Index, and Material Index passes are not anti-aliased.

Debug
   Render Time :guilabel:`Cycles`
      An estimate for how long in milliseconds each pixel took to render.
      Note, this pass is not supported on GPU rendering.
   Sample Count :guilabel:`Cycles`
      Number of samples calculated for each pixel, divided by the maximum number of samples.
      Used to analyze :ref:`adaptive sampling <bpy.types.CyclesRenderSettings.use_adaptive_sampling>`.

.. _bpy.types.ViewLayer.pass_alpha_threshold:

Alpha Threshold :guilabel:`Cycles`
   The Depth, Position, Normal, Vector, UV, and Index passes are only affected by surfaces with an opacity
   equal to or higher than this threshold. With value 0.0, the first surface hit will always write to these passes
   regardless of opacity. With higher values, surfaces that are mostly transparent will be skipped until
   an opaque surface is encountered.


Light
=====

Cycles
------

Diffuse
   .. _bpy.types.ViewLayer.use_pass_diffuse_direct:

   Direct
      The intensity and color of light that hit a surface with a Diffuse or Subsurface
      Scattering BSDF and did not yet bounce off/pass through any other surface
      (ignoring :doc:`Transparent </render/shader_nodes/shader/transparent>` ones).
      The color of the surface itself is not included.

   .. _bpy.types.ViewLayer.use_pass_diffuse_indirect:

   Indirect
      The intensity and color of light that hit a surface with a Diffuse or Subsurface
      Scattering BSDF and already bounced off/passed through another surface before
      (ignoring Transparent ones).
      The color of the surface itself is not included.

   .. _bpy.types.ViewLayer.use_pass_diffuse_color:

   Color
      The colors of Diffuse and Subsurface Scattering BSDFs,
      modified by any :doc:`Mix </render/shader_nodes/shader/mix>` and
      :doc:`Add </render/shader_nodes/shader/add>` Shader nodes.
      The intensity and color of light are not included.

.. _bpy.types.ViewLayer.use_pass_glossy_direct:
.. _bpy.types.ViewLayer.use_pass_glossy_indirect:
.. _bpy.types.ViewLayer.use_pass_glossy_color:

Glossy
   Direct, Indirect, Color
      Same as above, but for glossy BSDFs.

.. _bpy.types.ViewLayer.use_pass_transmission_direct:
.. _bpy.types.ViewLayer.use_pass_transmission_indirect:
.. _bpy.types.ViewLayer.use_pass_transmission_color:

Transmission
   Direct, Indirect, Color
      Same as above, but for transmissive BSDFs.

      The *Transparent* BSDF is not included; see :doc:`/render/cycles/render_settings/light_paths`
      for details. To create a transparent surface that does get included in this pass,
      use a :doc:`/render/shader_nodes/shader/glass` with the IOR set to 1.

Volume
   Direct, Indirect
      Same as above, but for volumetric BSDFs.

Other
   .. _bpy.types.ViewLayer.use_pass_emit:

   Emission
      Emission from directly visible surfaces.

   .. _bpy.types.ViewLayer.use_pass_environment:

   Environment
      Emission from the directly visible :doc:`/render/lights/world`. When the
      :doc:`/render/cycles/render_settings/film` is set to Transparent (meaning the world is excluded
      from the final render), this pass can be used to get the environment color and composite it back in.

   .. _bpy.types.ViewLayer.use_pass_ambient_occlusion:

   Ambient Occlusion
      Ambient occlusion from directly visible surfaces. This is a grayscale pass with values that go
      from 0 (fully occluded) to 1 (fully exposed), making it suitable for multiplying with a color
      image in the Compositor (see :doc:`/compositing/types/color/mix_color`).

      As an alternative to this pass, it's also possible to use the
      :doc:`/render/shader_nodes/input/ao` in materials.

   Shadow Catcher
      Shadows collected by objects with the :ref:`bpy.types.Object.is_shadow_catcher` option enabled.
      Can be multiplied with existing footage to (for example) have a rendered object cast a shadow
      on recorded ground.


EEVEE
-----

Diffuse
   Light
      The intensity and color of light that hit a surface with a Diffuse or Subsurface
      Scattering BSDF. The color of the surface itself is not included.
   Color
      The colors of Diffuse and Subsurface Scattering BSDFs,
      modified by any :doc:`Mix </render/shader_nodes/shader/mix>` and
      :doc:`Add </render/shader_nodes/shader/add>` Shader nodes.
      The intensity and color of light are not included.

Specular
   Light, Color
      Same as above, but for specular BSDFs.

.. _bpy.types.ViewLayerEEVEE.use_pass_volume_direct:

Volume
   Light
      Contains :doc:`Volume objects </modeling/volumes/introduction>`, as well as any
      volumes generated by the volume shader nodes
      (:doc:`/render/shader_nodes/shader/volume_principled`,
      :doc:`/render/shader_nodes/shader/volume_absorption`,
      and :doc:`/render/shader_nodes/shader/volume_scatter`), whether they're
      used in a material or in the World background.

Other
   Emission
      Emission from directly visible surfaces.
   Environment
      Emission from the directly visible :doc:`/render/lights/world`. When the
      :doc:`/render/cycles/render_settings/film` is set to Transparent (meaning the world is excluded
      from the final render), this pass can be used to get the environment color and composite it back in.
   Shadow
      A pass that's black for areas that don't receive direct light and white for ones that do.
      Mostly useful for compositing objects with shadow into existing footage.
   Ambient Occlusion
      Ambient occlusion from directly visible surfaces. This is a grayscale pass with values that go
      from 0 (fully occluded) to 1 (fully exposed), making it suitable for multiplying with a color
      image in the Compositor (see :doc:`/compositing/types/color/mix_color`).

      As an alternative to this pass, it's also possible to use the
      :doc:`/render/shader_nodes/input/ao` in materials.

   .. _bpy.types.ViewLayerEEVEE.use_pass_transparent:

   Transparent
      Contains :ref:`Blended <bpy.types.Material.surface_render_method>` surfaces,
      so they can be adjusted in the Compositor and later mixed with opaque passes.

      This pass only supports grayscale opacity.
      Colored opacity will show differently than in the Combined pass.

.. _bpy.types.ViewLayerEEVEE.ambient_occlusion_distance:

Occlusion Distance
   Maximum distance for objects to contribute to the Ambient Occlusion pass.

.. _render_layers_passes_cryptomatte:

Cryptomatte
===========

Cryptomatte is an image standard to efficiently create masks for specific objects or materials.
Its purpose is the same as the *Object Index* and *Material Index* passes,
but it has several advantages: it's easier to set up, can be used with other
compositing software than Blender, and supports multiple objects per pixel.
Specifically, it works with transparency, as well as motion blur and depth of field
when using Cycles.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_object:

Object
   Render cryptomatte passes for isolating objects.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_material:

Material
   Render cryptomatte passes for isolating materials.

.. _bpy.types.ViewLayer.use_pass_cryptomatte_asset:

Asset
   Render cryptomatte passes for isolating groups of objects with
   the same :doc:`parent </scene_layout/object/editing/parent>`.
   This option is not related to Blender's
   :doc:`asset </files/asset_libraries/introduction>` feature.

.. _bpy.types.ViewLayer.pass_cryptomatte_depth:

Levels
   The maximum number of objects to be distinguished per pixel.
   The Render Layers node will output half this many Cryptomatte images,
   named (for example) *CryptoObject00*, *CryptoObject01* and so on --
   the reason being that one Cryptomatte image can reference two objects per pixel.

   The first image references, for each pixel, the two objects that contribute
   the most to that pixel's color. The next image references the next two objects,
   and so on.

.. seealso::

   :doc:`/compositing/types/mask/cryptomatte`


.. _bpy.ops.scene.view_layer_add_aov:
.. _bpy.ops.scene.view_layer_remove_aov:
.. _bpy.types.AOV:

Shader AOV
==========

Shader AOVs (Arbitrary Output Variables) are custom render passes that can hold additional
information for use in compositing. Create a pass in the *Shader AOV* panel,
write to it from a material using the :doc:`/render/shader_nodes/output/aov`,
and finally read from it in the Compositor using the socket on the Render Layers node.

.. _bpy.types.ViewLayer.active_aov_index:

Name
   The name of the render pass. Used in both the AOV Output node and the
   Render Layers node. The name can be anything as long as it doesn't conflict
   with other (enabled) passes.

.. _bpy.types.AOV.type:

Data Type
   The type of data that the render pass stores per pixel.
   Use *Color* to store a color, normal, or other type of vector.
   Use *Value* to store a single number.


.. _bpy.ops.scene.view_layer_add_lightgroup:
.. _bpy.ops.scene.view_layer_remove_lightgroup:

Light Groups
============

:guilabel:`Cycles only`

A Light Group provides a limited *Combined* render pass where the scene is only illuminated by
certain lights. Multiple such passes can then be combined in compositing to construct a full render
with all the lights. The most straightforward way is to simply *Add* them together using
the :doc:`/compositing/types/color/mix_color`, but by making more complex combinations,
it's possible to change the color and intensity of individual lights without having to re-render.

To assign a Light object to a new or existing Light Group, use the panel
:menuselection:`Object --> Shading --> Light Group` (:ref:`details <bpy.types.Object.lightgroup>`).

To assign the World background to a Light Group, use the panel
:menuselection:`World --> Settings --> Light Group` (:ref:`details <bpy.types.World.lightgroup>`).

.. _bpy.types.ViewLayer.active_lightgroup_index:

Name
   The name of the light group.


Light Group Sync
----------------

These operators are available from the :bl-icon:`downarrow_hlt` button to the right of the
Light Group list.

.. _bpy.ops.scene.view_layer_add_used_lightgroups:

Add Used Lightgroups
   Create Light Groups for any lights that reference a non-existing one.

.. _bpy.ops.scene.view_layer_remove_unused_lightgroups:

Remove Unused Lightgroups
   Delete any Light Groups that are not referenced by any lights.


Combining
=========

Cycles
------

The different render passes can be combined to produce the final image as follows:

.. figure:: /images/render_layers_passes_combine.svg


EEVEE
-----

The passes can be combined to produce the final image as follows:

.. figure:: /images/render_layers_passes_eevee-combine.svg


EEVEE Limitations
=================

- :ref:`bpy.types.CameraDOFSettings` and :doc:`/render/eevee/render_settings/motion_blur`
  are not rendered in passes other than *Combined*.
  They can be emulated in the Compositor using the :doc:`/compositing/types/filter/blur/defocus`
  and the :doc:`/compositing/types/filter/blur/vector_blur`.
- Transparent materials that have their :ref:`bpy.types.Material.surface_render_method`
  set to *Blended* are not rendered in passes other than *Combined* and *Transparent*.
  Use the *Dithered* method instead.
- The :doc:`/render/shader_nodes/color/shader_to_rgb` only works correctly
  in the *Combined* pass as EEVEE excludes parts of the BSDF equation.
- There is a maximum of 16 *Color* and 16 *Value* AOVs (custom render passes).
