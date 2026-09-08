
***********
Frame Range
***********

.. figure:: /images/render_output_properties_frame_range_panel.png

   Frame Range panel.

This panel defines how long an animation will last in terms of frames.
Frames can be divided by the scene's :ref:`Frame Rate <bpy.types.RenderSettings.fps>`
to get the animation duration in terms of time.
For example, a 250 frame animation at a frame rate of 30 will last 8.3 seconds.

.. _bpy.types.Scene.frame_start:
.. _bpy.types.Scene.frame_end:

Frame Start, End
   Set the *Start* and *End* frames for :doc:`Rendering Animations </render/output/animation>`.

.. _bpy.types.Scene.frame_step:

Step
   Controls the number of frames to advance for each frame rendered, a value above 1 skips frames.
   This is also used when viewing rendered animations.


Time Stretching
===============

Use to remap the length of an animation; making it run slower or faster.
The *Old* and *New* settings may either be used as absolute values or as a ratio:
For example, setting *Old* to a value of 2 and *New* to 1 will run the animation twice as fast.

.. warning::

   Using *Time Stretching* will not influence the *Start* or *End* frames set above,
   so make sure that your animation is not cut off or has extraneous still frames at the end.

.. _bpy.types.RenderSettings.frame_map_old:

Old
   The length in frames of the original animation.

.. _bpy.types.RenderSettings.frame_map_new:

New
   The length in frames the new animation will last.
