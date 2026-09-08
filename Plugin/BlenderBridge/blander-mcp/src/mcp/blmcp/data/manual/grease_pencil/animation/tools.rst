
***************
Animation Tools
***************

.. _bpy.ops.grease_pencil.insert_blank_frame:

Insert Blank Keyframe (Active Layer)
====================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Insert Blank Keyframe (Active Layer)`
   :Shortcut:  :kbd:`Shift-I`

Add a new blank keyframe to the active layer at the current frame.
If there is already a keyframe at the current frame,
a new blank keyframe will be added on the next frame.

All Layers
   When enabled, Blank keyframe will be created on all layers, not only the active one.

Duration
   The number of blank frames to insert.


Insert Blank Keyframe (All Layers)
==================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Insert Blank Keyframe (All Layers)`

Same as :ref:`bpy.ops.grease_pencil.insert_blank_frame` but *All Layers* is enabled by default.


.. _bpy.ops.grease_pencil.frame_duplicate:

Duplicate Active Keyframe (Active Layer)
========================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Duplicate Active Keyframe (Active Layer)`

Duplicates the strokes on the last keyframe by copying them to the current frame.

Mode
   Pick which layers to duplicate.

   :Active: Duplicate only the active layer.
   :All: Duplicate all the layers.


Duplicate Active Keyframe (All Layers)
======================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Duplicate Active Keyframe (All Layers)`

Same as :ref:`bpy.ops.grease_pencil.frame_duplicate` but the *Mode* is set to *All* by default.


.. _bpy.ops.grease_pencil.delete_frame:

Delete Active Keyframe (Active Layer)
=====================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Delete Active Keyframe (Active Layer)`
   :Shortcut:  :kbd:`Alt-I`

Deletes the last keyframe in the Dope Sheet or the current keyframe if you are on one.

Type
   Pick which layer to delete keyframes.

   :Active Frame: Deletes current frame in the active layer.
   :All Active Frames: Delete active frames for all layers.


Delete Active Keyframe (All Layers)
===================================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Delete Active Keyframes (All Layers)`
   :Shortcut:  :kbd:`Shift-Delete`

Same as :ref:`bpy.ops.grease_pencil.frame_duplicate` but the *Type* is set to *All Active Frames* by default.


.. _bpy.ops.grease_pencil.interpolate_sequence:

Interpolate Sequence
====================

.. reference::

   :Mode:      Draw Mode, Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Interpolate Sequence`
   :Shortcut:  :kbd:`Shift-Ctrl-E`

Interpolate strokes between the previous and next keyframe by adding *multiple* keyframes.
A breakdown keyframe will be added on every frame between the previous and next keyframe.

Step
   Number of frames between generated interpolated frames.
Layer
    Layers included in the interpolation.
Exclude Break Downs
   Exclude existing Breakdowns keyframes as interpolation extremes.
Flip Mode
   Invert destination stroke to match start and end with source stroke.
Smooth
   Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise.
Iterations
   Number of times to smooth newly created strokes.
Type
   Interpolation method to use the next time *Interpolate Sequence* is run.


.. _bpy.ops.grease_pencil.bake_grease_pencil_animation:

Bake Object Transform to Grease Pencil
======================================

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Animation --> Bake Object Transform to Grease Pencil`

Applies all transform animation at Object level within a selected frame range to Grease Pencil object keyframes.

Start Frame, End Frame
   Start/End frame for the baking process.
Step
   Frame steps for the baking process.
Only Selected Keyframes
   Convert only the selected keyframes.
Target Frame
   Target destination frame for the baked animation.
Projection Type
   Sets the projection type to use for the converted strokes.
