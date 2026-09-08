.. index:: Geometry Nodes; Set Curve Normal
.. _bpy.types.GeometryNodeSetCurveNormal:

*********************
Set Curve Normal Node
*********************

.. figure:: /images/node-types_GeometryNodeSetCurveNormal.webp
   :align: right
   :alt: Set Curve Normal node.

The *Set Curve Normal* controls the method used to calculate curve normals for every curve.

The node doesn't set the normals directly, those are calculated later as necessary.
Combined with the :doc:`tilt </modeling/geometry_nodes/curve/read/curve_tilt>` attribute value
at each control point, this will define the final normals accessible with the
:doc:`/modeling/geometry_nodes/geometry/read/normal`.

Internally this node adjusts the values of the ``normal_mode`` attribute on each curve.


Inputs
======

Curve
   Standard geometry input, containing curves.

Selection
   Whether or not to change the value on each curve.

Mode
   The method for evaluation of the curve's normals

   :Minimum Twist:
      The final normals are calculated to have the smallest twist around
      the curve tangent across the whole curve.
   :Z-Up:
      The final normals are calculated so that they are perpendicular to the Z axis and the tangent.
      If a series of points is vertical, the X axis is used.
   :Free:
      Use the stored custom normal attribute (``custom_normal``) as the final normals.

      This mode adds a *Normal* input that can be used to set the value of the custom normal.

      .. note::

         Custom normals are not rotation invariant,
         meaning normals must be set **after** any rotation transformations;
         i.e. at the end of the node tree or at the bottom of the modifier stack.

Normal :guilabel:`Free`
   Input for the custom normal attribute (``custom_normal``) when using *Free* mode.


Outputs
=======

Curve
   Standard geometry output.
