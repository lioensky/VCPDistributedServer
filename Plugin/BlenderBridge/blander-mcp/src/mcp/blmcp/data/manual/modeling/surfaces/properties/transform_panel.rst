
***************
Transform Panel
***************

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Item --> Transform`

This panel contains the properties of the selected control points.
If multiple points are selected, it shows the averages of the values,
and allows changing those values for all the points in one go.

Control Point
   X, Y, Z
      The coordinates of the control point.
   W
      The :ref:`weight <modeling-surfaces-weight>` of the control point.
      The higher the weight, the more the control point pulls the surface towards itself.
Space
   Whether the coordinates are in object space (Local) or in world space (Global).

.. _surface-goal-weight:

Weight
   The "goal weight" when using :doc:`Soft Body </physics/soft_body/index>` physics.
   Higher values make the surface "stiffer" at that control point (as in, the control
   point will stay close to its original location, preventing deformation).
Radius
   Not applicable for Surface objects.
Tilt
   Not applicable for Surface objects.
