.. index:: Geometry Nodes; Trim Curve
.. _bpy.types.GeometryNodeTrimCurve:

***************
Trim Curve Node
***************

.. figure:: /images/node-types_GeometryNodeTrimCurve.webp
   :align: center
   :alt: Trim Curve node.

The *Trim Curve* node shortens each spline in the curve by removing sections at
the start and end of each spline.

Bézier splines will still be Bézier splines in the output, with the first and last control point and
its handles moved as necessary to preserve the shape.
NURBS splines will be transformed into poly splines in order to be trimmed.

.. warning::

   Currently the Trim Curve node does not support
   :doc:`cyclic </modeling/geometry_nodes/curve/read/is_spline_cyclic>` splines.

.. note::

   Since curve :doc:`normals </modeling/geometry_nodes/geometry/read/normal>` are calculated the final curve,
   this node may change the resulting normals when the **Minimum** twist method is used, since the **Minimum**
   method considers the entire length of the curve to decide the final normals. In some cases the
   :doc:`/modeling/geometry_nodes/attribute/capture_attribute` could be used to avoid this,
   by saving the original normals to be used later.


Inputs
======

Curve
   Standard geometry input with a curve component.

Selection
   A boolean field input for each curve indicating whether it is trimmed or not.

Start
   The factor or length used to determine where to start each output spline.

   .. note::

      If the *Start* input is larger than the *End*, then the resulting spline
      will have a single point, located at the sample location of the *Start* value.

End
   The factor or length used to determine where to end each output spline.


Properties
==========

Mode
   How to find endpoint positions for the trimmed spline.

   :Factor:
      Find the endpoint positions using a factor of each spline's length.
      The input values should be between 0 or 1.
   :Length:
      Find the endpoint positions using a length from the start of each spline.
      The input values should be between 0 and the length of the splines.


Outputs
=======

Curve
   Standard geometry output.
