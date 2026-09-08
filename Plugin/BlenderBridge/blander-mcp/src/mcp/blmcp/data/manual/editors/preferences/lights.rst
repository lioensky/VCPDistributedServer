.. _bpy.ops.preferences.studiolight:

******
Lights
******

.. figure:: /images/editors_preferences_section_lights.webp

   Blender Preferences Lights section.


.. _prefs-lights-studio:

Studio Lights
=============

Studio Lights are used to illuminate the 3D Viewport during *Solid View* and will not be rendered.
Unlike lights in the scene, the lighting direction follows the viewport orientation.


.. _bpy.types.UserSolidLight:

Editor
------

.. _bpy.types.PreferencesSystem.use_studio_light_edit:
.. _bpy.ops.preferences.studiolight_new:

There are up to four virtual light sources.

The Light toggles allow you to enable or disable individual lights.
At least one of the four lights must remain enabled for the 3D Viewport.
The lights are equal, except for their direction and color.
You can control the direction of the lights, as well as their diffuse and specular colors.

.. _bpy.types.UserSolidLight.use:

Use Light
   Toggles the specific light.

.. _bpy.types.UserSolidLight.diffuse_color:

Diffuse
   This is the constant color of the light.

.. _bpy.types.UserSolidLight.specular_color:

Specular
   This is the highlight color of the light.

.. _bpy.types.UserSolidLight.smooth:

Smooth
   Smooth the shading from this light.

   *This has the effect of lighting to be less direct.*

.. _bpy.types.UserSolidLight.direction:

Direction
   The direction of the light, (see :ref:`ui-direction-button`).

   The direction of the light will be the same as shown at the sphere surface.

.. _bpy.types.PreferencesSystem.light_ambient:

Ambient Color
   The color of unlit areas.


.. _prefs-lights-matcaps:

MatCaps
=======


This panel manages :term:`MatCap` image files
which can used to light the view when :ref:`MatCap <render-workbench-matcap>` shading is enabled.

Two kinds of images are supported for MatCaps. Regular image files and
multilayered OpenEXR files. When using multilayered OpenEXR files,
the layer named "diffuse" will be used as a diffuse pass, the layer named "specular"
will be used as a specular pass. Regular images will be handled as "diffuse" and
will not support specular highlighting.

The diffuse pass is multiplied with the base color of the objects and the specular pass is added on top.
MatCaps, that only have a diffuse pass tend to look very metallic,
with a separate specular pass it is possible to simulate a wider variety of materials.


HDRIs
=====

This panel manages :term:`HDRI` image files
which can be used to light the view when :ref:`Material Preview <3dview-material-preview>` or
:ref:`Rendered <3dview-rendered>` shading is enabled.
