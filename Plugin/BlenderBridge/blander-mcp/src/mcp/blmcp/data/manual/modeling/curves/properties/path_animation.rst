.. _curve-path-animation:

**************
Path Animation
**************

The *Path Animation* settings can be used to determine how child objects move along a certain path.

.. note::

   This feature is deprecated, but still available.
   A more future-proof method is the :doc:`/animation/constraints/relationship/follow_path`.

.. figure:: /images/modeling_curves_properties_path-animation_panel.png
   :align: center

   Path Animation panel.

.. _bpy.types.Curve.path_duration:

Frames
   The number of frames that are needed to traverse the path,
   defining the maximum value for the *Evaluation Time* setting.

.. _bpy.types.Curve.eval_time:

Evaluation Time
   Parametric position along the length of the curve that object following it should be at
   (the position is evaluated by dividing by the *Frames* value).
   By default, it is linked to the global frame number,
   but could be keyframed to give more control over the path animation.

.. _bpy.types.Curve.use_path_clamp:

Clamp
   Clamp the curve path children so they can't travel past the start/end point of the curve.

.. _bpy.types.Curve.use_path_follow:

Follow
   Make the curve path children rotate along the curvature of the path.


Example
=======

This example shows you how setup a *Path Animation*.

#. Add an object you want to animate and a path along which this object will move.
   In this example it's the *Monkey* and the *Bézier Circle*.
#. To parent the monkey to the Bézier circle, first select the monkey then the curve
   (so that the curve is the active object), press :kbd:`Ctrl-P` and select *Follow Path*.
   It will automatically animate *Evaluation Time* and activate *Follow* option
   in the *Path Animation* panel.
#. Select the monkey and
   :doc:`Clear Origin </scene_layout/object/editing/clear>` to reset its offset.
#. You can change the orientation of the monkey by changing
   the :doc:`Tracking Axis </scene_layout/object/properties/relations>`.

.. list-table::

   * - .. figure:: /images/modeling_curves_properties_path-animation_example-1.png

          Monkey parented to the Bézier Circle.

     - .. figure:: /images/modeling_curves_properties_path-animation_example-2.png

          The final result.
