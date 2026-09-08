.. _modeling-curves-transform-panel:

***************
Transform Panel
***************

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Transform`

When nothing is selected, the panel is empty.
When more than one vertex is selected, the median values are edited
and "Median" is added in front of the labels.

Control Point, Vertex
   The first controls (X, Y, Z) show the coordinates of the selected point or handle (vertex).
   In case of a NURBS curve, there is a fourth component available (W),
   which defines the :ref:`weight <curves_structure_nurbs_weight>`
   of the selected control point or the median weight.
Space
   The Space radio buttons let you choose if those coordinates are relative
   to the object origin (local) or the global origin (global).

   Global, Local

.. _curves-weight:

Weight
   Controls the "goal weight" of selected control points,
   which is used when a curve has :doc:`Soft Body </physics/soft_body/index>` physics,
   forcing the curve to "stick" to their original positions, based on the weight.
Radius
   Controls the width of the extrusion/bevel along the "spinal" curve.
   The radius will be interpolated from point to point (you can check it with the normals).
Tilt
   Controls how the normals (visualized as arrows)
   twist around each control point -- so it is only relevant with 3D curves!
   The tilt will be interpolated from point to point (you can check it with the normals).
