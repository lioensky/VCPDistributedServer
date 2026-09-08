
********
Segments
********

.. _bpy.ops.curves.subdivide:

Subdivide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Subdivide`

The *Subdivide* operator adds new control points to selected curve segments by dividing them into smaller sections.
This is useful for creating smoother transitions, preparing curves for finer adjustments,
or adding more detail for animation or modeling.

Number of Cuts
   Specifies the number of divisions for each selected segment; each cut adds one new control point per segment.


.. _bpy.ops.curves.switch_direction:

Switch Direction
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Switch Direction`

The *Switch Direction* operator reverses the direction of a selected curve.
The start point of the curve becomes the end point, and vice versa.
This operation does not change the visual appearance of the curve,
but affects its behavior when used as a path or with options like beveling and tapering.

