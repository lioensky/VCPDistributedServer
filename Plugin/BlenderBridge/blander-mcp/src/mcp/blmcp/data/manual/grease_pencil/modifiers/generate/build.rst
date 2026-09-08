.. index:: Grease Pencil Modifiers; Build Modifier
.. _bpy.types.GreasePencilBuildModifier:

**************
Build Modifier
**************

The *Build* modifier make strokes appear or disappear in a frame range to
create the effect of animating lines being drawn or erased.

.. seealso::

   This documentation refers to the Build Modifier specific to the Grease Pencil object.
   For uses with other object types refer to the general :doc:`/modeling/modifiers/generate/build`.


Options
=======

.. figure:: /images/grease-pencil_modifiers_generate_build_panel.png
   :align: right

   The Build modifier.

Mode
   Determines how many strokes are being animated at a time.

   :Sequential:
      Strokes appear/disappear one after the other, but only a single one changes at a time.
   :Concurrent:
      Multiple stroke appear/disappear at a time.
   :Additive:
      Builds only the strokes that are new compared to last keyframe.
      The assumption is Additive Drawing was used so that the shared strokes are the same.

Transition *(in Sequential and Concurrent Mode)*
   Determines the animation type to build the strokes.

   :Grow:
      Shows points in the order they occur in each stroke, from first to last stroke.
      (Simulating lines being drawn.)
   :Shrink:
      Hide points from the end of each stroke to the start, from last to first stroke.
      (Simulating lines being erased.)
   :Vanish:
      Hide points in the order they occur in each stroke, from first to last stroke.
      (Simulating ink fading or vanishing after getting drawn.)

Timing
   The way you want to time the building of the strokes.

   :Natural Drawing Speed:
      Use the recorded speed of the stylus when the strokes were drawn.
      Only available in Sequential and Additive Mode.

      Speed Factor
         The recorded speed is multiplied by this value.
      Maximum Gap
         The maximum gap between strokes in seconds.

   :Number of Frames:
      Set a fixed maximum number of frames for the build animation.
      (Unless another Grease Pencil keyframe occurs before this time has elapsed.)

      Frames
         The maximum number of frames used.
      Delay
         Number of frames after each Grease Pencil keyframe before the modifier has any effects.

   :Percentage Factor:
      Manually set a percentage factor to control the amount of the strokes that are visible.

      Factor
         The factor from 0 to 1.

   :Time Alignment:
      Only available in Concurrent Mode.

      Align Start
         All stroke start at the same time (i.e. shorter strokes finish earlier).
      Align End
         All stroke end at the same time (i.e. shorter strokes start later).

Object
   Use the distance to an object to define the order in which strokes appear.


Custom Range
------------

If enabled, only modify strokes during the specified frame range.

Start, End
   Determines the start and end frame for the build effect.


Fade
----

Factor
   Defines how much the stroke is fading in/out.

Thickness
   How much strength fading is applied to the stroke's thickness.

Opacity
   How much strength fading applies to the stroke's opacity.

Weight Output
   Assign a weight value to points that have started/finished the fade.


Influence Filters
-----------------

See :ref:`grease-pencil-modifier-influence-filters`.
