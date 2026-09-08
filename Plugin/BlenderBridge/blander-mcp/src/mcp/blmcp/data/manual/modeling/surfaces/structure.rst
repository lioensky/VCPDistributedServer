
*****************
Surface Structure
*****************

Surfaces are similar to :doc:`Curves </modeling/curves/structure>`,
in that they use Bézier or NURBS splines to produce smooth geometry
that follows a set of control points. The main difference, of course,
is that a Curve produces a line while a Surface produces a sheet.

A Surface object can contain multiple disconnected surfaces.
The one that's selected in Edit Mode is referred to as the
"active spline."

.. _modeling-surfaces-rows-grids:

Control Point Grid
==================

While a Surface can be compared to a mesh with a
:doc:`/modeling/modifiers/generate/subdivision_surface`,
it's more restrictive because the control points must be strictly arranged in a grid:
each "row" indicated by a yellow line must have the same number of
control points, and so does each "column" indicated by a pink line.
The only way to extend the surface is by
:doc:`extruding </modeling/surfaces/editing/control_points>` a complete row or column.

The :doc:`/modeling/surfaces/properties/active_spline` panel controls whether
the surface is cyclic (closed) in each direction of the grid, and whether Bézier
or NURBS should be used.

.. _modeling-surfaces-weight:

Weights
=======

The shape can be further tweaked by changing the weight of individual control
points in the :doc:`/modeling/surfaces/properties/transform_panel` found in the Sidebar.

The property is called *W*; while there is also one called *Weight*,
this is the :ref:`Goal Weight <surface-goal-weight>` for soft body simulations.

.. _fig-surface-intro-weight:

.. figure:: /images/modeling_surfaces_structure_weight.png

   A control point with a higher weight pulls the surface towards it.

.. note::

   If all control points have the same weight, they cancel each other out
   and the surface ends up looking the same as before. The weights must be
   different for there to be an effect.

Weights are necessary to achieve certain "pure" shapes like cylinders or spheres.
The :doc:`primitives </modeling/surfaces/primitives>` in the *Add* menu
have these preconfigured.

.. figure:: /images/modeling_surfaces_structure_weight-sphere.png

   Control point weights on a spherical Surface.
