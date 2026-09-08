.. index:: Geometry Nodes; Resample Curve
.. _bpy.types.GeometryNodeResampleCurve:

*******************
Resample Curve Node
*******************

.. figure:: /images/node-types_GeometryNodeResampleCurve.webp
   :align: center
   :alt: Resample Curve node.

The Resample Curve node creates a poly spline for each input spline.
In the *Count* and *Length* modes, the control points of the new poly
splines will have uniform spacing.

.. tip::

   Use a field as an input to have a different count/length for each spline.


Inputs
======

Curve
   Standard geometry input.

Selection
   Whether or not to resample each spline. True values mean spline will be resampled to a poly spline,
   false values mean the spline will be unaffected.

Mode
   How to specify the amount of samples.

   :Count:
      Sample the specified number of points along each spline.
   :Length:
      Calculate the number of samples by splitting each spline into segments with the specified length.
      The length will be rounded down so that a whole number of samples will fit in each input spline.
   :Evaluated:
      Evaluate the spline's points based on the resolution attribute for NURBS and Bézier splines.
      Changes nothing for poly splines.

Count :guilabel:`Count`
   The number of control points on the new splines.

Length :guilabel:`Length`
   The approximate length between the control points of the new splines.

   .. tip::

      A :doc:`/modeling/geometry_nodes/curve/operations/trim_curve` can be used with
      a multiple of the input length to make the distance between each sampled point exact,
      even when the length of the spline changes.


Outputs
=======

Curve
   Standard geometry output.
