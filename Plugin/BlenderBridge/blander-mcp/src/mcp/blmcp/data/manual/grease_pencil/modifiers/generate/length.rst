.. index:: Grease Pencil Modifiers; Length Modifier
.. _bpy.types.GreasePencilLengthModifier:

***************
Length Modifier
***************

The *Length* modifier can shrink or extend strokes.


Options
=======

.. figure:: /images/grease-pencil_modifiers_generate_length_panel.png
   :align: right

   The Length modifier.

Mode
   :Absolute: Length is in geometry space.
   :Relative: Length is in ratio to the stroke's length.

Start
   Added length to the start of the stroke. Negative value will shrink the stroke.

End
   Added length to the end of the stroke. Negative value will shrink the stroke.

Used Length
   Define what portion of the stroke is used to calculate the direction of the extension.


Curvature
---------

When enabled, the extension will follow the curvature of the stroke.

Point Density
   Multiplied by Start/End for the total point count.

Segment Influence
   Factor to determine how much the length of the individual segments
   should influence the final computed curvature. Higher factors makes
   small segments influence the overall curvature less.

Filter Angle
   Ignore points on the stroke that deviate from their neighbors by more
   than this angle when determining the extrapolation shape.

Invert
   Invert the curvature of the stroke's extension.


Random Offsets
--------------

Random Offset Start/End
   Size of random length added to the start/end of each stroke.

Random Noise Offset
   Smoothly offset each stroke's random value.

Seed
   Number used to generate different noise patterns.


Randomize
^^^^^^^^^

Re-randomizes values over time.

Step
   Number of frames before recalculate random values again.


Influence Filters
-----------------

See :ref:`grease-pencil-modifier-influence-filters`.
