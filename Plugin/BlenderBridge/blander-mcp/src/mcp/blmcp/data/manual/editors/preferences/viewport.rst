********
Viewport
********

.. figure:: /images/editors_preferences_section_viewport.webp

   Blender Preferences Viewport section.


Display
=======

.. _bpy.types.PreferencesView.show_object_info:

Text Info Overlay
   Object Info
      Display the active Object name and frame number at the top left of the 3D Viewport.

   .. _bpy.types.PreferencesView.show_view_name:

   View Name
      Display the name and type of the current view in the top left corner of the 3D Viewport.
      For example: "User Perspective" or "Top Orthographic".

.. _bpy.types.PreferencesView.show_playback_fps:

Playback Frame Rate (FPS)
   Show the frames per second screen refresh rate while an animation is played back.
   It appears in the top left of the 3D Viewport, displaying red if the frame rate set cannot be reached.

   .. _bpy.types.PreferencesView.playback_fps_samples:

   Frame Rate Samples
      Calculate the FPS displayed in the viewport based on an average of the current and previously displayed frames.
      A value of zero uses the number of frames in 1.0 second.

      - More samples represent the average FPS over a longer period of time,
        however sudden changes to performance result in a more gradual increase/decrease over time.
      - Fewer samples shows an FPS which more closely matches the actual performance,
        however the value may jitter - making the FPS difficult to comprehend.

.. _bpy.types.PreferencesView.gizmo_size:

Gizmo Size
   Diameter of the gizmo.

.. _bpy.types.PreferencesView.lookdev_sphere_size:

HDRI Preview Size
   Diameter of the HDRI sphere overlay.

.. _bpy.types.PreferencesView.mini_axis_type:

3D Viewport Axes
   :Interactive Navigation:
      Display the axis as an interactive gizmo.
      Click sets the viewport to display along this axis and dragging orbits the view.
   :Simple Axes:
      Display simple, less intrusive axis in the viewport.

      .. _bpy.types.PreferencesView.mini_axis_brightness:

      Brightness
         How vivid the colors of the simple axis are.
   :Off:
      Disables the viewport axis.

.. _bpy.types.PreferencesView.gizmo_size_navigate_v3d:

Size
   Diameter of the *3D Viewport Axis* widget.

.. _bpy.types.PreferencesView.use_fresnel_edit:

Fresnel -- Edit Mode
      Enable a fresnel effect on edit mesh overlays.
      It improves shape readability of very dense meshes, but increases eye fatigue when modeling lower poly.


.. _prefs-system-multisampling:

Quality
=======

.. _bpy.types.PreferencesSystem.viewport_aa:

Viewport Anti-Aliasing
   Control the :term:`Anti-Aliasing` for higher quality rendering.

.. _bpy.types.PreferencesSystem.use_overlay_smooth_wire:

Smooth Wires
   Overlay
      Display overlays with smooth wire, without this wires will be rendered aliased.
      To increase the visibility you can disable this for Edit Mode specificity (see below),
      since edges do not blend into other shaded regions.

   .. _bpy.types.PreferencesSystem.use_edit_mode_smooth_wire:

   Edit Mode
      Display smooth wire in Edit Mode, without this wires will be rendered aliased.


Textures
========

.. _bpy.types.PreferencesSystem.gl_texture_limit:

Limit Size
   Limit the maximum resolution for pictures used in textured display to save memory.
   The limit options are specified in a square of pixels
   (e.g: the option 256 means a texture of 256×256 pixels). This is useful for game engineers,
   whereas the texture limit matches paging blocks of the textures in the target graphic card memory.

.. _bpy.types.PreferencesSystem.anisotropic_filter:

Anisotropic Filtering
   Sets the level of anisotropic filtering.
   This improves the quality of textures that are rendered at the cost of performance.

.. _bpy.types.PreferencesSystem.gl_clip_alpha:

Clip Alpha
   Clip alpha below this threshold in the 3D Viewport.
   Note that, the default is set to a low value to prevent issues on some GPUs.

.. _bpy.types.PreferencesSystem.image_draw_method:

Image Display Method
   Method to render images; the following options are supported:

   :Automatic:
      Automatically use *GLSL* which runs on the GPU for performance but falls back to
      the CPU for large images which might be slow when loaded with the GPU.
   :2D Texture:
      Uses CPU for display transform and render images as a 2D texture.
   :GLSL:
      Fastest method using GLSL for display transform and render images as a 2D texture.


Subdivision
===========

.. _bpy.types.PreferencesSystem.use_gpu_subdivision:

GPU Subdivision
   Under certain circumstances, the GPU will be used to subdivide a mesh with a
   :doc:`Subdivision Surface modifier </modeling/modifiers/generate/subdivision_surface>`.
   This typically results in increased subdivision performance.
   
.. note::

   When enabled, normals and tangents are interpolated instead of being recomputed after smoothing.
   This can result in a change in shading compared to the CPU implementation.

.. note::

   This feature is not supported on Qualcomm GPUs on Windows
