
***************
Curve Structure
***************

Splines
=======

Splines are the fundamental components of curve objects, defining their shapes.
A curve object can consist of multiple splines,
similar to how a mesh object can contain multiple disconnected meshes.
Each spline's shape is determined by its :ref:`Control Points <curve-spline-types>`.
Splines come in several types: Poly, Bézier, and NURBS, each with its own algorithm for representing curves,
as described in the `Spline Types`_ section.

.. Splines have unique properties that can be adjusted in Edit Mode via the
.. :doc:`Active Spline </modeling/curves/properties/active_spline>` panel.


Control Points
--------------

Splines are made up of control points, which connect to form the spline.
Control points can be :doc:`selected </modeling/curves/selecting>` and transformed to adjust the spline's shape.
This is analogous to vertices in a mesh object.

.. seealso::

   :doc:`Curve Editing </modeling/curves/editing/index>`


.. _curves-spline-types:

Spline Types
============

Poly
----

Poly splines are the simplest type, with no interpolation between control points.
They are used when :ref:`converting meshes to curves <bpy.ops.object.convert>`
for accurate representation of the original mesh.
While Poly splines are precise, `Bézier`_ or `NURBS`_ splines are generally preferred for smooth curves.


.. _curves-bezier:

Bézier
------

Bézier splines use control points and handles to define their shape.
A curve segment exists between two control points, with the handles controlling the curvature.

In the illustration below, the control points are at the center of the pink lines, while the handles extend outward.
The arrows represent the curve normals, indicating direction and tilt.

.. figure:: /images/modeling_curves_structure_control-points-handles.png
   :align: center

   Bézier Curve in Edit Mode.


.. _curves-bezier-handle-type:

Handle Types
^^^^^^^^^^^^

Bézier curves support four handle types, which can be changed with :kbd:`V`:

.. figure:: /images/modeling_curves_structure_bezier-handle-types.png
   :align: right

   Bézier Curve Handle Types.

.. _curves-handle-type-auto:

:Automatic:
   Automatically adjusts handle length and direction for the smoothest curve.
   Displayed as yellow handles. Converts to *Aligned* when moved.
:Vector:
   Handles point directly toward adjacent control points, enabling straight lines or sharp corners.
   Displayed as green handles. Converts to *Free* when moved.
:Aligned:
   Handles remain on a straight line, ensuring smooth, continuous curves.
   Displayed as purple handles.
:Free:
   Handles move independently, allowing for asymmetric curves.
   Displayed as black handles.

.. note::

   When a control point is selected, its handles are highlighted in red, altering their usual color.
   For example, Vector handles (normally green) appear yellow when selected,
   which can be confused with Automatic handles.

   To disable this effect,
   adjust the color settings in :menuselection:`3D Viewport --> Active Spline` under Theme Preferences.


.. _curves-nurbs:

NURBS
-----

NURBS (Non-Uniform Rational B-Splines) are mathematically precise splines, offering exact shapes.
Unlike Bézier curves, which approximate shapes (e.g., a Bézier circle approximates a perfect circle),
NURBS can represent exact geometry.

For more information, refer to the `Wikipedia page <https://en.wikipedia.org/wiki/NURBS>`__.

.. .. _curves_structure_nurbs_weight:

.. NURBS control points have a unique weight property that determines their influence on the curve.
.. This weight differs from the :ref:`Goal Weight <curves-weight>` used in soft body simulations.
.. Weights can be adjusted in the *W* field of the :doc:`Transform panel </modeling/curves/editing/transform_panel>`.

.. note::

   If all control points have the same weight, their influences cancel out.
   Differences in weight cause the curve to move toward or away from specific control points.
