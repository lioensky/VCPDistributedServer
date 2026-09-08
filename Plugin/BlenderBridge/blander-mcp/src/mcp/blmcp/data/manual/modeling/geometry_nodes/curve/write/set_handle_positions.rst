.. index:: Geometry Nodes; Set Handle Positions
.. _bpy.types.GeometryNodeSetCurveHandlePositions:

*************************
Set Handle Positions Node
*************************

.. figure:: /images/node-types_GeometryNodeSetCurveHandlePositions.webp
   :align: right
   :alt: Set Handle Positions node.

The *Set Handle Positions* node sets the positions for the handles of :ref:`Bézier curves <curve-bezier>`.
They can be used to alter the generated shape of the curve.
The input node for this data is the :doc:`/modeling/geometry_nodes/curve/read/curve_handle_positions`.
See the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details.

.. note::

   When the position is changed, *Auto* handle types will be converted to *Aligned*, and *Vector* handle
   types will be converted to *Free*.

.. note::

   The left and right handles cannot be changed at the same time with this node. That is because it would
   break the alignment for left and right handles at the same control point.


Inputs
======

Curve
   Standard geometry input, containing curves.

Selection
   Whether or not to change the handle position on each control point.
   True values mean the resolution will be changed, false values mean
   the resolution will remain the same.

Position
   The new handle position.

.. note::

   The handle positions are the global position of the handle, they are not relative to
   the position of the corresponding control point.

Offset
   An optional translation for each handle. This is evaluated at the same time as the *Position* input,
   meaning that fields evaluated for it will not reflect the changed position.


Properties
==========

Left / Right
   Whether to set the handle position of the left or right handle.
   The *Left* handle is closer to the start of the spline, and the *Right* handle is closer to the end.


Outputs
=======

Curve
   Standard geometry output.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_set-handle-positions_example.png
   :align: center

Here, the handles are adjusted to the same position as the control points, but offset down in
the Z direction slightly. With the :doc:`/modeling/geometry_nodes/curve/write/set_spline_type`,
the curve can be a poly spline in Edit Mode, to make adjustment simpler for the user of the node group.
