.. index:: Grease Pencil Modifiers; Smooth Modifier
.. _bpy.types.GreasePencilSmoothModifier:

***************
Smooth Modifier
***************

The *Smooth* Modifier changes the value of one or more stroke/points properties like:
location, strength, thickness or UV texture position
trying to maintain similar values that make the line fluid and smoother.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_smooth_panel.png
   :align: right

   Smooth Modifier.

Affect
   Combination of stroke/points properties that will be affected by the smooth factor.

   :Position:
      Smooth affect the point location.
   :Strength:
      Smooth affect the point strength (opacity).
   :Thickness:
      Smooth affect the point thickness.
   :UV:
      Smooth affect the point UV rotation.

Factor
   Strength of the smooth effect.

Repeat
   The number of smoothing iterations, equivalent to executing the Smooth tool multiple times.
   High values can reduce the animation performance (FPS).

Keep Shape
   When enabled, the smoothing algorithm will try to maintain as close as possible the overall
   shape of the original stroke.

Smooth Ends
   Smooth the ends of the strokes.

Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
