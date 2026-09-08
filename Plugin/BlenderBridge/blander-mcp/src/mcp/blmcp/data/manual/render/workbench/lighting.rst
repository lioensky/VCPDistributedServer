
********
Lighting
********

The Workbench engine does not use the lights of the scene.
The lighting conditions that will be used can be set in the Lighting panel.

.. reference::

   :Panel:     :menuselection:`Properties --> Render --> Lighting`

.. _bpy.types.View3DShading.light:

:Flat:
   Objects are "shaded" in a flat color, without any highlights or shadows.

:Studio:
   Use a predefined studio lighting setup, such as a key light
   shining from the front and a rim light shining from the back.
   Click the sphere to choose a different setup.

   The studio lights can be configured in the :ref:`Preferences <prefs-lights-studio>`.
   By default, they follow the viewport camera around, but this can be changed:

   World Space Lighting
      Keep the lights fixed in place rather than following the viewport camera.
   Rotation
      The rotation of the lights on the Z axis.

.. _render-workbench-matcap:

:MatCap:
   Use a Material Capture, which is an image with texturing, lighting
   and even reflections baked into it. Objects are shaded by
   simply picking colors from this image based on the direction of
   the normal in relation to the camera.

   Click the sphere to choose a different MatCap,
   or the double arrow button to flip it horizontally.

   Custom MatCaps can be loaded in the :ref:`Preferences <prefs-lights-matcaps>`.

