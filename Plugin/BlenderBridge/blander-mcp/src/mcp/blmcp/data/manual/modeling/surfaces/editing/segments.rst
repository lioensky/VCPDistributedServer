
********
Segments
********

Subdivide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Subdivide`

Subdivides the selected segments (grid lines) by creating additional, evenly spaced control points in the middle.
These new points then give more fine-grained control over the surface's shape.

The selection must consist of complete rows or columns of the control point grid.

If not all control points of the surface are selected, it will be subdivided in one direction.
If all control points are selected, it will be subdivided in both directions.

Number of Cuts
   The number of control points to add in each segment.


.. _modeling_surfaces_editing_segments_switch-direction:

Switch Direction
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Switch Direction`

Reverses the internal order of all the control points in the surface. This also flips the surface's
face normals.

.. seealso::

   :ref:`Face Orientation Overlay <bpy.types.View3DOverlay.show_face_orientation>`
