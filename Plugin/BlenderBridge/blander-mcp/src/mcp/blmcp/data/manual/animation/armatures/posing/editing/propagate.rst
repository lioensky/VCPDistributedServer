.. _bpy.ops.pose.propagate:

*********
Propagate
*********

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Propagate`
   :Shortcut:  :kbd:`Alt-P`

The Propagate tool copies the pose of the selected bones on the current frame over
to the keyframes delimited by the *Termination Mode*.
It automates the process of copying and pasting.

Termination Mode
   Modes which determine how it decides when to stop overwriting keyframes.

   To Next Keyframe
      Simply copies the pose to the first keyframe after (but not including any keyframe on) the current frame.
   To Last Keyframe
      Will simply replace the last keyframe (i.e. making action cyclic).
   Before Frame
      To all keyframes between current frame and the *End frame* option.
      This option is best suited for use from scripts due to the difficulties in setting this frame value,
      though it is possible to set this manually
      via the :ref:`bpy.ops.screen.redo_last` panel if necessary.
   Before Last Keyframe
      To all keyframes from current frame until no more are found.
   On Selected Keyframes
      Will apply the pose of the selected bones to all selected keyframes.
   On Selected Markers
      To all keyframes occurring on frames with Scene Markers after the current frame.
End Frame
   Defines the upper-bound for the frame range within which keyframes
   will be affected (with the lower bound being the current frame).
