.. (todo move) introductory text parts to introduction.rst

**********************
2D Stabilization Panel
**********************

The purpose of 2D stabilization is to smooth out jerky camera handling on existing real-world footage.
To activate the 2D stabilizer, you need to set the toggle in the panel, and additionally you need to enable
*Show Stable* in the Clip Display pop-over.
Then you'll need to set up some tracking points to detect the image movements.

The 2D Stabilization panel is used to define the data used for 2D stabilization of the shot.
Several options are available in this panel: you may add a list of tracks to determine lateral image shifts
and another list of tracks to determine tilting and zooming movements.
Based on the average contribution of these tracks,
a compensating movement is calculated and applied to each frame.

When the footage includes panning and traveling movements,
the stabilizer tends to push the image out of the visible area.
This can be compensated by animating the parameters for the intentional,
"expected" camera movement.

.. note::

   To *activate* the 2D stabilizer, you need to set the toggle in the panel,
   and additionally you need to enable *Show Stable* in the *Clip Display* pop-over.


.. _bpy.types.MovieTrackingStabilization.use_2d_stabilization:

Options
=======

.. figure:: /images/movie-clip_tracking_clip_sidebar_stabilization_panel_panel.png
   :align: right
   :width: 213px

   2D Stabilization panel.

Anchor Frame
   Reference point to anchor stabilization:
   other frames will be adjusted relative to this frame's position, orientation and scale.
   You might want to select a frame number where your main subject is featured in an optimal way.

Stabilization Type
   Rotation
      In addition to location, stabilizes detected rotation around the *rotation pivot point*,
      which is the weighted average of all location tracking points.

   Scale
      Compensates any scale changes relative to center of rotation.

Tracks for Stabilization
   Location
      List of tracks to be used to compensate for camera jumps, or location movement.

   Rotation/Scale
      List of tracks to be used to compensate for camera tilts and scale changes.

Autoscale
   Finds smallest scale factor which, when applied to the footage,
   would eliminate all empty black borders near the image boundaries.

   Max
      Limits the amount of automatic scaling.

Expected Position X/Y
   Known relative offset of original shot, will be subtracted, e.g. for panning shots.
Expected Rotation
   Rotation present on original shot, will be compensated, e.g. for deliberate tilting.
Expected Zoom
   Explicitly scale resulting frame to compensate zoom of original shot.

Influence
   The amount of transformation applied to the footage can be controlled.
   In some cases it is not necessary to fully compensate camera jumps.
   The amount of stabilization applied to the footage can be controlled.
   In some cases you may not want to fully compensate some of the camera's jumps.
   Please note that these "\* *Influence*" parameters do control only the *compensation movements*
   calculated by the stabilizer, not the deliberate movements added through the "*Expected* \*"-parameters.

Interpolate
   The stabilizer calculates compensation movements with sub-pixel accuracy.
   Consequently, a resulting image pixel needs to be derived from several adjacent source footage pixels.
   Unfortunately, any interpolation causes some minor degree of softening and loss of image quality.

   Nearest
      No interpolation, uses nearest neighboring pixel.
      This setting basically retains the original image's sharpness.
      The downside is we also retain residual movement below the size of one pixel,
      and compensation movements are done in 1 pixel steps, which might be noticeable as irregular jumps.
   Bilinear
      Simple linear interpolation between adjacent pixels.
   Bicubic
      Highest quality interpolation, most expensive to calculate.
