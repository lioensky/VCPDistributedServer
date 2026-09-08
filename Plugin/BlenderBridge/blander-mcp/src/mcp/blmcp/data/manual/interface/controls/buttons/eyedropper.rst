.. _ui-eyedropper:
.. _bpy.ops.ui.eyedropper:

**********
Eyedropper
**********

The eyedropper (pipette icon) allows you to sample from anywhere in the Blender window.
The eyedropper can be used to select different kinds of data:

Color
   This is the most common usage. The eyedropper is used to sample a pixel's color from anywhere within Blender.

   .. note::

      The :ref:`View Transform <bpy.types.ColorManagedViewSettings.view_transform>` of the color management
      affects the color. In order to get consistent results, it should be set to *Standard*.
      If it's set to any other option, the eyedropper may return an inaccurate color.

Color Ramp
   Dragging the cursor over the window to sample a line which is converted into a color ramp.

Objects/Object-Data
   This is used with object buttons (such as parent, constraints or modifiers) to
   select an object from the 3D Viewport or Outliner, rather than having to select it from a drop-down.

Bones
   This is used when a subtarget to an armature can be chosen. It is possible to
   choose a bone from the 3D Viewport or from the outliner. Only bones that belong
   to the armature that was chosen as a target can be picked.

   .. note::

      In the 3D Viewport, bones can only be picked if the armature is in Pose Mode or in Edit Mode.

Camera Depth
   Number fields effecting distance can also use the eyedropper.

   This is used to set the camera's depth of field so the depth chosen is in focus.

- :kbd:`E` will activate the eyedropper while hovering over a button.
- :kbd:`LMB` dragging will mix the colors you drag over, which can help when sampling noisy imagery.
- :kbd:`Spacebar` resets and starts mixing the colors again.
