.. index:: Geometry Nodes; Interpolate Curves
.. _bpy.types.GeometryNodeInterpolateCurves:

***********************
Interpolate Curves Node
***********************

.. figure:: /images/node-types_GeometryNodeInterpolateCurves.webp
   :align: right
   :alt: Interpolate Curves node.

Generate new curves on points by interpolating between existing curves.
This is useful to have a smaller set of original curves to make editing easier and faster
while still generating high-density curves for the viewport or a final render.


Inputs
======

Guide Curves
   Base curves that new curves are interpolated between.
Guide Up
   Optional up vector that is typically a surface normal. Supplying an up vector will improve
   the quality of the interpolation, making it aware of the surface shape which it otherwise
   wouldn't have a way to know about.

   .. tip::

      In a typical "child hair" generation setup, this up direction is retrieved with a combination
      of the :doc:`/modeling/geometry_nodes/mesh/sample/sample_uv_surface` using the same geometry
      that the points were distributed on, and the :doc:`/modeling/geometry_nodes/geometry/read/normal`.

Guide Group ID
   Splits guides into separate groups. New curves interpolate existing curves from a single group.
   This input can be useful for generating hair parts by stopping curves in different sections
   (with different group IDs) from affecting each other.
Points
   The positions of the first root control points of the newly generated interpolated curves.
Points Up
   Optional up vector that is typically a surface normal.
Point Group ID
   The curve group to interpolate in.
Max Neighbors
   Maximum amount of close guide curves that are taken into account for interpolation.


Outputs
=======

Curves
   The guide curves with interpolated curves.
Closest Index
   Index of the closest guide curve for each generated curve.

   .. note::

      Internally this node mixes the data from multiple guide curves, with the maximum number
      of sources depending on the *Max Neighbors* input. This output is only the index of the curve
      with the largest weight.

Closest Weight
   Weight of the closest guide curve for each generated curve.
