**************
Brush Settings
**************

Each mode and brush has unique brush settings.
But there is also a lot of overlap or similar settings.
This page explains general and mode specific settings that are used across various brushes in more detail.

Changes to the settings of a brush asset are temporary and will be discarded when Blender is closed. To preserve
settings, save them to the currently active brush asset using *Save Changes to Asset*, or create a new brush asset
using *Duplicate Asset*, see :ref:`Asset Operators <brush-management-utility-operators>`. Loading a different file
while Blender remains open does not discard the settings.


Unified Settings
================

Some settings (e.g. size, strength, color), indicated with :bl-icon:`brushes_all`,
allow for using a per-mode setting instead of the individual brush setting.
These settings are shared across all brushes of a given mode (e.g. Sculpt Mode)
but do not overwrite the individual brush value.


.. _sculpt-tool-settings-brush-settings-general:

General
=======

.. _bpy.types.Brush.size:

Size
   This option controls the size of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by
   dragging the mouse from left to right and then :kbd:`LMB` to accept.
   Meanwhile the texture of the brush will be visible inside the circle.
   You can also enter the size numerically with the number keys.

   The size can be decreased/increased using :kbd:`[` and :kbd:`]` respectfully.

   :bl-icon:`stylus_pressure` (Size Pressure)
      Adjusts the size based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
   :bl-icon:`brushes_all` (Use Unified Size)
      Use the same brush *Size* across all brushes.
   :bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` (Expand/Collapse)
      Show or hide the customizable pressure curve.

      Custom Curve
         By default this is a straight line with positive slope such that
         increased pressure results in a larger brush size.

         For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.

Size Unit :guilabel:`Sculpt Mode`
   Controls how the brush *Size* is measured.

   :View:
      The *Size* is measured based on how the cursor appears on the monitor i.e. "screen space".
   :Scene:
      The *Size* is measured based on real world units.
      This means that the brush size stays consistent, independently from zooming in and out in the viewport.
      The unit type and scaling can be configured in the :ref:`Scene Units <bpy.types.UnitSettings>`.

.. _bpy.types.Brush.strength:

Strength
   For painting brushes the *Strength* defines the maximum effect of each brush stroke.
   For example, higher values cause a *Paint* brush to give each stroke a higher opacity.
   The opacity is never stronger than the set *Strength*,
   no matter how often the same surface is painted during the same stroke.

   For sculpting brushes on the other hand the *Strength* relates to how strong each step of the stroke is,
   resulting in a slower/faster buildup towards the full brush effect during the stroke.

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   and then moving the brush and then :kbd:`LMB`.
   You can also enter the strength numerically with the number keys.

   :bl-icon:`stylus_pressure` (Strength Pressure)
      Adjusts the strength based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
   :bl-icon:`brushes_all` (Use Unified Strength)
      Use the same brush *Strength* across all brushes.
   :bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` (Expand/Collapse)
      Show or hide the customizable pressure curve.

      Custom Curve
         By default this is a straight line with positive slope such that
         increased pressure results in a stronger brush deformation.

         For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.

Blend
   Set the way the color or value is applied over the targeted Color Attribute, Vertex Group or Image Texture.
   See :term:`Color Blend Modes`.

   - Add Alpha: makes the image more opaque where painted.
   - Erase Alpha: makes the image transparent where painted,
     allowing background colors and lower-level textures to show through.
     As you "paint", the false checkerboard background will be revealed.
     Using a tablet pen's eraser end will toggle on this mode.

   .. tip::

      In order to see the effects of the Erase and Add Alpha mix modes in the Image Editor,
      the :ref:`Display Channels <bpy.types.SpaceImageEditor.display_channels>`
      must be set to *Color & Alpha* or *Alpha*.
      Transparent (no alpha) areas will then show a checkered background.

Weight :guilabel:`Weight Paint`
   The weight value that is applied to the vertex group.

   Use :kbd:`Shift-X` to sample the weight value of clicked vertex.
   :kbd:`Shift-Ctrl-X` lets you select the group from which to sample from.

.. _bpy.types.Brush.direction:

Direction :kbd:`Ctrl` :guilabel:`Sculpt Mode`
   Brush direction toggle, *Add* raises geometry towards the brush,
   *Subtract* lowers geometry away from the brush. This setting can be toggled with :kbd:`Ctrl` while sculpting.

.. _bpy.types.Brush.normal_radius_factor:

Normal Radius :guilabel:`Sculpt Mode`
   Determines the ratio of how much the brush radius is used to
   sample the normal direction of the sculpt plane of the brush.
   For example, a smaller *Normal Radius* will lead to drastic changes in the brush orientation,
   like for following the contours of hard surface meshes more closely.
   A large *Normal Radius* will lead to smoother changes in orientation,
   like for building overall forms on organic sculptures.

.. _bpy.types.Brush.area_radius_factor:

Area Radius
   The ratio between the brush radius and
   the radius that is going to be used to sample the area plane depth.

.. _bpy.types.Brush.tilt_strength_factor:

Tilt Strength :guilabel:`Sculpt Mode`
   Determines how much the tilt of the user's tablet pen affects the brush normal.
   Negative values correspond to inverting the direction of the tilt.

.. _bpy.types.Brush.hardness:

Hardness :guilabel:`Sculpt Mode`
   How close the brush falloff starts from the edge of the brush.

.. _bpy.types.Brush.tip_roundness:

Tip Roundness
   The factor to control how round the brush is. A value of zero will make the brush square.
   Note, the :doc:`Brush Falloff </sculpt_paint/brush/falloff>`
   is only applied to the rounded portions of the brush.

.. _bpy.types.Brush.auto_smooth_factor:

Auto-smooth :guilabel:`Sculpt Mode`
   Sets the amount of smoothing to be applied to each stroke.

.. _bpy.types.Brush.topology_rake_factor:

Topology Rake :guilabel:`Sculpt Mode`
    The higher this setting is set, the more :doc:`Dyntopo </sculpt_paint/sculpting/tool_settings/dyntopo>`
    aligns mesh edges to the brush direction while tessellating the surface.
    This generates cleaner edge flow to help define sharp features.
    *Topology Rake* can have a severe performance impact so it works best on low-poly meshes.

    .. figure:: /images/sculpt-paint_sculpting_tool-settings_dyntopo_topology-rake.jpg

Normal Weight :kbd:`Ctrl` :guilabel:`Sculpt Mode`
   Constrains brush movement along the surface normal.
   Especially useful with the *Grab* brush, can be temporarily enabled by holding :kbd:`Ctrl`.
   E.g. *Grab* brush can be used to push a depression (hole) into the mesh when *Normal Weight* is set.

   Applies to *Grab* and *Snake Hook* brushes.

Plane Offset :guilabel:`Sculpt Mode`
   Offset for planar brushes (Clay, Fill, Flatten, Scrape),
   shifts the plane that is found by averaging the faces above or below.

Plane Trim :guilabel:`Sculpt Mode`
   Ability to limit the distance that planar brushes act.
   If trim is enabled vertices that are further away from the offset plane than
   the trim distance are ignored during sculpting.

.. _bpy.types.Brush.crease_pinch_factor:

Pinch/Magnify :guilabel:`Sculpt Mode`
   Pushes the mesh towards/away from the brush center during the stroke.

.. _bpy.types.Brush.deform_target:

Deformation Target
   How the deformation of the brush will affect the object.

   :Geometry: Deform the geometry directly.
   :Cloth Simulation:
      Deform the mesh while a :doc:`cloth simulation </sculpt_paint/sculpting/brushes/cloth>`
      is applied to it at the same time.


.. _sculpt-tool-settings-brush-settings-advanced:

Advanced
========

.. _sculpt-tool-settings-brush-type:

Brush Type
   Defines the basic behavior and the available settings. Through the settings of
   a brush type, brushes can be created that produce vastly different effects.

   The *Essentials* asset library contains brushes for each of the brush types. Their preview image
   and description should give a good idea of the effect the brush produces, with the particular
   combination of brush type and settings. Because of this, they are usually the more useful starting
   point for custom brushes than the mere brush type is, which is why the brush type is part of the
   *Advanced* brush settings.

   Brushes and Brush Types of each mode:

   - :doc:`Sculpt </sculpt_paint/sculpting/brushes/brushes>`
   - :doc:`Vertex Paint </sculpt_paint/vertex_paint/brushes>`
   - :doc:`Weight Paint </sculpt_paint/weight_paint/brushes>`
   - :doc:`Texture Paint </sculpt_paint/texture_paint/brushes>`

Accumulate
   Causes stroke dabs to accumulate on top of each other.

Front Faces Only
   When enabled, the brush only affects vertices that are facing the viewer.

Affect Alpha :guilabel:`2D Painting Only`
   When this is disabled, it prevents changes to the alpha channel while painting (Only in 3D Viewport).

Anti-Aliasing :guilabel:`2D Painting Only`
   Toggles :term:`Anti-Aliasing` around the brush,
   this is useful if you are working with pixel art or low resolution textures.

.. _bpy.types.Brush.use_automasking_topology:
.. _bpy.types.Brush.use_automasking_boundary_face_sets:
.. _bpy.types.Brush.use_automasking_boundary_edges:
.. _bpy.types.Brush.use_automasking_cavity:
.. _bpy.types.Brush.use_automasking_cavity_inverted:
.. _bpy.types.Brush.use_automasking_view_normal:
.. _bpy.types.Brush.use_automasking_start_normal:
.. _bpy.types.Brush.automasking:

Auto-Masking :guilabel:`Sculpt Mode`
   The auto-masking toggles in the brush settings are the same as the sculpt mode auto-masking settings.
   The difference is that these toggles can be customized per brush to create specific brush behaviors.

.. seealso::

   For more information on the Auto-Masking toggles, see :doc:`Auto-Masking </sculpt_paint/sculpting/controls>`.

.. _bpy.types.Brush.sculpt_plane:

Sculpt Plane :guilabel:`Sculpt Mode`
   Use this menu to set the plane in which the sculpting takes place.
   In other words, the primary direction that the vertices will move.

   :Area Plane:
      The movement takes place in the direction of average normal for all active vertices within the brush area.
      Essentially, this means that the direction is dependent on the surface beneath the brush.
   :View Plane:
      Sculpting in the plane of the current 3D Viewport.
   :X, Y, Z Plane:
      The movement takes place in the positive direction of one of the global axes.

.. _bpy.types.Brush.use_original_normal:
.. _bpy.types.Brush.use_original_plane:

Original :guilabel:`Sculpt Mode`
   Normal
      When locked it keeps using the normal of the surface where stroke was initiated,
      instead of the surface normal currently under the cursor.
   Plane
      When locked keep using the plane origin of surface where stroke was initiated,
      instead of the surface plane currently under the cursor.


Color Picker
============

.. _bpy.types.UnifiedPaintSettings.secondary_color:
.. _bpy.types.UnifiedPaintSettings.color:
.. _bpy.types.Brush.secondary_color:
.. _bpy.types.Brush.color:

.. rubric:: Color

Brushes have two colors that can be set using the :ref:`ui-color-picker`:

- **Primary Color**: The active color used for painting by default.
- **Secondary Color**: An alternate color that can be quickly accessed.

By default, painting uses the primary color. The secondary color can be used temporarily by holding :kbd:`Ctrl` while
painting. The two colors can also be swapped at any time using
:ref:`Swap Colors <bpy.ops.paint.brush_colors_flip>`.

.. _bpy.ops.paint.sample_color:

.. tip::

   - Press :kbd:`Shift-X` to sample a color at the mouse cursor position.
   - Press :kbd:`Shift-Ctrl-X` to sample the **merged viewport color**,
     including lighting, shading, and all visible layers.

   The sampled color becomes the primary color of the active Paint brush.

.. _bpy.ops.paint.brush_colors_flip:

:bl-icon:`file_refresh` (Swap Colors) :kbd:`X`
   Swaps the primary and secondary colors.

.. _bpy.types.UnifiedPaintSettings.use_unified_color:

:bl-icon:`brushes_all` (Use Unified Color)
   Use the same brush color across all brushes.

.. note::

   Note that Vertex Paint works in sRGB :term:`space <Color Space>`, and
   the RGB representation of the same colors will be different between the paint
   tools and the materials that are in linear space.

.. rubric:: Gradient

A gradient can be used as a color source.

Gradient Colors
   The :ref:`ui-color-ramp-widget` to define the gradient colors.
Mode
   :Pressure:
      Will choose a color from the color ramp according to the stylus pressure.
   :Clamp:
      Will alter the color along the stroke and as specified by *Gradient Spacing* option.
      With *Clamp* it uses the last color of the color ramp after the specified gradient.
   :Repeat:
      Similar to *Clamp*. After the last color it resets the color to the first color in the color ramp and
      repeats the pattern.


.. _bpy.types.UnifiedPaintSettings.use_color_jitter:

Randomize Color
---------------

Applies random variation to the brush color for more natural and varied strokes.
Useful for hand-painting textures or adding subtle irregularities.

.. _bpy.types.UnifiedPaintSettings.use_stroke_random*:
.. _bpy.types.UnifiedPaintSettings.use_random_press*:

The randomness can affect hue, saturation, and value independently.
Each channel also supports pressure sensitivity and stroke-based randomness.

.. _bpy.types.UnifiedPaintSettings.hue_jitter:

Hue
   Amount of random variation applied to the hue of the brush color.

   :bl-icon:`gp_select_strokes` (Stroke Random)
      Apply a single random hue per stroke instead of varying continuously during the stroke.
   :bl-icon:`stylus_pressure` (Use Pressure)
      Modulate hue variation based on pen pressure.

.. _bpy.types.UnifiedPaintSettings.saturation_jitter:

Saturation
   Amount of random variation applied to the saturation of the brush color.

   :bl-icon:`gp_select_strokes` (Stroke Random)
      Apply a single random saturation per stroke instead of varying continuously during the stroke.
   :bl-icon:`stylus_pressure` (Use Pressure)
      Modulate saturation variation based on pen pressure.

.. _bpy.types.UnifiedPaintSettings.value_jitter:

Value
   Amount of random variation applied to the value (brightness) of the brush color.

   :bl-icon:`gp_select_strokes` (Stroke Random)
      Apply a single random value per stroke instead of varying continuously during the stroke.
   :bl-icon:`stylus_pressure` (Use Pressure)
      Modulate value variation based on pen pressure.


Color Palette
=============

Color Palettes are a way of storing a brush's color so that it can be used at a later time.
This is useful when working with several colors at once.

Palette
   A :ref:`ui-data-block` to select a palette.

:bl-icon:`add` (New Pallet Color)
   Adds the current brush's primary *Color* to the palette.

:bl-icon:`remove` (Delete Pallet Color)
   Removes the currently selected color from the palette.

:bl-icon:`tria_up`/:bl-icon:`tria_down` (Move Pallet Color)
   Moves the selected color up/down one position.

:bl-icon:`sortsize` (Sort By)
   Sort Colors by Hue, Saturation, Value, Luminance.

Color List
   Each color that belongs to the palette is presented in a list.
   Clicking on a color will change the brush's primary *Color* to that color.
