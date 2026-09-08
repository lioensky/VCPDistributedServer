.. _bpy.types.View3DShading.type:
.. _view3d-viewport-shading:

****************
Viewport Shading
****************

.. reference::

   :Mode:      All Modes
   :Location:  :menuselection:`Header --> Viewport Shading`
   :Shortcut:  :kbd:`Z` :kbd:`Shift-Z`

Blender offers different shading modes for helping with different tasks.
For example, Solid shading is well-suited for modeling, while Rendered
is useful for setting up lighting.

The radio buttons let you change the shading mode, while the drop-down button
opens a popover with additional options described below.

Pressing :kbd:`Z` opens a pie menu for changing the shading mode.
Pressing :kbd:`Shift-Z` switches between the current shading mode and Wireframe.


.. _3dview-shading-rendered:

:bl-icon:`shading_wire` -- Wireframe
====================================

Only displays the edges (wireframes) of the objects in the scene.

.. _bpy.types.View3DShading.wireframe_color_type:

Wireframe Color
   How wireframes are colored. This affects the Wireframe shading mode and overlay.

   :Theme:
      Use the *Active Object*, *Wire*, or *Wire Edit* :doc:`theme color </editors/preferences/themes>`
      based on the object's current state.
   :Object:
      Use the color from the object's
      :ref:`Viewport Display <properties-object-viewport-display>` settings.
   :Random:
      Each object gets displayed in a random color.

.. _bpy.types.View3DShading.background_type:

Background
   How the background is displayed in the 3D Viewport.

   :Theme:
      Use the background of the theme. This can be configured in the
      :doc:`Themes Preferences </editors/preferences/themes>`
      under :menuselection:`3D Viewport --> Theme Space --> Gradient Colors`.
   :World:
      Use the color from the :doc:`World </render/lights/world>`'s Viewport Display options.
   :Custom:
      Select a custom color for the background of the 3D Viewport.

Options
-------

X-Ray :kbd:`Alt-Z`
   Make objects transparent, allowing you to see and select items that would otherwise be occluded.
   The slider controls object opacity.

Outline
   Draw an outline around objects. The color of the outline can be adjusted.


.. _3dview-shading-solid:

:bl-icon:`shading_solid` -- Solid
=================================

This mode utilizes the :doc:`Workbench Render Engine </render/workbench/introduction>` to render the 3D Viewport.
It shows solid geometry but uses simplified shading and lighting without the use of shader nodes.
Solid mode is good for modeling and sculpting, and is really useful with the multitude of
options to emphasize certain geometric features.

Lighting
   How lights are computed.

   :Flat:
      Do not calculate any lighting. The base color of the scene will be rendered.
   :Studio:
      Use studio lights to light the objects.
      The studio lights can be :ref:`configured in the preferences <prefs-lights-studio>`.
      Studio lights can follow the camera or be fixed. When fixed the angle of the lights can be adjusted.

      World Space Lighting
         Uses world space lighting so lights do not follow the view camera.
      Rotation
         The rotation of the studio lights on the Z axis.
   :MatCap:
      Use a material capture to light the objects in the scene.
      MatCaps can be flipped horizontally by clicking the Flip MatCap button.

      Custom MatCaps can be :ref:`loaded in the preferences <prefs-lights-matcaps>`.

.. _viewport_shading_solid_color:

Object Color
   The source to compute the color for objects in the viewport.

   :Material:
      Use the color that can be set per material
      in the Viewport Display :ref:`properties-material-viewport-display` panel.
   :Object:
      Use the color that can be set per object
      in the Viewport Display :ref:`properties-object-viewport-display` panel.
   :Random:
      A random color will be selected for every object in the scene.
   :Attribute:
      Display the active :ref:`Color Attribute <modeling-meshes-properties-object_data-color-attributes>`
      of an object. When an object has no active Color Attribute it will be rendered in the color set
      in the Viewport Display :ref:`properties-object-viewport-display` panel.
   :Texture:
      Show the texture from the active image texture node using the active UV map coordinates
      When an object has no active texture the object will be rendered with the settings
      in the Viewport Display :ref:`properties-material-viewport-display` panel.
   :Custom:
      Render the whole scene using a single color. The color can be chosen.

Background
   How the background is displayed in the 3D Viewport.

   :Theme:
      Use the background of the theme. This can be configured in the
      :doc:`Themes Preferences </editors/preferences/themes>`
      under :menuselection:`3D Viewport --> Theme Space --> Gradient Colors`.
   :World:
      Use the color from the :doc:`World </render/lights/world>`'s Viewport Display options.
   :Custom:
      Select a custom color for the background of the 3D Viewport.


Options
-------

Backface Culling
   Use backface culling to hide backsides of faces.

Outline
   Render the outline of objects in the viewport. The color of the outline can be adjusted.

Specular Highlighting
   Render specular highlights.

   .. note::

      Only available when Lighting is set to *Studio* lighting or when a MatCap
      has been selected that contains a specular pass.

.. _bpy.types.View3DShading.show_xray:

X-Ray :kbd:`Alt-Z`
   Render the scene transparent.
   With the slider you can control how transparent the scene should appear.

Shadow
   Renders a sharp shadow in the scene.

   Darkness
      Defines how dark the shadow should be rendered. This slider can be adjusted
      between 0 (shadow not visible) and 1 (shadow is black).

   Shadow Settings
      Direction
         Controls the direction of the light source that casts the shadows.

      Offset
         Controls the Shadow termination angle. It can be used to limit self shadowing artifacts.

      Focus
         Controls the falloff near the edge of the shadow.

Depth of Field
   Use the Depth of Field settings of the active camera in the viewport.
   Only visible when looking through the camera.

   The settings are located on :menuselection:`Properties --> Camera --> Depth of Field` panel.


Cavity
^^^^^^

Highlight ridges and valleys in the scene geometry.

Type
   Method how to calculate the cavity.

   :World: More precise but is slower to calculate.
   :Screen: Fast but does not take the size of the ridges and valleys into account.
   :Both: Both will use both methods.

Ridge
   Control the visibility of ridges.

Valley
   Control the visibility of valleys.


.. _3dview-material-preview:

:bl-icon:`shading_texture` -- Material Preview
==============================================

Render the 3D Viewport with :doc:`EEVEE </render/eevee/introduction>` and an HDRI environment.
This mode is particularly suited for previewing materials and painting textures.
You can select different lighting conditions to test your materials.

.. note::

   The Material Preview shading mode is not available when the scene's render engine
   is set to :doc:`Workbench </render/workbench/introduction>`.


Lighting
--------

Scene Lights
   Use the lights in the scene. When disabled (or when the scene contains no lights),
   a virtual light is used instead.

.. _bpy.types.View3DShading.use_scene_world:

Scene World
   Use the World of the scene.
   When disabled, a world will be constructed with the following options:

   HDRI Environment
      The environment map used to light the scene.
   Rotation
      The rotation of the environment on the Z axis.

      World Space Lighting
         Makes the lighting rotation fixed and not follow the camera.

   Strength
      Light intensity of the environment.
   World Opacity
      Opacity of the HDRI as a background image in the viewport.
   Blur
      Factor to unfocus the HDRI.
      Note that this does not change the diffusion of the lighting,
      only the appearance of the background.

Render Pass
   Instead of the combined render, show a specific
   :doc:`render pass </render/layers/passes>`.
   Useful to analyze and debug geometry, materials and lighting.

.. _bpy.types.View3DShading.use_compositor:

Compositor
   When to preview the result of :doc:`compositing </compositing/introduction>` in the 3D Viewport.

   :Disabled: Never show the compositing output.
   :Camera: Only show the compositing output when in :doc:`Camera View </editors/3dview/navigate/camera_view>`,
      which gives the best vantage point for previewing the final result.
   :Always: Always show the compositing output.


.. _3dview-rendered:

:bl-icon:`shading_rendered` -- Rendered
=======================================

Render the 3D Viewport using the scene's *Render Engine*, for interactive rendering.
This gives a preview of the final result before compositing, including scene lighting effects.

The options are the same as for *Material Preview*, except that
the *Render Pass* selector will offer different passes if the scene
uses the :doc:`Cycles </render/cycles/introduction>` render engine.
