.. _bpy.types.ToolSettings.use_grease_pencil_multi_frame_editing:

**********
Multiframe
**********

.. figure:: /images/grease-pencil_multiframe_panel.png
   :align: right

   Multiframe pop-over.


Multiframe allows you to draw, edit, sculpt, or weight painting on several frames at the same time.
Extremely useful to avoid repeating a task one frame at a time when animating.

.. _bpy.types.GPencilSculptSettings.use_multiframe_falloff:

Use Falloff
   When enabled, the effects on the strokes start to falloff from the current frame
   as defined by a :doc:`curve widget </interface/controls/templates/curve>`.


Usage
=====

#. Select the desired keyframes to draw, edit or sculpt at the same time.
#. Activate the Multiframe tool in the 3D Viewport's header with the toggle button (faded lines icon).
#. Once activated you can:

   - Select the points in all the selected keyframes and make your edits.
   - Start sculpting. The sculpt brushes will affects all the strokes in the selected keyframes.
   - Start weight painting. The weight paint brush will affect all the strokes in the selected keyframes.
   - Start Drawing. The new strokes will be added in all the selected keyframes.
     If you are using the Fill tool then it will be applied in all the selected keyframes.
   - When interpolating you can select the stroke from the different frames in the right order.
     Interpolate tool will use the selection order to calculate the correct stroke pairs.

.. note::

   Not all operators support Multiframe mode.
